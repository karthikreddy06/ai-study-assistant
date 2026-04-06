# AI Study Assistant - PowerShell Setup Script

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "AI Study Assistant - Complete Setup" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Check Python
Write-Host "[STEP 1] Checking Python installation..." -ForegroundColor Yellow
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "✗ ERROR: Python not found" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Step 2: Upgrade pip
Write-Host "[STEP 2] Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip -q
Write-Host "✓ Pip upgraded" -ForegroundColor Green
Write-Host ""

# Step 3: Install individual packages
Write-Host "[STEP 3] Installing dependencies..." -ForegroundColor Yellow

$packages = @("crewai", "openai", "python-dotenv", "requests", "pydantic")
foreach ($package in $packages) {
    Write-Host "Installing $package..." -ForegroundColor Cyan
    python -m pip install $package -q 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ $package" -ForegroundColor Green
    } else {
        Write-Host "  ⚠ $package (might fail if not available)" -ForegroundColor Yellow
    }
}
Write-Host ""

# Step 4: Verify installation
Write-Host "[STEP 4] Verifying installation..." -ForegroundColor Yellow

$modules = @("crewai", "openai", "dotenv", "requests", "pydantic")
foreach ($module in $modules) {
    $displayName = if ($module -eq "dotenv") { "python-dotenv" } else { $module }
    $importResult = python -c "import $module" 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ $displayName" -ForegroundColor Green
    } else {
        Write-Host "  ⚠ $displayName (not yet available)" -ForegroundColor Yellow
    }
}
Write-Host ""

# Step 5: Create .env if it doesn't exist
Write-Host "[STEP 5] Checking .env configuration..." -ForegroundColor Yellow
if (Test-Path ".env") {
    Write-Host "✓ .env file already exists" -ForegroundColor Green
} else {
    Write-Host "⚠ .env file not found" -ForegroundColor Yellow
    if (Test-Path ".env.example") {
        Copy-Item ".env.example" ".env"
        Write-Host "✓ .env file created from template" -ForegroundColor Green
        Write-Host ""
        Write-Host "IMPORTANT: Edit .env and add your OpenAI API key!" -ForegroundColor Red
        Write-Host "OPENAI_API_KEY=your_key_here" -ForegroundColor Yellow
    }
}
Write-Host ""

# Step 6: Run verification
Write-Host "[STEP 6] Running project verification..." -ForegroundColor Yellow
$pythonInfo = python -c "import sys; print(f'Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}')" 2>&1
Write-Host "  ✓ $pythonInfo" -ForegroundColor Green

$pythonFiles = (Get-ChildItem -Path "." -Filter "*.py" -Recurse).Count
Write-Host "  ✓ Found $pythonFiles Python files" -ForegroundColor Green
Write-Host ""

# Step 7: Ready message
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "✓ Setup Complete!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "NEXT STEPS:" -ForegroundColor Cyan
Write-Host "1. Edit .env file with your OpenAI API key" -ForegroundColor White
Write-Host "2. Run: python main.py" -ForegroundColor White
Write-Host ""
Write-Host "Press Enter to exit..." -ForegroundColor Gray
Read-Host
