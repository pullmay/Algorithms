# 基本的な入出力

# 整数
# 1
n = int(input())

# 複数の整数
# 1 2
n, k = map(int, input().split())

# リスト
# 1 2 3 4 5
A = list(map(int, input().split()))

# 複数行
# n <- 個数
# 1
# 2
# 3
A = [int(input()) for _ in range(n)]

# 二次元配列
# h w <- 3 5
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
A = [[int(x) for x in input().split()] for _ in range(h)]
# print(A) # [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

# grid
# h w <- height width
# s####
# ....#
# #####
# #...g
grid = [list(input()) for _ in range(h)]
# print(grid) # [['s', '#', '#', '#', '#'], ['.', '.', '.', '.', '#'], ['#', '#', '#', '#', '#'], ['#', '.', '.', '.', 'g']]
