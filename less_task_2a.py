'''
 Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
  принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и
   сложность алгоритмов.
Решето Эратосфена
Классический Алгоритм
'''

def prost_1(n):
   start_list = [i for i in range(n * 10 +1)]
   start_list[1] = 0
   for i in range(2,len(start_list)):
        if start_list[i] != 0:
            j = i + i
            while j <= n * 10:
                start_list[j] = 0
                j += i
   result = [i for i in start_list if i != 0]
   return result[n-1]
poryadok = int(input("Введите место простого числа: "))
print(prost_1(poryadok))


