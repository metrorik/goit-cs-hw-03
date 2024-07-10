import psycopg2
from psycopg2 import sql
from contextlib import closing

# підключення до бази даних PostgreSQL
conn_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '1111',
    'host': 'localhost',
    'port': '5432'
}

# SQL-запити для створення таблиць та вставки даних
queries = [
    # -- Створення таблиці users з унікальним email
    """
    CREATE TABLE IF NOT EXISTS users (
      id SERIAL PRIMARY KEY,
      fullname VARCHAR(30),
      email VARCHAR(100) UNIQUE
    );
    """,
    # -- Створення таблиці status з унікальним name
    """
    CREATE TABLE IF NOT EXISTS status (
      id SERIAL PRIMARY KEY,
      name VARCHAR(50) UNIQUE
    );
    """,
    # -- Вставка значень у таблицю status
    """
    INSERT INTO status (name) VALUES
    ('new'), 
    ('in progress'), 
    ('completed')
    ON CONFLICT (name) DO NOTHING;
    """,
    # -- Створення таблиці tasks з зовнішніми ключами та каскадним видаленням
    """
    CREATE TABLE IF NOT EXISTS tasks (
      id SERIAL PRIMARY KEY,
      title VARCHAR(100),
      description TEXT,
      status_id INTEGER REFERENCES status(id) ON DELETE CASCADE,
      user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
    );
    """
]

# Функція для виконання запитів
def execute_queries(queries):
    with closing(psycopg2.connect(**conn_params)) as conn:
        with conn.cursor() as cursor:
            for query in queries:
                cursor.execute(query)
                conn.commit()

# Виконання запитів
execute_queries(queries)

print("Таблиці створено та дані вставлено успішно.")
