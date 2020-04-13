from collections import deque

# 初期化
d = deque()
# deque([])

d = deque([0, 1, 2, 3, 4, 5])
# deque([0, 1, 2, 3, 4, 5])

# 両端への要素の追加 O(1)
d.append(6)
# deque([0, 1, 2, 3, 4, 5, 6])

d.appendleft(-1)
# deque([-1, 0, 1, 2, 3, 4, 5, 6])

# 両端に対する要素の削除 O(1)
# 引数を取らないことに注意
d.pop()
# 6

d.popleft()
# -1

# 要素の削除
# 複数あっても削除されるのは最初の要素のみ
d.remove(3)
# deque([1, 2, 4, 5])

# indexの取得
d.index(2)
# 1

# 要素数
len(d)
# 4

# 特定要素の個数
d.count(1)
# 1
