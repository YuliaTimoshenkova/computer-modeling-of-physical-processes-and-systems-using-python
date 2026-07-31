#!/usr/bin/env python
# coding: utf-8

# Ячейка № 1

# подключение библиотеки numpy
import numpy as np

# подключение библиотеки matplotlib.pyplot
import matplotlib.pyplot as plt

# подключение библиотеки matplotlib.animation
import matplotlib.animation as animation


# Ячейка № 2

# задание функции,
# возвращающей значения
# коэффициентов Alpha и Gamma,
# вычисленных в соответствие с
# методом продольно-поперечной прогонки
def Coeff(Nx, Ny, C):
    # инициализация массивов, используемых
    # для хранения коэффициентов
    # метода продольно-поперечной прогонки
    N = max(Nx, Ny)
    ALPHAxx = np.zeros(N)
    ALPHAyx = np.zeros(N)
    ALPHAxy = np.zeros(N)
    ALPHAyy = np.zeros(N)
    GAMMAxx = np.zeros(N)
    GAMMAxy = np.zeros(N)
    GAMMAyx = np.zeros(N)
    GAMMAyy = np.zeros(N)
    S = np.zeros([8, N])

    # задание краевых условий
    # с нулевыми потоками
    ALPHAxx[Nx - 1] = 1
    ALPHAyx[Nx - 1] = 1

    # обратный проход по оси OX
    i = Nx - 1
    while i >= 1:
        GAMMAxx[i] = 1 / (C[5] + C[4] * ALPHAxx[i])
        ALPHAxx[i - 1] = -C[4] * GAMMAxx[i]
        GAMMAyx[i] = 1 / (C[7] + C[6] * ALPHAyx[i])
        ALPHAyx[i - 1] = -C[6] * GAMMAyx[i]
        i = i - 1

    # задание краевых условий
    # с нулевыми потоками
    ALPHAxy[Ny - 1] = 1
    ALPHAyy[Ny - 1] = 1

    # реализация обратного
    # прохода по оси OY
    j = Ny - 1
    while j >= 1:
        GAMMAxy[j] = 1 / (C[5] + C[4] * ALPHAxy[j])
        ALPHAxy[j - 1] = -C[4] * GAMMAxy[j]
        GAMMAyy[j] = 1 / (C[7] + C[6] * ALPHAyy[j])
        ALPHAyy[j - 1] = -C[6] * GAMMAyy[j]
        j = j - 1

    if ~(Nx == Ny):
        if Nx < Ny:
            for i in range(Ny - Nx):
                GAMMAxx[i + Nx] = 0
                ALPHAxx[i + Nx] = 0
                GAMMAyx[i + Nx] = 0
                ALPHAyx[i + Nx] = 0
    else:
        for i in range(Nx - Ny):
            GAMMAxy[i + Ny] = 0
            ALPHAxy[i + Ny] = 0
            GAMMAyy[i + Ny] = 0
            ALPHAyy[i + Ny] = 0

    S[0, :] = ALPHAxx[:]
    S[1, :] = ALPHAxy[:]
    S[2, :] = ALPHAyx[:]
    S[3, :] = ALPHAyy[:]
    S[4, :] = GAMMAxx[:]
    S[5, :] = GAMMAxy[:]
    S[6, :] = GAMMAyx[:]
    S[7, :] = GAMMAyy[:]

    return S


# Ячейка № 3

# задание функции, возвращающей
# численное решение СДУ (8.116)


def Density(Nx, Ny, dT, C, Cc, X, Y):
    BETAxx = np.zeros(Nx)
    BETAyx = np.zeros(Nx)
    BETAxy = np.zeros(Ny)
    BETAyy = np.zeros(Ny)

    # реализация прохода
    # по каждому из узлов
    # координатной сетки
    for j in range(Ny):
        # вычисление коэффициентов BETA
        BETAxx[Nx - 1] = 0
        BETAyx[Nx - 1] = 0
        i = Nx - 1

        # реализация прохода
        # в обратном направлении
        while i >= 1:
            X_2 = (X[i, j] ** 2) * Y[i, j] * dT
            Sx = X[i, j] * C[3] + C[2] + X_2
            Sy = Y[i, j] + C[1] * X[i, j] - X_2
            BETAxx[i - 1] = (Sx - C[4] * BETAxx[i]) * Cc[4, i]
            BETAyx[i - 1] = (Sy - C[6] * BETAyx[i]) * Cc[6, i]
            i = i - 1

        # реализация прохода
        # в прямом направлении

        # задание начальных условий
        # с нулевыми потоками
        X[0, j] = BETAxx[0] / (1 - Cc[0, 0])
        Y[0, j] = BETAyx[0] / (1 - Cc[2, 0])
        for i in range(Nx):
            X[i + 1, j] = Cc[0, i] * X[i, j] + BETAxx[i]
            Y[i + 1, j] = Cc[2, i] * (Y[i, j]) + BETAyx[i]

    # реализация прохода
    # по каждому из узлов
    # координатной сетки
    for i in range(Nx + 1):
        # вычисление коэффициентов BETA
        BETAxy[Ny - 1] = 0
        BETAyy[Ny - 1] = 0
        j = Ny - 1

        # реализация прохода
        # в обратном направлении
        while j >= 1:
            BETAxy[j - 1] = X[i, j] - C[4] * BETAxy[j] * Cc[5, j]
            BETAyy[j - 1] = (Y[i, j] - C[6]) * BETAyy[j] * Cc[7, j]
            j = j - 1

        # задание начальных значений
        # для краевых условий
        X[i, 0] = BETAxy[0] / (1 - Cc[1, 0])
        Y[i, 0] = BETAyy[0] / (1 - Cc[7, 0])

        # вычисление плотностей
        # первого и второго реагентов
        for j in range(Ny):
            X[i, j + 1] = Cc[1, j] * X[i, j] + BETAxy[j]
            Y[i, j + 1] = Cc[3, j] * Y[i, j] + BETAyy[j]

        return (X, Y)

# Ячейка № 4

# задание функции, возвращающей
# мгновенные значения плотностей
# концентраций реагентов
# в узлах координатной сетки
# заданной в плоскости XOY
def Reagent_Concentation(A, B, Dx, Dy, dT, Nx, Ny, Nt):
    # инициализация массивов, используемых
    # для хранения начальных значений
    # концентраций реагентов
    S1_start = np.zeros([Nx + 1, Ny + 1])
    S2_start = np.zeros([Nx + 1, Ny + 1])

    # генерация независимых целочисленных
    # случайных выборок в соответствие с
    # равномерным законом распределения
    # на интервале [0,1000]
    Noise1 = np.random.randint(0, 1000, size=(Nx + 1, Ny + 1))
    Noise2 = np.random.randint(0, 1000, size=(Nx + 1, Ny + 1))

    # инициализация начальной
    # концентрации реагентов
    for i in range(Nx + 1):
        for j in range(Ny + 1):
            S1_start[i, j] = A * (-0.2 + 0.4 * 10**-3 * Noise1[i, j])
            S2_start[i, j] = B / A * (-0.2 + 0.4 * 10**-3 * Noise2[i, j])

    # вычисление значений констант,
    # используемых в  методе
    # продольно-поперечной прогонки
    C = np.zeros(8)
    C[0] = 1 / (Nx - 1)
    C[1] = B * dT
    C[2] = A * dT
    C[3] = 1 - (B + 1) * dT
    C[4] = -Dx * dT / C[0] ** 2
    C[5] = 1 - 2 * C[4]
    C[6] = -Dy * dT / C[0] ** 2
    C[7] = 1 - 2 * C[6]
    # вычисление значений коэффициентов,
    # используемых в методе
    # продольно-поперечной прогонки
    Cc = Coeff(Nx, Ny, C)

    [S1, S2] = Density(Nx, Ny, dT, C, Cc, S1_start, S2_start)

    # инициализация массивов, используемых
    # хранения значений концентраций реагентов
    # на соответствующем шаге вычисления
    # численного решения СДУ (8.117)
    s1 = np.zeros([Nt + 1, Nx + 1, Ny + 1])
    s2 = np.zeros([Nt + 1, Nx + 1, Ny + 1])
    s1[0, :, :] = S1_start
    s2[0, :, :] = S2_start

    # вычисление значений концентраций реагентов
    # в каждом узле временной сетки,
    # выбранной для вычисления
    # численного решения СДУ (8.117)
    for i in range(Nt):
        [S1, S2] = Density(Nx, Ny, dT, C, Cc, S1, S2)
        s1[i + 1, :, :] = S1
        s2[i + 1, :, :] = S2

    return s1, s2

# Ячейка № 5

# задание концентраций реагентов
A = 2
B = 7

# задание значений
# коэффициентов диффузии реагентов
Dx = 10**-3
Dy = 10**-3

# задание значения шага
# временной сетки
dT = 2 * 10**-2

# задание числа узлов координатной сетки
Nx = 25
Ny = 29

# задание числа узлов временной сетки
Nt = 1500

# вычисление мгновенных значений
# плотностей концентраций реагентов
# в узлах координатной сетки
# заданной в плоскости XOY
s1, s2 = Reagent_Concentation(A, B, Dx, Dy, dT, Nx, Ny, Nt)


# Ячейка № 6

# визуализация плотностей концентраций
# реагентов в выбранный момент времени

# задание номера шага по времени,
# выбранного для отображения решения СДУ (8.117)
Nk = 0

fig = plt.figure(figsize=(11, 7))
ax1 = fig.add_subplot(1, 2, 1)
ax1.imshow(s1[Nk, :, :].T, cmap="copper", origin="lower", interpolation="quadric")

ax2 = fig.add_subplot(1, 2, 2)

im = ax2.imshow(s2[Nk, :, :].T, cmap="copper", origin="lower", interpolation="quadric")

# определение положения текущих осей графика
pos = ax2.get_position()

# задание координат места расположения цветовой шкалы
cax = fig.add_axes([pos.x1 + 0.01, pos.y0, 0.02, pos.height])

# размещение цветовой шкалы в указанном месте
plt.colorbar(im, cax=cax)

plt.show()

# Ячейка № 7

# создание анимационного клипа,
# демонстрирующего изменения концентраций
# первого и второго реагентов во времени

fig = plt.figure(figsize=(11, 7))
ax1 = fig.add_subplot(1, 2, 1)
im1 = ax1.imshow(
    s1[0, :, :].T, cmap="copper", origin="lower", interpolation="quadric", animated=True
)
ax2 = fig.add_subplot(1, 2, 2)
im2 = ax2.imshow(
    s2[0, :, :].T, cmap="copper", origin="lower", interpolation="quadric", animated=True
)
dfr = 10


def animate(i):
    im1.set_data(s1[dfr * (i), :, :].T)
    im1.autoscale()
    im2.set_data(s2[dfr * (i), :, :].T)
    im2.autoscale()
    return im1, im2


ani = animation.FuncAnimation(fig, animate, (Nt // dfr) + 1, interval=100, blit=False)
plt.close()

from IPython.display import HTML

HTML(ani.to_jshtml())

# Ячейка № 8

# визуализация зависимостей
# концентраций реагентов
# в выбранной точке координатной сетки
# от времени

# инициализация массивов,
# используемых для хранения
# значений зависимостей
# концентраций реагентов в выбранном узле
# координатной сетки от времени
t = np.zeros(Nt + 1)
Q1 = np.zeros(Nt + 1)
Q2 = np.zeros(Nt + 1)

# извлечение значений зависимостей
# концентраций реагентов в выбранном узле
# координатной сетки от времени
# из матриц, содержащих численное решение СДУ (8.117)
for i in range(Nt + 1):
    X_1 = s1[i, :, :]
    Y_1 = s2[i, :, :]
    t[i] = i * dT
    Q1[i] = X_1[9, 9]
    Q2[i] = Y_1[9, 9]

# визуализация зависимостей
# концентраций реагентов от времени
# в выбранном узле координатной сетки

fig = plt.figure(figsize=(9, 5))

# визуализация зависимости
# концентрации первого реагента
# в выбранном узле координатной сетки
# от времени
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(t, Q1, "black")

# визуализация зависимости
# концентрации второго реагента
# в выбранном узле координатной сетки
# от времени
ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(t, Q2, "black")

plt.show()
