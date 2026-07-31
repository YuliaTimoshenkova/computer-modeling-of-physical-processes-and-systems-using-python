#!/usr/bin/env python
# coding: utf-8

# Ячейка № 1

# задание функций, описывающих волны,
# распространяющиеся в положительном и
# отрицательном направлениях оси oX
# подключение библиотеки numpy
import numpy as np

# подключение библиотеки matplotlib
import matplotlib.pyplot as plt


# Ячейка № 2

# задание функции, возвращающей
# решение волнового уравнения (9.52)
# в момент времени t = 0
def Wave(A, x):
    return A * np.exp(-(x**2))


# Ячейка № 3

# задание функции, описывающей волну,
# распространяющуюся в
# положительном направлении оси oX
def Wave_p(A, x, v, t):
    return Wave(A, x - v * t)


# Ячейка № 4

# задание функции, описывающей волну,
# распространяющуюся в
# отрицательном направлении оси oX
def Wave_n(A, x, v, t):
    return Wave(A, x + v * t)


# Ячейка № 5

# вычисление решения
#  ДУ (9.52)

# задание значения
# скорости движения волны
v = 0.05

# задание значения
# амплитуды волны
A = 1

# задание координатной сетки
X_min = -2 * np.pi
X_max = 2 * np.pi
Nx = 101
x = np.linspace(X_min, X_max, Nx)

# задание временной сетки
T_min = 0
T_max = 50
Nt = 201
t = np.linspace(T_min, T_max, Nt)

M_p = np.zeros([Nt, Nx])
M_n = np.zeros([Nt, Nx])

for i in range(Nt):
    for j in range(Nx):
        M_p[i, j] = Wave_p(A, x[j], v, t[i])
        M_n[i, j] = Wave_n(A, x[j], v, t[i])


# Ячейка № 6

# визуализация решений
# волнового уравнения (9.52)
# в выбранные моменты времени

fig = plt.figure(figsize=(11, 5))

# визуализация решений
# волнового уравнения (9.52)
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(x, M_p[0, :], "-k", lw=1)
ax1.plot(x, M_p[100, :], "k--", lw=1)
ax1.plot(x, M_p[200, :], "k-.", lw=1)
ax1.grid(True)

# визуализация решений
# волнового уравнения (9.52)
ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(x, M_n[0, :], "-k", lw=1)
ax2.plot(x, M_n[100, :], "k--", lw=1)
ax2.plot(x, M_n[200, :], "k-.", lw=1)
ax2.grid(True)

plt.show()

# Ячейка № 7

# визуализация решений
# волнового уравнения (9.52)
# в виде 3D-поверхности

[X, Y] = np.meshgrid(x, t)
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(121, projection="3d")
CS1 = ax1.plot_surface(X, Y, M_p, cmap="gray")
ax1.set_xlabel(r"$x$")
ax1.set_ylabel(r"$t$")

ax2 = fig.add_subplot(122, projection="3d")
CS2 = ax2.plot_surface(X, Y, M_n, cmap="gray")
ax2.set_xlabel(r"$x$")
ax2.set_ylabel(r"$t$")

plt.show()

# Ячейка # 8

# визуализация решений
# волнового уравнения (9.52)
# в виде карты линий уровня

fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(121)
CS1 = ax1.contourf(X, Y, M_p, levels=50)

ax2 = fig.add_subplot(122)
CS2 = ax2.contourf(X, Y, M_n, levels=50)

plt.show()
