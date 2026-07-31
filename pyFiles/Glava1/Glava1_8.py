#!/usr/bin/env python
# coding: utf-8

# вычисление проекций векторов
# на выбранный вектор в соответствие
# с алгоритмом вычисления
# "правильного" значения угла

# Ячейка № 1

# подключение библиотеки numpy
import numpy as np

# подключение библиотеки matplotlib.pyplot
import matplotlib.pyplot as plt


# Ячейка № 2

# задание функции, возвращающей
# истинное значения угла
# между вектором R и
# положительным направлением
# оси абсцисс, отсчитываемым
# против часовой стрелки


def Angle_True(R):
    # задание единичного вектора, сонаправленного
    # с осью абсцисс
    Ex = [1, 0]

    # вычисление скалярного произведения
    # векторов R, Ex
    dot_R_Ex = np.dot(R, Ex)

    # вычисление длины вектора R
    R_norm = np.linalg.norm(R)

    # вычисление значения угла поворота
    # вектора Ex к вектору R
    # как угла против часовой стрелки
    # с учетом номеров квартилей,
    # в которых находятся конце данных векторов
    if (R[0] >= 0) and (R[1] >= 0):
        Angle_R_Ex = np.arccos(dot_R_Ex / R_norm)
    if (R[0] <= 0) and (R[1] > 0):
        Angle_R_Ex = np.arccos(dot_R_Ex / R_norm)
    if (R[0] <= 0) and (R[1] <= 0):
        Angle_R_Ex = 2 * np.pi - np.arccos(dot_R_Ex / R_norm)
    if (R[0] >= 0) and (R[1] < 0):
        Angle_R_Ex = 2 * np.pi - np.arccos(dot_R_Ex / R_norm)
    return Angle_R_Ex

# Ячейка № 3

# задание функции,
# возвращающей истинное
# значение проекции
# вектора b на вектор a
def Vector_Projection(b, a):
    # вычисление истинного значения угла между
    # вектором b и положительным направлением
    # оси абсцисс
    AngleB = Angle_True(b)

    # вычисление истинного значения угла между
    # вектором a и положительным направлением
    # оси абсцисс
    AngleA = Angle_True(a)

    # вычисление длины проекции вектора b на вектор a
    L = np.linalg.norm(b) * np.cos(AngleB - AngleA)

    # вычисление координат проекции вектора b на вектор a
    z = np.array([L * np.cos(AngleA), L * np.sin(AngleA)])

    return z

# Ячейка № 4

# задание номера квадранта,
# в котором находится вектор a
K = 4

# задание координат вектора a
a = np.array(
    [np.cos(np.pi / 6 + np.pi / 2 * (K - 1)), np.sin(np.pi / 6 + np.pi / 2 * (K - 1))]
)

# задание координат вектора -а, используемого далее
# для визуализации прямой, проходящей через вектор a
a1 = -a

# визуализация проекций векторов b1, b2, b3, b4 на вектор a
a1 = -np.asarray(a)

# задание вектора b1
b1 = np.array([np.cos(np.pi / 3), np.sin(np.pi / 3)])

# вычисление координат проекции
# вектора b1 нав вектор a
b1_projection = Vector_Projection(b1, a)

# визуализация проекции вектора b1 на вектор a
fig = plt.figure(figsize=(8, 7))
plt.subplot(2, 2, 1)
plt.title("a)", fontsize=9)
plt.plot([0, a[0]], [0, a[1]], "-k", lw=1)
plt.plot([0, a1[0]], [0, a1[1]], "--k", lw=1)
plt.axis([-1, 1, -1, 1])
plt.axis("equal")
plt.plot(a[0], a[1], "o", color="black")
plt.plot(0, 0, "o", color="black")
plt.plot([0, b1[0]], [0, b1[1]], ":k", lw=1)
plt.plot(b1[0], b1[1], "*", color="black")
plt.plot([b1[0], b1_projection[0]], [b1[1], b1_projection[1]], ":k", lw=1)
plt.plot(b1_projection[0], b1_projection[1], "*", color="black")
plt.plot([0, b1_projection[0]], [0, b1_projection[1]], "-k", lw=3)
plt.grid(True)

# задание вектора b2
b2 = np.array([np.cos(np.pi / 3 + np.pi / 2), np.sin(np.pi / 3 + np.pi / 2)])

# вычисление координат
# проекции вектора b2
# на вектор a
b2_projection = Vector_Projection(b2, a)

# визуализация проекции вектора b2 на вектор a
plt.subplot(2, 2, 2)
plt.title("б)", fontsize=9)
plt.plot([0, a[0]], [0, a[1]], "-k", lw=1)
plt.plot([0, a1[0]], [0, a1[1]], "--k", lw=1)
plt.axis([-1, 1, -1, 1])
plt.axis("equal")
plt.plot(a[0], a[1], "o", color="black")
plt.plot(0, 0, "o", color="black")
plt.plot([0, b2[0]], [0, b2[1]], ":k", lw=1)
plt.plot(b2[0], b2[1], " *", color="black")
plt.plot([b2[0], b2_projection[0]], [b2[1], b2_projection[1]], ":k", lw=1)
plt.plot(b2_projection[0], b2_projection[1], "*", color="black")
plt.plot([0, b2_projection[0]], [0, b2_projection[1]], "-k", lw=3)
plt.grid(True)


# задание  вектора b3
b3 = np.array([np.cos(np.pi / 3 + np.pi), np.sin(np.pi / 3 + np.pi)])

# вычисление координат
# проекции вектора b3
# на вектор а
b3_projection = Vector_Projection(b3, a)

# визуализация проекции вектора b3 на вектор a
plt.subplot(2, 2, 3)
plt.title("в)", fontsize=9)
plt.plot([0, a[0]], [0, a[1]], "-k", lw=1)
plt.plot([0, a1[0]], [0, a1[1]], "--k", lw=1)
plt.axis([-1, 1, -1, 1])
plt.axis("equal")
plt.plot(a[0], a[1], "o", color="black")
plt.plot(0, 0, "o", color="black")
plt.plot([0, b3[0]], [0, b3[1]], ":k", lw=1)
plt.plot(b3[0], b3[1], "*", color="black")
plt.plot([b3[0], b3_projection[0]], [b3[1], b3_projection[1]], ":k", lw=1)
plt.plot(b3_projection[0], b3_projection[1], "*", color="black")
plt.plot([0, b3_projection[0]], [0, b3_projection[1]], "-k", lw=3)
plt.grid(True)

# задание вектора b4
b4 = np.array([np.cos(np.pi / 3 + 3 * np.pi / 2), np.sin(np.pi / 3 + 3 * np.pi / 2)])

# вычисление координат
# проекции вектора b4
# на вектор а
b4_projection = Vector_Projection(b4, a)

# визуализация проекции вектора b4 на вектор a
plt.subplot(2, 2, 4)
plt.title("г)", fontsize=9)
plt.plot([0, a[0]], [0, a[1]], "-k", lw=1)
plt.plot([0, a1[0]], [0, a1[1]], "--k", lw=1)
plt.axis([-1, 1, -1, 1])
plt.axis("equal")
plt.plot(a[0], a[1], "o", color="black")
plt.plot(0, 0, "o", color="black")
plt.plot([0, b4[0]], [0, b4[1]], ":k", lw=1)
plt.plot(b4[0], b4[1], "*", color="black")
plt.plot([b4[0], b4_projection[0]], [b4[1], b4_projection[1]], ":k", lw=1)
plt.plot(b4_projection[0], b4_projection[1], "*", color="black")
plt.plot([0, b4_projection[0]], [0, b4_projection[1]], "-k", lw=3)
plt.grid(True)

plt.show()
