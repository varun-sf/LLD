from task import Task
class User:
    def __init__(self,  name, email, is_admin):
        self.id = id(self)
        self.name = name
        self.email = email
        self.admin = is_admin
        self.created_tasks = {}
        self.assigned_tasks = {}

    def create_task(self,  name, description, priority):
        task = Task(name, description, priority)
        self.created_tasks[task.id] = task
        print(task)
        return task
    
    def assign_task(self, task):
        self.assigned_tasks[task.id] = task
    
    def get_all_tasks(self):
        for task in self.created_tasks.values():
           print(task)
