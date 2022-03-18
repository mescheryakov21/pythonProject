'''
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.Программа должнавычислять
сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести
полученную матрицу.
'''

matrix_full = []
for i in range(5):
    matrix_row = []
    sum = 0
    for j in range(3):
        k = int(input(f'Введите элемент {i + 1} строки: '))
        sum += k
        matrix_row.append(k)
        if j == 2:
            matrix_row.append(sum)

    matrix_full.append(matrix_row)

for line in matrix_full:
    for i in line:
        print(f"{i:>4}", end="")
    print()
