'''
 Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м
  включительно. Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке
  '''
import cProfile
def func_1():  # Рекурсия
    def printing(k, i):
        if k < 127:
            if i < 10:
                return str(k) + "-" + chr(k) + " " + printing(k + 1, i + 1)
            return str(k) + "-" + chr(k)
        return str(k) + "-" + chr(k)
    k = 32
    while k < 127:
        printing(k, 1)
        k += 10
#cProfile.run('func_1()')
# less_4_task_1.func_1()"
# 1000 loops, best of 5: 142 usec per loop
# 196 function calls (110 primitive calls) in 0.000 seconds
# 96/10    0.000    0.000    0.000    0.000 less_4_task_1.py:9(printing)
#    96    0.000    0.000    0.000    0.000 {built-in method builtins.chr}



def func_2(): #Цикл
    for i in range(32, 128):
        k = chr(i)
        if (i+1-32) % 10 == 0:
            k = 1
#cProfile.run('func_2()')
# less_4_task_1.func_2()"
# 1000 loops, best of 5: 27.5 usec per loop
# 100 function calls in 0.000 seconds
# 96    0.000    0.000    0.000    0.000 {built-in method builtins.chr}


def func_3():
    alphavit_dict = {i: chr(i) for i in range(32, 128)}
    for key, value in alphavit_dict.items():
        if (key - 31) % 10 != 0:
            k = 4 #print(key, value, sep= '-', end=' ')
        else:
            k = 3 #print(key, value, sep= '-', end=' ')
            k = 0 #print()