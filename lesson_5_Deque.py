from collections import deque
a = deque()
b = deque('adfefsadaaef')
c = deque([1, 2, 3, 4, 5, 7], maxlen=15)
print(a, b, c, sep='\n')

# c.extendleft(b)
# print("*" * 50)
# print(c, sep='\n')
# c.reverse()
# print(c)
c.rotate(-2)
print(c)