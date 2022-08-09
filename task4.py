"""Создайте метод класса для работы с БД В БД
Если передан 1 аргумент, вставить в таблицу запись с числом 3.
Если переданы 2 аргумента: проверить является ли второй аргумент числом. Если условие верно, то
удалить первую запись из БД.
Если переданы 2 аргумента, их значения неизвестны, а 3 является числом, то обновить на число 77 запись 3."""

import sqlite3


class Table:
    """класс для работы с БД"""
    db = sqlite3.connect('task4.db')  # создаем базу данных
    cursor = db.cursor()  # объект курсор для взаимодействия с БД
    # создание таблицы
    cursor.execute("""CREATE TABLE IF NOT EXISTS 'table_4'(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    col_1 INTEGER)""")

    @classmethod
    def change_table(cls, *args):
        if len(args) == 1:  # если передан один параметр
            cls.cursor.execute("""INSERT INTO table_4 (col_1) VALUES (3)""")  # добавляем строку со значением 3
            print('Добавлена строка со значением 3')
        elif len(args) == 2 and isinstance(args[1], (int, float)):  # если передано 2 параметра и второй - число
            cls.cursor.execute("""SELECT id FROM table_4""")  # получаем все данные из таблицы
            index_data = cls.cursor.fetchall()  # записываем данные в переменную
            first_id: int = min([i[0] for i in index_data])  # находим минимальный индекс
            cls.cursor.execute("""DELETE FROM table_4 WHERE id=?""", (first_id,))  # удалям первую строку
            print(f"Строка {first_id} удалена")
        elif len(args) == 3 and isinstance(args[2], (int, float)):  # если передано 3 параметра и третий - число
            cls.cursor.execute("""SELECT id FROM table_4""")  # получаем все данные из таблицы
            index_data = cls.cursor.fetchall()  # записываем данные в переменную
            index_list = [i[0] for i in index_data]  # находим минимальный индекс
            first_id = min(index_list)  # находим минимальный индекс
            if len(index_list) >= 3:  # проверяем в таблице наличие минимум 3 строк
                cls.cursor.execute("""UPDATE table_4 SET col_1=77 WHERE id=?""", (first_id + 2,))  # изменяем 3 строку
                print(f"В третью строку внесено значение 77")
            else:
                print('Размер таблицы меньше 3 строк')

        cls.db.commit()  # сохраняем изменения

    @classmethod
    def get_table(cls):
        """функция для вывода на экран """
        cls.cursor.execute("""SELECT * FROM table_4""")
        data_table = cls.cursor.fetchall()
        return data_table


# тесты
Table.change_table(1)
print(Table.get_table())
Table.change_table('a')
print(Table.get_table())
Table.change_table(2)
print(Table.get_table())
Table.change_table(2)
print(Table.get_table())
Table.change_table(2, 4)
print(Table.get_table())
Table.change_table('d', False, 34)
print(Table.get_table())
