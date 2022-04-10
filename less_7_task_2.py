'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''

import random

def slit_arr(array):
    '''
    Метод сортировки Слияние
    :param array:  - неотсортированный массив
    :return: - отсортированный массив
    '''
    if len(array) == 1:
        return array



size = 20
array_ramd = [random.randint(0, 49) for i in range(size)]
print(array_ramd)
slit_arr(array_ramd)