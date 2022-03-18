import timeit

print(timeit.timeit("x = 2 + 2"))
print(timeit.timeit("s = sum(range(10))"))