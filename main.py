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

if __name__ == "__main__":
    app.run(debug=True)