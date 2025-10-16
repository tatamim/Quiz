-- Quiz 1: Python Basics
INSERT INTO quizzes (title, description) VALUES ('Python Basics', 'Basic questions about Python programming.');

-- Questions for Quiz 1
INSERT INTO questions (quiz_id, question_text) VALUES (1, 'What is the output of print(2 + 2)?');
INSERT INTO options (question_id, option_text, is_correct) VALUES (1, '3', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (1, '4', 1);
INSERT INTO options (question_id, option_text, is_correct) VALUES (1, '5', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (1, 'Error', 0);

INSERT INTO questions (quiz_id, question_text) VALUES (1, 'Which keyword is used to define a function in Python?');
INSERT INTO options (question_id, option_text, is_correct) VALUES (2, 'func', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (2, 'def', 1);
INSERT INTO options (question_id, option_text, is_correct) VALUES (2, 'function', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (2, 'define', 0);

INSERT INTO questions (quiz_id, question_text) VALUES (1, 'What is the correct file extension for Python files?');
INSERT INTO options (question_id, option_text, is_correct) VALUES (3, '.pyth', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (3, '.pt', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (3, '.py', 1);
INSERT INTO options (question_id, option_text, is_correct) VALUES (3, '.python', 0);

INSERT INTO questions (quiz_id, question_text) VALUES (1, 'How do you create a list in Python?');
INSERT INTO options (question_id, option_text, is_correct) VALUES (4, '[]', 1);
INSERT INTO options (question_id, option_text, is_correct) VALUES (4, '{}', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (4, '()', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (4, '<>', 0);

INSERT INTO questions (quiz_id, question_text) VALUES (1, 'What is the output of print(type(5))?');
INSERT INTO options (question_id, option_text, is_correct) VALUES (5, '<class ''float''>', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (5, '<class ''int''>', 1);
INSERT INTO options (question_id, option_text, is_correct) VALUES (5, '<class ''str''>', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (5, '<class ''bool''>', 0);

-- Quiz 2: SQL Fundamentals
INSERT INTO quizzes (title, description) VALUES ('SQL Fundamentals', 'Basic questions about SQL.');

-- Questions for Quiz 2
INSERT INTO questions (quiz_id, question_text) VALUES (2, 'What does SQL stand for?');
INSERT INTO options (question_id, option_text, is_correct) VALUES (6, 'Structured Query Language', 1);
INSERT INTO options (question_id, option_text, is_correct) VALUES (6, 'Simple Query Language', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (6, 'Standard Query Language', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (6, 'Sequential Query Language', 0);

INSERT INTO questions (quiz_id, question_text) VALUES (2, 'Which SQL keyword is used to retrieve data from a database?');
INSERT INTO options (question_id, option_text, is_correct) VALUES (7, 'GET', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (7, 'SELECT', 1);
INSERT INTO options (question_id, option_text, is_correct) VALUES (7, 'FETCH', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (7, 'RETRIEVE', 0);

INSERT INTO questions (quiz_id, question_text) VALUES (2, 'Which SQL clause is used to filter records?');
INSERT INTO options (question_id, option_text, is_correct) VALUES (8, 'FILTER', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (8, 'WHERE', 1);
INSERT INTO options (question_id, option_text, is_correct) VALUES (8, 'HAVING', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (8, 'SORT', 0);

INSERT INTO questions (quiz_id, question_text) VALUES (2, 'What is the SQL command to create a table?');
INSERT INTO options (question_id, option_text, is_correct) VALUES (9, 'CREATE TABLE', 1);
INSERT INTO options (question_id, option_text, is_correct) VALUES (9, 'MAKE TABLE', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (9, 'NEW TABLE', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (9, 'ADD TABLE', 0);

INSERT INTO questions (quiz_id, question_text) VALUES (2, 'Which SQL keyword is used to sort the result-set?');
INSERT INTO options (question_id, option_text, is_correct) VALUES (10, 'SORT BY', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (10, 'ORDER BY', 1);
INSERT INTO options (question_id, option_text, is_correct) VALUES (10, 'GROUP BY', 0);
INSERT INTO options (question_id, option_text, is_correct) VALUES (10, 'ARRANGE BY', 0);