#!/bin/bash

# Ensure pip is installed
if ! command -v pip &> /dev/null
then
    echo "pip could not be found. Please install pip first."
    exit 1
fi

# Install the package
pip install .

echo "Installation complete! Run 'organize --help' to get started."
