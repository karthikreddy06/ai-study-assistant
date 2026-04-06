# AI Study Assistant - Windows PowerShell Startup Script

Write-Host "================================" -ForegroundColor Cyan
Write-Host "AI Study Assistant Launcher" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (-not (Test-Path "venv")) {
    Write-Host "Virtual environment not found." -ForegroundColor Yellow
    Write-Host "Creating virtual environment..." -ForegroundColor Cyan
    python -m venv venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Error creating virtual environment." -ForegroundColor Red
        Write-Host "Please ensure Python 3.10+ is installed and in PATH." -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Cyan
& "venv\Scripts\Activate.ps1"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error activating virtual environment." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if requirements are installed
Write-Host "Checking dependencies..." -ForegroundColor Cyan
$output = python -m pip show crewai 2>$null
if (-not $output) {
    Write-Host "Dependencies not installed." -ForegroundColor Yellow
    Write-Host "Installing requirements..." -ForegroundColor Cyan
    pip install -r requirements.txt
}

# Check if .env file exists
if (-not (Test-Path ".env")) {
    Write-Host ""
    Write-Host "WARNING: .env file not found!" -ForegroundColor Red
    Write-Host "Please copy .env.example to .env and add your OpenAI API key." -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to continue"
}

# Run the application
Write-Host ""
Write-Host "Starting AI Study Assistant..." -ForegroundColor Green
Write-Host ""
python main.py

Read-Host "Press Enter to exit"
