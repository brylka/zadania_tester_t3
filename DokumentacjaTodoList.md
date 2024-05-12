
# Dokumentacja klasy TodoList

## Przegląd
Klasa `TodoList` zapewnia metody do interakcji z bazą danych MySQL w celu zarządzania listą zadań. Umożliwia dodawanie, usuwanie, oznaczanie zadań jako wykonane oraz pobieranie wszystkich zadań z bazy danych.

## Metody

### `__init__(self, db)`
Konstruktor tworzący nową instancję klasy TodoList.
- **Parametry:**
  - `db`: Obiekt `pymysql.connections.Connection` reprezentujący połączenie z bazą danych.

### `add_task(self, task)`
Dodaje nowe zadanie do listy zadań.
- **Parametry:**
  - `task`: Ciąg znaków reprezentujący opis zadania.
- **Zwraca:**
  - ID nowo dodanego zadania jako liczba całkowita.

### `remove_task(self, task_id)`
Usuwa zadanie z listy zadań, używając jego ID.
- **Parametry:**
  - `task_id`: Liczba całkowita identyfikująca zadanie do usunięcia.
- **Zwraca:**
  - Nic.

### `mark_task_as_done(self, task_id)`
Oznacza konkretne zadanie jako wykonane, używając jego ID.
- **Parametry:**
  - `task_id`: Liczba całkowita identyfikująca zadanie do oznaczenia jako wykonane.
- **Zwraca:**
  - Nic.

### `get_all_tasks(self)`
Pobiera wszystkie zadania z listy zadań.
- **Zwraca:**
  - Listę słowników, gdzie każdy słownik reprezentuje zadanie z kluczami takimi jak `id`, `task` i `done`.

## Przykład użycia
```python
import pymysql
db = pymysql.connect(host='localhost', user='user', password='password', db='database_name')
todolist = TodoList(db)

# Dodawanie zadań
todolist.add_task("Naucz się SQL")
todolist.add_task("Przygotuj obiad")

# Oznaczanie zadania jako wykonane
todolist.mark_task_as_done(1)

# Usuwanie zadania
todolist.remove_task(2)

# Pobieranie wszystkich zadań
tasks = todolist.get_all_tasks()
print(tasks)
```
