'''
2. Закодируйте любую строку по алгоритму Хаффмана.
'''
from collections import Counter, deque
from binarytree import bst, Node

stroka = 'viva la vita'
d = Counter(stroka)
deq = deque(d)
tree_hof = Node('')
dict_spam = dict()
print(d)
print(deq)
while len(d) > 1:
    # a = deq.pop()
    key1, item1 = d.popitem()
    key2, item2 = d.popitem()
    if item1 > item2:
        tree_hof.right = Node(key1)
        tree_hof.left = Node(key2)
    else:
        tree_hof.right = Node(key2)
        tree_hof.left = Node(key1)
    dict_spam[tree_hof] = item2 + item1
    d.update(dict_spam)
    print(tree_hof)
print(tree_hof)
