'''В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны
 между собой (оба минимальны), так и различаться.
'''
import random

arr_first = [random.randint(-5, 5) for _ in range(10)]
print(arr_first)
min_v1, min_v2 = arr_first[0], arr_first[1]
s = float('inf')
for i in range(1, len(arr_first)):
    if arr_first[i] <= min_v1:
        s = min_v1
        min_v1 = arr_first[i]
    elif arr_first[i] <= min_v2:
        min_v2 = arr_first[i]
    if s <= min_v2:
        min_v2 = s
print(f'Первое минимальное {min_v1}, второе минимальное {min_v2}')
