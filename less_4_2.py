import cProfile
import functools
def test_func(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Тест {i} ОК')

@functools.lru_cache()
def func1(i):
    if i < 2:
        return i
    return func1(i - 2) + func1(i - 1)

# cProfile.run('func1(15)')
# test_func(func1)
# для 10
# 1000 loops, best of 5: 50.6 usec per loop
#  180 function calls (4 primitive calls) in 0.000 seconds
# 177/1    0.000    0.000    0.000    0.000 less_4_2.py:9(func1)
# less_4_2.func1(10)" мемоизация
# 1000 loops, best of 5: 230 nsec per loop
#
# для 15
# 1000 loops, best of 5: 570 usec per loop
# 1976 function calls (4 primitive calls) in 0.001 seconds
# 1973/1    0.001    0.000    0.001    0.001 less_4_2.py:9(func1)
# "less_4_2.func1(15)" мемоизация
# 1000 loops, best of 5: 225 nsec per loop
