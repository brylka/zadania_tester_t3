import pymysql

class TodoList:
    def __init__(self, db):
        self.db = db
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        #self.tasks = []
        #self.current_id = 0
    def add_task(self, task):
        sql = "INSERT INTO tasks (task, done) VALUES (%s, %s)"
        self.cursor.execute(sql, (task, False))
        self.db.commit()
        return self.cursor.lastrowid
        #self.current_id += 1
        #self.tasks.append({'id' : self.current_id, 'task' : task, 'done' : False})
        #return self.current_id
    def remove_task(self, task_id):
        sql = "DELETE FROM tasks WHERE id = %s"
        self.cursor.execute(sql, (task_id))
        self.db.commit()
        #new_tasks = []
        #for task in self.tasks:
        #    if task['id'] != task_id:
        #        new_tasks.append(task)
        #self.tasks = new_tasks

    def mark_task_as_done(self, task_id):
        sql = "UPDATE tasks SET done = TRUE WHERE id = %s"
        self.cursor.execute(sql, (task_id))
        self.db.commit()
        #for task in self.tasks:
        #    if task['id'] == task_id:
        #        task['done'] = True
        #        break

    def get_all_tasks(self):
        sql = "SELECT * FROM tasks"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
        #return self.tasks


if __name__ == '__main__':
    db = pymysql.connect(host='localhost', user='root', password='', db='todolist')
    todolist = TodoList(db)

    print(todolist.get_all_tasks())
    task_id = todolist.add_task("Nauka kasowania")
    print(todolist.get_all_tasks())
    todolist.mark_task_as_done(task_id)
    print(todolist.get_all_tasks())
    todolist.remove_task(task_id)
    print(todolist.get_all_tasks())
    db.close()



# CREATE TABLE tasks (id INT NOT NULL AUTO_INCREMENT , task TEXT NOT NULL , done BOOLEAN NOT NULL DEFAULT FALSE , PRIMARY KEY (`id`))