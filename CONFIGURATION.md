# Configuration Guide

## Project Configuration

This guide explains all configuration options and customization possibilities for the AI Study Assistant.

## Environment Variables

### Required Variables

#### OPENAI_API_KEY
- **Purpose:** Authentication for OpenAI API
- **Format:** Starts with `sk-`
- **Example:** `OPENAI_API_KEY=sk-proj-1234567890abcdef`
- **Getting your key:** https://platform.openai.com/api-keys

### Optional Variables

```env
# Specify OpenAI model (default: gpt-4)
OPENAI_MODEL=gpt-4

# Set temperature for creativity (0-2)
# Lower = more deterministic, Higher = more creative
OPENAI_TEMPERATURE=0.7

# Set max tokens per request (default: 4000)
OPENAI_MAX_TOKENS=4000
```

## Agent Configuration

### Modifying Agent Behavior

Edit `agents/` files to customize agent personalities and goals.

#### Teacher Agent (`agents/teacher_agent.py`)

```python
# Modify the goal
goal="Explain complex topics in a clear, engaging, and educational manner. "
     "Break down topics into simple, understandable concepts for beginners."

# Modify the backstory
backstory="You are an experienced educator with 20+ years of teaching experience..."
```

### Task Configuration

Edit `tasks/` files to modify task descriptions and expected outputs.

#### Teaching Task (`tasks/teaching_task.py`)

```python
description=f"""
Explain the topic: "{topic}" in a clear, structured, and engaging manner.
...
"""
```

## Application Configuration

### CLI Output Configuration

In `utils/helpers.py`, modify color codes:

```python
class Colors:
    HEADER = '\033[95m'    # Magenta
    BLUE = '\033[94m'
    CYAN = '\033[96m'      # Default for headers
    GREEN = '\033[92m'     # Default for success
    YELLOW = '\033[93m'    # Default for warnings
    RED = '\033[91m'       # Default for errors
```

### File Output Configuration

In `utils/helpers.py`, modify save behavior:

```python
def create_results_filename(topic):
    # Change the filename format
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    topic_clean = topic.lower().replace(" ", "_")[:30]
    return f"study_results_{topic_clean}_{timestamp}.txt"
```

## Crew Configuration

### Process Settings

In `crew/crew_setup.py`, modify crew processes:

```python
# Sequential: Agents run one after another
process=Process.sequential

# Hierarchical: One agent manages others
process=Process.hierarchical

# Managers: Specific manager for delegation
manager_llm=OpenAI(model_name="gpt-4")
```

### Verbose Logging

In agent files, control verbosity:

```python
verbose=True   # Show detailed execution
verbose=False  # Show minimal output
```

## API Customization

### Using Different LLM Providers

To use Azure OpenAI, Ollama, or other providers, modify `crew/crew_setup.py`:

```python
# Example: Using Azure OpenAI
from langchain_openai import AzureOpenAI

crew = Crew(
    agents=[...],
    tasks=[...],
    llm=AzureOpenAI(
        azure_endpoint="...",
        api_version="...",
        deployment_name="..."
    )
)
```

### Custom Model Configuration

```python
# Using different model
os.environ["OPENAI_API_MODEL"] = "gpt-3.5-turbo"

# Using custom API endpoint
os.environ["OPENAI_API_BASE"] = "https://api.openai.com/v1"
```

## Quiz Configuration

### Change Number of Questions

In `tasks/quiz_task.py`:

```python
# Change from 8-10 to different range
"Create a quiz with 15-20 questions..."
```

### Adjust Question Difficulty

In `tasks/quiz_task.py`:

```python
# Modify difficulty distribution
- Concept recall questions (easy) - 30%
- Application questions (medium) - 50%
- Critical thinking questions (hard) - 20%
```

## Output Customization

### Change Results Directory

In `utils/helpers.py`:

```python
results_dir = Path("my_custom_results_folder")
```

### Modify Report Format

In `utils/helpers.py`, edit `create_full_report()`:

```python
report = f"""
{===}
Your Custom Report Title
{===}
...
"""
```

## Logging Configuration

### Enable File Logging

Add to `main.py`:

```python
import logging

logging.basicConfig(
    filename='study_assistant.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

### Set Log Level

```python
# Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
log_level = "INFO"
```

## Performance Tuning

### Timeout Configuration

In `crew/crew_setup.py`, add timeout:

```python
crew = Crew(
    agents=[...],
    tasks=[...],
    timeout_seconds=300  # 5 minutes
)
```

### Batch Processing

Modify to process multiple topics:

```python
def batch_study(topics):
    results = []
    for topic in topics:
        result = create_study_crew_interactive(topic)
        results.append(result)
    return results
```

## Memory Configuration

### Persistent Storage

Add to store learning history:

```python
import json

def save_session(topic, results):
    session_data = {
        'topic': topic,
        'timestamp': get_timestamp(),
        'results': results
    }
    # Save to database or file
```

### Session Management

```python
def load_previous_sessions():
    # Load and display previous study sessions
    pass

def create_study_continuation(topic):
    # Resume learning where you left off
    pass
```

## Security Configuration

### API Key Management

```python
# Don't hardcode keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Use secret manager
from keyring import get_password
OPENAI_API_KEY = get_password("openai", "api_key")
```

### Rate Limiting

```python
import time

def rate_limited_api_call(func, max_calls_per_min=60):
    delay = 60 / max_calls_per_min
    time.sleep(delay)
    return func()
```

## Database Integration

### SQLite Storage

```python
import sqlite3

def save_to_database(topic, explanation, notes):
    conn = sqlite3.connect('study_sessions.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sessions (topic, explanation, notes)
        VALUES (?, ?, ?)
    ''', (topic, explanation, notes))
    conn.commit()
    conn.close()
```

## Web Integration

### Flask Web Interface

```python
from flask import Flask

app = Flask(__name__)

@app.route('/study/<topic>')
def study(topic):
    results = create_study_crew_interactive(topic)
    return render_template('results.html', results=results)
```

## Testing Configuration

### Unit Tests

```python
import pytest

def test_teacher_agent():
    agent = create_teacher_agent()
    assert agent.role == "Excellent Teacher"
```

### Integration Tests

```python
def test_full_workflow():
    result = create_study_crew_interactive("Python Basics")
    assert result is not None
```

## Advanced Options

### Custom Agent Parameters

```python
Agent(
    role="...",
    goal="...",
    backstory="...",
    verbose=True,
    allow_delegation=True,  # Allow agent to delegate tasks
    tools=[...],            # Add tools
    function_calling_llm=None,  # Custom LLM for functions
)
```

### Custom Task Parameters

```python
Task(
    description="...",
    expected_output="...",
    agent=agent,
    async_execution=False,      # Run async
    output_file=None,           # Save output
    callback=None,              # Custom callback
    human_input=False,          # Require human input
)
```

## Deployment Configuration

### Environment-Specific Settings

```python
import os

ENV = os.getenv("ENVIRONMENT", "development")

if ENV == "production":
    VERBOSE = False
    TIMEOUT = 600
    MAX_RETRIES = 3
else:
    VERBOSE = True
    TIMEOUT = 300
    MAX_RETRIES = 1
```

## Troubleshooting Configuration Issues

### If agents are not responding:
1. Check API key is valid
2. Verify API quota
3. Check internet connection
4. Try with simpler topic

### If output is too long:
1. Reduce token limits
2. Modify task descriptions
3. Adjust model selection

### If costs are high:
1. Use cheaper models (gpt-3.5-turbo)
2. Reduce output verbosity
3. Set token limits

## Configuration Examples

### Minimal Configuration

```env
OPENAI_API_KEY=sk-...
```

### Standard Configuration

```env
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.7
```

### Advanced Configuration

```env
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.7
OPENAI_MAX_TOKENS=4000
LOG_LEVEL=INFO
SAVE_RESULTS=true
DATABASE_PATH=./study_sessions.db
```

## Getting Help

For configuration issues:
1. Check the specific configuration section above
2. Verify environment variables are set correctly
3. Test with default configuration first
4. Check logs for error messages

---

**Configuration complete! Run `python main.py` to start.** 🚀
