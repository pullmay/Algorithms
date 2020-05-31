# Ref: https://www.slideshare.net/iwiwi/ss-3578491

import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

class SegTree:
    def __init__(self, init_lst, func, default_val):
        n = len(init_lst)
        self.m = pow(2, (n - 1).bit_length()) # n 以上の最小の 2 のべき乗
        self.func = func # 適用関数
        self.default_val = default_val # 初期値
        self.seg = [self.default_val] * (2 * m - 1) # # 配列の要素数は 2 * m - 1
        # Build Segment Tree
        # 葉
        for i in range(n):
            self.seg[self.m - 1 + i] = init_lst[i]
        # 親に伝播させていく
        for i in range(self.m - 2, -1, -1):
            self.seg[i] = self.func(self.seg[2 * i + 1], self.seg[2 * i + 2])
    
    # 値の更新
    # 配列の k 番目の要素を x に変更
    def update(self, k, x):
        k += self.m - 1
        self.seg[k] = x
        while k > 1:
            k = (k - 1) // 2
            self.seg[k] = self.func(self.seg[2 * k + 1], self.seg[2 * k + 2])
        
    def query(self, a, b):
        return self.query_sub(a, b, 0, 0, self.m)

    def query_sub(self, a, b, k, l, r):
        if r <= a or b <= l:
            return self.default_val
        elif a <= l and r <= b:
            return self.seg[k]
        else:
            vl = self.query_sub(a, b, 2 * k + 1, l, (l + r) // 2)
            vr = self.query_sub(a, b, 2 * k + 2, (l + r) // 2, r)
            return self.func(vl, vr)

# --- usage --- #
# 入力
n, q = map(int, input().split())
A = list(map(int, input().split()))
# セグメント木の構築
segtree = SegTree(A, min, float('inf'))

# クエリの処理
for i in range(q):
    l, r = map(int, input().split())
    res = segtree.query(l, r)
    print(res)