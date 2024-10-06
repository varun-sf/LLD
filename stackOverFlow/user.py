from question import Question
from answer import Answer
from comment import Comment
from vote import Vote
class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.questions = {}
        self.answers = {}
        self.comments = {}

    def add_question(self,title, content):
        question = Question(title, content)
        self.questions[question.id] = question
        return question
    
    def add_answer(self, question: Question, answer):
        answer = Answer(answer)
        question.add_answer(answer)
        return answer
    
    def add_comment(self, answer: Answer, comment):
        comment = Comment(comment)
        answer.add_comment(comment)
    
    def add_vote(self, entity, value):
        if value not in [1,-1]:
            raise ValueError("Invalid value")
        vote = Vote(self.id, value)
        entity.add_vote(vote)
        