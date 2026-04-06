from crewai import Task

def create_teaching_task(agent, topic):
    return Task(
        description=f"""
Explain '{topic}' in a detailed and factual way.

If it is a historical topic:
- Include timeline
- Key events
- Important people
- Causes and consequences

Do NOT give generic explanations.
Be specific and accurate.
""",
        agent=agent
    )