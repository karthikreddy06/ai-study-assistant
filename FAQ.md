# Frequently Asked Questions (FAQ)

## Installation & Setup

### Q1: Do I need to install anything else besides Python?
**A:** No, only Python 3.10+ is required. All other dependencies are in `requirements.txt` and will be installed via pip.

### Q2: How do I get an OpenAI API key?
**A:** 
1. Go to https://platform.openai.com/api-keys
2. Sign in with your OpenAI account (create one if needed)
3. Click "Create new secret key"
4. Copy the key (starts with "sk-")
5. Add it to your `.env` file as: `OPENAI_API_KEY=sk-...`

### Q3: Will this work without an API key?
**A:** No, an OpenAI API key is required to run the application.

### Q4: Can I use a different LLM service instead of OpenAI?
**A:** Yes, with some modifications. See CONFIGURATION.md for details on using Azure OpenAI or other providers.

### Q5: Which version of Python should I use?
**A:** Python 3.10 or higher. We recommend Python 3.11 or 3.12 for best performance.

### Q6: What if Python isn't recognized in my terminal?
**A:** Either:
- Use the full path to Python (e.g., `C:\Python311\python.exe`)
- Add Python to your system PATH
- Open a new terminal after installing Python

### Q7: How do I create a virtual environment?
**A:**
```bash
python -m venv venv
# Then activate it:
venv\Scripts\activate  # Windows CMD
# or
venv\Scripts\Activate.ps1  # Windows PowerShell
# or
source venv/bin/activate  # macOS/Linux
```

### Q8: What does "venv" mean?
**A:** Virtual environment - an isolated Python workspace for this project to prevent conflicts with other Python projects.

### Q9: Can I run this on Windows/Mac/Linux?
**A:** Yes! It works on all three. Installation steps are similar, with slight differences in activation commands.

### Q10: How much storage space does this need?
**A:** 
- Initial download: ~200MB
- Virtual environment: ~200-300MB
- Saved results: Varies (typically 100KB-2MB per session)
- Total: ~500MB to 1GB recommended

## Usage & Functionality

### Q11: What topics can I study?
**A:** Any topic you want! History, science, math, programming, languages, arts, etc. Try "Photosynthesis", "Python Functions", "World War II", etc.

### Q12: Does it work with very broad topics?
**A:** Better results with specific topics. Instead of "Science", try "Photosynthesis" or "Cell Structure".

### Q13: Can I study multiple topics in one session?
**A:** Currently the application handles one topic per session, but you can restart for new topics.

### Q14: How long does it take to study one topic?
**A:** Typically 2-5 minutes depending on topic complexity and internet speed. First run may take longer.

### Q15: Can I interrupt the application?
**A:** Yes, press Ctrl+C to stop. Your work will be lost unless you saved it.

### Q16: What format should my quiz answers be in?
**A:** Follow the format shown:
```
Q1: A
Q2: B
Q3: Your detailed answer here
Q4: C
Q5: True
```

### Q17: Can the evaluator handle all answer formats?
**A:** Yes! It handles multiple choice (A/B/C/D), True/False, and short answers.

### Q18: How accurate is the evaluation?
**A:** The evaluator uses AI to assess answers fairly, but quality depends on answer clarity and topic complexity.

### Q19: Can I get scores for my answers?
**A:** Yes! The evaluator provides:
- Individual question scores
- Overall percentage score
- Performance level assessment
- Detailed feedback

### Q20: What if I don't want to answer the quiz?
**A:** Just press Enter or type nothing when asked. The program will skip evaluation.

## Results & Output

### Q21: Where are my study results saved?
**A:** In the `study_results/` folder in your project directory.

### Q22: What format are the saved files?
**A:** Plain text (.txt) files with all materials organized in sections.

### Q23: Can I share the saved files?
**A:** Yes! The .txt files can be opened in any text editor or shared with others.

### Q24: What's the filename format?
**A:** `study_results_[topic]_[YYYYMMDD_HHMMSS].txt`
Example: `study_results_photosynthesis_20240101_143022.txt`

### Q25: Can I change the output format?
**A:** Yes, edit `utils/helpers.py` to customize the `create_full_report()` function.

### Q26: How big are the saved files?
**A:** Typically 50KB-500KB per session depending on topic length and quiz complexity.

### Q27: Can I export results to PDF?
**A:** Not directly, but you can open the .txt file and print to PDF.

### Q28: Can I organize results by topic?
**A:** Yes, the topic name is in the filename. You can create subfolders manually.

### Q29: Is my data stored on OpenAI's servers?
**A:** Your prompts are sent to OpenAI's API but not stored long-term. See OpenAI's privacy policy for details.

### Q30: Can I delete old results?
**A:** Yes, simply delete the files from the `study_results/` folder.

## Configuration & Customization

### Q31: How do I change which AI model is used?
**A:** Edit your `.env` file:
```env
OPENAI_MODEL=gpt-3.5-turbo  # Cheaper, faster
OPENAI_MODEL=gpt-4          # More capable, slower
```

### Q32: Can I make the explanations longer or shorter?
**A:** Yes, modify the task descriptions in `tasks/teaching_task.py`.

### Q33: How do I change the number of quiz questions?
**A:** Edit `tasks/quiz_task.py` and change "8-10 questions" to your preferred number.

### Q34: Can I customize the agent personalities?
**A:** Yes! Edit the `backstory` and `goal` in each agent file.

### Q35: How do I add custom colors to the output?
**A:** Edit the `Colors` class in `utils/helpers.py`.

### Q36: Can I disable colored output?
**A:** Yes, modify `main.py` to call `print()` instead of `print_colored()`.

### Q37: How do I enable more detailed logging?
**A:** Change `verbose=False` to `verbose=True` in `agents/` files.

### Q38: Can I change the study results folder name?
**A:** Yes, edit `utils/helpers.py` line with `results_dir = Path("new_name")`.

### Q39: Can I set a custom API timeout?
**A:** Yes, see CONFIGURATION.md for advanced options.

### Q40: How do I run this without saving results?
**A:** Simply answer "no" when asked if you want to save results.

## Performance & Troubleshooting

### Q41: Why is the application slow?
**A:** 
- First run initializes agents (normal)
- Slow internet connection
- OpenAI API is slow
- Using a slower model (gpt-3.5-turbo)

Solution: Use gpt-3.5-turbo for faster (but less capable) responses.

### Q42: I'm getting "OPENAI_API_KEY not found" error
**A:**
1. Create `.env` file in project root
2. Add: `OPENAI_API_KEY=your_key_here`
3. Restart terminal
4. Run application again

### Q43: Getting "ModuleNotFoundError" errors?
**A:**
```bash
pip install -r requirements.txt
```
Make sure virtual environment is activated.

### Q44: What does "connection timeout" mean?
**A:** Your internet connection is too slow or OpenAI API is temporarily down. Try again later.

### Q45: Can't activate virtual environment on Windows?
**A:**
PowerShell: Update execution policy
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try: `venv\Scripts\Activate.ps1`

### Q46: Application crashes randomly?
**A:**
- Check API key has quota
- Try with simpler topic
- Update packages: `pip install --upgrade -r requirements.txt`
- Restart terminal

### Q47: Output is garbled or showing strange characters?
**A:** Terminal encoding issue. Try:
- Windows: Use Windows Terminal instead of CMD
- macOS/Linux: Check terminal encoding settings

### Q48: Am I being charged for API usage?
**A:** Yes, OpenAI charges for API usage. Check your OpenAI account for usage details and costs.

### Q49: How much does it cost to run?
**A:** Depends on OpenAI's pricing and your usage. Typical session: $0.01-$0.10.

### Q50: How can I reduce costs?
**A:**
- Use gpt-3.5-turbo instead of gpt-4
- Set token limits in configuration
- Reduce number of questions in quiz

## Advanced Questions

### Q51: Can I run multiple study sessions in parallel?
**A:** Not recommended. Run them sequentially for now.

### Q52: Can I integrate this with other tools?
**A:** Yes, with modifications. See CONFIGURATION.md for integration examples.

### Q53: How can I add a web interface?
**A:** Build a Flask/Streamlit wrapper. See CONFIGURATION.md for examples.

### Q54: Can I add database storage?
**A:** Yes, modify helpers.py to save to SQLite or other databases.

### Q55: How do I contribute improvements?
**A:** Fork the project and submit changes. See comments in code for improvement ideas.

### Q56: Can I use this for educational institutions?
**A:** Possibly, but check OpenAI's terms. May need institutional API account.

### Q57: What's the maximum topic complexity it can handle?
**A:** The AI can handle most topics, but very niche topics may have limited explanations.

### Q58: Can I feed it custom data instead of letting it generate?
**A:** Yes, modify tasks to accept predefined content in CONFIGURATION.md.

### Q59: How do I implement spaced repetition?
**A:** See CONFIGURATION.md for example code to store and schedule reviews.

### Q60: Can I use this offline?
**A:** No, requires internet connection for OpenAI API calls.

## Getting Help

### Q61: Where can I find more help?
**A:** 
1. Check README.md - comprehensive guide
2. Check WINDOWS_SETUP.md - Windows specific help
3. Check CONFIGURATION.md - advanced options
4. Look at the code comments

### Q62: How do I report a bug?
**A:** 
1. Note the error message
2. Check if .env has valid API key
3. Try reinstalling dependencies
4. Check terminal output for details

### Q63: What should I do if the AI gives wrong information?
**A:** 
1. Try rephrasing the topic
2. Verify the answer independently
3. Try a different AI model

### Q64: Can the AI misunderstand my question?
**A:** Yes, AI can make mistakes. Always verify important information.

### Q65: Is this suitable for academic study?
**A:** Yes, as a study aid. But verify all information and don't rely solely on AI-generated content.

### Q66: Can I use results for publishing?
**A:** The AI-generated content is based on training data. Always cite sources properly.

### Q67: What if the explanation is too technical?
**A:** Edit the task description to ask for simpler explanations (see CONFIGURATION.md).

### Q68: What if the quiz is too hard?
**A:** Edit quiz_task.py to adjust difficulty levels.

### Q69: Can the bot hallucinate (make up information)?
**A:** Rarely, but it can happen. Always verify important facts.

### Q70: How do I provide feedback about the results?
**A:** Use the results to identify areas for improvement and study those topics more.

## System & Requirements

### Q71: What OS is supported?
**A:** Windows, macOS, and Linux - all with Python 3.10+

### Q72: Do I need GPU for this?
**A:** No, it runs on CPU. GPU not required.

### Q73: How much RAM do I need?
**A:** Minimum 2GB, recommended 4GB+

### Q74: How much internet bandwidth is required?
**A:** Moderate usage - typically 1-10MB per session

### Q75: Can I run this on old computers?
**A:** If they support Python 3.10+ and have decent internet, yes.

### Q76: Does this work on Raspberry Pi?
**A:** Possibly, if Raspberry Pi OS supports Python 3.10+. May be slow.

### Q77: Can I run it on cloud services (AWS, Azure, etc.)?
**A:** Yes, with appropriate Python environment setup.

### Q78: What about mobile devices?
**A:** Not tested, but theoretically possible with Python support on mobile.

### Q79: Can I run this in Docker?
**A:** Yes, create a Dockerfile with Python 3.10+ and required dependencies.

### Q80: Is this tool open source?
**A:** Yes, provided for educational purposes. Modify as needed.

## Final Questions

### Q81: What's the difference between this and ChatGPT?
**A:** This uses CrewAI to orchestrate multiple specialized agents for structured learning workflows.

### Q82: Why use multiple agents instead of one AI?
**A:** Different agents focus on different tasks better (teaching vs. testing vs. evaluation).

### Q83: Can I use this indefinitely?
**A:** Yes, as long as your OpenAI API account has available credits.

### Q84: What happens if my API key expires?
**A:** Requests will fail. Generate a new key and update .env file.

### Q85: Can I share my API key with others?
**A:** No! Keep your API key private. Anyone with it can use your account and incur charges.

### Q86: What's the best way to use this application?
**A:** 
1. Study a topic
2. Review the notes
3. Take the quiz
4. Study areas where you struggled
5. Save results for review

### Q87: How often should I use this?
**A:** As often as you want - no daily limits except your OpenAI API quota.

### Q88: Can I combine this with human tutoring?
**A:** Yes! AI can't replace human teachers, but it's great supplementary learning.

### Q89: Is this for students only?
**A:** No, anyone wanting to learn new topics can use it.

### Q90: What makes this better than other learning tools?
**A:** Multi-agent collaboration, interactive workflow, and immediate feedback.

### Q91: Can I customize everything?
**A:** Almost everything! See CONFIGURATION.md for extensive customization options.

### Q92: Project won't start - what do I do?
**A:**
1. Check Python version: `python --version`
2. Check API key in .env
3. Check dependencies: `pip install -r requirements.txt`
4. Restart terminal
5. Try again

### Q93: Which file should I edit to change [X]?
**A:** 
- Agent behavior: Edit `agents/` files
- Task descriptions: Edit `tasks/` files
- UI/Output: Edit `main.py` or `utils/helpers.py`
- See CONFIGURATION.md for specifics

### Q94: Can I use this for professional training?
**A:** Possibly, with appropriate OpenAI terms compliance and verification of content.

### Q95: What's the best topic to start with?
**A:** Something moderate - not too simple, not too complex. Example: "Machine Learning Basics"

### Q96: How do I get the most from study results?
**A:** Read carefully, take your own notes, try the quiz multiple times, identify weak areas.

### Q97: Can I export quiz for offline use?
**A:** Yes, saved results include quiz questions in .txt format.

### Q98: Is there a mobile app version?
**A:** Not currently, but you can build one using this as backend.

### Q99: Can I use this for language learning?
**A:** Yes! Try topics like "Spanish Grammar Basics" or "French Pronunciation".

### Q100: Where do I go from here?
**A:** 
1. Read all documentation
2. Try multiple topics
3. Explore customization options
4. Integrate with other tools if needed
5. Share your results and feedback

---

**Still have questions? Check the relevant documentation files or examine the code comments for implementation details.** 📚

Happy Learning! 🎓
