import sqlite3

connection = sqlite3.connect('products.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
    )
    ''')

    for i in range(1, 5):
        cursor.execute('REPLACE INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
                       (f'{i}', f'Продукт {i}', f'Описание {i}', f'{i * 100}'))
    connection.commit()
    # connection.close()


def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    return products


def add_user(username, email, age, balance=1000):
    cursor.execute(
        f"REPLACE INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', {age}, {balance})")
    connection.commit()


def is_included(username):
    query = "SELECT * FROM Users WHERE username = ?"
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    if user:
        return True
    else:
        return False
