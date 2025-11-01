"""
Performance optimization utilities for Recipe Finder
Includes caching, connection pooling, and performance helpers
"""

import time
import hashlib
import json
from typing import Any, Callable, Optional, Dict
from functools import wraps
from datetime import datetime, timedelta

# In-memory cache with TTL (Time To Live)
_cache: Dict[str, tuple[Any, float]] = {}
_cache_stats = {"hits": 0, "misses": 0, "size": 0}

# Cache configuration
DEFAULT_CACHE_TTL = 3600  # 1 hour in seconds
MAX_CACHE_SIZE = 1000  # Maximum cached items


def cache_key(*args, **kwargs) -> str:
    """
    Generate a cache key from function arguments.
    
    Args:
        *args: Positional arguments
        **kwargs: Keyword arguments
    
    Returns:
        Hash string as cache key
    """
    # Create a stable string representation
    key_parts = [str(arg) for arg in args]
    key_parts.extend(f"{k}={v}" for k, v in sorted(kwargs.items()))
    key_string = "|".join(key_parts)
    
    # Hash for shorter keys
    return hashlib.md5(key_string.encode()).hexdigest()


def cached(ttl: int = DEFAULT_CACHE_TTL):
    """
    Decorator to cache function results with TTL.
    
    Args:
        ttl: Time to live in seconds (default: 1 hour)
    
    Usage:
        @cached(ttl=600)  # Cache for 10 minutes
        def expensive_function(param):
            return some_slow_operation(param)
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            global _cache, _cache_stats
            
            # Generate cache key
            key = f"{func.__module__}.{func.__name__}:{cache_key(*args, **kwargs)}"
            
            # Check cache
            if key in _cache:
                value, expiry = _cache[key]
                if time.time() < expiry:
                    _cache_stats["hits"] += 1
                    return value
                else:
                    # Expired, remove from cache
                    del _cache[key]
                    _cache_stats["size"] = len(_cache)
            
            # Cache miss - compute value
            _cache_stats["misses"] += 1
            result = func(*args, **kwargs)
            
            # Store in cache with expiry time
            expiry_time = time.time() + ttl
            _cache[key] = (result, expiry_time)
            _cache_stats["size"] = len(_cache)
            
            # Prevent cache from growing too large
            if len(_cache) > MAX_CACHE_SIZE:
                _evict_oldest_cache_entries()
            
            return result
        
        return wrapper
    return decorator


def _evict_oldest_cache_entries():
    """Remove oldest 20% of cache entries when cache is full"""
    global _cache
    
    # Sort by expiry time and remove oldest 20%
    sorted_items = sorted(_cache.items(), key=lambda x: x[1][1])
    num_to_remove = max(1, len(_cache) // 5)
    
    for i in range(num_to_remove):
        key, _ = sorted_items[i]
        del _cache[key]


def clear_cache():
    """Clear all cached data"""
    global _cache, _cache_stats
    _cache.clear()
    _cache_stats = {"hits": 0, "misses": 0, "size": 0}


def get_cache_stats() -> Dict[str, Any]:
    """
    Get cache performance statistics.
    
    Returns:
        Dictionary with hits, misses, size, hit rate
    """
    total = _cache_stats["hits"] + _cache_stats["misses"]
    hit_rate = (_cache_stats["hits"] / total * 100) if total > 0 else 0
    
    return {
        "hits": _cache_stats["hits"],
        "misses": _cache_stats["misses"],
        "size": _cache_stats["size"],
        "hit_rate": f"{hit_rate:.1f}%",
        "total_requests": total
    }


class Timer:
    """Context manager for timing code blocks"""
    
    def __init__(self, name: str = "Operation"):
        self.name = name
        self.start_time = None
        self.elapsed = None
    
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self
    
    def __exit__(self, *args):
        self.elapsed = time.perf_counter() - self.start_time
    
    def __str__(self):
        if self.elapsed is not None:
            return f"{self.name}: {self.elapsed:.3f}s"
        return f"{self.name}: not completed"


def benchmark(func: Callable) -> Callable:
    """
    Decorator to benchmark function execution time.
    
    Usage:
        @benchmark
        def slow_function():
            # ... code ...
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"⏱️  {func.__name__} took {elapsed:.3f}s")
        return result
    return wrapper


# Session pooling for HTTP requests
_http_session_pool: Dict[str, Any] = {}


def get_http_session(provider: str):
    """
    Get or create a reusable HTTP session for a provider.
    Sessions maintain connection pools for better performance.
    
    Args:
        provider: Provider name (e.g., "themealdb", "spoonacular")
    
    Returns:
        requests.Session object
    """
    import requests
    
    if provider not in _http_session_pool:
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'RecipeFinder/1.0',
            'Connection': 'keep-alive'
        })
        
        # Configure connection pooling
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=10,
            pool_maxsize=20,
            max_retries=2,
            pool_block=False
        )
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        
        _http_session_pool[provider] = session
    
    return _http_session_pool[provider]


def close_all_sessions():
    """Close all HTTP sessions (call on app shutdown)"""
    global _http_session_pool
    for session in _http_session_pool.values():
        session.close()
    _http_session_pool.clear()


# Memoization for expensive pure functions
def memoize(func: Callable) -> Callable:
    """
    Simple memoization decorator for pure functions.
    Unlike @cached, this never expires (use for deterministic functions).
    
    Usage:
        @memoize
        def fibonacci(n):
            if n < 2: return n
            return fibonacci(n-1) + fibonacci(n-2)
    """
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = cache_key(*args, **kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    return wrapper


# Lazy evaluation helper
class LazyProperty:
    """
    Decorator for lazy-loaded properties.
    The property is computed once and cached.
    
    Usage:
        class MyClass:
            @LazyProperty
            def expensive_property(self):
                return compute_something_expensive()
    """
    
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        # Compute and cache the value
        value = self.func(instance)
        setattr(instance, self.name, value)
        return value


def batch_process(items: list, func: Callable, batch_size: int = 10):
    """
    Process items in batches to avoid memory issues with large datasets.
    
    Args:
        items: List of items to process
        func: Function to apply to each item
        batch_size: Number of items per batch
    
    Yields:
        Results from processing each item
    """
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        for item in batch:
            yield func(item)


# Performance monitoring
class PerformanceMonitor:
    """Track performance metrics across the application"""
    
    def __init__(self):
        self.metrics = {
            "api_calls": 0,
            "cache_hits": 0,
            "total_time": 0.0,
            "searches": 0
        }
    
    def record_api_call(self, duration: float):
        """Record an API call"""
        self.metrics["api_calls"] += 1
        self.metrics["total_time"] += duration
    
    def record_cache_hit(self):
        """Record a cache hit"""
        self.metrics["cache_hits"] += 1
    
    def record_search(self):
        """Record a search operation"""
        self.metrics["searches"] += 1
    
    def get_stats(self) -> Dict[str, Any]:
        """Get performance statistics"""
        avg_time = (self.metrics["total_time"] / self.metrics["api_calls"] 
                   if self.metrics["api_calls"] > 0 else 0)
        
        return {
            **self.metrics,
            "avg_api_time": f"{avg_time:.3f}s",
            "cache_hit_rate": (
                f"{self.metrics['cache_hits'] / self.metrics['searches'] * 100:.1f}%"
                if self.metrics['searches'] > 0 else "0%"
            )
        }
    
    def reset(self):
        """Reset all metrics"""
        self.metrics = {
            "api_calls": 0,
            "cache_hits": 0,
            "total_time": 0.0,
            "searches": 0
        }


# Global performance monitor instance
perf_monitor = PerformanceMonitor()
