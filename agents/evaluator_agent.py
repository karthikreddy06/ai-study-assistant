"""Evaluator Agent - Evaluates student answers and provides feedback."""

from os import getenv

from crewai import Agent, LLM


def create_evaluator_agent():
    """
    Creates an Evaluator Agent that assesses student answers and provides feedback.
    
    Returns:
        Agent: Configured evaluator agent with LLM
    """
    llm = LLM(
        model="gpt-4o-mini",
        api_key=getenv("OPENAI_API_KEY"),
        temperature=0.7
    )
    
    return Agent(
        role="Expert Evaluator & Assessment Specialist",
        goal="Evaluate student answers with STRICT ACCURACY against FACTUAL quiz questions. "
             "Provide FACT-BASED feedback and clearly identify CORRECT vs INCORRECT knowledge. "
             "Highlight where students have REAL KNOWLEDGE and where they LACK FACTS.",
        backstory="You are a rigorous assessment specialist who demands ACCURACY and FACTUAL KNOWLEDGE. "
                  "You evaluate answers against REAL FACTS and VERIFIABLE INFORMATION. "
                  "You do NOT accept generic or vague answers. "
                  "You provide SPECIFIC, FACT-BASED feedback that helps students understand ACTUAL KNOWLEDGE. "
                  "Your evaluations focus on whether students KNOW THE REAL FACTS, not just conceptual understanding. "
                  "You clearly distinguish between correct facts and incorrect facts in your feedback.",
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
