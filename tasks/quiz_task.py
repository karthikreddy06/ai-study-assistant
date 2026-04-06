"""Quiz Task - Quiz Agent generates assessment questions."""

import sys
from pathlib import Path

# Try to import from real crewai, fall back to stub if unavailable
try:
    from crewai import Task
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from crewai_stub import Task


def create_quiz_task(agent, teaching_output):
    """
    Creates a quiz task for the quiz agent.
    
    Args:
        agent: The quiz agent
        teaching_output: The explanation from the teacher
        
    Returns:
        Task: Configured quiz task
    """
    return Task(
        description=f"""
Generate quiz questions about '{teaching_output}'.

* Use real factual content
* Avoid generic questions
* Include correct answers
""",
        expected_output="Quiz with answers",
        agent=agent,
    )
