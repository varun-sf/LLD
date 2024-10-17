from task_management_system import TaskManagementSystem

class TaskSystemDemo:
    @staticmethod
    def run():
      system = TaskManagementSystem()
      user_id = system.create_user("varun","tilkireddy@gmail.com", False)
      system.create_task(user_id, "Task 1", "This is a task","low")
      system.create_task(user_id, "Task 2", "This is a task","low")
      system.get_all_tasks(user_id)




if __name__ =="__main__":
    TaskSystemDemo.run()