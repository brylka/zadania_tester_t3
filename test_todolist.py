import unittest
from todolist import TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todolist = TodoList()
        self.todolist.add_task("Inicjalne zadanie")
    def test_add_task(self):
        size = len(self.todolist.get_all_tasks())
        #self.assertEqual(0, len(self.todolist.get_all_tasks()))
        test_id = self.todolist.add_task("Zadanie testowe")
        self.assertEqual(size + 1, len(self.todolist.get_all_tasks()))
        #self.assertEqual({'id' : test_id, 'task' : "Zadanie testowe", 'done' : False}, self.todolist.get_all_tasks()[-1])
        self.assertEqual(test_id, self.todolist.get_all_tasks()[-1]['id'])
        self.assertEqual("Zadanie testowe", self.todolist.get_all_tasks()[-1]['task'])
        self.assertEqual(False, self.todolist.get_all_tasks()[-1]['done'])

    def test_remove_task(self):
        #self.assertEqual(0, len(self.todolist.get_all_tasks()))
        size = len(self.todolist.get_all_tasks())
        test_id = self.todolist.add_task("Zadanie testowe")
        self.assertEqual(size + 1, len(self.todolist.get_all_tasks()))
        self.todolist.remove_task(test_id)
        self.assertEqual(size, len(self.todolist.get_all_tasks()))

    def test_mark_task_as_done(self):
        #self.assertEqual(0, len(self.todolist.get_all_tasks()))
        test_id = self.todolist.add_task("Zadanie testowe")
        #self.assertEqual(1, len(self.todolist.get_all_tasks()))
        self.assertFalse(self.todolist.get_all_tasks()[-1]['done'])
        self.todolist.mark_task_as_done(test_id)
        #self.assertEqual({'id': 1, 'task': "Zadanie testowe", 'done': True}, self.todolist.get_all_tasks()[0])
        #self.assertEqual(True, self.todolist.get_all_tasks()[0]['done'])
        self.assertTrue(self.todolist.get_all_tasks()[-1]['done'])
if __name__ == "__main__":
    unittest.main()