import unittest
import pymysql
from todolistmysql import TodoList

class TestTodoList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       cls.db = pymysql.connect(host='localhost', user='root', password='', db='todolist')
       cls.todolist = TodoList(cls.db)

    def test_add_task(self):
        test_id = self.todolist.add_task("Przykładowe zadanie testowe")
        tasks = self.todolist.get_all_tasks()
        found = False
        for task in tasks:
            if task['id'] == test_id:
                found = True
                break
        self.assertTrue(found)





if __name__ == "__main__":
    unittest.main()