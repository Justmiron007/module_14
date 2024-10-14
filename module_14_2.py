import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')
for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i}', f'example{i}@gmail.com', f'{i}0', '1000'))

for i in range(1, 11):
    if not (i - 1) % 2:
        cursor.execute('UPDATE Users SET balance = 500 WHERE id = ?', (i,))

for i in range(1, 11):
    if not (i - 1) % 3:
        cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

cursor.execute('DELETE FROM Users WHERE id=?', (6,))
cursor.execute('SELECT COUNT(*) FROM Users')
total = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()[0]
print(total_balance / total)

connection.commit()
connection.close()
