'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''

import random

def slit_arr(arr):
    if len(arr) == 1:
        return arr
    a = slit_arr(arr[:len(arr) // 2])
    b = slit_arr(arr[len(arr) // 2:])
    k = 0
    l = 0
    c = list()
    while k < len(a) and l < len(b):
        if a[k] < b[l]:
            c.append(a[k])
            k += 1
        else:
            c.append(b[l])
            l += 1
    if len(a) > k:
        c.extend(a[k:])
    elif len(b) > l:
        c.extend(b[l:])
    return c

size = 100
array_ramd = [random.randint(0, 49) for i in range(size)]
print(array_ramd)
print(slit_arr(array_ramd))
