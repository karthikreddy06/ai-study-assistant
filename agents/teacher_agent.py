"""Teacher Agent - Explains topics clearly and breaks them down into concepts."""

import sys
from pathlib import Path
from os import getenv

# Try to import from real crewai, fall back to stub if unavailable
try:
    from crewai import Agent
    from crewai import LLM
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from crewai_stub import Agent, LLM


def create_teacher_agent():
    """
    Creates a Teacher Agent that explains topics clearly and breaks them down.
    
    Returns:
        Agent: Configured teacher agent with LLM
    """
    llm = LLM(model="gpt-4o-mini")
    
    return Agent(
        role="Expert Teacher",
        goal="Teach the topic clearly with real facts",
        backstory="A knowledgeable educator who explains topics deeply and accurately.",
        llm=llm,
        verbose=True
    )
