import sqlite3

def create_db():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    sql = """CREATE TABLE IF NOT EXISTS Task (id INTEGER KEY AUTOINCREMENT, text VARCHAR(1000) NOT NULL DEFAULT '',
             is done INTEGER DEFAULT  0
             )
    """

    cursor.execute(sql)
    conn.commit()

def add_task(task_text):
    ...