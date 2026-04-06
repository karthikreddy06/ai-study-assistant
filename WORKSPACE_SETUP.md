# 🚀 WORKSPACE SETUP - Step-by-Step Guide

## ✅ Setup Options

Choose one method below to set up your workspace:

---

## 🔷 Option 1: Automated Setup (EASIEST)

### For Windows Command Prompt (CMD):
```bash
setup_complete.bat
```

### For Windows PowerShell:
```powershell
.\setup_complete.ps1
```

**What it does:**
- ✅ Verifies Python installation
- ✅ Upgrades pip
- ✅ Installs all dependencies
- ✅ Verifies installations
- ✅ Creates .env file (if missing)
- ✅ Shows next steps

---

## 🔷 Option 2: Manual Setup (STEP-BY-STEP)

### Step 1: Verify Python (30 seconds)
```bash
python --version
```
**Expected Output:** `Python 3.10.x` or higher ✓

### Step 2: Upgrade pip (1 minute)
```bash
python -m pip install --upgrade pip
```

### Step 3: Install Dependencies (3-5 minutes)
```bash
# Install primary dependencies
python -m pip install crewai
python -m pip install openai
python -m pip install python-dotenv
python -m pip install requests
python -m pip install pydantic
```

**Or all at once:**
```bash
pip install crewai openai python-dotenv requests pydantic
```

### Step 4: Verify Installation (1 minute)
```bash
python -c "import crewai; print('✓ CrewAI OK')"
python -c "import openai; print('✓ OpenAI OK')"
python -c "import dotenv; print('✓ python-dotenv OK')"
```

### Step 5: Create .env Configuration
```bash
# Copy template
copy .env.example .env
```

Edit `.env` and add your key:
```env
OPENAI_API_KEY=sk-your_actual_key_here
```

### Step 6: Test Application (30 seconds)
```bash
python main.py
```

---

## 🔷 Option 3: Full Project Structure Setup

### Create Virtual Environment (optional but recommended):
```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate  # Windows CMD/PowerShell
# or
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

---

## 📋 SETUP CHECKLIST

Before running the application, verify:

- [ ] Python 3.10+ installed? (`python --version`)
- [ ] All files extracted? (20+ files visible)
- [ ] Dependencies can install? (Try one: `pip install openai`)
- [ ] `.env` file created? (with `OPENAI_API_KEY`)
- [ ] API key is valid? (from https://platform.openai.com/api-keys)
- [ ] No typos in `.env`? (Check exact format)

---

## 🔧 FILE STRUCTURE AFTER SETUP

```
ai-study-assistant/
├── main.py ........................... ✓ Ready
├── setup_complete.bat ............... ✓ Run this first
├── setup_complete.ps1 ............... ✓ Or this
├── .env ............................. ✓ Create & configure
├── .env.example ..................... ✓ Template
├── requirements.txt ................. ✓ Reference
├── agents/ .......................... ✓ Ready
├── tasks/ ........................... ✓ Ready
├── crew/ ............................ ✓ Ready
└── utils/ ........................... ✓ Ready
```

---

## 📝 .ENV CONFIGURATION

### Copy from .env.example
```bash
copy .env.example .env
```

### Edit .env file
Add your OpenAI API key:
```env
OPENAI_API_KEY=sk-proj-1234567890abcdefghijklmnopqrstuvwxyz
```

**How to get API key:**
1. Go to https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key (starts with `sk-`)
4. **IMPORTANT:** Never share this key!

**Where to put it:**
```
✓ In .env file (safe, recommended)
✗ NOT in code files
✗ NOT in git commits
```

---

## ⚠️ COMMON SETUP ISSUES

### Issue: "Python not found"
**Solution:**
```bash
# Check if Python is in PATH
where python

# If not found, use full path
C:\Users\YourName\AppData\Local\Python\Python314\python.exe main.py

# Or add Python to PATH (see WINDOWS_SETUP.md)
```

### Issue: "ModuleNotFoundError"
**Solution:**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Or manually
pip install openai crewai python-dotenv requests pydantic
```

### Issue: "API key not found"
**Solution:**
1. Verify `.env` exists in project root
2. Check format: `OPENAI_API_KEY=sk-...`
3. No spaces around `=`
4. No quotes around key
5. Restart terminal after creating .env

### Issue: "SSL certificate error"
**Solution:**
```bash
# Install certifi
pip install --upgrade certifi

# Or use --trusted-host
pip install --trusted-host pypi.python.org -r requirements.txt
```

### Issue: "Permission denied"
**Solution:**
```bash
# Run as Administrator (Windows)
# Right-click CMD/PowerShell → "Run as administrator"

# Or use sudo (macOS/Linux)
sudo pip install -r requirements.txt
```

---

## 🎯 VERIFICATION TESTS

### Test 1: Python & Pip
```bash
python --version
pip --version
```

### Test 2: Import All Modules
```bash
python -c "import crewai; import openai; import dotenv; import requests; import pydantic; print('✓ All imports OK')"
```

### Test 3: API Key Configuration
```bash
python -c "import os; from dotenv import load_dotenv; load_dotenv(); key=os.getenv('OPENAI_API_KEY'); print('✓ API key found' if key else '✗ API key missing')"
```

### Test 4: Project Structure
```bash
python -c "from pathlib import Path; files = list(Path('.').glob('**/*.py')); print(f'✓ Found {len(files)} Python files'); agents = list(Path('agents').glob('*.py')); print(f'✓ Found {len(agents)} agent files')"
```

### Test 5: Run Application
```bash
python main.py
```

---

## 📊 EXPECTED SETUP TIME

| Step | Time |
|------|------|
| Option 1 (Automated) | 5-10 min |
| Option 2 (Manual) | 10-15 min |
| Option 3 (Full venv) | 15-20 min |

---

## ✅ YOU'RE READY WHEN

- ✅ Python 3.10+ installed
- ✅ All 20+ files present
- ✅ Dependencies installed (no import errors)
- ✅ `.env` file created with valid API key
- ✅ Can run: `python main.py`
- ✅ Application starts without errors

---

## 🚀 READY TO START?

### If you used Option 1 or 2:
```bash
python main.py
```

### Then:
1. Enter a topic you want to study
2. Watch the AI generate learning materials
3. Answer the quiz
4. Get detailed feedback!

---

## 📍 NEXT STEPS AFTER SETUP

1. **Read Documentation**
   - Quick reference: `QUICK_REFERENCE.md` (2 min)
   - Full guide: `README.md` (20 min)

2. **Try Sample Topics**
   - "Python Functions"
   - "Photosynthesis"
   - "Machine Learning Basics"

3. **Review Results**
   - Look in `study_results/` folder
   - Check saved .txt files
   - Review feedback

4. **Customize (Optional)**
   - Edit agents in `agents/` folder
   - Modify tasks in `tasks/` folder
   - See `CONFIGURATION.md` for options

---

## 💬 STILL NEED HELP?

| Question | Answer |
|----------|--------|
| Can't run setup? | See "Common Issues" above |
| API key problems? | Check FAQ.md #2 and #42 |
| Python not working? | Read WINDOWS_SETUP.md |
| Slow performance? | Normal first run, wait or check internet |
| General help? | Check FAQ.md (100 answers!) |

---

## 🎊 SETUP COMPLETE SUCCESS

You'll know setup worked when:
- ✅ No errors during `pip install`
- ✅ `.env` file has API key
- ✅ `python main.py` starts without errors
- ✅ Application prompts for topic input
- ✅ Can generate explanation, notes, and quiz

---

**Choose Option 1 (automated) or Option 2 (manual) above and get started!** 🚀
