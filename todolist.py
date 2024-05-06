class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority
        self.completed = False

    def update_task(self, name=None, description=None, priority=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if priority:
            self.priority = priority

    def mark_completed(self):
        self.completed = True

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, task_name, **kwargs):
        for task in self.tasks:
            if task.name == task_name:
                task.update_task(**kwargs)
                break

    def mark_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_completed()
                break

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for task in self.tasks:
                status = "Completed" if task.completed else "Pending"
                print(f"{task.name} - {task.description} - Priority: {task.priority} - Status: {status}")

if __name__ == "__main__":
    todo_list = ToDoList()

    task1 = Task("Task 1", "Description for Task 1", "High")
    task2 = Task("Task 2", "Description for Task 2", "Low")

    todo_list.add_task(task1)
    todo_list.add_task(task2)

    todo_list.display_tasks()

    todo_list.update_task("Task 1", description="Updated description")
    todo_list.mark_completed("Task 2")

    todo_list.display_tasks()