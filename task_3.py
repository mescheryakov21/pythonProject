'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random

arr_first = [random.randint(-10, 100) for _ in range(10)]
print(arr_first)
item_max_v = arr_first[0]
item_min_v = arr_first[0]
max_ind = 0
min_ind = 0
for i in range(len(arr_first)):
    if arr_first[i] > item_max_v:
        item_max_v = arr_first[i]
        max_ind = i
    elif arr_first[i] < item_min_v:
        item_min_v = arr_first[i]
        min_ind = i

arr_first[max_ind], arr_first[min_ind] = arr_first[min_ind], arr_first[max_ind]
print(f'Максимальное значение в массиве соит на {max_ind} месте, а минимальное на {min_ind} месте')
print(arr_first)

