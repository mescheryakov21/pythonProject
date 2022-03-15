'''
4. Определить, какое число в массиве встречается чаще всего.
'''
import random

def arr_count(a, k):
    count = 0
    for i in a:
        if k == i:
            count += 1
    return count

dict_arr = {}
arr_first = [random.randint(-10, 10) for _ in range(100)]
for item in arr_first:
    count_i = arr_count(arr_first, item)
    dict_arr[item] = count_i
max_count = 0
arr_key = dict_arr.keys()
max_key = 0
for key, value in dict_arr.items():
    if value > max_count:
        max_count = value
        max_key = key
print(f'значение {max_key}, повторяется максимально {max_count} раз')
