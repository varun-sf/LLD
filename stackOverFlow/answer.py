from datetime import datetime
from voteable import Voteable

class Answer(Voteable):
    def __init__(self, content):
        super().__init__()
        self.id = id(self)
        self.content = content
        self.created_on = datetime.now()
        self.comments = []
        
    def add_comment(self, comment):
        self.comments.append(comment)

    
    