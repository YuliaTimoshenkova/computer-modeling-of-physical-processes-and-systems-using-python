#!/usr/bin/env python
# coding: utf-8

# визуализация изображения
# треугольного ковра Серпинского

# Ячейка № 1

# подключение библиотеки numpy
import numpy as np

# подключение библиотеки matplotlib.pyplot
import matplotlib.pyplot as plt


# Ячейка № 2

# задание функции, возвращающей
# изображение треугольного
# ковра Серпинского
def Serpinsky(L_max):
    # L_max - порядок ковра Серпинского

    # задание рекурсивной функции,
    # прорисовывающей треугольники белого цвета
    # соответствующих размеров
    def Simplex(x1, y1, x2, y2, x3, y3, n, L_max):
        # входные переменные:
        # x1, y1 - координаты первой
        #          вершины треугольника
        # x2, y2 - координаты второй
        #          вершины треугольника
        # x3, y3 - координаты третьей
        #          вершины треугольника
        # n - номер текущего порядка
        #     треугольников
        # L_max - порядок треугольного
        #         ковра Серпинского

        if n < L_max:
            # вычисление значений
            # координат вершин треугольников
            # данного уровня
            dx = (x2 - x1) / 2
            dy = (y3 - y1) / 2
            X1_n = x1 + dx
            Y1_n = y1
            X2_n = x1 + dx + dx / 2
            Y2_n = y1 + dy
            X3_n = x1 + dx / 2
            Y3_n = y1 + dy

            # увеличение значения
            # счетчика порядка
            # треугольного ковра Серпинского
            n = n + 1

            # визуализация данного треугольника
            ax.add_patch(
                plt.Polygon(
                    [[X1_n, Y1_n], [X2_n, Y2_n], [X3_n, Y3_n]], facecolor="white"
                )
            )
            # рекурсия
            Simplex(x1, y1, X1_n, Y1_n, X3_n, Y3_n, n, L_max)
            Simplex(X1_n, Y1_n, x2, y2, X2_n, Y2_n, n, L_max)
            Simplex(X3_n, Y3_n, X2_n, Y2_n, x3, y3, n, L_max)

    # задание координат
    # вершин базового треугольника
    x1 = 0
    y1 = 0

    x2 = 1
    y2 = 0

    x3 = 0.5
    y3 = np.sin(np.pi / 3)

    # создание графического окна
    F = plt.figure(figsize=(8, 8))

    ax = F.add_subplot()

    # отображение базового треугольника черного цвета
    polygon1 = np.array([[x1, y1], [x2, y2], [x3, y3]])
    ax.add_patch(plt.Polygon(polygon1, facecolor="black"))
    plt.axis("equal")
    # отключение нумерации
    # осей графика
    plt.axis("off")

    # вызов рекурсивной
    # функции Simplex
    Simplex(x1, y1, x2, y2, x3, y3, 0, L_max)

    plt.show()

# Ячейка № 3

# построение изображения
# треугольного ковра Серпинcкого
Serpinsky(8)


# визуализация изображения
# квадратного ковра Серпинского

# Ячейка № 4

# задание функции,
# возвращающей значения
# квадратного ковра Серпинского
def Serpinsky_Qu(L_max):
    # L_max - порядок квадратного
    #         ковра Серпинского

    # задание рекурсивной функции,
    # прорисовывающей квадраты
    # белого цвета
    # соответствующих размеров
    def Quadrate(x1, y1, x2, y2, x3, y3, x4, y4, n, L_max):
        # входные переменные:
        # x1, y1 - координаты первой
        #          вершины квадрата
        # x2, y2 - координаты второй
        #          вершины квадрата
        # x3, y3 - координаты третьей
        #          вершины квадрата
        # x4, y4 - координаты четвертой
        #          вершины квадрата
        # n - номер текущего порядка
        #     треугольников
        # L_max - порядок квадратного
        #         ковра Серпинского

        if n < L_max:
            # вычисление значений
            # координат вершин квадратов
            # данного уровня
            dx = (x2 - x1) / 3
            dy = (y3 - y1) / 3
            X1_n = x1 + dx
            Y1_n = y1 + dy
            X2_n = x1 + dx + dx
            Y2_n = y1 + dy
            X3_n = x1 + dx + dx
            Y3_n = y1 + dy + dy
            X4_n = x1 + dx
            Y4_n = y1 + dy + dy
            # визуализация данного квадрата
            ax.add_patch(
                plt.Polygon(
                    [[X1_n, Y1_n], [X2_n, Y2_n], [X3_n, Y3_n], [X4_n, Y4_n]],
                    facecolor="white",
                )
            )
            # увеличение значения
            # счетчика порядка
            # квадратного ковра Серпинского
            n = n + 1

            # рекурсия
            Quadrate(x1, y1, x1 + dx, y1, x1 + dx, y1 + dy, x1, y1 + dy, n, L_max)
            Quadrate(
                x1 + dx,
                y1,
                x1 + 2 * dx,
                y1,
                x1 + 2 * dx,
                y1 + dy,
                x1 + dx,
                y1 + dy,
                n,
                L_max,
            )
            Quadrate(
                x1 + 2 * dx, y1, x2, y1, x2, y1 + dy, x1 + 2 * dx, y1 + dy, n, L_max
            )
            Quadrate(
                x1 + 2 * dx,
                y1 + dy,
                x2,
                y1 + dy,
                x2,
                y1 + 2 * dy,
                x1 + 2 * dx,
                y1 + 2 * dy,
                n,
                L_max,
            )
            Quadrate(
                x1 + 2 * dx,
                y1 + 2 * dy,
                x2,
                y1 + 2 * dy,
                x2,
                y3,
                x1 + 2 * dx,
                y3,
                n,
                L_max,
            )
            Quadrate(
                x1 + dx,
                y1 + 2 * dy,
                x1 + 2 * dx,
                y1 + 2 * dy,
                x1 + 2 * dx,
                y4,
                x1 + dx,
                y4,
                n,
                L_max,
            )
            Quadrate(
                x1, y1 + 2 * dy, x1 + dx, y1 + 2 * dy, x1 + dx, y4, x1, y4, n, L_max
            )
            Quadrate(
                x1,
                y1 + dy,
                x1 + dx,
                y1 + dy,
                x1 + dx,
                y1 + 2 * dy,
                x1,
                y1 + 2 * dy,
                n,
                L_max,
            )

    # задание  координат вершин
    # базового прямоугольника
    x1 = 0
    y1 = 0
    x2 = 1
    y2 = 0
    x3 = 1
    y3 = 1
    x4 = 0
    y4 = 1

    # отображение базового квадрата черного цвета
    F = plt.figure(figsize=(8, 8))
    ax = F.add_subplot()
    polygon1 = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    ax.add_patch(plt.Polygon(polygon1, facecolor="black"))
    # отключение нумерации
    # осей графика
    plt.axis("off")

    # вызов рекурсивной
    # функции Quadrate
    Quadrate(x1, y1, x2, y2, x3, y3, x4, y4, 0, L_max)

    plt.show()

# Ячейка № 5

# построение изображения
# квадратного ковра Серпинского
Serpinsky_Qu(5)


# визуализация изображения
# кривой Коха

# Ячейка № 6

# задание функции, возвращающей
# изображение кривой Коха
def Koch(N):
    # задание рекурсивной функции,
    # возвращающей изображения
    # отрезков кривой Коха-
    def Coord(X1, Y1, X2, Y2, n):
        # входные переменные
        # X1, Y1 - координаты левого конца
        #          отрезка кривой Коха
        # X2, Y2 - координаты правого конца
        #          отрезка кривой Коха
        # n - текущее значение
        #     порядка кривой Коха

        if n > 0:
            # вычисление координат отрезков
            # кривой Коха на текущем шаге рекурсии
            dx = (X2 - X1) / 3
            dy = (Y2 - Y1) / 3
            X1_n = X1 + dx
            Y1_n = Y1 + dy
            X2_n = X1 + 2 * dx
            Y2_n = Y1 + 2 * dy
            X_mid = dx / 2 - dy * np.sin(np.pi / 3) + X1_n
            Y_mid = dy / 2 + dx * np.sin(np.pi / 3) + Y1_n
            # рекурсия
            Coord(X1, Y1, X1_n, Y1_n, n - 1)
            Coord(X1_n, Y1_n, X_mid, Y_mid, n - 1)
            Coord(X_mid, Y_mid, X2_n, Y2_n, n - 1)
            Coord(X2_n, Y2_n, X2, Y2, n - 1)
        else:
            # визуализация данного
            # отрезка кривой Коха
            plt.plot([X1, X2], [Y1, Y2], "-k", lw=1)

    # задание координат
    # концов базового
    # отрезка кривой Коха
    x1 = 0
    y1 = 0
    x2 = 1
    y2 = 0

    # инициализация графического окна
    F = plt.figure(figsize=(8, 8))
    F.add_subplot()
    plt.axis("off")
    plt.axis("equal")
    Coord(x1, y1, x2, y2, N)

    plt.show()

# Ячейка № 7

# построение изображения
# кривой Коха 4-го порядка

Koch(6)

# визуализация изображения
# снежинки Коха

# Ячейка № 8

# задание рекурсивной
# функции, возвращающей
# правило генерации снежинки Коха
def Rule_Koch_Snowflake(L_max, Axiom, New_F, n, Tmp):
    # входные переменные:
    # L_max - порядок снежинки Коха
    # Axiom - аксиома
    # New_F - порождающее правило
    # n -текущий порядок снежинки Коха
    # Tmp - строка, используемая для
    #       хранения порождающего правила

    while n <= L_max:
        if n == 1:
            Tmp = Axiom
            n = n + 1
        else:
            # замена замена каждой переменной F
            # в строке Tmp порождающим правилом New_F
            Tmp = Tmp.replace("F", New_F)
            # увеличение текущего
            # номера рекурсии на 1
            n = n + 1
            # рекурсия
            Tmp = Rule_Koch_Snowflake(L_max, Axiom, New_F, n, Tmp)

    return Tmp


# Ячейка № 9

# задание функции, возвращающей
# координаты снежинки Коха
def Coord(L_max, Axiom, New_F, Alpha, Teta, P):
    # входные переменные:
    # L_max - порядок снежинки Коха
    # Axiom - аксиома
    # New_F - порождающее правило
    # n -текущий порядок снежинки Коха
    # Alpha, Teta - значения углов поворота
    #               черепашки
    # P - массив, используемый для хранения
    #     координат отрезков траектории черепашки

    # вызов рекурсивной функции
    # возвращающей правило
    # движения черепашки
    Rule = Rule_Koch_Snowflake(L_max, Axiom, New_F, 1, "")

    # вычисление координат
    # отрезков траектории черепашки
    # в соответствие с в соответствие с правилом
    Tmp = np.array([0, 0])
    for i in range(len(Rule)):
        if Rule[i] == "F":
            Size = P.shape
            Tmp = P[Size[0] - 1]
            R = np.array([[np.cos(Alpha), np.sin(Alpha)]])
            R = R / (4**L_max)
            Tmp = Tmp + R
            P = np.vstack((P, Tmp))
        if Rule[i] == "+":
            Alpha = Alpha + Teta
        if Rule[i] == "-":
            Alpha = Alpha - Teta
    return P

# Ячейка № 10

# задание функции, возвращающей
# изображение снежинки Коха
def Koch_Snowflake(N):
    # задание порождающих аксиом
    Axiom = "F++F++F"
    New_F = "F-F++F-F"
    Teta = np.pi / 3
    Alpha = 0
    P = np.array([[0, 0]])

    # вызов функции, возвращающей
    # координаты снежинки Коха
    P = Coord(N, Axiom, New_F, Alpha, Teta, P)

    # визуализация снежинки Коха
    F = plt.figure(figsize=(8, 8))
    F.add_subplot()
    plt.axis("off")
    plt.plot(P[:, 0], P[:, 1], "-k", lw=1)

# Ячейка № 11

# визуализация снежинки Коха
# 4-го порядка
Koch_Snowflake(4)

# визуализация изображения
# дракона Хартера-Хайтвея

# Ячейка № 12

# задание функции, возвращающей
# правило построения
# дракона Хартера-Хайтвея
def L_Dracon(L_max, Axiom, New_F, New_X, New_Y, n, Tmp):
    # входные переменные:
    # L_max - порядок снежинки Коха
    # Axiom - аксиома
    # New_F, New_X, New_Y - порождающие правила
    # n -текущий порядок дракона Хартера-Хайтвея
    # Alpha, Teta - значения углов поворота
    #               черепашки
    # Тmp - строка, используемая для хранения
    #       правила движения черепашки

    if n <= L_max + 1:
        if n == 1:
            Tmp = Axiom
        M = len(Tmp)
        Tmp1 = ""
        for i in range(M):
            if Tmp[i] == "F":
                Tmp1 = Tmp1 + New_F
            if Tmp[i] == "X":
                Tmp1 = Tmp1 + New_X
            if Tmp[i] == "Y":
                Tmp1 = Tmp1 + New_Y
            if not (Tmp[i] == "X") and not (Tmp[i] == "Y") and not (Tmp[i] == "F"):
                Tmp1 = Tmp1 + Tmp[i]
        Tmp = Tmp1
        n = n + 1
        # рекурсия
        Tmp = L_Dracon(L_max, Axiom, New_F, New_X, New_Y, n, Tmp)

    return Tmp


# Ячейка № 13

# задание функции, возвращающей
# значения координат отрезков
# дракона Хартера-Хайтвея
def Coord_D(L_max, Axiom, New_F, New_X, New_Y, Alpha, Teta, P):
    # входные переменные:
    # L_max - порядок снежинки Коха
    # Axiom - аксиома
    # New_F, New_X, New_Y - порождающие правила
    # n -текущий порядок дракона Хартера-Хайтвея
    # Alpha, Teta - значения углов поворота
    #               черепашки
    # P - массив содержащий координату
    #     стартовой точки черепашки

    # вызов рекурсивной функции Rule
    Rule = L_Dracon(L_max, Axiom, New_F, New_X, New_Y, 1, "")

    # вычисление значений координат
    # тракутории черепашки
    Tmp = np.array([0, 0])
    for i in range(len(Rule)):
        if Rule[i] == "F":
            Size = P.shape
            Tmp = P[Size[0] - 1]
            R = np.array([[np.cos(Alpha), np.sin(Alpha)]])
            R = R / (2**L_max)
            Tmp = Tmp + R
            # добавление новых координат
            # черепашки в массив P
            P = np.vstack((P, Tmp))
        if Rule[i] == "+":
            Alpha = Alpha + Teta
        if Rule[i] == "-":
            Alpha = Alpha - Teta

    return P


# Ячейка № 14

# задание функции, возвращающей
# изображение дракона Хартера-Хайтвея
def Dracon(N):
    # задание аксиомы
    Axiom = "FX"
    # порождающие правила
    New_F = "F"
    New_X = "X+YF+"
    New_Y = "-FX-Y"
    Teta = np.pi / 2
    Alpha = 0

    # задание координат начальной
    # точки траектории черепашки
    P = np.array([[0, 0]])

    # вычисление координат отрезков дракона Хартера-Хайтвея
    P = Coord_D(N, Axiom, New_F, New_X, New_Y, Alpha, Teta, P)

    # визуализация дракона Хартера-Хайтвея
    F = plt.figure(figsize=(8, 8))
    F.add_subplot()
    plt.axis("off")
    plt.plot(P[:, 0], P[:, 1], "-k", lw=1)

    plt.show()

# Ячейка № 15

# визуализация дракона Хартера-Хайтвея
# 12-го порядка

Dracon(12)

# визуализация изображений
# фракталов Дракон, Гильберта,
# Госпера, Серпинского, Остров,
# Пеано

# Ячейка № 16

# задание функции выбора порождающих
# правил фрактала в зависимости
# от его названия: Dracon, Hilbert curve,
#  Gosper curve, Serpinsky curve, Island,
# Peano


def Fractal_Select(Name):
    # Name - название фрактала

    if Name == "Dracon":
        # порождающие правила фрактала Дракон
        Axiom = "FX"
        New_F = "F"
        New_X = "X+YF+"
        New_Y = "-FX-Y"
        Teta = np.pi / 2
        Alpha = 0

    if Name == "Hilbert curve":
        # порождающие правила фрактала Гильберта
        Axiom = "X"
        New_F = "F"
        New_X = "-YF+XFX+FY-"
        New_Y = "+XF-YFY-FX+"
        Teta = np.pi / 2
        Alpha = 0

    if Name == "Gosper curve":
        # порождающие правила фрактала Госпера
        Axiom = "XF"
        New_F = "F"
        New_X = "X+YF++YF-FX--FXFX-YF+"
        New_Y = "-FX+YFYF++YF+FX--FX-Y"
        Teta = np.pi / 3
        Alpha = 0

    if Name == "Peano curve":
        # порождающие правила фрактала Пеано,
        # заполняющей плоскость
        Axiom = "F"
        New_F = "F-F+F+F+F-F-F-F+F"
        New_X = ""
        New_Y = ""
        Teta = np.pi / 4
        Alpha = np.pi / 4

    if Name == "Serpinsky curve":
        # порождающие правила фрактала Серпинского
        Axiom = "F+XF+F+XF"
        New_F = "F"
        New_X = "XF-F+F-XF+F+XF-F+F-X"
        New_Y = ""
        Teta = np.pi / 2
        Alpha = np.pi / 4

    if Name == "Island":
        # порождающие правила фрактала Остров
        Axiom = "F+F+F+F"
        New_F = "F+F-F-FFF+F+F-F"
        New_X = ""
        New_Y = ""
        Teta = np.pi / 2
        Alpha = 0

    return Axiom, New_F, New_X, New_Y, Teta, Alpha

# Ячейка № 17


def Rule_Fractal(L_max, Axiom, New_F, New_X, New_Y, n, Tmp):
    if n <= L_max + 1:
        if n == 1:
            Tmp = Axiom
        M = len(Tmp)
        Tmp1 = ""
        for i in range(M):
            if Tmp[i] == "F":
                Tmp1 = Tmp1 + New_F
            if Tmp[i] == "X":
                Tmp1 = Tmp1 + New_X
            if Tmp[i] == "Y":
                Tmp1 = Tmp1 + New_Y
            if Tmp[i] == "+" or Tmp[i] == "-":
                Tmp1 = Tmp1 + Tmp[i]
        Tmp = Tmp1
        n = n + 1
        Tmp = L_Dracon(L_max, Axiom, New_F, New_X, New_Y, n, Tmp)
    return Tmp

# Ячейка № 18


def F_Coord(L_max, Axiom, New_F, New_X, New_Y, Alpha, Teta, P):
    Rule = Rule_Fractal(L_max, Axiom, New_F, New_X, New_Y, 1, "")
    Tmp = np.array([0, 0])
    for i in range(len(Rule)):
        if Rule[i] == "F":
            Size = P.shape
            Tmp = P[Size[0] - 1]
            R = np.array([[np.cos(Alpha), np.sin(Alpha)]])
            R = R / (2**L_max)
            Tmp = Tmp + R
            P = np.vstack((P, Tmp))
        if Rule[i] == "+":
            Alpha = Alpha + Teta
        if Rule[i] == "-":
            Alpha = Alpha - Teta
    return P

# Ячейка № 19


def Fractal(Name, N):
    # входные переменные:
    # Name - название фрактала
    # N - порядок фрактала

    # выбор аксиомы и порождающего правила,
    # соответствующих названию фрактала
    Axiom, New_F, New_X, New_Y, Teta, Alpha = Fractal_Select(Name)

    # задание значений координат
    # начальной точки фрактала
    # (соотвественно, начальной точки
    # траектории черепашки)
    P = np.array([[0, 0]])

    # вычисление координат отрезков фрактала
    P = F_Coord(N, Axiom, New_F, New_X, New_Y, Alpha, Teta, P)

    # визуализация фрактала
    F = plt.figure(figsize=(8, 8))
    F.add_subplot()
    plt.axis("off")

    plt.plot(P[:, 0], P[:, 1], "-k", lw=1)

# Ячейка № 20

Fractal("Peano curve", 4)

# Fractal('Dracon', 12)
# Fractal('Hilbert curve', 5)
# Fractal('Gosper curve', 4)
# Fractal('Serpinsky curve', 4)
# Fractal('Island', 2)

# визуализация фракталов
# Цветок, Куст, Снежинка

# Ячейка № 21

# задание функции, возвращающей
# правило построения фрактала
def L2_Fractal(L_max, Axiom, New_F, n, Tmp):
    while n <= L_max:
        if n == 1:
            Tmp = Axiom
            n = n + 1
        else:
            Tmp = Tmp.replace("F", New_F)
            n = n + 1
            Tmp = L2_Fractal(L_max, Axiom, New_F, n, Tmp)

    return Tmp


# Ячейка № 22
# задание функции, возвращающей
# изображение фрактала


def Coord2(L_max, Axiom, New_F, Alpha, Teta, P):
    # вычисление правила построения фрактала
    Rule = L2_Fractal(L_max, Axiom, New_F, 1, "")

    # вычисление координат отрезков фрактала
    # и их визуализация
    Tmp = np.array([0, 0])
    x0 = Tmp[0]
    y0 = Tmp[1]

    St = np.empty(shape=(0, 3), dtype=np.float64)

    for i in range(len(Rule)):
        if Rule[i] == "F":
            x1 = x0 + np.cos(Alpha)
            y1 = y0 + np.sin(Alpha)

            X = np.array([x0, x1])
            Y = np.array([y0, y1])

            x0 = x1
            y0 = y1

            # построение данного отрезка фрактала
            plt.plot(X, Y, "-k", lw=1)

        if Rule[i] == "+":
            Alpha = Alpha + Teta

        if Rule[i] == "-":
            Alpha = Alpha - Teta

        if Rule[i] == "[":
            St = np.vstack((St, np.array([x0, y0, Alpha])))

        if Rule[i] == "]":
            Size = St.shape

            if St.shape[0] == 1:
                x0 = St[0][0]
                y0 = St[0][1]
                Alpha = St[0][2]
                St = np.empty(shape=(0, 3), dtype=np.float64)

            if St.shape[0] >= 2:
                x0 = St[Size[0] - 1][0]
                y0 = St[Size[0] - 1][1]
                Alpha = St[Size[0] - 1][2]
                St = St[0 : Size[0] - 1, 0 : Size[1]]


# Ячейка № 23

# задание функции выбора порождающих
# правил фрактала в зависимости
# от его названия: Flower, Snowflake,
# Bush, Tree
def Fractal2(Name_Fractal, L_max):
    if Name_Fractal == "Flower":
        Axiom = "F[+F+F][-F-F][++F][--F]F"
        New_F = "FF[++F][+F][F][-F][--F]"
        Teta = np.pi / 16
        Alpha = np.pi / 2

    if Name_Fractal == "Snowflake":
        Axiom = "[F]+[F]+[F]+[F]+[F]+[F]"
        New_F = "F[++F][-FF]FF[F][+F][-F]FF"
        Teta = np.pi / 3
        Alpha = 0

    if Name_Fractal == "Bush":
        Axiom = "F"
        New_F = "-F+F+[+F-F-]-[-F+F+F]"
        Teta = np.pi / 2
        Alpha = np.pi / 2

    if Name_Fractal == "Tree":
        Axiom = "F"
        New_F = "FF-[-F+F+F]+[+F-F-F]"
        Teta = 22.5 * np.pi / 180
        Alpha = np.pi / 2

    p = [0, 0]
    F = plt.figure(figsize=(8, 8))
    F.add_subplot()
    plt.axis("off")

    Coord2(L_max, Axiom, New_F, Alpha, Teta, p)

# Ячейка № 24

# визуализация изображения
# выбранного фрактала

# Fractal2('Flower', 3)
# Fractal2('Bush', 4)
# Fractal2('Snowflake', 3)
Fractal2("Tree", 3)

