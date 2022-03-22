'''
 Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
  принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и
   сложность алгоритмов.
Решето Эратосфена
Классический Алгоритм
'''

def prost_1(n):
   if n == 0:
       return 0
   result = [] * n
   k = 1
   if result[n-1] != None:
       return result[n - 1]
   while n > len(result)
   start_list = [i for i in range(k)]
   start_list[1] = 0
   for i in range(2, k):
        if start_list[i] != 0:
            j = i + i
            while j < k:
                start_list[j] = 0
                j += i
   result = [i for i in start_list if i != 0]
   return result[n-1]

# poryadok = 1
# while poryadok != 0:
#     poryadok = int(input("Введите место простого числа: "))
#     print(prost_1(poryadok))

# "less_task_2a.prost_1(10)"
# 1000 loops, best of 5: 57.9 usec per loop
# less_task_2a.prost_1(100)"
# 1000 loops, best of 5: 7.8 msec per loop