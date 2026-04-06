@echo off
REM AI Study Assistant - Comprehensive Setup Script

echo.
echo ============================================
echo AI Study Assistant - Complete Setup
echo ============================================
echo.

REM Step 1: Check Python
echo [STEP 1] Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python not found
    pause
    exit /b 1
)
echo ✓ Python found
echo.

REM Step 2: Upgrade pip
echo [STEP 2] Upgrading pip...
python -m pip install --upgrade pip
echo ✓ Pip upgraded
echo.

REM Step 3: Install individual packages
echo [STEP 3] Installing dependencies...

echo Installing crewai...
python -m pip install crewai
if errorlevel 1 echo WARNING: crewai might not be available yet

echo Installing openai...
python -m pip install openai

echo Installing python-dotenv...
python -m pip install python-dotenv

echo Installing requests...
python -m pip install requests

echo Installing pydantic...
python -m pip install pydantic

echo.
echo ✓ Dependencies installed (see warnings above if any)
echo.

REM Step 4: Verify installation
echo [STEP 4] Verifying installation...
python -c "import crewai; print('✓ CrewAI imported successfully')" 2>nul || echo ⚠ CrewAI import failed
python -c "import openai; print('✓ OpenAI imported successfully')" 2>nul || echo ⚠ OpenAI import failed
python -c "import dotenv; print('✓ python-dotenv imported successfully')" 2>nul || echo ⚠ python-dotenv import failed
python -c "import requests; print('✓ Requests imported successfully')" 2>nul || echo ⚠ Requests import failed
python -c "import pydantic; print('✓ Pydantic imported successfully')" 2>nul || echo ⚠ Pydantic import failed
echo.

REM Step 5: Create .env if it doesn't exist
echo [STEP 5] Checking .env configuration...
if exist ".env" (
    echo ✓ .env file already exists
) else (
    echo ⚠ .env file not found
    echo Creating .env from template...
    copy .env.example .env
    echo ✓ .env file created
    echo.
    echo IMPORTANT: Edit .env and add your OpenAI API key!
    echo OPENAI_API_KEY=your_key_here
)
echo.

REM Step 6: Run verification
echo [STEP 6] Running project verification...
python -c "import sys; print(f'✓ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}')"
python -c "from pathlib import Path; import json; files = list(Path('.').glob('**/*.py')); print(f'✓ Found {len(files)} Python files')"
echo.

REM Step 7: Ready message
echo ============================================
echo ✓ Setup Complete!
echo ============================================
echo.
echo NEXT STEPS:
echo 1. Edit .env file with your OpenAI API key
echo 2. Run: python main.py
echo.
pause
