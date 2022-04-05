'''
 Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м
  включительно. Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке
  '''
import sys

print(sys.version, sys.platform)

def func_1():  # Рекурсия
    def printing(k, i):
        if k < 127:
            if i < 10:
                # print(sys.getsizeof(i)
                return str(k) + "-" + chr(k) + " " + printing(k + 1, i + 1)
            return str(k) + "-" + chr(k)
        return str(k) + "-" + chr(k)

    k = 32
    while k < 127:
        print(printing(k, 1))
        k += 10
    print("*" * 50)
    print(sys.getsizeof(k)) # Занимает по 28 бит переменная "k" и "i" , так как оба типа целые числа



def func_2(): #Цикл
    for i in range(32, 128):
        k = chr(i)
        if (i-32) % 10 == 0:
            # print(sys.getsizeof(i)
            print()
            print(f'{i}-{k}', end=' ')
        else:
            print(f'{i}-{k}', end=' ')
    print()
    print("*" * 50)
    print(sys.getsizeof(k)) #Занимает 50 бит переменная "k", так как типа Строка, и 28 бит переменная "i"


def func_3(): # словарь
    alphavit_dict = {i: chr(i) for i in range(32, 128)}
    for key, value in alphavit_dict.items():
        if (key - 31) % 10 != 0:
            print(key, value, sep= '-', end=' ')
            # print(sys.getsizeof(key))
            # print(sys.getsizeof(value))
        else:
            print(key, value, sep= '-', end=' ')
            print()
    print(sys.getsizeof(alphavit_dict)) # Переменная "key" 28 бит типа Целое
                                        # Переменная "value 50 бит тип Строка
                                        # Словарь занимает 4696 бит

func_3()
