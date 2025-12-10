#!/bin/bash
# Launcher script for worm animation

# Path to Blender on macOS
BLENDER="/Applications/Blender.app/Contents/MacOS/Blender"

# Path to the Python script
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/worm_animation.py"

echo "Starting Blender with worm animation..."
echo "Script: $PYTHON_SCRIPT"
echo ""

# Run Blender with the script
"$BLENDER" --python "$PYTHON_SCRIPT"
