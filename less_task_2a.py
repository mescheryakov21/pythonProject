'''
 Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
  принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и
   сложность алгоритмов.
Решето Эратосфена
Классический Алгоритм
'''

def test_func(func):
    lst = [2, 3, 5, 7, 11, 13]
    for i in range(len(lst)):
        assert lst[i] == func(i)

def prost_1(n):
    if i != 0:
       start_list = [i for i in range(n)]
       start_list[1] = 0
       for i in range(2, n + 1):
            if start_list[i] != 0:
                j = i + i
                while j <= n:
                    start_list[j] = 0
                    j += i
       result = [i for i in start_list if i != 0]
       return result[n-1]

test_func(prost_1)


