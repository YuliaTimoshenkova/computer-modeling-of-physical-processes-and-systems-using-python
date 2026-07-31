#!/usr/bin/env python
# coding: utf-8

# Ячейка № 1

# вычисление и визуализация
# численного решения СДУ (3.14)

# Ячейка № 1

# подключение библиотеки numpy
import numpy as np

# подгружаем из библиотеки scipy.integrate
# функцию solve_ivp,  реализующей
# метод Рунге-Кутты 4-5 порядка
from scipy.integrate import solve_ivp

# подключение библиотеки matplotlib.pyplot
import matplotlib.pyplot as plt


# Ячейка № 2

# задание функция, возвращающей значения
# первых производных в (3.14)
def AngleXY(t, y):
    # объявление глобальной переменной
    global g

    # инициализация массива размерностью 1 х 4
    dy = np.zeros(4)

    # вычисление значений первых производных
    dy[0] = y[1]
    dy[1] = 0
    dy[2] = y[3]
    dy[3] = -g

    return dy

# Ячейка № 3

# задание значения ускорения
# свободного падения
g = 9.8

# задание начальных условий СДУ (3.14)
x0 = 0
y0 = 0
vx0 = 2
vy0 = 5

# задание значений
# границ временного интервала
a = 0
b = 1.02

# задание максимального
# шага интегрирования СДУ (3.13)
step = 0.01

# вызов функции, возвращающей
# численное решение системы ОДУ (3.13)
a_sol = solve_ivp(AngleXY, [a, b], [x0, vx0, y0, vy0], max_step=step)

# визуализация численного решения системы ОДУ (3.14)
fig = plt.figure(figsize=(7, 7))

# визуализация зависимости x(t)
ax = plt.subplot(2, 2, 1)
ax.plot(a_sol.t[:], a_sol.y[0, :], "-k", lw=1)
ax.grid(True)
ax.set_title("а)", fontsize=10)

# визуализация зависимости y(t)
ax = plt.subplot(2, 2, 2)
ax.plot(a_sol.t[:], a_sol.y[1, :], "-k", lw=1)
ax.grid(True)
ax.set_title("б)", fontsize=10)

ax = plt.subplot(2, 2, 3)
ax.plot(a_sol.t[:], a_sol.y[2, :], "-k", lw=1)
ax.grid(True)
ax.set_title("в)", fontsize=10)

# визуализация зависимости vx=vx(t)
ax = plt.subplot(2, 2, 4)
ax.plot(a_sol.t[:], a_sol.y[3, :], "-k", lw=1)
ax.grid(True)
ax.set_title("г)", fontsize=10)

plt.show()

fig2 = plt.figure(figsize=(7, 7))
ax = plt.subplot(2, 2, 1)
ax.plot(a_sol.y[0, :], a_sol.y[2, :], "-k", lw=1)
ax.grid(True)
ax.set_title("д)", fontsize=10)

plt.show()
