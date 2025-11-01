@echo off
REM Recipe Finder Launcher for Windows
REM Double-click this file to launch the GUI

echo.
echo ================================
echo   Recipe Finder - Launcher
echo ================================
echo.
echo Starting GUI application...
echo.

cd /d "%~dp0"
python gui.py

if errorlevel 1 (
    echo.
    echo ERROR: Failed to launch GUI
    echo.
    echo Possible fixes:
    echo   1. Install dependencies: pip install -r requirements.txt
    echo   2. Check Python is installed: python --version
    echo.
    pause
)
