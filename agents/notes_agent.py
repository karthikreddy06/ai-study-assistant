"""Notes Agent - Converts explanations into structured study notes."""

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


def create_notes_agent():
    """
    Creates a Notes Agent that converts explanations into structured study notes.
    
    Returns:
        Agent: Configured notes agent with LLM
    """
    llm = LLM(
        model="gpt-4o-mini",
        api_key=getenv("OPENAI_API_KEY"),
        temperature=0.7
    )
    
    return Agent(
        role="Precision Study Notes Specialist",
        goal="Create DETAILED, FACT-BASED study notes with REAL information, dates, names, and specifics. "
             "NO generic language. NO placeholder text. ONLY real, verifiable information.",
        backstory="You are an expert at synthesizing FACTUAL information into organized study materials. "
                  "You include REAL facts, dates, names, events, and specific details. "
                  "You NEVER use generic phrases like 'this concept' or 'in general'. "
                  "Your notes are precise, detailed, and ready for serious study and examination preparation. "
                  "You demand HIGH SPECIFICITY in every point you document. "
                  "Every fact in your notes must be REAL and VERIFIABLE.",
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
