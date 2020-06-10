from itertools import combinations, permutations

# combinations
# 第一引数: 第一引数にイテラブル(e.g., リストや集合set型)
# 第二引数: 選択する個数
lst = list(range(5)) # [0,1,2,3,4]
c = combinations(lst, 2)

print(c)
# <itertools.combinations object at 0x000001CB30DD7DB8>

for v in c:
	print(v)

# (0, 1)
# (0, 2)
# (0, 3)
# (0, 4)
# (1, 2)
# (1, 3)
# (1, 4)
# (2, 3)
# (2, 4)
# (3, 4)

# リスト化可能
print(list(combinations(lst, 2)))
# [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]


# 順列
# 第一引数: 第一引数にイテラブル(e.g., リストや集合set型)
# 第二引数: 選択する個数
lst = [7, 8, 9]
p = permutations(lst, len(lst))

for v in p:
	print(v)
	
# (7, 8, 9)
# (7, 9, 8)
# (8, 7, 9)
# (8, 9, 7)
# (9, 7, 8)
# (9, 8, 7)

# リスト化可能
print(list(permutations(lst, len(lst))))
# [(7, 8, 9), (7, 9, 8), (8, 7, 9), (8, 9, 7), (9, 7, 8), (9, 8, 7)]
