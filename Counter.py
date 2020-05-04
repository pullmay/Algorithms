# Ref: https://note.nkmk.me/python-collections-counter/

from collections import Counter

lst = ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'c']
c = Counter(lst)

print(c)
# Counter({'a': 4, 'b': 3, 'c': 1})

print(c['a']) # 4
print(c['b']) # 3
print(c['c']) # 1
print(c['d']) # 0

print(c.keys())
# dict_keys(['a', 'b', 'c'])
print(c.values())
# dict_values([4, 3, 1])
print(c.items())
# dict_items([('a', 4), ('b', 3), ('c', 1)])

print(c.most_common())
# [('a', 4), ('b', 3), ('c', 1)]

# 出現回数の最も多い要素
print(c.most_common()[0])
# ('a', 4)

# values, counts
values, counts = zip(*c.most_common())
print(values)
# ('a', 'b', 'c')
print(counts)
# (4, 3, 1)

