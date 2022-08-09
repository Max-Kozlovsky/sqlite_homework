"""Создайте новую Базу данных
Поля: id, 2 целочисленных поля. Целочисленные поля заполняются рандомно от 0 до 9.
Выберите случайную запись из БД
Если каждое число данной записи чётное, то удалите эту запись, если нечётное, то обновите данные в ней на(2,2) """

import sqlite3
import random


def show_results() -> list:
    """Функция создает запрос на получение всех данных из таблицы и возвращает эти данные"""
    cursor.execute("""SELECT * FROM table_3""")
    data_table = cursor.fetchall()
    return data_table


db = sqlite3.connect('task3.db')  # создаем базу данных
cursor = db.cursor()  # объект курсор для взаимодействия с БД

# создание таблицы с двумя колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS
    table_3 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col_1 INT,
    col_2 INT)
    ''')

for _ in range(5):  # заполняем таблицу случайными числами
    num1: int = random.randint(0, 9)
    num2: int = random.randint(0, 9)
    cursor.execute("""INSERT INTO table_3 (col_1, col_2) VALUES(?,?)""", (num1, num2))
db.commit()  # сохраняем изменения

data: list = show_results()  # сохраняем данные из таблицы в переменную
print(data)

random_raw: tuple = random.choice(data)  # выбираем из таблицы случайную строку
print(random_raw)

if not random_raw[1] % 2 and not random_raw[2] % 2:  # если значения четные, удаляем строку
    cursor.execute(f"""DELETE FROM table_3 WHERE id=?""", (random_raw[0],))
    print(f'Уалена строка № {random_raw[0]}')
if random_raw[1] % 2 and random_raw[2] % 2:  # если значения нечетные, устанавливаем новые начения
    cursor.execute(f"""UPDATE table_3 SET col_1=2, col_2=2 WHERE id=?""", (random_raw[0],))
    print(f"Изменены значения в строке № {random_raw[0]}")

db.commit()  # сохраняем изменения
print(show_results())
