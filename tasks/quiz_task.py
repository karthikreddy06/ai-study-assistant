from crewai import Task

def create_quiz_task(agent, topic):
    return Task(
        description=f"""
Create a quiz about '{topic}'.

- 3 MCQs
- 2 short questions
- Provide correct answers

Questions must be based on real facts.
""",
        agent=agent
    )