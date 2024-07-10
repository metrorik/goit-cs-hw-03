import psycopg2
from faker import Faker

# підключення до бази даних PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1111",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Ініціалізація бібліотеки Faker\
fake = Faker()

# наповнення таблиці users
def seed_users(n):
    for _ in range(n):
        fullname = fake.name()
        email = fake.email()
        cursor.execute(
            "INSERT INTO users (fullname, email) VALUES (%s, %s) ON CONFLICT (email) DO NOTHING;",
            (fullname, email)
        )
    conn.commit()

# наповнення таблиці tasks
def seed_tasks(n):
    cursor.execute("SELECT id FROM users;")
    user_ids = [row[0] for row in cursor.fetchall()]
    
    cursor.execute("SELECT id FROM status;")
    status_ids = [row[0] for row in cursor.fetchall()]

    for _ in range(n):
        title = fake.sentence(nb_words=6)
        description = fake.text()
        status_id = fake.random_element(elements=status_ids)
        user_id = fake.random_element(elements=user_ids)
        cursor.execute(
            "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);",
            (title, description, status_id, user_id)
        )
    conn.commit()

# Виклик функцій для заповнення даними
seed_users(9)  # 9 користувачів
seed_tasks(29)  # 29 завдань

# Закриття підключення до бази даних
cursor.close()
conn.close()
