"""Helper utilities for CLI output, file handling, and logging."""

import os
from datetime import datetime
from pathlib import Path


class Colors:
    """ANSI color codes for terminal output."""
    
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def print_colored(text, color="CYAN", bold=False):
    """
    Print colored text to console.
    
    Args:
        text (str): Text to print
        color (str): Color name (HEADER, BLUE, CYAN, GREEN, YELLOW, RED)
        bold (bool): Whether to make text bold
    """
    color_code = getattr(Colors, color, Colors.CYAN)
    bold_code = Colors.BOLD if bold else ""
    print(f"{bold_code}{color_code}{text}{Colors.END}")


def format_section(title, content, width=80):
    """
    Format a section with title and content.
    
    Args:
        title (str): Section title
        content (str): Section content
        width (int): Terminal width
        
    Returns:
        str: Formatted section
    """
    separator = "=" * width
    output = f"\n{separator}\n"
    output += f"{Colors.BOLD}{Colors.CYAN}{title}{Colors.END}\n"
    output += f"{separator}\n"
    output += f"{content}\n"
    return output


def get_timestamp():
    """
    Get current timestamp as formatted string.
    
    Returns:
        str: Formatted timestamp
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_results_filename(topic):
    """
    Create a filename for saving results.
    
    Args:
        topic (str): The study topic
        
    Returns:
        str: Filename for results
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    topic_clean = topic.lower().replace(" ", "_")[:30]
    return f"study_results_{topic_clean}_{timestamp}.txt"


def save_to_file(content, filename=None, topic=None):
    """
    Save content to a text file.
    
    Args:
        content (str): Content to save
        filename (str, optional): Specific filename to use
        topic (str, optional): Topic name (used to generate filename if not provided)
        
    Returns:
        str: Path to saved file
        
    Raises:
        ValueError: If neither filename nor topic is provided
    """
    if not filename:
        if not topic:
            raise ValueError("Either filename or topic must be provided")
        filename = create_results_filename(topic)
    
    # Create results directory if it doesn't exist
    results_dir = Path("study_results")
    results_dir.mkdir(exist_ok=True)
    
    filepath = results_dir / filename
    
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return str(filepath)
    except IOError as e:
        print(f"Error saving file: {e}")
        raise


def create_full_report(topic, explanation, notes, quiz, evaluation=None):
    """
    Create a comprehensive report with all outputs.
    
    Args:
        topic (str): The study topic
        explanation (str): Teacher's explanation
        notes (str): Study notes
        quiz (str): Quiz with questions
        evaluation (str, optional): Evaluation results
        
    Returns:
        str: Formatted report
    """
    report = f"""
{'='*80}
AI STUDY ASSISTANT - COMPREHENSIVE STUDY REPORT
{'='*80}

TOPIC: {topic}
Generated: {get_timestamp()}

{'='*80}
SECTION 1: TOPIC EXPLANATION
{'='*80}

{explanation}

{'='*80}
SECTION 2: STUDY NOTES
{'='*80}

{notes}

{'='*80}
SECTION 3: QUIZ
{'='*80}

{quiz}
"""
    
    if evaluation:
        report += f"""
{'='*80}
SECTION 4: EVALUATION & RESULTS
{'='*80}

{evaluation}
"""
    
    report += f"""
{'='*80}
END OF REPORT
{'='*80}
"""
    
    return report


def print_progress(step, total, message):
    """
    Print progress indicator.
    
    Args:
        step (int): Current step
        total (int): Total steps
        message (str): Progress message
    """
    percentage = (step / total) * 100
    bar_length = 30
    filled = int(bar_length * step / total)
    bar = "█" * filled + "░" * (bar_length - filled)
    
    print(f"\n[{bar}] {percentage:.0f}% - {message}")


def validate_topic(topic):
    """
    Validate that topic is not empty.
    
    Args:
        topic (str): Topic to validate
        
    Returns:
        bool: True if valid
        
    Raises:
        ValueError: If topic is empty or invalid
    """
    if not topic or not topic.strip():
        raise ValueError("Topic cannot be empty")
    if len(topic) < 3:
        raise ValueError("Topic must be at least 3 characters long")
    if len(topic) > 200:
        raise ValueError("Topic must be less than 200 characters")
    return True


def log_message(message, level="INFO"):
    """
    Log a message with timestamp and level.
    
    Args:
        message (str): Message to log
        level (str): Log level (INFO, WARNING, ERROR)
    """
    timestamp = get_timestamp()
    print(f"[{timestamp}] [{level}] {message}")
