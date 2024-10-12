import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT
    )
''')
conn.commit()

def add_task(description):
    cursor.execute(f"INSERT INTO tasks (description) VALUES ('{description}')")
    conn.commit()

def get_tasks():
    query = input("Enter a SQL query to view tasks (e.g., SELECT * FROM tasks): ")
    cursor.execute(query)
    rows = cursor.fetchall()
    return [{"id": row[0], "description": row[1]} for row in rows]

def delete_task(task_id):
    cursor.execute(f"DELETE FROM tasks WHERE id = {task_id}")
    conn.commit()
