from flask import Flask, request, jsonify, render_template, redirect, url_for
import pymysql
from todolistmysql import TodoList

app = Flask(__name__)

def get_db_connection():
    connection = pymysql.connect(host='localhost', user='root', password='', db='todolist', cursorclass=pymysql.cursors.DictCursor)
    return connection

@app.route('/tasks.json', methods=['GET'])
def tasks_json():
    db = get_db_connection()
    todolist = TodoList(db)
    tasks = todolist.get_all_tasks()
    db.close()
    return jsonify(tasks)

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    db = get_db_connection()
    todolist = TodoList(db)
    if request.method == 'POST':
        if 'task' in request.form:
            task_description = request.form['task']
            todolist.add_task(task_description)
        elif 'delete' in request.form:
            task_id = request.form['delete']
            todolist.remove_task(int(task_id))
        elif 'done' in request.form:
            task_id = request.form['done']
            todolist.mark_task_as_done(int(task_id))
        db.close()
        return redirect(url_for('tasks'))
    else:
        tasks = todolist.get_all_tasks()
        db.close()
        return render_template('tasks.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
