import cProfile

def test_func(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Тест {i} ОК')

def func1_dict(i):
    fib_d = {0: 0, 1: 1}

    def _func1_dict(i):
        if i in fib_d:
            return fib_d[i]
        fib_d[i] = _func1_dict(i - 1) + _func1_dict(i - 2)
        return fib_d[i]
    return _func1_dict(i)
# test_func(func1_dict)
cProfile.run('func1_dict(15)')

# test_func(func1)
# для 10
# "less_4_22.func1_dict(10)"
# 1000 loops, best of 5: 10.5 usec per loop
# 23 function calls (5 primitive calls) in 0.000 seconds
# 19/1    0.000    0.000    0.000    0.000 less_4_22.py:12(_func1_dict)

# для 15
# "less_4_22.func1_dict(15)"
# 1000 loops, best of 5: 15.4 usec per loop
# 33 function calls (5 primitive calls) in 0.000 seconds
# 29/1    0.000    0.000    0.000    0.000 less_4_22.py:12(_func1_dict)
