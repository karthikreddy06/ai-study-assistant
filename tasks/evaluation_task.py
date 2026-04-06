from crewai import Task

def create_evaluation_task(agent, topic, answers):
    return Task(
        description=f"""
Evaluate the user's answers about '{topic}'.

User answers:
{answers}

- Give score
- Provide feedback
- Correct mistakes

Be specific. Do NOT use generic text.
""",
        agent=agent
    )