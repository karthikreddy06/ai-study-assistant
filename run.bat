@echo off
REM AI Study Assistant - Windows Batch Startup Script

echo ================================
echo AI Study Assistant Launcher
echo ================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Virtual environment not found.
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Error creating virtual environment.
        echo Please ensure Python 3.10+ is installed and in PATH.
        pause
        exit /b 1
    )
)

REM Activate virtual environment
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo Error activating virtual environment.
    pause
    exit /b 1
)

REM Check if requirements are installed
python -m pip show crewai >nul 2>&1
if errorlevel 1 (
    echo Dependencies not installed.
    echo Installing requirements...
    pip install -r requirements.txt
)

REM Check if .env file exists
if not exist ".env" (
    echo.
    echo WARNING: .env file not found!
    echo Please copy .env.example to .env and add your OpenAI API key.
    echo.
    pause
)

REM Run the application
echo.
echo Starting AI Study Assistant...
echo.
python main.py

pause
