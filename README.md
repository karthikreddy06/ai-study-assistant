# AI Study Assistant - Multi-Agent Learning System

An intelligent, collaborative AI-powered learning system using CrewAI framework. Multiple AI agents work together to teach, take notes, generate quizzes, and evaluate student performance.

## 🎯 Project Overview

The AI Study Assistant is a sophisticated multi-agent system that revolutionizes personalized learning. It simulates a complete educational workflow:

1. **Teacher Agent** - Explains topics clearly and breaks them into digestible concepts
2. **Notes Agent** - Converts explanations into well-structured study materials
3. **Quiz Agent** - Generates comprehensive assessments with multiple question types
4. **Evaluator Agent** - Assesses student answers and provides constructive feedback

## ✨ Key Features

- **Multi-Agent Collaboration** - Specialized AI agents working in harmony
- **Comprehensive Learning Path** - From explanation through evaluation
- **Structured Output** - Professional study materials and assessments
- **Interactive CLI** - User-friendly command-line interface
- **Result Persistence** - Save all study materials and evaluations
- **Error Handling** - Robust error management and validation
- **Colored Output** - Beautiful, readable terminal interface
- **Logging** - Built-in logging for tracking operations

## 🏗️ Project Structure

```
ai-study-assistant/
├── agents/                    # AI Agent definitions
│   ├── __init__.py
│   ├── teacher_agent.py      # Explains topics
│   ├── notes_agent.py        # Creates study notes
│   ├── quiz_agent.py         # Generates quizzes
│   └── evaluator_agent.py    # Evaluates answers
│
├── tasks/                     # Task definitions for agents
│   ├── __init__.py
│   ├── teaching_task.py      # Teaching task
│   ├── notes_task.py         # Note-taking task
│   ├── quiz_task.py          # Quiz generation task
│   └── evaluation_task.py    # Evaluation task
│
├── crew/                      # Crew orchestration
│   ├── __init__.py
│   └── crew_setup.py         # Crew configuration and execution
│
├── utils/                     # Utility functions
│   ├── __init__.py
│   └── helpers.py            # Helper functions for CLI, file I/O, etc.
│
├── main.py                    # Main CLI application entry point
├── requirements.txt           # Python dependencies
├── .env.example              # Example environment configuration
└── README.md                 # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- OpenAI API key (or compatible LLM API)
- pip (Python package manager)

### Installation

1. **Clone or download the project**

```bash
cd ai-study-assistant
```

2. **Create a Python virtual environment** (recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the project root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

Or set it as a system environment variable:

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY = "your_api_key_here"
```

**Windows (CMD):**
```cmd
set OPENAI_API_KEY=your_api_key_here
```

**macOS/Linux:**
```bash
export OPENAI_API_KEY="your_api_key_here"
```

## 💻 How to Run

### Basic Usage

```bash
python main.py
```

The application will:
1. Prompt you to enter a topic
2. Generate a detailed explanation
3. Create study notes
4. Generate a quiz
5. Allow you to answer questions
6. Provide evaluation and feedback
7. Optionally save results to a file

### Example Session

```
$ python main.py

================================================================================
  AI STUDY ASSISTANT - MULTI-AGENT LEARNING SYSTEM
================================================================================

Welcome! This system helps you learn any topic with AI-powered assistance.

How it works:
  1. You provide a topic you want to learn
  2. Teacher Agent explains the topic clearly
  3. Notes Agent creates study notes
  4. Quiz Agent generates assessment questions
  5. You answer the quiz questions
  6. Evaluator Agent provides feedback and scores your answers

Let's get started!

Enter the topic you want to study (e.g., 'Photosynthesis', 'Python Functions'):
Topic: Photosynthesis

📚 Starting learning phase...

[████████████████████████████] 33% - Generating teaching explanation

STEP 1: TEACHER'S EXPLANATION
================================================================================

[Detailed explanation of photosynthesis...]

STEP 2: STUDY NOTES
================================================================================

[Structured study notes...]

STEP 3: QUIZ TIME!
================================================================================

[Quiz questions...]

Your answers: Q1: A, Q2: B, Q3: The process by which plants convert sunlight...

📊 Starting evaluation phase...

STEP 4: EVALUATION RESULTS
================================================================================

[Evaluation and feedback...]

Would you like to save all results to a file? (yes/no)
Save results? (yes/no): yes
✓ Results saved successfully to: study_results/study_results_photosynthesis_20240101_101530.txt
```

## 📋 Agent Specifications

### 1. Teacher Agent

- **Role:** Excellent Teacher
- **Goal:** Explain complex topics clearly and break them into simple concepts
- **Responsibility:** Provide comprehensive, beginner-friendly explanations

### 2. Notes Agent

- **Role:** Academic Note-Taker
- **Goal:** Convert explanations into structured study notes
- **Responsibility:** Create bullet points, key takeaways, and revision materials

### 3. Quiz Agent

- **Role:** Quiz Master
- **Goal:** Generate comprehensive quizzes with varied question types
- **Responsibility:** Create MCQ and short-answer questions of varying difficulty

### 4. Evaluator Agent

- **Role:** Expert Evaluator & Feedback Provider
- **Goal:** Assess answers with fairness and provide constructive feedback
- **Responsibility:** Score responses and identify learning gaps

## 🔄 Workflow Explanation

```
┌─────────────┐
│   Topic     │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│ Teacher Agent       │ ─────► Explanation
│ (Explains Topic)    │
└─────────────────────┘
       │
       ▼
┌─────────────────────┐
│ Notes Agent         │ ─────► Study Notes
│ (Takes Notes)       │
└─────────────────────┘
       │
       ▼
┌─────────────────────┐
│ Quiz Agent          │ ─────► Quiz Questions
│ (Generates Tasks)   │
└─────────────────────┘
       │
       ▼
┌─────────────────────┐
│ User Input          │ ─────► User Answers
│ (Answer Quiz)       │
└─────────────────────┘
       │
       ▼
┌─────────────────────┐
│ Evaluator Agent     │ ─────► Evaluation & Score
│ (Assesses Answers)  │
└─────────────────────┘
```

## 📁 Output Files

Results are saved in the `study_results/` directory with the following naming format:

```
study_results_[topic]_[YYYYMMDD_HHMMSS].txt
```

Each file contains:
- Topic and timestamp
- Full teacher explanation
- Complete study notes
- All quiz questions
- Evaluation results and scores

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for LLM access | Yes |

### Advanced Configuration

Edit `crew/crew_setup.py` to:
- Change the LLM model (default: gpt-4)
- Adjust crew process (sequential/hierarchical)
- Modify agent parameters

## 🧪 Testing

Run the application with a test topic:

```bash
python main.py
# Enter: "Python List Methods"
```

## 🐛 Error Handling

The application includes comprehensive error handling for:

- Missing API key
- Network/API errors
- Invalid user input
- File I/O errors

Error messages are displayed in red with helpful guidance.

## 📝 Logging

The system logs all major operations:
- Session start/end
- Topic validation
- Agent execution
- Phase completion
- Errors

Logs appear with timestamps in the format: `[YYYY-MM-DD HH:MM:SS]`

## 🎨 CLI Features

- **Colored Output:** Easy-to-read colored terminal text
- **Progress Indicators:** Visual progression through phases
- **Structured Sections:** Clear separation of content
- **User-Friendly Prompts:** Clear instructions for input
- **Emoji Indicators:** Visual cues for different operations

## 📚 Example Topics to Try

- Photosynthesis
- Python List Methods
- World War II
- Machine Learning Basics
- Quantum Computing
- Biology Cell Structure
- History of the Internet
- Creative Writing Techniques

## 🔐 Security Notes

- Keep your `.env` file private - never commit it to version control
- Use a `.gitignore` entry: `*.env` and `.env`
- Rotate your API keys regularly
- Don't share your API key in code or documentation

## 💡 Tips for Best Results

1. **Clear Topics:** Use specific, well-defined topics for better explanations
2. **Detailed Answers:** Provide thorough quiz answers for better evaluation
3. **Follow Format:** When answering, use the suggested format (Q1: A, Q2: B, etc.)
4. **Save Results:** Keep saved files for future reference
5. **Review Materials:** Read through notes before answering quiz

## 🚀 Next Steps / Future Enhancements

Potential additions to this project:
- Web interface using Streamlit or Flask
- Database integration for tracking progress
- Multiple difficulty levels
- Audio explanations
- Spaced repetition system
- Progress analytics
- Peer learning features
- Real-time progress tracking

## 🤝 Contributing

Feel free to:
- Report issues
- Suggest improvements
- Add new agent types
- Enhance the UI/UX
- Optimize performance

## 📄 License

This project is provided as-is for educational and learning purposes.

## ⚠️ Troubleshooting

### "OPENAI_API_KEY not found"
- Check that `.env` file exists in project root
- Verify API key is correctly set
- Try restarting the terminal

### "ModuleNotFoundError: No module named 'crewai'"
- Run: `pip install -r requirements.txt`
- Verify virtual environment is activated

### "crewai version mismatch"
- Update packages: `pip install --upgrade -r requirements.txt`

### Slow responses
- Normal for first-time use (agent initialization)
- Check internet connection
- Verify OpenAI API status

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify environment setup
3. Check API key validity
4. Review error messages carefully

## 📖 Additional Resources

- [CrewAI Documentation](https://docs.crewai.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)

---

**Happy Learning! 🎓**

Build with ❤️ using CrewAI and OpenAI
