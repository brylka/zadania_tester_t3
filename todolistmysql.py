import pymysql

class TodoList:
    def __init__(self, db):
        self.db = db
        self.cursor = self.db.cursor()
        #self.tasks = []
        #self.current_id = 0
    def add_task(self, task):
        self.current_id += 1
        self.tasks.append({'id' : self.current_id, 'task' : task, 'done' : False})
        return self.current_id
    def remove_task(self, task_id):
        new_tasks = []
        for task in self.tasks:
            if task['id'] != task_id:
                new_tasks.append(task)
        self.tasks = new_tasks

    def mark_task_as_done(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['done'] = True
                break
    def get_all_tasks(self):
        return self.tasks


if __name__ == '__main__':
    db = pymysql.connect(host='localhost', user='root', password='', db='todolist')
    todolist = TodoList(db)


# CREATE TABLE tasks (id INT NOT NULL AUTO_INCREMENT , task TEXT NOT NULL , done BOOLEAN NOT NULL DEFAULT FALSE , PRIMARY KEY (`id`))