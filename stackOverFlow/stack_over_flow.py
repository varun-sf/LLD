from user import User
from question import Question
from answer import Answer

class StackOverFlow:
    def __init__(self):
        self.users = []
        self.questions = []

    def add_user(self, name, email):
        user = User(len(self.users)+1, name, email)
        self.users.append(user)
        return user
    
    def create_question(self, title, content, user: User):
        question = user.add_question(title, content)
        self.questions.append(question)
        return question
        
    def add_answer(self, question: Question, content, user: User):
        answer = user.add_answer(question, content)
        return answer
        

    def add_comment(self, answer: Answer, content, user: User):
        user.add_comment(answer, content)

    def add_vote(self, entity, value, user: User):
        user.add_vote(entity, value)

    def search_box(self, query):
        
        questions = [i for i in self.questions if query.lower() in i.title.lower()]
        ans = []
        for q in questions:
            ans.append({"title": q.title,
                        "content": q.content,
                        "answers": [i.content for i in q.answers],
                        "total_votes": q.get_total_votes()
                        })
            
        return ans
