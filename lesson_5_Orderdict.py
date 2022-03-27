from collections import OrderedDict

a = {'mouse': 4, 'cat': 4, 'dog': 3}
b = {'mouse': 4, 'cat': 4, 'dog': 3}
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
print(new_a)
new_b = OrderedDict(reversed(sorted(a.items(), key=lambda x: x[1])))
print(new_b)

new_b.move_to_end('mouse', last=False)
print(new_b)
# print("*" * 50)
# print(a == b)
# print(new_a == new_b)