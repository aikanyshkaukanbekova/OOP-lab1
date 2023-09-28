#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import math


class Triangle:
    """
    Класс "Треугольник" хранящий в себе информацию о длине трех сторон и углов
    """

    def __init__(self, a, b, c):
        """
        Конструктор класса, принимающий значения сторон a, b и c
        """
        self.a = a
        self.b = b
        self.c = c
        # Вызываем приватный метод для подсчета углов треугольника
        self._calculate_degrees()

    def get_a(self):
        """
        Возвращает значение стороны a
        """
        return self.a

    def get_b(self):
        """
        Возвращает значение стороны b
        """
        return self.b

    def get_c(self):
        """
        Возвращает значение стороны c
        """
        return self.c

    def set_a(self, value):
        """
        Устанавливает значение стороны a
        """
        self.a = value
        # Вызываем приватный метод для подсчета углов треугольника
        self._calculate_degrees()

    def set_b(self, value):
        """
        Возвращает значение стороны b
        """
        self.b = value
        # Вызываем приватный метод для подсчета углов треугольника
        self._calculate_degrees()

    def set_c(self, value):
        """
        Возвращает значение стороны c
        """
        self.c = value
        # Вызываем приватный метод для подсчета углов треугольника
        self._calculate_degrees()

    def area(self):
        """
        Возвращает площадь треугольника
        """
        s = (self.a + self.b + self.c) / 2
        # Высчитываем площадь треугольника по формуле
        # math.sqrt - функция квадратного корня
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        """
        Возвращает периметр треугольника
        """
        return self.a + self.b + self.c

    def height_a(self):
        """
        Возвращает высоту стороны a
        """
        return 2 * self.area() / self.a

    def height_b(self):
        """
        Возвращает высоту стороны b
        """
        return 2 * self.area() / self.b

    def height_c(self):
        """
        Возвращает высоту стороны c
        """
        return 2 * self.area() / self.c

    def print_type(self):
        """
        Метод выводит в консоль тип треугольника
        Если тип не удалось вывести - не выводит ничего
        """
        # У равностороннего треугольника все три стороны равны между собой
        if self.a == self.b == self.c:
            print("Треугольник равносторонний")
        # У равнобедренноо треугольника два катета равны
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            print("Треугольник равнобедренный")
        # У прямоугольного треугольника один угол равен 90 градусов
        elif self.first_angle_degree == 90 or self.second_angle_degree == 90 or self.third_angle_degree == 90:
            print("Треугольник прямоугольный")

    def _calculate_degrees(self):
        """
        Приватный метод для подсчета градусов всех треух углов.
        Учитывая длины сторон a, b и c взятых из полей класса
        """
        self.first_angle_degree = math.degrees(
            math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c)))
        self.second_angle_degree = math.degrees(
            math.acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c)))
        self.third_angle_degree = math.degrees(
            math.acos((self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b)))

    def display(self):
        """
        Метод выводит в консоль значения сторон треугольника
        """
        print(f"(a: {self.a}, b: {self.b}, c: {self.c})")


if __name__ == '__main__':
    # Создаем произвольный треугольник
    triangle = Triangle(6, 8, 10)

    # Выводим его в консоль
    triangle.display()
    # Выводим тип треугольника в консоль
    triangle.print_type()

    # Выводим значение стороны a в консоль
    print(triangle.get_a())
    # Устанавливаем новое значение для стороны a
    triangle.set_a(10)
    # Выводим треугольник в консоль
    triangle.display()

    # Выводим в консоль площадь, периметр и высоту всех трех сторон треугольника
    print(f"Площадь: {triangle.area()}")
    print(f"Периметр: {triangle.perimeter()}")
    print(f"Высота a: {triangle.height_a()}")
    print(f"Высота b: {triangle.height_b()}")
    print(f"Высота c: {triangle.height_c()}")
