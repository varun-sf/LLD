from user import User
class TaskManagementSystem:
    def __init__(self):
        self.users = {}
        self.tasks = {}

    def create_user(self, name, email, is_admin):
        user = User(name,email,is_admin)
        self.users[user.id] =  user
        return user.id
    
    def create_task(self, user_id, name, description, priority):
        user = self.users.get(user_id, None)
        if user is None:
            return "Invalid user_id"
        task = user.create_task(name, description, priority)
        self.tasks[task.id] = task
        return task.id


    def assign_task(self, user_id, assign_id):
        admin_user = self.users.get(user_id, None)
        user = self.users.get(assign_id, None)
        if admin_user is None or user is None:
            return "Invalid ids"
        if not admin_user.is_admin:
            return "Unauthorised"
        user.assign_task(user)
    
    def get_all_tasks(self, user_id):
        user = self.users.get(user_id,None)
        if user is None:
            return "Invalid user_id"
        return user.get_all_tasks()
        

