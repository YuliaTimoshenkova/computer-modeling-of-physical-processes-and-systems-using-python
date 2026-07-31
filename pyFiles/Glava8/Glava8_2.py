#!/usr/bin/env python
# coding: utf-8

# Ячейка № 1

# подключение библиотеки numpy
import numpy as np

# подключение метода solve_ivp
# из библиотеки scipy.integrate
from scipy.integrate import solve_ivp

# подключение библиотеки matplotlib.pyplot
import matplotlib.pyplot as plt

# подключение библиотеки matplotlib.animation
import matplotlib.animation as animation

# Ячейка № 2

# задание функции,
# возвращающей значения
# первых производных в (8.16)
def Oscillator(t, z):
    # инициализация массива, используемого для
    # хранения значений первых производных
    dy = np.zeros(2)

    # вычисление значений первых производных
    dy[0] = z[1]
    dy[1] = -(omega**2) * np.sin(z[0])
    return dy

# Ячейка № 3

# задание значения
# ускорения свободного падения
g = 9.8

# задание длины маятника
L = 1

# вычисление периода колебаний
# линейного математического маятника
T = 2 * np.pi * (L / g) ** 0.5

# вычисление значения циклической частоты
# линейного математического маятника
omega = np.sqrt(g / L)

# задание значения массы маятника
m = 1

# задание начального угла отклонения
# математического маятника от вертикали
phi0 = np.pi * 0.9

# задание начального значения скорости
# математического маятника
dphi_dt0 = 0

# задание длительности временного интервала,
# на котором вычисляется численное решение СДУ (8.4)
N = 10**4
Tmax = 10 * T

# задание шага интегрирования СДУ (8.16)
dt = Tmax / N

# вычисление численного решения СДУ (8.16)
Solv = solve_ivp(Oscillator, [0, Tmax], [phi0, dphi_dt0], max_step=dt)

# размещение значений координат узлов
# временной сетки, на которой найдены численные решения
# системы ОДУ (8.4) в массив t
t = Solv.t

# размещение мгновенных значений
# угла отклонения математического маятника
# от вертикали в массив phi
phi = Solv.y[0, :]

# размещение мгновенных значений
# угловой скорости математического маятника
# составляющей скорости в массив dphi_dt
dphi_dt = Solv.y[1, :]

# определение числа узлов временной сетки
Np = len(t)

# инициализация массивов, используемых
# для хранения мгновенных значений
# декартовых координат и энергии математического маятника.
x = np.zeros(Np)
y = np.zeros(Np)
E = np.zeros(Np)

# вычисление декартовых координат
# математического маятника
for i in range(Np):
    # Квадрант I
    if (phi[i] >= 0) & (phi[i] >= np.pi / 2):
        x[i] = L * np.sin(np.pi - phi[i])
        y[i] = L * np.cos(np.pi - phi[i])
    # Квадрант II
    if (phi[i] < 0) & (np.abs(phi[i]) >= np.pi / 2):
        x[i] = -L * np.sin(np.pi - np.abs(phi[i]))
        y[i] = L * np.cos(np.pi - np.abs(phi[i]))
    # Квадрант III
    if (phi[i] < 0) & (np.abs(phi[i]) < np.pi / 2):
        x[i] = -L * np.sin(np.abs(phi[i]))
        y[i] = -L * np.cos(np.abs(phi[i]))
    # Квадрант IV
    if (phi[i] > 0) & (phi[i] <= np.pi / 2):
        x[i] = L * np.sin(phi[i])
        y[i] = -L * np.cos(phi[i])

# вычисление энергии математического маятника
# в соответствие с (8.20)
E = m * (L * dphi_dt) ** 2 / 2 + m * g * L * (1 - np.cos(phi))


# Ячейка № 4

# визуализация зависимости угла
# отклонения математического маятника
# от вертикали

fig = plt.figure(figsize=(11, 9))
ax = fig.add_subplot(2, 2, 1)
ax.plot(t, phi, "-k", lw=1)
ax.grid(True)
ax.set_title("а)")

# визуализация зависимости x=x(t)
ax = fig.add_subplot(2, 2, 2)
ax.plot(t, x, "-k", lw=1)
ax.grid(True)
ax.set_title("б)")

# визуализация зависимости y=y(t)
ax = fig.add_subplot(2, 2, 3)
ax.plot(t, y, "-k", lw=1)
ax.grid(True)
ax.set_title("в)")

# визуализация зависимости E(t)-E(0)
ax = fig.add_subplot(2, 2, 4)
ax.plot(t, (E - E[0]) * 10**13, "-k", lw=1)
ax.grid(True)
ax.set_title("д)")

plt.show()

# Ячейка № 5

# визуализация зависимости
# длины радиуса-вектора
# от времени

fig = plt.figure(figsize=(9, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(t, np.sqrt(x**2 + y**2), "-k", lw=1)
ax1.grid(True)
ax1.set_title("а)")

# визуализация зависимости x = x(theta)
ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(phi, x, "-k", lw=1)
ax2.grid(True)
ax2.set_title("б)")

plt.show()

# Ячейка № 6

# создание анимационного клипа

fig = plt.figure(figsize=(9, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)


def animate(i):
    nf = 50
    # анимация зависимости угла отклонения
    # математического маятника от вертикали
    ax1.clear()
    ax1.set_xlim(t.min() - 0.2, t.max() + 0.2)
    ax1.set_ylim(phi.min() - 0.2, phi.max() + 0.2)
    ax1.grid(True)
    ax1.set_title("а)")
    ax1.plot(t[0 : nf * i], phi[0 : nf * i], "-k", lw=1)
    ax1.plot(t[nf * i], phi[nf * i], "ro")

    # анимация траектории движения
    # математического маятника
    ax2.clear()
    ax2.set_xlim(-1.1, 1.1)
    ax2.set_ylim(-1.1, 1.1)
    ax2.grid(True)
    ax2.set_title("б)")
    ax2.tick_params(labelsize=9)
    O = [0, 0]
    M = [x[nf * i], y[nf * i]]
    coord = list(zip(O, M))
    ax2.plot(coord[0], coord[1], "-k", lw=1)
    ax2.plot(x[nf * i], y[nf * i], "ro")


# воспроизведение анимационного клипа
ani = animation.FuncAnimation(fig, animate, 100, interval=100, blit=False)
plt.close()

from IPython.display import HTML

HTML(ani.to_jshtml())
