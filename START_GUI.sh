#!/bin/bash
# Recipe Finder Launcher for Mac/Linux
# Make executable: chmod +x START_GUI.sh
# Then run: ./START_GUI.sh

echo ""
echo "================================"
echo "  Recipe Finder - Launcher"
echo "================================"
echo ""
echo "Starting GUI application..."
echo ""

cd "$(dirname "$0")"
python3 gui.py

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Failed to launch GUI"
    echo ""
    echo "Possible fixes:"
    echo "  1. Install dependencies: pip3 install -r requirements.txt"
    echo "  2. Check Python is installed: python3 --version"
    echo ""
    read -p "Press Enter to exit..."
fi
