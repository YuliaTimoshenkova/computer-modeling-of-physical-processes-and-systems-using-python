#!/usr/bin/env python
# coding: utf-8

# визуализация вектора напряженности
# электрического поля волны,
# распространяющейся вдоль оси OY

# Ячейка № 1

# подключение библиотеки numpy
import numpy as np

# подключение пакета matplotlib.pyplot
import matplotlib.pyplot as plt

# Ячейка № 2

# задание координатной сетки
# по оси OY
Np = 100
Y_min = 0
Y_max = 2
y = np.linspace(Y_min, Y_max, Np)

# задание амплитуд напряженностей
# составляющих электромагнитной волны
# по осям OX, OZ
Ex0 = 1
Ez0 = 1

# инициализация массива Ex,
# используемого для хранения
# значений составляющей напряженности
# электрического поля по оси OX
Ex = np.zeros(Np)

# вычисление значений
# составляющей напряженности
# электрического поля по оси OX
# в момент времени t = 1.2
t = 2.1
Ex[:] = Ex0 * np.cos(2 * np.pi * y[:] - 2 * np.pi * t + np.pi / 2)

# инициализация массива Ey,
# используемого для хранения
# значений составляющей напряженности
# электрического поля по оси OX
Ez = np.zeros(Np)

# вычисление значений
# составляющей напряженности
# электрического поля по оси OY
# в момент времени t = 1.2
Ez[:] = Ez0 * np.cos(2 * np.pi * y[:] - 2 * np.pi * t)


# визуализация вектора напряженности
# электромагнитного поля в плоскости XOZ
# в выбранных узлах координатной сетки

# задание радиуса-вектора
# точки начала координат
origin = np.array([0, 0])

# задание вектора, содержащего значения
# составляющих напряженностей
# электрического в точке y = 0
vector1 = np.array([Ex[0], Ez[0]])

# задание вектора, содержащего значения
# составляющих напряженностей
# электрического в точке y = 0.385
vector2 = np.array([Ex[10], Ez[10]])

# задание вектора, содержащего значения
# составляющих напряженностей
# электрического в точке y = 0.769
vector3 = np.array([Ex[20], Ez[20]])

# задание вектора, содержащего значения
# составляющих напряженностей
# электрического в точке y = 1.346
vector4 = np.array([Ex[35], Ez[35]])


fig = plt.figure(figsize=(13, 11))
# визуализация вектора напряженности
# электрического поля в точке y = 0
ax = plt.subplot(2, 2, 1, projection="polar")
ax.quiver(*origin, *vector1, scale=2)
ax.set_rmin(0)
ax.set_rmax(1)
ax.set_rticks([0.5, 1, 1.5, 1])  # Less radial ticks
ax.set_rlabel_position(-22.5)
ax.set_title("a)", fontsize=9)

# визуализация вектора напряженности
# электрического поля в точке y = 0.385
ax = plt.subplot(2, 2, 2, projection="polar")
ax.quiver(*origin, *vector2, scale=2)
ax.set_rmin(0)
ax.set_rmax(1)
ax.set_rticks([0.5, 1, 1.5, 1])  # Less radial ticks
ax.set_rlabel_position(-22.5)
ax.set_title("б)", fontsize=9)

# визуализация вектора напряженности
# электрического поля в точке y = 0.769
ax = plt.subplot(2, 2, 3, projection="polar")
ax.quiver(*origin, *vector3, scale=2)
ax.set_rmin(0)
ax.set_rmax(1)
ax.set_rticks([0.5, 1, 1.5, 1])  # Less radial ticks
ax.set_rlabel_position(-22.5)
ax.set_title("в)", fontsize=9)

# визуализация вектора напряженности
# электрического поля в точке y = 1.346
ax = plt.subplot(2, 2, 4, projection="polar")
ax.quiver(*origin, *vector4, scale=2)
ax.set_rmin(0)
ax.set_rmax(1)
ax.set_rticks([0.5, 1, 1.5, 1])  # Less radial ticks
ax.set_rlabel_position(-22.5)
ax.set_title("г)", fontsize=9)

plt.show()

# Ячейка № 3

# 3D визуализация напряженности
# электрического поля
# электромагнитной волны

# задание числа узлов и
# значений координат
# координатной сетки
Np = 53
x = np.zeros(Np)
z = np.zeros(Np)
y = np.linspace(Y_min, Y_max, Np)

# инициализация массива Ex,
# используемого для хранения
# значений составляющей напряженности
# электрического поля по оси OX
Ex = np.zeros(Np)
t = 2.1
Ex[:] = Ex0 * np.cos(2 * np.pi * y[:] - 2 * np.pi * t + np.pi / 2)

# инициализация массива Ey,
# используемого для хранения
# значений составляющей напряженности
# электрического поля по оси OY
Ey = np.zeros(Np)

# инициализация массива Ez,
# используемого для хранения
# значений составляющей напряженности
# электрического поля по оси OZ
Ez = np.zeros(Np)
Ez[:] = Ez0 * np.cos(2 * np.pi * y[:] - 2 * np.pi * t)

# 3D визуализация напряженности
# электрического поля
# электромагнитной волны

fig = plt.figure(figsize=(15, 11))

# визуализация напряженности
# электрического поля
# электромагнитной волны в виде
# 3D векторов
ax = plt.subplot(1, 2, 1, projection="3d")
ax.quiver(x, y, z, Ex, Ey, Ez, length=0.05, color="black", normalize=True)
plt.tick_params(axis="both", which="major", labelsize=8)
ax.set_xlim([-0.1, 0.1])
ax.set_xticks(np.linspace(-0.1, 0.1, 5))
ax.set_yticks(np.linspace(Y_min, Y_max, 5))
ax.set_zlim([-0.1, 0.1])
ax.set_zticks(np.linspace(-0.1, 0.1, 5))
ax.set_xlabel(r"$X$", fontsize=8)
ax.set_ylabel(r"$Y$", fontsize=8)
ax.set_zlabel(r"$Z$", fontsize=8)

# визуализация напряженности
# электрического поля в виде
# линии, проходящей через концы
# векторов напряженностей
# электрического поля
ax = plt.subplot(1, 2, 2, projection="3d")
ax.plot(Ex, y, Ez, color="black")
plt.tick_params(axis="both", which="major", labelsize=8)
ax.set_xlim([-1.0, 1.0])
ax.set_xticks(np.linspace(-1.0, 1.0, 5))
ax.set_yticks(np.linspace(Y_min, Y_max, 5))
ax.set_zlim([-1.0, 1.0])
ax.set_zticks(np.linspace(-1.0, 1.0, 5))
ax.set_xlabel(r"$X$", fontsize=8)
ax.set_ylabel(r"$Y$", fontsize=8)
ax.set_zlabel(r"$Z$", fontsize=8)

plt.show()
