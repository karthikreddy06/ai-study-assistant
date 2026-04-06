"""Crew Setup - Orchestrates agents and tasks for the study workflow."""

from crewai import Crew, Process

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents import (
    create_teacher_agent,
    create_notes_agent,
    create_quiz_agent,
    create_evaluator_agent,
)
from tasks import (
    create_teaching_task,
    create_notes_task,
    create_quiz_task,
    create_evaluation_task,
)


def create_study_crew(topic, user_answers=None):
    """
    Creates and configures the study crew with all agents and tasks.
    
    Args:
        topic (str): The topic to study
        user_answers (str, optional): User's answers for evaluation
        
    Returns:
        tuple: (teaching_output, notes_output, quiz_output, evaluation_output)
    """
    
    # Create agents
    teacher_agent = create_teacher_agent()
    notes_agent = create_notes_agent()
    quiz_agent = create_quiz_agent()
    evaluator_agent = create_evaluator_agent()
    
    # Create teaching task
    teaching_task = create_teaching_task(teacher_agent, topic)
    
    # We'll create the crew with just the teacher for the first step
    crew_teach = Crew(
        agents=[teacher_agent],
        tasks=[teaching_task],
        process=Process.sequential,
        verbose=True,
    )
    
    # Execute teaching - pass topic as input
    print(f"\n[TEACHING] Working on topic: {topic}...")
    teaching_output = crew_teach.kickoff(inputs={"topic": topic})
    print(f"[OK] Teaching output generated\n")
    
    # Create notes task using teaching output
    notes_task = create_notes_task(notes_agent, str(teaching_output))
    
    crew_notes = Crew(
        agents=[notes_agent],
        tasks=[notes_task],
        process=Process.sequential,
        verbose=True,
    )
    
    # Execute notes creation - pass topic
    print("[NOTES] Creating study notes...")
    notes_output = crew_notes.kickoff(inputs={"topic": topic})
    print("[OK] Study notes generated\n")
    
    # Create quiz task using teaching output
    quiz_task = create_quiz_task(quiz_agent, str(teaching_output))
    
    crew_quiz = Crew(
        agents=[quiz_agent],
        tasks=[quiz_task],
        process=Process.sequential,
        verbose=True,
    )
    
    # Execute quiz generation - pass topic
    print("[QUIZ] Generating quiz questions...")
    quiz_output = crew_quiz.kickoff(inputs={"topic": topic})
    print("[OK] Quiz generated\n")
    
    # Handle evaluation if user answers provided
    evaluation_output = None
    if user_answers:
        eval_task = create_evaluation_task(
            evaluator_agent, str(quiz_output), user_answers
        )
        
        crew_eval = Crew(
            agents=[evaluator_agent],
            tasks=[eval_task],
            process=Process.sequential,
            verbose=True,
        )
        
        # Execute evaluation
        print("[EVALUATOR] Evaluating responses...")
        evaluation_output = crew_eval.kickoff()
        print("[OK] Evaluation complete\n")
    
    return teaching_output, notes_output, quiz_output, evaluation_output


def create_study_crew_interactive(topic):
    """
    Creates a crew for interactive study workflow (without user answers initially).
    
    Args:
        topic (str): The topic to study
        
    Returns:
        tuple: (teaching_output, notes_output, quiz_output)
    """
    teaching_output, notes_output, quiz_output, _ = create_study_crew(topic)
    return teaching_output, notes_output, quiz_output


def create_evaluation_crew(quiz_output, user_answers):
    """
    Creates just the evaluation crew for assessing user answers.
    
    Args:
        quiz_output (str): The quiz questions
        user_answers (str): User's answers
        
    Returns:
        str: Evaluation output
    """
    evaluator_agent = create_evaluator_agent()
    eval_task = create_evaluation_task(evaluator_agent, quiz_output, user_answers)
    
    crew_eval = Crew(
        agents=[evaluator_agent],
        tasks=[eval_task],
        process=Process.sequential,
        verbose=True,
    )
    
    return crew_eval.kickoff(inputs={"answers": user_answers})
