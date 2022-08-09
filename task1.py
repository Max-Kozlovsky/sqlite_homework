"""Создайте новую Базу данных. В ней создайте таблицу с тремя полями, два текстовых, одно – целое число.
Число запрашивается с клавиатуры, а слова задаются статически.
* Выведите каждую запись в отдельную строку"""

import sqlite3

db = sqlite3.connect('task1.db')  # создаем базу данных
cursor = db.cursor()  # объект курсор для взаимодействия с БД

# создание таблицы с тремя колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS  
                task_1(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               col_1 TEXT,
               col_2 TEXT,
               col_3 BIG_INT)
               ''')

for i in range(1, 6):  # заполнение таблицы
    num = int(input('enter a integer: '))
    col1 = f'value{i}'
    col2 = f'arg{i}'
    cursor.execute("""INSERT INTO task_1(col_1, col_2, col_3) VALUES(?,?,?)""", (col1, col2, num))

db.commit()  # сохраняем изменения
cursor.execute("""SELECT * FROM task_1""")  # запрос всех данных из таблицы
k: list = cursor.fetchall()  # сохраняем запрос в переменную
print(k)
