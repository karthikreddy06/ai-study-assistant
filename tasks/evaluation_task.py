"""Evaluation Task - Evaluator Agent assesses answers."""

import sys
from pathlib import Path

# Try to import from real crewai, fall back to stub if unavailable
try:
    from crewai import Task
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from crewai_stub import Task


def create_evaluation_task(agent, quiz_output, user_answers_text):
    """
    Creates an evaluation task for the evaluator agent.
    
    Args:
        agent: The evaluator agent
        quiz_output: The quiz questions and answers
        user_answers_text: The user's answers
        
    Returns:
        Task: Configured evaluation task
    """
    return Task(
        description=f"""
Evaluate the user's answers about the topic.

User answers: {{answers}}

* Compare answers with correct ones
* Give score
* Provide feedback

DO NOT generate generic explanations.
""",
        expected_output="Evaluation result with score",
        agent=agent,
    )
