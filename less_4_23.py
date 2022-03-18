import cProfile

def test_func(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Тест {i} ОК')

def func1_lst(i):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _func1_lst(i):
        if fib_l[i] == None:
           fib_l[i] = _func1_lst(i - 1) + _func1_lst(i - 2)
        return fib_l[i]
    return _func1_lst(i)
#test_func(func1_lst)
cProfile.run('func1_lst(15)')

# для 10
# "less_4_23.func1_lst(10)"
# 1000 loops, best of 5: 27.4 usec per loop
# 23 function calls (5 primitive calls) in 0.000 seconds
# 19/1    0.000    0.000    0.000    0.000 less_4_23.py:13(_func1_lst)


# для 15
# "less_4_23.func1_lst(15)"
# 1000 loops, best of 5: 32.3 usec per loop
# 33 function calls (5 primitive calls) in 0.000 seconds
# 29/1    0.000    0.000    0.000    0.000 less_4_23.py:13(_func1_lst