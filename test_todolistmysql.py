import unittest
import pymysql
from todolistmysql import TodoList

class TestTodoList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = pymysql.connect(host='localhost', user='root', password='', db='todolist')
        cls.todolist = TodoList(cls.db)
        with cls.db.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE tasks")

    @classmethod
    def tearDownClass(cls):
        with cls.db.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE tasks")
        cls.db.close()

    def test_1_add_task(self):
        test_id = self.todolist.add_task("Przykładowe zadanie testowe")
        tasks = self.todolist.get_all_tasks()
        found = False
        for task in tasks:
            if task['id'] == test_id:
                found = True
                break
        self.assertTrue(found)

    def test_2_mark_task_as_done(self):
        test_id = self.todolist.add_task("Przykładowe zadanie testowe do oznaczenia")
        self.todolist.mark_task_as_done(test_id)
        tasks = self.todolist.get_all_tasks()
        done = False
        for task in tasks:
            if task['id'] == test_id and task['done'] == True:
                done = True
                break
        self.assertTrue(done)

    def test_3_remove_task(self):
        test_id = self.todolist.add_task("Przykładowe zadanie testowe do usunięcia")
        self.todolist.remove_task(test_id)
        tasks = self.todolist.get_all_tasks()
        found = False
        for task in tasks:
            if task['id'] == test_id:
                found = True
                break
        self.assertFalse(found)

    def test_4_get_all_tasks(self):
        self.todolist.add_task("Dodatkowe zadanie")
        tasks = self.todolist.get_all_tasks()
        self.assertLess(0,len(tasks))

if __name__ == "__main__":
    unittest.main()