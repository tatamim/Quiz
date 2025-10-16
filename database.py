import sqlite3
from models import Question, Quiz, Option
import os

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            # Check if the database file exists
            is_new_db = not os.path.exists(self.db_name)
            self.conn = sqlite3.connect(self.db_name)
            self.cur = self.conn.cursor()
            # Enforce foreign key constraints (important for data integrity)
            self.cur.execute("PRAGMA foreign_keys = ON;")
            return is_new_db # Return if it's a new database
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            raise

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    # --- Methods for Database Setup ---
    def _execute_sql_file(self, filename):
        """Helper function to execute SQL commands from a file."""
        try:
            with open(filename, 'r') as f:
                sql_script = f.read()
            # executescript() handles multiple SQL statements in a string
            self.cur.executescript(sql_script)
            self.conn.commit()
            print(f"Successfully executed SQL from {filename} ")
        except FileNotFoundError:
            print(f"Error: SQL file not found: {filename}. Cannot set up database.")
        except sqlite3.Error as e:
            print(f"Error executing SQL from {filename}: {e}")
            self.conn.rollback()

    def setup_database(self, schema_file, data_file):
        """Creates tables using schema_file and populates initial data using data_file."""
        print("Setting up database schema...")
        self._execute_sql_file(schema_file)
        print("Populating initial data...")
        self._execute_sql_file(data_file) 
    # --- End of Database Setup Methods ---

    # --- Methods for Quiz Application ---
    # --- encapsulated database operations ---
    def get_all_quizzes(self):
        try:
            self.cur.execute("SELECT quiz_id, title, description FROM quizzes")
            rows = self.cur.fetchall()
            return [Quiz(row[0], row[1], row[2]) for row in rows]
        except sqlite3.Error as e:
            print(f"Error fetching quizzes: {e}")
            return []

    def get_questions_for_quiz(self, quiz_id):
        try:
            self.cur.execute("SELECT question_id, question_text FROM questions WHERE quiz_id = ?", (quiz_id,))
            question_rows = self.cur.fetchall()
            questions = []
            for q_row in question_rows:
                question = Question(q_row[0], q_row[1])
                self.cur.execute("SELECT option_id, option_text, is_correct FROM options WHERE question_id = ?", (q_row[0],))
                option_rows = self.cur.fetchall()
                question.options = [Option(o_row[0], o_row[1], o_row[2]) for o_row in option_rows]
                questions.append(question)
            return questions
        except sqlite3.Error as e:
            print(f"Error fetching questions: {e}")
            return []

    def save_quiz_result(self, user_name, quiz_id, score):
        try:
            self.cur.execute("INSERT INTO quiz_results (user_name, quiz_id, score) VALUES (?, ?, ?)", (user_name, quiz_id, score))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error saving quiz result: {e}")
            self.conn.rollback()

    #Bonus feature: Fetch top 5 high scores for a quiz
    def get_high_scores(self, quiz_id):
        try:
            self.cur.execute("SELECT user_name, score, date_taken FROM quiz_results WHERE quiz_id = ? ORDER BY score DESC LIMIT 5", (quiz_id,))
            return self.cur.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching high scores: {e}")
            return []