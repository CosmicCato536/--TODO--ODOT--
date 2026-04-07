import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def create_db():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            login VARCHAR(1000) NOT NULL DEFAULT '',
            password VARCHAR(1000) NOT NULL DEFAULT ''
        )
          '''
    cursor.execute(sql)

    sql = '''CREATE TABLE IF NOT EXISTS task (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            text VARCHAR(1000) NOT NULL DEFAULT '',
            is_done INTEGER DEFAULT  0,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user(id)
        )
          '''
    cursor.execute(sql)


    conn.commit()

def add_task(task_text):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO task (text) VALUES (?)", (task_text,))
    conn.commit()

def get_tasks():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM task")
    tasks = cursor.fetchall()
    return tasks

def delete_task(task_id):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM task WHERE id = ?", (task_id,))
    conn.commit()

def change_task_status(task_id):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE task SET is_done = 1-is_done WHERE id = ?", (task_id,))
    conn.commit()

def add_user(login, password):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)

    cursor.execute("INSERT INTO user (login, password) VALUES (?, ?)", (login, hashed_password))
    print("Создан пользователь" + login)
    conn.commit()

def is_user_exists(login):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user WHERE login = ?", (login,))
    user = cursor.fetchone()

    return user != None

def get_users():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()
    return users

def auth_user(login, password):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user WHERE login=? AND password=?", (login, password)
                   )
    user = cursor.fetchone()
    if not user:
        return -1
    
    if check_password_hash(user[2], password):
        return user[0]
    else:
        return -1

if __name__ == "__main__":
    create_db()
    add_user("admin", "SAIKT")
    add_user("user", "password")

    users = get_users()
    print(users)