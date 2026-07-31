#!/usr/bin/env python
# coding: utf-8

# визуализация изображения
# треугольного ковра Серпинского
# на основе алгоритма РСИФ

# Ячейка № 1

# подключение библиотеки numpy
import numpy as np

# подключение библиотеки matplotlib.pyplot
import matplotlib.pyplot as plt


# Ячейка № 2

# инициализация генератора случайных чисел
np.random.seed()


# задание функции,возвращающей значения
# чисел из диапазона: 0, 1,..., Basis^Power
# (Basis, Power -- числа в десятичной
# системе счисление) в системе
# счисления по основанию Basis
def Rule(Basis, Power):
    # входные переменные:
    # Basis - основание системы счисления
    # Power - показатель степени

    Tmp_list = []
    for i in range(Basis**Power + 1):
        Str_Digit = ""
        Number = i
        while Number > 0:
            Str_Digit = str(Number % Power) + Str_Digit
            Number = Number // Power
        if i == 0:
            Str_Digit = "0"
            Tmp_list.append("0")
        else:
            Tmp_list.append(Str_Digit)

    return Tmp_list


# Ячейка № 3

# задание функции, возвращающей изображение
# треугольного ковра Серпинского
# с помощью системы итерированных функций
def Serpynsky_RSIF(N_Iter, N_Trial):
    # входные переменные:
    # N_Iter - порядок ковра
    # N_Trial - число испытаний
    #           метода Монте-Карло

    # задание координат вершин
    # базового треугольника
    x1 = 0
    y1 = 0
    x2 = 1
    y2 = 1
    x3 = 1 / 2
    y3 = np.sin(np.pi / 3)

    # инициализация генератора случайных чисел
    np.random.seed()

    # задание координат
    # начальной точки
    Flag = 0
    while Flag == 0:
        Tmp_X = np.random.uniform(0, 1)
        Tmp_Y = np.sqrt(3) / 2 * np.random.uniform(0, 1)
        if (
            -np.sqrt(3) * Tmp_X + Tmp_Y <= 0
            and np.sqrt(3) * Tmp_X + Tmp_Y - np.sqrt(3) <= 0
        ):
            x0 = Tmp_X
            y0 = Tmp_Y
            Flag = 1

    # создание массива, содержащего правила итераций
    Cod_list = Rule(3, N_Iter)

    # задание значений параметров
    # аффинных преобразований
    a1 = np.array([0, 0])
    a2 = np.array([1 / 2, 0])
    a3 = np.array([1 / 4, np.sqrt(3) / 4])
    A = np.array([[1 / 2, 0], [0, 1 / 2]])

    # создание графического окна
    F = plt.figure(figsize=(8, 8))
    ax = F.add_subplot()
    polygon1 = np.array([[x1, y1], [x2, y2], [x3, y3]])

    # визуализация базового треугольника
    ax.add_patch(plt.Polygon(polygon1, facecolor="white"))
    plt.axis("equal")
    plt.axis("off")

    # визуализация треугольного ковра Серпинского
    Draw_Fractal(N_Iter, N_Trial, x0, y0, A, a1, a2, a3, Cod_list)

    plt.show()

# Ячейка № 4

# задание функции, возвращающей
# изображение фрактала


def Draw_Fractal(N_Iter, N_Trial, x0, y0, A, a1, a2, a3, Cod_list):
    for n in range(3**N_Iter):
        X1 = np.zeros(N_Trial)
        Y1 = np.zeros(N_Trial)
        X = x0
        Y = y0
        for m in range(N_Trial):
            N_R = np.random.randint(0, len(Cod_list) - 1)
            Tmp = Cod_list[N_R]
            Len_Tmp = len(Tmp)
            for j in range(Len_Tmp):
                if Tmp[j] == "0":
                    [X, Y] = Affin_Transform(X, Y, A, a1)
                if Tmp[j] == "1":
                    [X, Y] = Affin_Transform(X, Y, A, a2)
                if Tmp[j] == "2":
                    [X, Y] = Affin_Transform(X, Y, A, a3)
            X1[m] = X
            Y1[m] = Y

        plt.plot(X1, Y1, ".k", markersize=0.1)

# Ячейка № 5

# задание функции, возвращающей
# результат аффинных преобразований
# координат точек
def Affin_Transform(X, Y, A, a):
    # входные переменные:
    # X, Y - координаты точки
    # A, a - значения параметров
    #        аффинных преобразований
    R = np.array([X, Y])
    R = A.dot(R) + a
    x_Tr = R[0]
    y_Tr = R[1]

    return x_Tr, y_Tr


# Ячейка № 6

# визуализация треугольного ковра
# Серпинского пятого порядка
Serpynsky_RSIF(5, 10**4)
