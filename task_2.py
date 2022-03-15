'''
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
 надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
 т. к. именно в этих позициях первого массива стоят четные числа.
'''
import random
arr_first = [random.randint(-10,100) for _ in range(10)]
arr_second = []
print(arr_first)
for i, item in enumerate(arr_first):
    if item % 2 == 0:
        arr_second.append(i)
print(arr_second)
