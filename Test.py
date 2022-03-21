'''
Решето Эратосфена
'''
n = int(input("Введите простое число до какого числа простые включительно: "))
start_list =[i for i in range(n+1)]
start_list[1] = 0
for i in range(2, n+1):
    if start_list[i] != 0:
        j = i + i
        while j <= n:
            start_list[j] = 0
            j += i
result = [i for i in start_list if i != 0]
print(result)