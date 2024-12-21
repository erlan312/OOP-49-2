import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    fio VARCHAR (100) NOT NULL,
    age INTEGER NOT NULL,
    hobby TEXT
    )
""")

connect.commit()

# CRUD - Create Read Update Delete

def add_user(fio, age, hobby=""):
    cursor.execute('INSERT INTO users(fio, age, hobby) VALUES (?, ?, ?)', (fio, age, hobby))
    connect.commit()
    print(f"Пользователь {fio} добавлен.")

add_user('Илья Муромец', 26, 'Бегать')
add_user('John Doe', 27, 'Спать')

def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if users:
        print("Список всех пользователей:")
        for user in users:
            print(f'FIO: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}')
    else:
        print("Список пользователей пуст.")

def get_users_by_age(age):
    cursor.execute('SELECT * FROM users WHERE age = ?', (age,))
    users = cursor.fetchall()

    if users:
        print(f"Пользователи с возрастом {age}:")
        for user in users:
            print(f'FIO: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}')
    else:
        print(f"Пользователей с возрастом {age} не найдено.")




add_user('Илья Муромец', 26, 'Бегать')
add_user('John Doe1', 23, 'Спать')
add_user('John Doe2', 24, 'Играть')
add_user('John Doe3', 25, 'Гулять')
add_user('John Doe4', 27, 'Ничего')

# Пример использования функций
get_all_users()  # Вывод всех пользователей
print()  # Пустая строка для читаемости

# Пример поиска пользователей по возрасту
get_users_by_age(27)

connect.close()

