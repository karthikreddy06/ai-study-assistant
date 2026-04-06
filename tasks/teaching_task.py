"""Teaching Task - Teacher Agent explains the topic."""

import sys
from pathlib import Path

# Try to import from real crewai, fall back to stub if unavailable
try:
    from crewai import Task
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from crewai_stub import Task


def create_teaching_task(agent, topic):
    """
    Creates a teaching task for the teacher agent.
    
    Args:
        agent: The teacher agent
        topic: The topic to explain
        
    Returns:
        Task: Configured teaching task
    """
    return Task(
        description=f"""
Explain '{topic}' in a detailed, factual, and specific way.

If it is a historical topic:

* Include timeline
* Key events
* Important people
* Causes and consequences

Do NOT give generic explanations.
Be specific to the topic.
""",
        expected_output="A detailed and factual explanation",
        agent=agent,
    )
