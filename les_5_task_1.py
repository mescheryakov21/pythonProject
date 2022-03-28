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
    profit = int(input(f'Введите прибыль за IV квартала {k}го предприятия: '))
    dict_spam = {'name': name_firma, 'profit': profit }
    full_dict = full_dict.new_child(dict_spam)
    k += 1
    sum_profit += profit
arg_profit = sum_profit / n
# if profit < arg_profit:
print(full_dict, sum_profit, arg_profit )