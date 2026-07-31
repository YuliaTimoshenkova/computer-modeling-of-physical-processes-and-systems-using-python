#!/usr/bin/env python
# coding: utf-8

# Ячейка № 1

# вычисления проекций векторов:
# [cos(pi/3), sin(pi/3)],
# [cos(pi/3+pi/2), sin(pi/3+pi/2)],
# [cos(pi/3+pi), sin(pi/3+pi)],
# [cos(pi/3+3*pi/2), sin(pi/3+ 3*pi/2)],
# на вектор [cos(pi/6), sin(pi/6)]

# подключение библиотеки numpy
import numpy as np

# подключение библиотеки matplotlib.pyplot
import matplotlib.pyplot as plt

# Ячейка № 2

# задание координат вектора a
a = np.array([np.cos(np.pi / 6), np.sin(np.pi / 6)])

# задание координат вектора -а, используемого далее
# для визуализации прямой, проходящей через вектор a
a1 = -a

# задание координат вектора b1
b = np.array([np.cos(np.pi / 3), np.sin(np.pi / 3)])
b1 = 0.7 * b

# вычисление длины вектора а
a_norm = np.linalg.norm(a)

# вычисление длины вектора b1
b1_norm = np.linalg.norm(b1)

# вычисление скалярного произведения
# векторов a и b1
dot_a_b1 = np.dot(a, b1)

# вычисление угла между векторами а и b1
Angle_a_b1 = np.arccos(dot_a_b1 / (a_norm * b1_norm))

# вычисление матрицы поворота, входящей в (1.28)
M1 = np.array(
    [
        [np.cos(Angle_a_b1), np.sin(Angle_a_b1)],
        [-1 * np.sin(Angle_a_b1), np.cos(Angle_a_b1)],
    ]
)

# вычисление проекции вектора b1 на вектор а
b1_projection = np.dot(M1, b1)

# задание координат вектора b2
b = np.array([np.cos(np.pi / 3 + np.pi / 2), np.sin(np.pi / 3 + np.pi / 2)])
b2 = 0.7 * b

# вычисление длины вектора b2
b2_norm = np.linalg.norm(b2)

# вычисление скалярного произведения
# векторов b2 и а
dot_a_b2 = np.dot(a, b2)

# вычисление угла между векторами а и b2
Angle_a_b2 = np.arccos(dot_a_b2 / (a_norm * b2_norm))

# вычисление матрицы поворота, входящей в (1.28)
M2 = np.array(
    [
        [np.cos(Angle_a_b2), np.sin(Angle_a_b2)],
        [-np.sin(Angle_a_b2), np.cos(Angle_a_b2)],
    ]
)

# вычисление проекции вектора b2 на вектор а
b2_projection = np.dot(M2, b2)

# задание координат вектора b3
b = np.array([np.cos(np.pi / 3 + np.pi), np.sin(np.pi / 3 + np.pi)])
b3 = 0.7 * b

# вычисление длины вектора b3
b3_norm = np.linalg.norm(b3)

# вычисление скалярного произведения
# векторов b3 и а
dot_a_b3 = np.dot(a, b3)

# вычисление угла между векторами а и b3
Angle_a_b3 = np.arccos(dot_a_b3 / (a_norm * b3_norm))

# вычисление матрицы поворота, входящей в (1.28)
M3 = np.array(
    [
        [np.cos(Angle_a_b3), np.sin(Angle_a_b3)],
        [-np.sin(Angle_a_b3), np.cos(Angle_a_b3)],
    ]
)

# вычисление проекции вектора b3 на вектор а
b3_projection = np.dot(M3, b3)

# задание координат вектора b4
b = np.array([np.cos(np.pi / 3 + 3 * np.pi / 2), np.sin(np.pi / 3 + 3 * np.pi / 2)])
b4 = 0.7 * b

# вычисление длины вектора b4
b4_norm = np.linalg.norm(b4)

# вычисление скалярного произведения
# векторов b4 и а
dot_a_b4 = np.dot(a, b4)

# вычисление угла между векторами а и b4
Angle_a_b4 = np.arccos(dot_a_b4 / (a_norm * b4_norm))
# вычисление матрицы поворота, входящей в (1.28)
M4 = np.array(
    [
        [np.cos(Angle_a_b4), np.sin(Angle_a_b4)],
        [-np.sin(Angle_a_b4), np.cos(Angle_a_b4)],
    ]
)

# вычисление проекции вектора b4 на вектор а
b4_projection = np.dot(M4, b4)

# визуализация проекций векторов b1, b2, b3, b4 на вектор a

# визуализация проекции вектора b1 на вектор a
fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(2, 2, 1)
plt.title("$\pi/3$", fontsize=9)

# визуализация вектора а
plt.plot([0, a[0]], [0, a[1]], "-k", lw=1)

# визуализация вектора -а
plt.plot([0, a1[0]], [0, a1[1]], "--k", lw=1)

plt.axis([-1, 1, -1, 1])
plt.axis("equal")

# визуализация конца вектора а
plt.plot(a[0], a[1], "o", color="black")

# визуализация вектора b1
plt.plot([0, b1[0]], [0, b1[1]], "k", lw=1)

# визуализация конца вектора b1
plt.plot(b1[0], b1[1], "*", color="black")

# визуализация отрезка, соединяющего
# конец вектора b1 и конец его проекции на вектор a
plt.plot([b1[0], b1_projection[0]], [b1[1], b1_projection[1]], "-k", lw=1)

# визуализация конца проекции вектора b1 на вектор а
plt.plot(b1_projection[0], b1_projection[1], "*", color="black")
plt.grid(True)

# визуализация проекции вектора b2 на вектор a
plt.subplot(2, 2, 2)
plt.title("$\pi/3+\pi/2$", fontsize=9)

# визуализация вектора а
plt.plot([0, a[0]], [0, a[1]], "-k", lw=1)

# визуализация вектора -а
plt.plot([0, a1[0]], [0, a1[1]], "--k", lw=1)

plt.axis([-1, 1, -1, 1])
plt.axis("equal")

# визуализация конца вектора а
plt.plot(a[0], a[1], "o", color="black")

# визуализация вектора b2
plt.plot([0, b2[0]], [0, b2[1]], "-k", lw=1)

# визуализация конца вектора b2
plt.plot(b2[0], b2[1], "*", color="black")

# визуализация отрезка, соединяющего
# конец вектора b2 и конец его проекции на вектор a
plt.plot([b2[0], b2_projection[0]], [b2[1], b2_projection[1]], ":k", lw=1)

# визуализация конца проекции вектора b2 на вектор а
plt.plot(b2_projection[0], b2_projection[1], "*", color="black")
plt.grid(True)

# визуализация проекции вектора b3 на вектор a
plt.subplot(2, 2, 3)
plt.title("$\pi/3+\pi$", fontsize=9)

# визуализация вектора а
plt.plot([0, a[0]], [0, a[1]], "-k", lw=1)

# визуализация вектора -а
plt.plot([0, a1[0]], [0, a1[1]], "--k", lw=1)

plt.axis([-1, 1, -1, 1])
# plt.axis('equal')

# визуализация конца вектора а
plt.plot(a[0], a[1], "o", color="black")

# визуализация вектора b3
plt.plot([0, b3[0]], [0, b3[1]], ":k", lw=1)

# визуализация конца вектора b3
plt.plot(b3[0], b3[1], "*", color="black")

# визуализация отрезка, соединяющего
# конец вектора b3 и конец его проекции на вектор a
plt.plot([b3[0], b3_projection[0]], [b3[1], b3_projection[1]], ":k", lw=1)

# визуализация конца проекции вектора b3 на вектор а
plt.plot(b3_projection[0], b3_projection[1], "*", color="black")
plt.grid(True)

# визуализация проекции вектора b4 на вектор a
plt.subplot(2, 2, 4)
plt.title("$\pi/3+3\pi/2$", fontsize=9)

# визуализация вектора а
plt.plot([0, a[0]], [0, a[1]], "-k", lw=1)

# визуализация вектора -а
plt.plot([0, a1[0]], [0, a1[1]], "--k", lw=1)

plt.axis([-1, 1, -1, 1])
plt.axis("equal")

# визуализация конца вектора а
plt.plot(a[0], a[1], "o", color="black")

# визуализация вектора b4
plt.plot([0, b4[0]], [0, b4[1]], "-k", lw=1)

# визуализация конца вектора b4
plt.plot(b4[0], b4[1], "*", color="black")

# визуализация отрезка, соединяющего
# конец вектора b4 и конец его проекции на вектор a
plt.plot([b4[0], b4_projection[0]], [b4[1], b4_projection[1]], ":k", lw=1)

# визуализация конца проекции вектора b4 на вектор а
plt.plot(b4_projection[0], b4_projection[1], "*", color="black")
plt.grid(True)

plt.show()
