#!/usr/bin/env python
# coding: utf-8

# вычисление численного решения
# уравнения Лапласа

# Ячейка № 1

# подключение библиотеки numpy
import numpy as np

# подключение библиотеки matplotlib.pyplot
import matplotlib.pyplot as plt

# подключение библиотеки matplotlib.animation
import matplotlib.animation as animation


# Ячейка № 2

# задание функции, возвращающей:
# x - массив, содержащий координаты узлов сетки
# phi - массив, содержащий решения
# уравнения Лапласа на соответствующем шаге
# итерационного процесса
def IterationL(N, Omega, Number_of_Iteration, phi):
    # входные переменные:
    # N - число узлов координатной сетки
    # Number_of_Iteration - число итераций
    #  phi - массив размерности
    # Number_of_Iteration * N * N,
    # содержащий граничные условия
    # и начальное приближение

    # вычисляем координаты узлов сетки
    x = np.linspace(0, 1, N)

    # вычисляем решения уравнения Лапласа
    # на каждом шаге итерационного процесса и
    # сохраняем их в массиве phi
    for j in range(Number_of_Iteration - 1):
        for i in range(N - 2):
            for k in range(N - 2):
                phi[j + 1, i + 1, k + 1] = (1 - Omega) * phi[
                    j, i + 1, k + 1
                ] + Omega / 4 * (
                    phi[j, i + 2, k + 1]
                    + phi[j, i, k + 1]
                    + phi[j, i + 1, k + 2]
                    + phi[j, i + 1, k]
                )
    return x, phi


# Ячейка № 3

# вычисление и визуализация
# численных решений уравнения Лапласа

# задание числа узлов координатной сетки
N = 71

# задание числа итераций
Niter = 300

# инциализация массива phi,
# используемого для хранения
# численного решения уравнения Лапласа
phi = np.zeros([Niter, N, N])

# задание граничных условий
# для каждого шага
# итерационного процесса
for k in range(Niter):
    for i in range(N - 1):
        phi[k, i, 0] = 10
        phi[k, i, N - 1] = 10
        phi[k, 0, i] = -10
        phi[k, N - 1, i] = -10

# задание начального приближения
# решения уравнения Лапласа
for i in range(N - 2):
    for j in range(N - 2):
        phi[0, i + 1, j + 1] = 12

# задание значения параметра релаксации
Omega = 1

# вычисление численных решений уравнения Лапласа
x, phi = IterationL(N, Omega, Niter, phi)


# Ячейка № 4

# статическая визуализация
# численных решений уравнения Лапласа
# на выбранных шагах итерационного процесса

# вычисление координат узлов двумерной сетки,
# использованной для вычисления численного
# решения уравнения Лапласа
[X2, Y2] = np.meshgrid(x, x)

# визуализация численных решений уравнения Лапласа
fig = plt.figure(figsize=(13, 13))

# визуализация численного решения уравнения Лапласа
# на 101-ом шаге итерационного процесса
ax = fig.add_subplot(1, 2, 1)
CS = ax.contour(X2, Y2, phi[49, :, :], colors="black", levels=15)
ax.clabel(CS, fontsize=8)
ax.set_aspect("equal", adjustable="box")
plt.title(r"а)", fontsize=10)

# визуализация численного решения уравнения Лапласа
# на последнем шаге итерационного процесса
ax = fig.add_subplot(1, 2, 2)
CS = ax.contour(X2, Y2, phi[299, :, :], colors="black", levels=15)
ax.clabel(CS, fontsize=8)
ax.set_aspect("equal", adjustable="box")
plt.title(r"б)", fontsize=10)

plt.show()

# Ячейка № 5

# динамическая визуализация
# уравнений Лапласа

fig, ax = plt.subplots(figsize=(7, 7))


# задание функции, возвращающей
# карту эквипотенциалей
# численных решений уравнения Лапласа
# на каждом шаге итерационного процесса
def animate(i):
    ax.clear()
    CS = ax.contour(X2, Y2, phi[i, :, :], colors="black", levels=15)
    ax.clabel(CS)


# создание анимационного клипа
ani = animation.FuncAnimation(fig, animate, 200, interval=50, blit=False)
plt.close()

from IPython.display import HTML

HTML(ani.to_jshtml())

