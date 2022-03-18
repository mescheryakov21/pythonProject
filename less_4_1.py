import cProfile

def len_arr(arr):
    return len(arr)

def sum_arr(arr):
    s = 0
    for i in arr:
        s += i
    return s

def main():
    lst = [i for i in range(10000)]
    a = len_arr(lst)
    b = sum_arr(lst)

cProfile.run('main()')
