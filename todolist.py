class TodoList:
    def __init__(self):
        self.tasks = []
        self.current_id = 0
    def add_task(self, task):
        self.current_id += 1
        self.tasks.append({'id' : self.current_id, 'task' : task, 'done' : False})
        return self.current_id
    def remove_task(self, task_id):
        pass
    def mark_task_as_done(self, task_id):
        pass
    def get_all_tasks(self):
        return self.tasks


if __name__ == '__main__':
    todolist = TodoList()
    print(todolist.get_all_tasks())
    todolist.add_task("Zadanie testowe")
    print(todolist.get_all_tasks())
    todolist.add_task("Inne zadanie")
    print(todolist.get_all_tasks())