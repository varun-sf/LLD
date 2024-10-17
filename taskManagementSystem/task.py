from status import Status
class Task:
    def __init__(self, name, description, priority):
        self.id = id(self)
        self.name  = name
        self.description =  description
        self.status = Status.CREATED
        self.priority = priority

    def change_status(self,  status: Status):
        self.status = status 
    
    def  __str__(self):
        return  f"Task {self.id} - {self.name} -description- {self.description}- status- {self.status}-priority- {self.priority}"



