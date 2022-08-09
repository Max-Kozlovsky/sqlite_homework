"""Создайте новую Базу данных.
Поля: id, 2 целочисленных поля. Целочисленные поля заполняются рандомно от 0 до 9
Посчитайте среднее арифметическое всех элементов без учёта id
Если среднее арифметическое больше количества записей в БД, то удалите четвёртую запись БД"""

import sqlite3
import random


def show_results() -> list:
    """Функция создает запрос на получение всех данных из таблицы и возвращает эти данные"""
    cursor.execute("""SELECT * FROM table_2""")
    data_table = cursor.fetchall()
    return data_table


db = sqlite3.connect('task2.db')  # создаем базу данных
cursor = db.cursor()  # объект курсор для взаимодействия с БД

# создание таблицы с двумя колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS
    table_2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col_1 INT,
    col_2 INT)
    ''')

for _ in range(5):  # заполняем таблицу случайными числами
    num1: int = random.randint(5, 20)
    num2: int = random.randint(5, 20)
    cursor.execute("""INSERT INTO table_2 (col_1, col_2) VALUES(?,?)""", (num1, num2))
db.commit()  # сохраняем изменения

data: list = show_results()  # сохраняем данные из таблицы в переменную
print(data)

sum_elements: int = sum([sum(elem[1:]) for elem in data])  # находим сумму всех элементов (за исключением поля id)
count_elements: int = len(data) * 2  # количество элементов
average: float = round(sum_elements / count_elements, 2)  # среднее арифметическое значений (за исключением поля id)
print(f'Среднее арифметическое всех элементов таблицы: {average}')

# удаление 4 строки  при выполнении условия
if average > count_elements:
    cursor.execute("""DELETE FROM table_2 WHERE id=4""")
    db.commit()

print(show_results())
