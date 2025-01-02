@echo off

REM Check if Python is installed and is version 3.x
python --version 2>nul | findstr /R "^Python 3.*" >nul
IF ERRORLEVEL 1 (
    echo Python 3 is not installed or not in PATH. Please install Python 3 and try again.
    exit /b 1
)

REM Install the Organizer package
python -m pip install --user .
IF ERRORLEVEL 1 (
    echo Installation failed. Please check for errors above.
    exit /b 1
)

echo Installation complete! Use the 'organize' command to run the tool.
pause

