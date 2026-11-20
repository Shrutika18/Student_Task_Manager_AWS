
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = "tasks.db"


# Database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Create database table
def create_table():
    conn = get_db_connection()

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


# Home page - Read tasks
@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks ORDER BY id DESC").fetchall()
    conn.close()

    return render_template('index.html', tasks=tasks)


# Add task - Create
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()

    if title:
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO tasks (title, description) VALUES (?, ?)",
            (title, description)
        )
        conn.commit()
        conn.close()

    return redirect(url_for('index'))


# Edit task - Update
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    conn = get_db_connection()

    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?", (id,)
    ).fetchone()

    if task is None:
        conn.close()
        return "Task not found", 404

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()

        if title:
            conn.execute(
                "UPDATE tasks SET title = ?, description = ? WHERE id = ?",
                (title, description, id)
            )
            conn.commit()

        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('edit.html', task=task)


# Complete task
@app.route('/complete/<int:id>')
def complete_task(id):
    conn = get_db_connection()
    conn.execute(
        "UPDATE tasks SET completed = 1 WHERE id = ?", (id,)
    )
    conn.commit()
    conn.close()

    return redirect(url_for('index'))


# Delete task
@app.route('/delete/<int:id>')
def delete_task(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))


# Start application
create_table()

if __name__ == '__main__':
    app.run(debug=False)

