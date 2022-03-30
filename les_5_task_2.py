'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
 представляется как массив, элементы которого — цифры числа.
'''
from collections import deque

def test(a,b):
    a = int(a, 16)
    b = int(b, 16)
    print(f'Тест сложение {format(a + b, "X")}')
    print(f'Тест умножение {format(a * b,"X")}')

def sum_hex(a, b, l):
    dict_val = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    a.reverse()
    b.reverse()
    for i in range(l):
        print(dict_val)
    return

len_deq = 0
a_1 = deque(input("Введите первое шестнадцатиричное число: "))
a_2 = deque(input("Введите второе шестнадцатиричное число: "))
# test(a_1, a_2)
# dict_val = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
#             'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
raz = abs(len(a_1) - len(a_2))
if len(a_1) > len(a_2):
    len_deq = len(a_1)
    a_2.extendleft(list('0' * raz))
else:
    len_deq = len(a_2)
    a_1.extendleft(list('0' * raz))
sum_hex(a_1, a_2, len_deq)
# print(len(a_2))
print(a_1)
print(a_2)