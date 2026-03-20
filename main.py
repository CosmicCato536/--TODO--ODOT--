from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route("/")
def index():
    tasks= database.get_tasks()
    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)