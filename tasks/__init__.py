"""Tasks module for AI Study Assistant."""

from .teaching_task import create_teaching_task
from .notes_task import create_notes_task
from .quiz_task import create_quiz_task
from .evaluation_task import create_evaluation_task

__all__ = [
    "create_teaching_task",
    "create_notes_task",
    "create_quiz_task",
    "create_evaluation_task",
]
