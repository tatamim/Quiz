import sqlite3
from database import DatabaseManager


def add_quiz(db):
    title = input("Enter quiz title: ").strip()
    description = input("Enter quiz description (optional): ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    
    try:
        db.cur.execute("INSERT INTO quizzes (title, description) VALUES (?, ?)", (title, description))
        db.conn.commit()
        quiz_id = db.cur.lastrowid
        print(f"Quiz '{title}' added successfully with ID {quiz_id}.")
    except sqlite3.Error as e:
        print(f"Error adding quiz: {e}")

def add_question(db):
    quizzes = db.get_all_quizzes()
    if not quizzes:
        print("No quizzes available. Add a quiz first.")
        return
    
    print("\nAvailable Quizzes:")
    for i, quiz in enumerate(quizzes, 1):
        print(f"{i}. {quiz.title}")
    
    try:
        quiz_num = int(input("Select a quiz by number to add a question: ").strip())
        if 1 <= quiz_num <= len(quizzes):
            quiz_id = quizzes[quiz_num - 1].quiz_id
            question_text = input("Enter question text: ").strip()
            if not question_text:
                print("Question text cannot be empty.")
                return
            
            db.cur.execute("INSERT INTO questions (quiz_id, question_text) VALUES (?, ?)", (quiz_id, question_text))
            db.conn.commit()
            question_id = db.cur.lastrowid
            print(f"Question added successfully with ID {question_id}.")
            
            # Add options (assume 4 options, as in sample data)
            print("Now add 4 options (A, B, C, D). Specify which one is correct.")
            options = []
            letters = ['A', 'B', 'C', 'D']
            for letter in letters:
                option_text = input(f"Enter option {letter} text: ").strip()
                if not option_text:
                    print("Option text cannot be empty.")
                    return
                options.append((option_text, 0))  # Default to incorrect
            
            correct_letter = input("Enter the correct option letter (A/B/C/D): ").strip().upper()
            if correct_letter not in letters:
                print("Invalid correct option.")
                return
            correct_index = letters.index(correct_letter)
            options[correct_index] = (options[correct_index][0], 1)  # Set to correct
            
            for option_text, is_correct in options:
                db.cur.execute("INSERT INTO options (question_id, option_text, is_correct) VALUES (?, ?, ?)",
                               (question_id, option_text, is_correct))
            db.conn.commit()
            print("Options added successfully.")
        else:
            print("Invalid quiz number.")
    except ValueError:
        print("Please enter a valid number.")
    except sqlite3.Error as e:
        print(f"Error adding question/options: {e}")
        db.conn.rollback()

def main():
    db = DatabaseManager('quiz.db')
    db.connect()
    
    while True:
        print("\nAdmin Panel Options:")
        print("1. Add a new quiz")
        print("2. Add a question (and options) to an existing quiz")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_quiz(db)
        elif choice == '2':
            add_question(db)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
    db.close()

if __name__ == "__main__":
    main()