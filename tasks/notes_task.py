"""Notes Task - Notes Agent creates structured study notes."""

import sys
from pathlib import Path

# Try to import from real crewai, fall back to stub if unavailable
try:
    from crewai import Task
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from crewai_stub import Task


def create_notes_task(agent, teaching_output):
    """
    Creates a notes task for the notes agent.
    
    Args:
        agent: The notes agent
        teaching_output: The explanation from the teacher
        
    Returns:
        Task: Configured notes task
    """
    return Task(
        description=f"""
Create structured study notes for '{teaching_output}'.

* Include key facts
* Important details
* Real examples
* No generic placeholders
""",
        expected_output="Clear and useful notes",
        agent=agent,
    )
