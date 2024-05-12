import unittest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By

def generate_random_string(length=8):
    letters = string.ascii_letters
    random_string = ''
    for i in range(length):
        random_char = random.choice(letters)
        random_string += random_char
    return random_string

class TestTodoApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Ustawienia przeglądarki
        cls.random_task_name = f"Task {generate_random_string()}"
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://127.0.0.1:5000/tasks")
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        # Zamykanie przeglądarki po zakończeniu testów
        cls.driver.quit()

    def test_1_add_task(self):
        # Dodaj zadanie
        self.driver.find_element(By.NAME, "task").send_keys(self.random_task_name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Dodaj zadanie']").click()
        time.sleep(2)

        # Pobierz wszystkie elementy listy zadań
        tasks = self.driver.find_elements(By.CSS_SELECTOR, "li.task-not-done")

        # Sprawdź, czy ostatnio dodane zadanie znajduje się na liście
        if tasks:
            task_text = tasks[-1].text
            self.assertIn(self.random_task_name, task_text)
        else:
            self.fail("No tasks found")

    def test_2_mark_task_as_done(self):
        # Oznacz ostatnio dodane zadanie jako wykonane
        self.driver.find_element(By.XPATH, f"//li[contains(text(), '{self.random_task_name}')]//button[text()='Wykonane']").click()
        time.sleep(2)

        # Sprawdź, czy zadanie jest oznaczone jako wykonane
        task_elements = self.driver.find_elements(By.CSS_SELECTOR, "li.task-done")
        found = False
        for task_element in task_elements:
            if self.random_task_name in task_element.text:
                found = True
                break
        self.assertTrue(found, "Task was not marked as done correctly.")

    def test_3_delete_task(self):
        # Usuń ostatnie zadanie
        self.driver.find_element(By.XPATH,f"//li[contains(text(), '{self.random_task_name}')]//button[text()='Usuń']").click()
        time.sleep(2)

        # Sprawdź, czy zadanie zostało usunięte
        tasks_elements = self.driver.find_elements(By.CSS_SELECTOR, "li")
        task_present = False
        for task_element in tasks_elements:
            if self.random_task_name in task_element.text:
                task_present = True
                break
        self.assertFalse(task_present, "Task was not removed successfully.")

if __name__ == "__main__":
    unittest.main()
