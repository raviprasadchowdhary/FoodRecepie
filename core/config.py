"""
Fast mode configuration for Recipe Finder
Use this for instant results without waiting for APIs
"""

# Fast mode settings
FAST_MODE = True  # Set to True for instant results
SKIP_API_CALLS = True  # Skip API calls entirely
USE_FALLBACK_ONLY = True  # Use only fallback recipes

# Timeout settings (seconds)
FAST_REQUEST_TIMEOUT = 1  # Very short timeout for APIs
FAST_RATE_LIMIT = 0.05  # Minimal rate limiting

# Cache settings
FAST_CACHE_TTL = 7200  # 2 hours (longer cache for faster repeat searches)

def is_fast_mode():
    """Check if fast mode is enabled"""
    return FAST_MODE

def get_timeout():
    """Get current timeout setting"""
    return FAST_REQUEST_TIMEOUT if FAST_MODE else 10

def get_rate_limit():
    """Get current rate limit delay"""
    return FAST_RATE_LIMIT if FAST_MODE else 0.5

def should_skip_api():
    """Check if API calls should be skipped"""
    return SKIP_API_CALLS and FAST_MODE
