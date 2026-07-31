#!/usr/bin/env python
# coding: utf-8

# вычисление численного решения
# уравнения Пуассона

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
# уравнения Пуассона на соответствующем шаге
# итерационного процесса
def IterationP(x1, x2, y1, y2, F, Nx, Ny, Omega, Number_of_Iteration, phi):
    # входные переменные:
    # Nx - число узлов координатной сетки по оси OX
    # Ny - число узлов координатной сетки по оси OY
    # Number_of_Iteration - число итераций
    # phi - массив размерности
    # Number_of_Iteration * N * N,
    # содержащий граничные условия
    # и начальное приближение

    # вычисляем координаты узлов сетки
    X = np.linspace(0, 1, Nx)
    Y = np.linspace(0, 1, Ny)
    dx = X[1] - X[0]
    dy = Y[1] - Y[0]
    x, y = np.meshgrid(X, Y)

    # вычисляем решения уравнения Лапласа
    # на каждом шаге итерационного процесса и
    # сохраняем их в массиве phi
    for j in range(Number_of_Iteration - 1):
        for i in range(Nx - 2):
            for k in range(Ny - 2):
                if (
                    (x[i, k] >= x1)
                    and (x[i, k] <= x2)
                    and (y[i, k] >= y1)
                    and (y[i, k] <= y2)
                ):
                    phi[j + 1, i + 1, k + 1] = F
                else:
                    phi[j + 1, i + 1, k + 1] = (
                        (1 - Omega) * phi[j, i + 1, k + 1]
                        + Omega
                        / 4
                        * (
                            phi[j, i + 2, k + 1]
                            + phi[j, i, k + 1]
                            + phi[j, i + 1, k + 2]
                            + phi[j, i + 1, k]
                        )
                        + F * dx * dy
                    )
    return x, y, phi


# Ячейка № 3

# вычисление и визуализация
# численного решения
# уравнения Пуассона (5.69)

# задание значения плотности
# электрических зарядов в (5.69)
F = 7

# задание координат левой нижней (x1, y1) и
# правой верхней (x2, y2) вершин прямоугольной
# области, в которой плотность электрического
# заряда равна F
x1 = 0.4
y1 = 0.4
x2 = 0.6
y2 = 0.6

# задание числа узлов координатной сетки
# по оси OX
Nx = 101

# задание числа узлов координатной сетки
# по оси OY
Ny = 101

# задание числа итераций
Niter = 300

# инициализация массива phi,
# используемого для хранения
# численного решения уравнения Пуассона
phi = np.zeros([Niter, Nx, Ny])

# задание граничных условий
# для каждого шага
# итерационного процесса
for k in range(Niter):
    for i in range(Nx - 1):
        phi[k, i, 0] = 0
        phi[k, i, Nx - 1] = 0
    for j in range(Ny - 1):
        phi[k, 0, j] = 0
        phi[k, Ny - 1, j] = 0

# задание начального приближения
# решения уравнения Пуассона
for i in range(Nx - 2):
    for j in range(Ny - 2):
        phi[0, i + 1, j + 1] = 12

# задание значения параметра релаксации
Omega = 1

# вычисление численных решений уравнения Пуассона
x, y, phi = IterationP(x1, x2, y1, y2, F, Nx, Ny, Omega, Niter, phi)


# Ячейка № 4

# статическая визуализация
# численных решений уравнения Пуассона
# на выбранных шагах итерационного процесса

# визуализация численных решений уравнения Пуассона
fig = plt.figure(figsize=(13, 13))

# визуализация численного решения уравнения Пуассона
# на 101-ом шаге итерационного процесса
ax = fig.add_subplot(1, 2, 1)
CS = ax.contour(x, y, phi[49, :, :], colors="black", levels=11)
ax.clabel(CS, fontsize=8)
ax.set_aspect("equal", adjustable="box")
plt.title(r"а)", fontsize=10)

# визуализация численного
# решения уравнения Пуассона
# на последнем шаге итерационного процесса
ax = fig.add_subplot(1, 2, 2)
CS = ax.contour(x, y, phi[299, :, :], colors="black", levels=11)
ax.clabel(CS, fontsize=8)
ax.set_aspect("equal", adjustable="box")
plt.title(r"б)", fontsize=10)

plt.show()


# Ячейка № 5

# динамическая визуализация
# уравнений Лапласа

# задание максимального размера анимации (в Мб),
# размещаемой на данной веб-страннице
plt.rcParams["animation.embed_limit"] = 100.0


fig, ax = plt.subplots(figsize=(7, 7))


# задание функции, возвращающей
# карту эквипотенциалей
# численных решений уравнения Лапласа
# на каждом шаге итерационного процесса
def animate(i):
    ax.clear()
    CS = ax.contour(x, y, phi[i, :, :], colors="black", levels=11)
    ax.clabel(CS)


# создание анимационного клипа
ani = animation.FuncAnimation(fig, animate, 300, interval=50, blit=False)
plt.close()

from IPython.display import HTML

HTML(ani.to_jshtml())

