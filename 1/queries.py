import psycopg2
from contextlib import closing

# підключення до бази даних PostgreSQL
conn_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '1111',
    'host': 'localhost',
    'port': '5432'
}

# виконання запиту та виведення результату
def execute_query(query):
    with closing(psycopg2.connect(**conn_params)) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            if cursor.description:
                for row in cursor.fetchall():
                    print(row)
            else:
                conn.commit()

# SQL-запити
queries = [
    "SELECT * FROM tasks WHERE user_id = 1;",
    "SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');",
    "UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1;",
    "SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);",
    "INSERT INTO tasks (title, description, status_id, user_id) VALUES ('New Task Title', 'Task Description', (SELECT id FROM status WHERE name = 'new'), 1);",
    "SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');",
    "DELETE FROM tasks WHERE id = 1;",
    "SELECT * FROM users WHERE email LIKE 'david11@example.com';",
    "UPDATE users SET fullname = 'New Marcus' WHERE id = 1;",
    """SELECT status.name, COUNT(tasks.id) AS task_count
       FROM tasks
       JOIN status ON tasks.status_id = status.id
       GROUP BY status.name;""",
    """SELECT tasks.*
       FROM tasks
       JOIN users ON tasks.user_id = users.id
       WHERE users.email LIKE '%@example.com';""",
    "SELECT * FROM tasks WHERE description IS NULL OR description = '';",
    """SELECT users.fullname, tasks.title, tasks.description
       FROM tasks
       INNER JOIN users ON tasks.user_id = users.id
       WHERE tasks.status_id = (SELECT id FROM status WHERE name = 'in progress');""",
    """SELECT users.fullname, COUNT(tasks.id) AS task_count
       FROM users
       LEFT JOIN tasks ON users.id = tasks.user_id
       GROUP BY users.fullname;"""
]

# результати всіх запитів
for query in queries:
    print(f"Executing query: {query}")
    execute_query(query)
    print("\n")
