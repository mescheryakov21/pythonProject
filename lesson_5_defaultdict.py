from collections import defaultdict
from collections import Counter
s = 'skflgj;asjpwejfafsfFWAGFVAGSFGGasfdg'
a = defaultdict(int)
for i in s:
    a[i] += 1
print(a)
c = Counter(s)
print(c)
