# -*- coding: utf-8 -
import sqlite3


class SQLighter:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select(self, x):
        x = x.replace('@', 'æ').replace('ё', 'е').replace('Ё', 'Е')
        with self.connection:

            def nocase(lc):
                return lc.lower()

            self.connection.create_function("mylower", 1, nocase)
            arr = (self.cursor.execute('SELECT iron, rus, desc FROM dict WHERE mylower(rus) = ? OR mylower(iron) = ?',
                                (x.lower(), x.lower(),)).fetchall())

        # если слова нету в словаре
        if not arr:
            return ['😔нæма зонын тæлмац - %s' % x]

        # слово есть
        else:
            s = []
            for i in arr:
                if i[0] == i[1]:  # если на осет = рус
                    s.append(i[0])
                elif x.lower() == i[0].lower():  # значение = осет *** .lower() потому, что чувствит регистр
                    # # если есть описание - добавить
                    # if i[2] is None:
                    #     a = i[1]
                    # else:
                    #     a = i[1] + ' ' + str(i[2])
                    # s.append(a)
                    '''если описание None, то верхнее если пустая строка то нижнее'''
                    a = i[1] + ' ' + str(i[2])
                    s.append(a)
                else:  # значение = рус
                    s.append(i[0])
            return s

            # print(arr)

            #     слово неполное
            #       начало слова
            #       серидина
            #       конец
            #
            #     функция которая позволяет находить похожее слово если не нашлось искомое,
            #       например: лететь(не найдено) - возможно вы имели ввиду летать?
            # написать за базу Вячесдаву Иванову

    def close(self):
        self.connection.close()


        # db = SQLighter('main.db')
        # print(db.select(input()))
        # db.close()


        # буква @
        # description
        #     если есть описание добаить в продолжение перевода
        #     если нету тоесть значение ноун ничего не вставлять
        # верхний нижний регистр