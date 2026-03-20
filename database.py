import sqlite3

def create_db():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    sql = """CREATE TABLE IF NOT EXISTS Task (id INTEGER PRIMARY KEY AUTOINCREMENT, text VARCHAR(1000) NOT NULL DEFAULT '',
             is_done INTEGER DEFAULT  0
             )
    """

    cursor.execute(sql)
    conn.commit()

def add_task(task_text):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Task (text) VALUES (?)", (task_text,))
    conn.commit()

def get_tasks():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Task")
    tasks = cursor.fetchall()
    return tasks

if __name__ == "__main__":
    create_db()
    add_task("task 1")
    add_task("task 2")

    tasks = get_tasks()
    for task in tasks:
        print(task)