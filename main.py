from database import DatabaseManager
from models import Quiz
import sqlite3
def main():
    db = DatabaseManager('quiz.db')
    is_new_db = db.connect()

    # Check if the quizzes table exists
    try:
        db.cur.execute("SELECT 1 FROM quizzes LIMIT 1")
        table_exists = True
    except sqlite3.Error:
        table_exists = False

    # Initialize database with schema and sample data if it's a new database or tables don't exist
    if is_new_db or not table_exists:
        print("Initializing database...")
        try:
            db.setup_database('schema.sql', 'sample_data.sql')
        except Exception as e:
            print(f"Failed to set up database: {e}. Please ensure schema.sql and sample_data.sql are in the correct directory.")
            db.close()
            return

    while True:
        print("Welcome to the Quiz Application!")
        user_name = input("Please enter your name: ").strip()
        if not user_name:
            print("Name cannot be empty. Please try again.")
            continue

        while True:
            print("\nOptions:")
            print("1. Take a quiz")
            print("2. View high scores for a quiz")
            print("3. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                quizzes = db.get_all_quizzes()
                if not quizzes:
                    print("No quizzes available. Please ensure the database is properly initialized.")
                    continue

                print("\nAvailable Quizzes:")
                for i, quiz in enumerate(quizzes, 1):
                    print(f"{i}. {quiz.title} - {quiz.description}")

                try:
                    quiz_num = int(input("Select a quiz by number: ").strip())
                    if 1 <= quiz_num <= len(quizzes):
                        selected_quiz = quizzes[quiz_num - 1]
                        selected_quiz.load_questions(db)

                        score = 0
                        for question in selected_quiz.questions:
                            question.display()
                            answer = input("Your answer (A/B/C/D): ").strip().upper()
                            if not answer in ['A', 'B', 'C', 'D']:
                                print("Invalid answer. Please use A, B, C, or D.")
                                continue
                            if question.check_answer(answer):
                                score += 1

                        total_questions = len(selected_quiz.questions)
                        print(f"You scored {score} out of {total_questions}!")

                        db.save_quiz_result(user_name, selected_quiz.quiz_id, score)
                    else:
                        print("Invalid quiz number. Please select a number from the list.")
                except ValueError:
                    print("Please enter a valid number.")

            elif choice == '2':
                quizzes = db.get_all_quizzes()
                if not quizzes:
                    print("No quizzes available. Please ensure the database is properly initialized.")
                    continue

                print("\nAvailable Quizzes:")
                for i, quiz in enumerate(quizzes, 1):
                    print(f"{i}. {quiz.title}")

                try:
                    quiz_num = int(input("Select a quiz by number to view high scores: ").strip())
                    if 1 <= quiz_num <= len(quizzes):
                        selected_quiz = quizzes[quiz_num - 1]
                        high_scores = db.get_high_scores(selected_quiz.quiz_id)
                        if high_scores:
                            print(f"\nTop 5 High Scores for {selected_quiz.title}:")
                            for hs in high_scores:
                                print(f"User: {hs[0]}, Score: {hs[1]}, Date: {hs[2]}")
                        else:
                            print("No scores available for this quiz.")
                    else:
                        print("Invalid quiz number. Please select a number from the list.")
                except ValueError:
                    print("Please enter a valid number.")

            elif choice == '3':
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

        another = input("Do you want to start over? (yes/no): ").strip().lower()
        if another not in ['yes', 'y']:
            break

    db.close()

if __name__ == "__main__":
    main()