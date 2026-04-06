from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

def create_teacher_agent():
    return Agent(
        role="Expert History Teacher",
        goal="Explain topics clearly with real facts and examples",
        backstory="An experienced educator who teaches with real-world knowledge.",
        llm=llm,
        verbose=True
    )