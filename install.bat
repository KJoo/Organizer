@echo off

REM Ensure pip is available
where pip >nul 2>nul
IF ERRORLEVEL 1 (
    echo pip is not installed. Please install Python and pip first.
    exit /b 1
)

REM Install the package
pip install .

echo Installation complete! Run 'organize --help' to get started.
