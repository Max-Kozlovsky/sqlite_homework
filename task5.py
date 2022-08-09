"""Создать таблицу в Базе Данных с тремя колонками(id, 2 - text, 3 - text).
Заполнить её с помощью INSERT данными (3 записи).
Удалить с помощью DELETE 2 запись.
Обновить значения 3-ей записи на: hello world с помощью UPDATE
*Записать данные с таблицы в файл в три колонки.
Первая – id, вторая и третья с данными. """

import sqlite3
import csv

db = sqlite3.connect('task5.db')  # создаем базу данных
cursor = db.cursor()  # объект курсор для взаимодействия с БД

# создание таблицы
cursor.execute("""CREATE TABLE IF NOT EXISTS 'table_5' (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                col_1 TEXT,
                col_2 TEXT
                )""")

for elem in 'abc':  # заполняем таблицу
    cursor.execute("""INSERT INTO table_5 (col_1, col_2) VALUES (?, ?)""", (elem, elem))

cursor.execute("""DELETE FROM table_5 WHERE id=2""")  # удаляем вторую строку

cursor.execute("""UPDATE table_5 SET col_1='hello', col_2='world' WHERE id=3""")  # изменяем значение третьей строки
db.commit()  # сохраняем изменения

cursor.execute("""SELECT * FROM table_5 """)  # получаем данные из таблицы
data = cursor.fetchall()  # записываем данные в переменную
print(data)

with open('data.csv', 'w', newline='') as file:  # записываем данные в файл
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['id', 'col1', 'col2'])
    for elem in data:
        writer.writerow(elem)
