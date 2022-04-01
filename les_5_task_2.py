'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
 представляется как массив, элементы которого — цифры числа.
'''
from collections import deque



def sum_hex(a, b, l, dict_val):
    '''
    Принимает слагаемые в виде списка порядков
    Принимает длинну максимального слагаемого
    Принимает Словарь справочник
    Возвращает Сумма в виде списка порядков
    '''
    sum_list = []
    sum_pos_up = 0 
    for i in range(l-1, -1, -1):
        sum_first = sum_pos_up + dict_val.get(a[i]) + dict_val.get(b[i])
        if sum_first >= 16:
            sum_pos1 = sum_first % 16
            sum_pos_up = sum_first // 16
        else:
            sum_pos1 = sum_first
            sum_pos_up = 0
        if i == 0 and sum_pos_up > 0:
            sum_list.append(sum_pos1)
            sum_list.append(sum_pos_up)
        else:
            sum_list.append(sum_pos1)
    return mod_hex(sum_list, dict_val)


def mult_hex(a, b, dict_val):
    '''
    Принимает множители и справочный словарь
    Возвращает Произведение
    '''
    mult_list = []
    mult_pos_up = 0
    a.reverse()
    b.reverse()
    mult_sum = 0
    for k in range(len(a)):
        for i in range(len(b)):
            mult_first = mult_pos_up + dict_val.get(a[k]) * dict_val.get(b[i]) * pow(16, k + i)
            mult_sum += mult_first
    mult_list = hex_mag(mult_sum, mult_list)
    return mod_hex(mult_list, dict_val)


def hex_mag(num, lst):
    '''
    Получает Произведение в десятиричной системе исчисления
    Возвращает интерпретацию шестнадцатиричного преобразованного числа ввиде списка порядков начиная с наименьшего
    Значения Порядков в десятичной системе исчисления
    '''
    if num > 16:
        lst.append(num % 16)
        num = num // 16
        return hex_mag(num, lst)
    lst.append(num)
    return lst
    

def mod_hex(lst_sum, dct):
    '''
    Принимает список с порядками шестнадцатиричного числа - Значения Порядков в десятичной системе исчисления
    Принимает Список справочник
    Возвращает шестнадцатиричное число списком порядков начиная с наибольшего
    '''
    vivod = deque()
    for i in lst_sum:
        for key, value in dct.items():
            if i == value:
                vivod.appendleft(key)
    return vivod
        

len_deq = 0
a_1 = deque(input("Введите первое шестнадцатиричное число: "))
a_2 = deque(input("Введите второе шестнадцатиричное число: "))
dict_val = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
raz = abs(len(a_1) - len(a_2))
if len(a_1) > len(a_2):
    len_deq = len(a_1)
    a_2.extendleft(list('0' * raz))
else:
    len_deq = len(a_2)
    a_1.extendleft(list('0' * raz))
print()   
print(f'Сумма {a_1} и {a_2}  равно: \n {sum_hex(a_1, a_2, len_deq, dict_val)}')
print()
print(f'Произведение {a_1} на {a_2} равно: \n {mult_hex(a_1, a_2, dict_val)}')
