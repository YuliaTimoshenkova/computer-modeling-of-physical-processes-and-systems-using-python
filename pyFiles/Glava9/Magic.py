#!/usr/bin/env python
# coding: utf-8

# Ячейка № 1

import numpy as np
# программный инструмент
# для генерации магической матрицы
# выбранного размера


def oddOrderMagicSquare(n):
    p = np.linspace(1, n, n, dtype=int)
    M = n * ((p[..., None] + p - (n + 3) // 2) % n) + (p[..., None] + 2 * p - 2) % n + 1
    return M


def magic(n):
    if n % 2 == 1:
        M = oddOrderMagicSquare(n)

    elif n % 4 == 0:
        J = np.fix((np.linspace(1, n, n, dtype=int) % 4) / 2)
        K = J[..., None] == J
        tmp = np.arange(1, n * n + 1, n, dtype=int)
        M = tmp[..., None] + np.linspace(0, n - 1, n, dtype=int)
        M[K] = n * n + 1 - M[K]

    else:
        p = n // 2
        M = oddOrderMagicSquare(p)
        M1 = np.stack((M, M + 2 * p * p), axis=1).reshape(p, n)
        M2 = np.stack((M + 3 * p * p, M + p * p), axis=1).reshape(p, n)
        M = np.stack([M1, M2]).reshape(n, n)
        if n == 2:
            return M
        i = np.linspace(1, p, p, dtype=int)
        i = i[..., None]
        k = (n - 2) // 4
        j = np.concatenate(
            (np.linspace(1, k, k, dtype=int), np.arange(n - k + 2, n + 1, 1, dtype=int))
        )
        M[i - 1, j - 1], M[i + p - 1, j - 1] = M[i + p - 1, j - 1], M[i - 1, j - 1]
        i = k + 1
        j = np.array((1, i), dtype=int)
        M[i - 1, j - 1], M[i + p - 1, j - 1] = M[i + p - 1, j - 1], M[i - 1, j - 1]

    return M


# Ячейка # 2

# задаем число строк и столбцов матрицы
N = 18
# вычисляем элементы магической матрицы
Mm = magic(N)

# распечатываем целочисленную матрицу х
print(Mm)

# вычисляем суммы по столбцам, строкам и диагоналям
# сгенерированной матрицы
s1 = 0
s2 = 0
Qq = np.zeros(N)
Qp = np.zeros(N)

for i in range(N):
    Qq[i] = np.sum(Mm[i, :])
    Qp[i] = np.sum(Mm[:, i])

for i in range(N):
    s1 = s1 + Mm[i, i]
    s2 = s2 + Mm[N - i - 1, N - i - 1]
# проверяем, что сгенерированная матрица
# явялется магической матрицей
Test = 0
if s1 == s2:
    for i in range(N):
        if ~(s1 == s2 == Qq[i] == Qp[i]):
            Test = 1
if Test == 0:
    print(
        "\n Матрица магическая \n\n",
        "Суммы по столбцам, строкам и диагоналям равняются",
        int(s1),
    )
else:
    print("Матрица не является магической")
