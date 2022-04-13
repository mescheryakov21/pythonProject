'''
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
 Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
  которые не меньше медианы, в другой — не больше медианы.
'''
import random

m = int(input('Введите натуральное число m для расчета размера массива: '))
l = 2 * m + 1
array_ramd = [random.randint(-10, 10) for i in range(l)]

n = 0
while n < len(array_ramd):
    z = array_ramd[n]
    men = 0
    bol = 0
    ravn = 0
    for i in range(len(array_ramd)): # считаем сколько раз значение больше, меньше и равно значению сравнения
        if n != i:
            if z < array_ramd[i]:
                men += 1
            elif z > array_ramd[i]:
                bol += 1
            else:
                ravn += 1

    while ravn > 0: # распределение равных элементов по счетчикам
        if men > bol:
            bol += 1
        else:
            men +=1
        ravn -= 1

    if men == bol:
        break
    n += 1

print(array_ramd)
array_ramd.sort()
print(array_ramd)
print(f"Медианной является число {z}")
