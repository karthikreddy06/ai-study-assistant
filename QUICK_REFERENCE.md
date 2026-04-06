# QUICK REFERENCE CARD

## 🚀 3-MINUTE SETUP

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set API key (.env file)
OPENAI_API_KEY=your_key

# 3. Run application
python main.py
```

## 📂 FILE STRUCTURE

```
ai-study-assistant/
├── main.py              # Main application
├── setup.py             # Auto-setup script
├── requirements.txt     # Dependencies
├── .env.example         # API key template
├── run.bat / run.ps1    # Launchers
├── agents/              # AI agents (4 files)
├── tasks/               # Task definitions (4 files)
├── crew/                # Orchestration (2 files)
├── utils/               # Helpers (2 files)
└── *.md                 # Documentation (6 files)
```

## 🎯 WORKFLOW

```
Topic → Explanation → Notes → Quiz → Evaluation → Save
```

## 📝 KEY FILES TO KNOW

| File | Purpose |
|------|---------|
| main.py | Run app with: `python main.py` |
| .env | Put API key here |
| agents/ | Where AI agents live |
| tasks/ | How jobs are defined |
| crew/crew_setup.py | Orchestrates everything |
| utils/helpers.py | Output & file handling |

## 💻 COMMANDS

```bash
# Setup
python setup.py           # Automated setup

# Run
python main.py            # Start application
run.bat                   # Windows batch launcher
./run.ps1                 # PowerShell launcher

# Install
pip install -r requirements.txt

# Activate venv (Windows)
venv\Scripts\activate
```

## 🔑 API KEY

1. Go to https://platform.openai.com/api-keys
2. Create key (starts with `sk-`)
3. Add to `.env`: `OPENAI_API_KEY=sk-...`

## 📚 DOCUMENTATION

| File | Info |
|------|------|
| README.md | Full guide |
| WINDOWS_SETUP.md | Windows help |
| CONFIGURATION.md | Advanced options |
| FAQ.md | 100 Q&A |
| PROJECT_SUMMARY.md | Overview |
| INSTALLATION_SUMMARY.md | Installation |

## 🐛 QUICK FIXES

```
Issue: API key not found
→ Create .env file with API key

Issue: Module not found
→ pip install -r requirements.txt

Issue: Python not found
→ Use full path or add to PATH

Issue: Slow response
→ Normal first run, check internet
```

## 🎓 TIPS

✅ Use specific topics (not too broad)
✅ Read all materials carefully
✅ Answer quiz questions thoughtfully
✅ Save results for revision
✅ Try different topics

## 📊 WHAT YOU GET

- ✅ Explanation (800+ words)
- ✅ Study Notes (10+ points)
- ✅ Quiz (8-10 questions)
- ✅ Evaluation (with scores)
- ✅ Saved Results (.txt file)

## ⚙️ CUSTOMIZATION

Want to change something?

| What | Where |
|------|-------|
| Agent behavior | `agents/*.py` |
| Task descriptions | `tasks/*.py` |
| Colors | `utils/helpers.py` |
| Questions count | `tasks/quiz_task.py` |
| Output format | `utils/helpers.py` |
| Save location | `utils/helpers.py` |

## 🆘 HELP

```bash
# View README
cat README.md

# View Windows setup
cat WINDOWS_SETUP.md

# View FAQ
cat FAQ.md

# Check configuration options
cat CONFIGURATION.md
```

## 📱 SYSTEM REQUIREMENTS

- Python 3.10+
- Internet connection
- OpenAI API key
- 512MB RAM minimum
- 500MB disk space

## 💰 COSTS

- Typical session: $0.01 - $0.10
- Check OpenAI rates: https://openai.com/pricing
- Set limits to control costs (see CONFIGURATION.md)

## 🌐 PLATFORMS

- ✅ Windows
- ✅ macOS  
- ✅ Linux
- ✅ Cloud services

## 📍 GETTING HELP

1. Check README.md
2. Check WINDOWS_SETUP.md (Windows users)
3. Check FAQ.md (100 questions)
4. Check CONFIGURATION.md (custom options)
5. Read code comments

## 🎬 QUICK START EXAMPLE

```bash
# Terminal
$ python main.py

# Input
Enter topic: Python Functions

# Output
[Detailed explanation]
[Study notes]
[Quiz questions]

# Answer
Your answers: Q1: A, Q2: B, Q3: A function is...

# Result
[Evaluation with score]

# Save
Save results? yes
✓ Saved to: study_results/...
```

## 📈 FEATURES

- Multi-agent AI system
- Interactive learning
- Quiz generation
- Answer evaluation
- Result saving
- Colored output
- Error handling
- Full customization

## 🎯 BEST USE CASES

✅ Academic study
✅ Professional training
✅ Self-directed learning
✅ Exam preparation
✅ Concept explanation
✅ Quick summaries
✅ Skill development

## 🚀 DEPLOYMENT OPTIONS

- Local machine (easiest)
- Cloud services (AWS/Azure/GCP)
- Docker container
- Virtual machine
- Server/VPS

## 📊 PERFORMANCE

- First run: ~2-5 minutes
- Typical session: 2-5 minutes
- Follow-up sessions: <5 minutes
- Network usage: 1-10MB per session
- Cost: $0.01-$0.10 per session

## ⭐ PROJECT STATS

- 20+ files created
- 1500+ lines of code
- 5+ documentation files
- 4 specialized agents
- 15+ features
- 100+ FAQ answers

## 🏆 HIGHLIGHTS

1. ✨ Clean, modular code
2. 📚 Comprehensive documentation
3. 🔧 Highly customizable
4. 🎯 Production-ready
5. 💻 Windows-optimized
6. 🚀 Easy to use
7. 🎓 Educational value
8. 🤖 Advanced AI architecture

## 📝 QUICK REFERENCE

```python
# How agents work
@agents: Teacher, Notes, Quiz, Evaluator
@flow: Sequential (one after another)
@model: GPT-4 (customizable)
@language: Python 3.10+

# How to use
topic → crew.kickoff() → results

# How to customize
Edit agents/*.py or tasks/*.py files
```

## 🎊 READY TO START?

```bash
1. pip install -r requirements.txt
2. Create .env with OPENAI_API_KEY
3. python main.py
4. Enter a topic and learn!
```

---

**See full documentation files for detailed information!** 📖

*Bookmark this for quick reference* ⭐
