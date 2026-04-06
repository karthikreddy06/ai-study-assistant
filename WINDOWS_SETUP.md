# AI Study Assistant - Windows Setup Guide

## Windows-Specific Installation Guide

This guide provides step-by-step instructions for setting up the AI Study Assistant on Windows.

### Prerequisites

- **Python 3.10 or higher** - [Download here](https://www.python.org/downloads/)
- **OpenAI API Key** - [Get it here](https://platform.openai.com/api-keys)
- **Terminal/Command Prompt** (PowerShell or CMD)

### Step 1: Download and Extract Project

1. Download the project files
2. Extract to your desired location (e.g., `C:\Users\YourUsername\AI Study Assistant`)
3. Open Command Prompt or PowerShell in the project directory

### Step 2: Verify Python Installation

Open Command Prompt and run:

```cmd
python --version
```

Should show: `Python 3.10.x` or higher

If you get "python is not recognized", add Python to PATH or use the full path to Python.

### Step 3: Create Virtual Environment

Run in the project directory:

```cmd
python -m venv venv
```

This creates a `venv` folder (may take a minute).

### Step 4: Activate Virtual Environment

**Using Command Prompt (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Using PowerShell:**
```powershell
venv\Scripts\Activate.ps1
```

You should see `(venv)` prefix in your terminal prompt.

**Note:** If PowerShell gives an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Step 5: Install Dependencies

With virtual environment activated, run:

```cmd
pip install -r requirements.txt
```

This may take 2-3 minutes. You'll see packages being installed.

### Step 6: Configure Environment Variables

1. In the project directory, find or create a `.env` file
2. Add your OpenAI API key:

```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

**Where to get your API key:**
1. Go to https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key (it starts with `sk-`)
4. Paste it in the `.env` file

### Step 7: Run the Application

With virtual environment still activated, run:

```cmd
python main.py
```

You should see the welcome screen!

### Quick Start Script (Alternative)

If you prefer automated setup, run:

```cmd
python setup.py
```

This script will:
- Check Python version
- Create virtual environment
- Install dependencies
- Set up .env file

## Troubleshooting for Windows

### Issue: "python is not recognized"

**Solution 1:** Use full path to Python:
```cmd
C:\Users\YourUsername\AppData\Local\Programs\Python\Python310\python.exe -m venv venv
```

**Solution 2:** Add Python to PATH:
1. Search for "Environment Variables" in Windows
2. Click "Edit the system environment variables"
3. Click "Environment Variables"
4. Under "System variables", find and select `Path`
5. Click "Edit"
6. Click "New" and add your Python installation path (e.g., `C:\Users\YourUsername\AppData\Local\Programs\Python\Python310`)
7. Click OK and restart terminal

### Issue: "venv is not activated"

Check if terminal shows `(venv)` before the prompt. If not, run:

**CMD:**
```cmd
venv\Scripts\activate.bat
```

**PowerShell:**
```powershell
venv\Scripts\Activate.ps1
```

### Issue: "ModuleNotFoundError: No module named 'crewai'"

Run:
```cmd
pip install -r requirements.txt
```

Make sure virtual environment is activated (see `(venv)` in prompt).

### Issue: "OPENAI_API_KEY not found"

1. Check that `.env` file exists in project root
2. Verify the exact content is: `OPENAI_API_KEY=your_key_here`
3. Restart the terminal after creating/editing `.env`

### Issue: "ModuleNotFoundError" after installation

Try upgrading pip:
```cmd
python -m pip install --upgrade pip
```

Then reinstall requirements:
```cmd
pip install -r requirements.txt
```

### Issue: PowerShell Execution Policy Error

Run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate venv again.

## Using the Application

### Basic Usage

```cmd
python main.py
```

### Enter a Topic

When prompted, type a topic you want to learn about:
```
Topic: Photosynthesis
```

### Answer the Quiz

Copy the quiz to a text file, answer the questions, then paste your answers like:
```
Q1: A
Q2: B
Q3: The process by which plants convert sunlight into chemical energy
Q4: C
Q5: True
```

### Save Results

When asked if you want to save results, type `yes` to save all materials to a file.

## File Locations

- **Project folder:** Where you extracted the files
- **Virtual environment:** `venv/` subfolder
- **Saved results:** `study_results/` subfolder
- **Environment settings:** `.env` file in root directory

## Keeping Your System Updated

To update packages later:

```cmd
pip install --upgrade -r requirements.txt
```

To see what's installed:

```cmd
pip list
```

## Uninstalling/Cleanup

To remove the virtual environment:

```cmd
rmdir /s venv
```

To completely uninstall Python from Windows, use:
- Settings → Apps → Add or remove programs → Find Python → Uninstall

## Next Steps

1. ✅ Complete the setup above
2. 📖 Read the main README.md
3. 🚀 Run `python main.py`
4. 📚 Try with test topics
5. 💾 Save your results

## Getting Help

If you're still having issues:

1. **Check Python version:** `python --version` (should be 3.10+)
2. **Verify API key:** Check that `.env` has valid key
3. **Reinstall packages:** `pip install --force-reinstall -r requirements.txt`
4. **Restart terminal:** Sometimes terminal needs refresh
5. **Check internet:** Ensure you have active internet connection

## System Requirements

| Item | Requirement |
|------|-------------|
| OS | Windows 10/11 |
| Python | 3.10+ |
| RAM | 4GB minimum, 8GB recommended |
| Disk Space | 2GB free space |
| Internet | Required (for OpenAI API calls) |

---

**Ready to learn? Run `python main.py` and enjoy! 🎓**
