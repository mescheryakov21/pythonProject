"""
сортировку улучшить
проверить последний отсортированный с предшествующим
"""

"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
 на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. 
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

import random
import cProfile
# def sort():
def sort_boble(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i + 1], array[i]  =  array[i], array[i + 1]
        n += 1
    print(array)

size = 10
array_ramd = [random.randint(-100, 99) for i in range(size)]
print(array_ramd)
sort_boble(array_ramd)

# cProfile.run('sort()')
# 100 loops, best of 5: 331 nsec per loop
# 105 function calls in 0.000 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 less_7_task_1.py:17(sort)
#         1    0.000    0.000    0.000    0.000 less_7_task_1.py:18(sort_boble)
#         1    0.000    0.000    0.000    0.000 less_7_task_1.py:28(<listcomp>)
#        10    0.000    0.000    0.000    0.000 random.py:239(_randbelow_with_getrandbits)
#        10    0.000    0.000    0.000    0.000 random.py:292(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:366(randint)
#        30    0.000    0.000    0.000    0.000 {built-in method _operator.index}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        19    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        10    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects
