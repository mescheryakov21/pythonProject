'''
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

import random

matrix_full = [[random.randint(-10, 10) for _ in range(5)] for _ in range(4)]
for line in matrix_full:
    for i in line:
        print(f'{i:>4}', end='')
    print()

max_value = float('-inf')
for i in range(len(matrix_full[0])):
    min_colum = matrix_full[0][i]
    for j in range(len(matrix_full)):
        if matrix_full[j][i] < min_colum:
            min_colum = matrix_full[j][i]
    if min_colum > max_value:
        max_value = min_colum
print(f'максимальный элемент из миниимальных по столбцам {max_value}')
