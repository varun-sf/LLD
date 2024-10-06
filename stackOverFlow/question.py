from datetime import datetime
from voteable import Voteable

class Question(Voteable):
    def __init__(self, title, content):
        super().__init__()
        self.id = id(self)
        self.content = content
        self.title = title
        self.created_on = datetime.now()
        self.answers = []
        
    def add_answer(self, answer):
        self.answers.append(answer)

    

    