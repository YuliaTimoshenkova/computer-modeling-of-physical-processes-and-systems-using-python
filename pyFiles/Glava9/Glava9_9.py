#!/usr/bin/env python
# coding: utf-8

# Ячейка № 1

# подключение библиотеки numpy
import numpy as np

# импорт модуля optimize из библиотеки scipy
from scipy import optimize

# импорт модуля pyplot из библиотеки matplotlib
from matplotlib import pyplot as plt

# Ячейка № 2

# задание функции,
# у которой ищутся нули
def f(k):
    return Omega - g * k + T / r0 * k**3


# Ячейка № 3

# нахождение корней нелинейного уравнения,
# зависящего от одной переменной
# с помощью метода половинного деления

# задание значений параметров функции
g = 980
T = 72
r0 = 1
Omega = 1000

# визуализация графика функции f(x)
# для нахождения отрезков на которых
# функция f(x)
# пересекает ось абсцисс (отделение корней)
x = np.linspace(-5, 5, 100)
fig, ax = plt.subplots(figsize=(7, 5), layout="tight")
ax.plot(x, f(x), "-k", lw=1)
ax.grid(True)
plt.show()

# нахождение корня x1 уравнения f(x) = 0 на отрезке [-5,-2]
print("Результаты поиска корня на отрезке [5,-2]:", "\n")
solution = optimize.root_scalar(f, bracket=[-5, -2], method="bisect")
print(solution, "\n")

# вычисление значения функции f(x1)
print("f(x1) = ", f(solution.root), "\n")

# нахождение корня x2 уравнения f(x) = 0 на отрезке [-2,2]
print("Результаты поиска корня на отрезке [-2,2]:", "\n")
solution = optimize.root_scalar(f, bracket=[-2, 2], method="bisect")
print(solution, "\n")

# вычисление значения функции f(x2)
print("f(x2) = ", f(solution.root), "\n")

# нахождение корня x3 уравнения f(x) = 0 на отрезке [2,4]
print("Результаты поиска корня на отрезке [2,4]:", "\n")
solution = optimize.root_scalar(f, bracket=[2, 4], method="bisect")
print(solution, "\n")

# вычисление значения функции f(x3)
print("f(x3) = ", f(solution.root))

