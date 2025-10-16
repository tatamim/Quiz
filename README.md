Python & SQL Command-Line Quiz System

Overview

This is a command-line application that allows users to take quizzes on various topics using Python 3 and SQLite. The project demonstrates Object-Oriented Programming (OOP) principles and database interaction.
Setup Instructions

Prerequisites:

Python 3.x installed on your system.
No additional server setup is required for SQLite as it is built into Python.


Project Structure:

main.py: The entry point of the application.
database.py: Manages database connections and queries.
models.py: Defines the Quiz, Question, and Option classes.
schema.sql: Defines the database schema.
sample_data.sql: Populates the database with sample quizzes.


Installation:

Ensure all files are in the same directory.
No external dependencies are required beyond Python's standard library.


Initialize the Database:

Run python main.py for the first time. The application will create quiz.db and populate it with tables and sample data from schema.sql and sample_data.sql.


Running the Application:

Execute python main.py in your terminal.
Follow the prompts to enter your name, select a quiz, answer questions, and view high scores.



Usage

Enter your name when prompted.
Choose from options: "Take a quiz", "View high scores for a quiz", or "Exit".
Select a quiz by number and answer questions with A, B, C, or D.
View your score and decide to take another quiz or exit.

Notes

The database (quiz.db) will be created automatically if it doesn't exist.
Ensure schema.sql and sample_data.sql are in the same directory as main.py, or adjust the paths in main.py accordingly.

Bonus Features

View the top 5 high scores for a specific quiz.
Basic error handling for invalid inputs (e.g., non-numeric choices).

Contributing
This is a student project. For enhancements (e.g., an admin module), contact the developer.