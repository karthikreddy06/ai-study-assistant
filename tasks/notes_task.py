from crewai import Task

def create_notes_task(agent, topic):
    return Task(
        description=f"""
Create clear study notes for '{topic}'.

- Include key facts
- Important details
- Bullet points
- Real examples

Avoid generic placeholders.
""",
        agent=agent
    )