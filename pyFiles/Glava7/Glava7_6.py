#!/usr/bin/env python
# coding: utf-8

# визуализация функции Si(x)/pi

# подключение библиотеки numpy
import numpy as np

# подключение библиотеки matplotlib.pyplot
import matplotlib.pyplot as plt

# подключение библиотеки scipy.special
import scipy.special

# вычисление значений функции Si(x)
x = np.arange(0, 30, 3 * 10**-3)
y = scipy.special.sici(x)

# визуализация функции Si(x)/pi
fig = plt.figure(figsize=(7.5, 5))
ax = fig.add_subplot()
plt.plot(x, y[0] / np.pi, "-k", lw=1)
plt.grid(True)
plt.show()
