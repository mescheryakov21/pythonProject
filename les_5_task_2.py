'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
 представляется как массив, элементы которого — цифры числа.
'''
from collections import defaultdict
from collections import deque
from collections import OrderedDict
from collections import defaultdict

def test(a,b):
    a = int(a, 16)
    b = int(b, 16)
    print(f'Тест сложение {format(a + b, "X")}')
    print(f'Тест умножение {format(a * b,"X")}')

a_1 = input("Введите первое шестнадцатиричное число: ")
a_2 = input("Введите второе шестнадцатиричное число: ")
# test(a_1, a_2)

print()
print()
print()
print()