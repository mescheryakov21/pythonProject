'''
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''
import random

arr_first = [random.randint(-10, 10) for _ in range(20)]
max_negativ = -10
pos_max = 0
for i, item in enumerate(arr_first):
    if item < 0:
        if item > max_negativ:
            max_negativ = item
            pos_max = i
print(f'максимальный отрицательный элемент в массиве \n {arr_first} \n является {max_negativ}, который стоит на позиции {pos_max} ')
