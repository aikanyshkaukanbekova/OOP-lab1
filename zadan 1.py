#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import math

class Pair:
    """
    Класс, хранящий введенные числа k и n в полях first и second
    """

    def __init__(self, first, second):
        """
        Конструктор класса, принимает два параметра, валидирует их и сохраняет в поля
        """
        # Удостоверимся, что first является целым числом
        if not isinstance(first, int):
            raise TypeError("Значение first должно быть целым положительным числом")

        # Удостоверимся, что second является целым числом
        if not isinstance(second, int):
            raise TypeError("Значение second должно быть целым положительным числом")

        # Удостоверимся, что first является положительным числом
        if first < 0:
            raise ValueError("Значение first должно быть положительным")

        # Удостоверимся, что second является целым числом
        if second < 0:
            raise ValueError("Значение second должно быть положительным")

        # Удостоверимся, что число first больше second
        if first > second:
            raise ValueError("Значение first должно быть меньше либо равно чем second")

        # Записываем значения в поля
        self.first = first
        self.second = second

    def combination(self):
        """
        Метод высчитывает значения по формуле, с использованием переданных в конструкторе значений
        """
        return math.factorial(self.second) / (math.factorial(self.second - self.first) * math.factorial(self.first))

    def display(self):
        """
        Метод выводит экземпляра класса в консоль с указанием переданных в конструктор значений полей first и second
        """
        print(f"({self.first}, {self.second})")

    @classmethod
    def read(cls):
        """
        Статичный метод для создания экземпляра класса с запрашиваеним значений в консоли
        """
        k = int(input("Введите число k: "))
        n = int(input("Введите число n: "))

        return cls(k, n)


def make_pair(first, second):
    """
    Функция создания экземпляра класса Pair, принимая значения полей как аргументы
    """
    return Pair(first, second)


if __name__ == '__main__':
    # Создаем экземпляр класса, запрашивая значения через консоль
    pair = Pair.read()
    # Отображаем созданный объект в консоли
    pair.display()
    # Выводим посчитанное по формуле значение с использованием метода combination
    print(pair.combination())
