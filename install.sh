#!/bin/bash

# Ensure pip is available
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install it first."
    exit 1
fi

# Install the Organizer package
python3 -m pip install --user .
if [ $? -eq 0 ]; then
    echo "Installation complete! Use the 'organize' command to run the tool."
else
    echo "Installation failed. Please check for errors above."
fi

