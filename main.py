import os
from dotenv import load_dotenv
from crewai import Crew, Process

from agents.teacher_agent import create_teacher_agent
from tasks.teaching_task import create_teaching_task
from tasks.notes_task import create_notes_task
from tasks.quiz_task import create_quiz_task

# Load API key
load_dotenv()

def main():
    print("\n=== AI STUDY ASSISTANT ===\n")

    topic = input("Enter topic: ")

    # Create agent
    teacher = create_teacher_agent()

    # STEP 1: Teaching + Notes ONLY
    teaching_task = create_teaching_task(teacher, topic)
    notes_task = create_notes_task(teacher, topic)

    crew = Crew(
        agents=[teacher],
        tasks=[teaching_task, notes_task],
        process=Process.sequential
    )

    result = crew.kickoff()

    print("\n=== LEARNING OUTPUT ===\n")
    print(result)

    # 🔥 ASK USER BEFORE QUIZ
    choice = input("\nDo you want a quiz? (yes/no): ").strip().lower()

    if choice == "yes":
        quiz_task = create_quiz_task(teacher, topic)

        quiz_crew = Crew(
            agents=[teacher],
            tasks=[quiz_task],
            process=Process.sequential
        )

        quiz_result = quiz_crew.kickoff()

        print("\n=== QUIZ ===\n")
        print(quiz_result)

    else:
        print("\n👍 Okay! No quiz. Learning session complete.")

if __name__ == "__main__":
    main()