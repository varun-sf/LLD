from datetime import datetime
from voteable import Voteable

class Comment(Voteable):
    def __init__(self, content):
        super().__init__()
        self.id = id(self)
        self.content = content
        self.created_on = datetime.now()
    
    
        