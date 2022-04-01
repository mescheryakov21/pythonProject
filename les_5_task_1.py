'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для
 каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
  вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''
from collections import ChainMap
n = int(input("Введите количество предприятий: "))
k = 1
full_dict = ChainMap()
sum_profit = 0
while k <= n:
    name_firma = input(f'Введите наименование {k}го предприятия: ')
    profit = float(input(f'Введите прибыль за IV квартала {k}го предприятия: '))
    dict_spam = {'name': name_firma, 'profit': profit }
    full_dict = full_dict.new_child(dict_spam)
    k += 1
    sum_profit += profit
arg_profit = sum_profit / n
a = list()
b = list()

for i in range(n):
    c = full_dict.maps[i]['profit']
    if c > arg_profit:
        a.append(full_dict.maps[i]['name'])
    else:
        b.append(full_dict.maps[i]['name'])
print(f'Предприятия с большей прибылью, чем среднее {arg_profit}: {a} \nПредприятия с меньшей прибылью чем среднее {arg_profit}: {b}')
