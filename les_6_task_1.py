'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''
import random

arr_first = [random.randint(-5, 5) for _ in range(10)]
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
start_sum = min_ind
finish_sum = max_ind
if start_sum == finish_sum:
    print(f'Минимальное и максимальное число одно и тоже {item_min_v}')
elif start_sum > finish_sum:
    start_sum, finish_sum = finish_sum, start_sum
sum=0
for i in range(start_sum+1, finish_sum):
    sum += arr_first[i]
print(sum)
