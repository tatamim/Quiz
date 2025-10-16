class Quiz:
    def __init__(self, quiz_id, title, description):
        self.quiz_id = quiz_id
        self.title = title
        self.description = description
        self.questions = []

    def load_questions(self, db_manager):
        self.questions = db_manager.get_questions_for_quiz(self.quiz_id)

class Question:
    def __init__(self, question_id, question_text):
        self.question_id = question_id
        self.question_text = question_text
        self.options = []
    
    def display(self):
        print(self.question_text)
        letters = ['A', 'B', 'C', 'D']
        for i, option in enumerate(self.options):
            if i < len(letters):
                print(f"{letters[i]}. {option.option_text}")
    
    def check_answer(self, answer):
        letters = ['A', 'B', 'C', 'D']
        try:
            index = letters.index(answer.upper())
            if index < len(self.options):
                return self.options[index].is_correct == 1
        except ValueError:
            return False
        return False
    
class Option:
    def __init__(self, option_id, option_text, is_correct):
        self.option_id = option_id
        self.option_text = option_text
        self.is_correct = is_correct

        