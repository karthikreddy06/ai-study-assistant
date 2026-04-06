"""Quiz Agent - Generates comprehensive quizzes for assessment."""

from os import getenv

from crewai import Agent, LLM


def create_quiz_agent():
    """
    Creates a Quiz Agent that generates comprehensive quizzes.
    
    Returns:
        Agent: Configured quiz agent with LLM
    """
    llm = LLM(
        model="gpt-4o-mini",
        api_key=getenv("OPENAI_API_KEY"),
        temperature=0.7
    )
    
    return Agent(
        role="Expert Assessment Specialist",
        goal="Generate quizzes with REAL, FACTUAL questions based on actual knowledge of the subject. "
             "Questions must test REAL understanding, not generic concepts. NO template-based questions.",
        backstory="You are an expert assessment specialist who creates CHALLENGING, FACT-BASED quizzes. "
                  "You create questions that test REAL KNOWLEDGE of the subject matter. "
                  "You NEVER create generic questions like 'What is a concept?' or 'How does X work in general?'. "
                  "Your questions include SPECIFIC facts, dates, names, and scenarios. "
                  "Your quizzes require students to demonstrate ACTUAL KNOWLEDGE, not conceptual understanding. "
                  "Every question is grounded in REAL FACTS and VERIFIABLE INFORMATION.",
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
