from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

@app.route("/")
def index():
    tasks= database.get_tasks()
    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_text = request.form.get('task-text')
    if task_text:
        database.add_task(task_text)
    return redirect(url_for('index'))

@app.route("/delete", methods=['POST'])
def delete():
    task_id = request.form.get('task-id')

    if task_id:
        database.delete_task(task_id)
    return redirect(url_for('index'))

@app.route('/change_status', methods=['POST'])
def change_status():
    task_id = request.form.get('task-id')

    if task_id:
        database.change_task_status(task_id)
    return redirect(url_for('index'))

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        login = request.form["login"]
        pass1 = request.form["pass1"]
        pass2 = request.form["pass2"]
        errors = []
        # проверка существования пользователя
        if database.is_user_exists(login):
            errors.append("Такой пользователь уже существует")
        # проверка на одинаковость паролей
        if pass1 != pass2:
            errors.append("Пароли НЕ совпадают")

        # проверка качества пароля
        if len(pass1) < 4:
            errors.append("Пароль должен содержать не менее 4 символов")
        
        if len(errors) == 0:
            database.add_user(login, pass1)
            return render_template("success_register.html")
        
        else:
            return render_template("register.html", errors=errors)
        
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]

        auth_user = database.auth_user(login, password)
        if auth_user == -1:
            return render_template("login.html", errors=["Неверный логин или пароль"])
        
if __name__ == "__main__":
    app.run(debug=True)