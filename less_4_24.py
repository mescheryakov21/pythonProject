# import cProfile
import cProfile


def test_func(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Тест {i} ОК')

def fib_cikl(n):
    if n < 2:
        return n

    first, second = 0, 1
    for i in range(2, n + 1):
        first, second = second, first + second
    return second

cProfile.run('fib_cikl(1500)')

# test_func(fib_cikl)
# "less_4_24.fib_cikl(10)"
# 1000 loops, best of 5: 1.94 usec per loop
# 4 function calls in 0.000 seconds


# "less_4_24.fib_cikl(15)"
# 1000 loops, best of 5: 2.56 usec per loop
# 4 function calls in 0.000 seconds