
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from pathlib import Path

app = Flask(__name__)

DATABASE = Path(__file__).with_name("tasks.db")


# Database connection
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Create database table
def create_table():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


# Home page - display all tasks
@app.route("/")
def index():

    conn = get_db()

    tasks = conn.execute(
        "SELECT * FROM tasks ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template("index.html", tasks=tasks)


# Add a new task
@app.route("/add", methods=["POST"])
def add_task():

    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()

    if title:
        conn = get_db()

        conn.execute(
            "INSERT INTO tasks (title, description) VALUES (?, ?)",
            (title, description)
        )

        conn.commit()
        conn.close()

    return redirect(url_for("index"))


# Edit task
@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):

    conn = get_db()

    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    if task is None:
        conn.close()
        return "Task not found", 404

    if request.method == "POST":

        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()

        if title:
            conn.execute(
                """UPDATE tasks
                   SET title = ?, description = ?
                   WHERE id = ?""",
                (title, description, task_id)
            )

            conn.commit()
            conn.close()

            return redirect(url_for("index"))

    conn.close()

    return render_template("edit.html", task=task)


# Mark task as completed
@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):

    conn = get_db()

    conn.execute(
        """UPDATE tasks
           SET completed = CASE
               WHEN completed = 0 THEN 1
               ELSE 0
           END
           WHERE id = ?""",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("index"))


# Delete task
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):

    conn = get_db()

    conn.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("index"))


if __name__ == "__main__":

    create_table()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
