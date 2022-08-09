"""Создать 2 таблицы в Базе Данных
Одна будет хранить текстовые данные(1 колонка). Другая числовые(1 колонка).
Есть список, состоящий из чисел и слов. Если элемент списка слово, записать его в
соответствующую таблицу, затем посчитать длину слова и записать её в числовую таблицу.
Если элемент списка число: проверить, если число чётное записать его в таблицу чисел, если нечётное, то записать во
вторую таблицу слово: «нечётное»
Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице. Если меньше, то обновить 1
запись в первой таблице на «hello»"""

import sqlite3


def show_table_s():
    """Функция возвращает содержимое таблицы со строками"""
    db1.commit()
    cursor1.execute("""SELECT * FROM table_s""")
    s = cursor1.fetchall()
    return s


def show_table_i():
    """Функция возвращает содержимое таблицы с числами"""
    db2.commit()
    cursor2.execute("""SELECT * FROM table_i""")
    i = cursor2.fetchall()
    return i


lst: list = [1, 2, 'world', 3, 4, 'python', 5, 'good']  # тестовый список

# создаем базу данных для строк
db1 = sqlite3.connect('hw1.db')
cursor1 = db1.cursor()
cursor1.execute("""CREATE TABLE IF NOT EXISTS table_s(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data1 TEXT
                    )""")

# создаем базу данных для чисел
db2 = sqlite3.connect('hw2.db')
cursor2 = db2.cursor()
cursor2.execute("""CREATE TABLE IF NOT EXISTS table_i(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data2 INTEGER
                    )""")

for elem in lst:  # перебираем элементы списка
    if isinstance(elem, str):  # если элемент является строкой
        cursor1.execute("""INSERT INTO table_s (data1) VALUES (?)""", (elem,))
        cursor2.execute("""INSERT INTO table_i (data2) VALUES (?)""", (len(elem),))
    elif isinstance(elem, int):  # если элемент является числом
        if elem % 2 == 0:  # четным
            cursor2.execute("""INSERT INTO table_i (data2) VALUES (?)""", (elem,))
        else:  # нечетным
            cursor1.execute("""INSERT INTO table_s (data1) VALUES ('нечетное')""")

if len(show_table_i()) > 5:  # если в таблице с числами больше 5 значений
    cursor1.execute("""DELETE FROM table_s WHERE id=1""")
    db1.commit()
else:  # если в таблице с числами меньше 5 значений
    cursor1.execute("""UPDATE table_s SET data1='hello' WHERE id=1""")
    db1.commit()

print(show_table_s())

print(show_table_i())
