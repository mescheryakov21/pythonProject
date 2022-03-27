from collections import defaultdict
from collections import Counter
s = 'skflgj;asjpwejfafsfFWAGFVAGSFGGasfdg'
a = defaultdict(int)
for i in s:
    a[i] += 1
# print(a)
c = Counter(s)
# print(c)
list_1 = [('cat', 2), ('dog', 1), ('cat', 2)]
b = defaultdict(list)
c = defaultdict(set)
for i, j in list_1:
    b[i].append(j)
for i, j in list_1:
    c[i].add(j)
print(b, c, sep="\n")

