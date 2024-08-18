from faker import Faker
import sqlite3

fake = Faker()

# Підключення до бази даних SQLite
conn = sqlite3.connect('task_management.db')
cursor = conn.cursor()

# Заповнення таблиці users
for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cursor.execute('''INSERT INTO users (fullname, email) VALUES (?, ?)''', (fullname, email))

# Заповнення таблиці status
statuses = ['new', 'in progress', 'completed']
for status in statuses:
    cursor.execute('''INSERT INTO status (name) VALUES (?)''', (status,))

# Заповнення таблиці tasks
for _ in range(20):
    title = fake.text(max_nb_chars=50)
    description = fake.text(max_nb_chars=200)
    status_id = fake.random_int(min=1, max=3)
    user_id = fake.random_int(min=1, max=10)
    cursor.execute('''INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)''', (title, description, status_id, user_id))

# Збереження змін у базі даних
conn.commit()

# Закриття з'єднання з базою даних
conn.close()
