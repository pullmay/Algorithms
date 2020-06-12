class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)] # parents
        self.rank = [1] * n # height of tree
        self.size = [1] * n # size[i] -> iをrootとするgroupのサイズ

    # 木の根を返す
    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # xとyの属する集合を併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parents[x] = y
            self.size[y] += self.size[x] 
        else:
            self.parents[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # xとyが同じグループに属しているかを判定する
    def same(self, x, y):
        return self.find(x) == self.find(y)

    #--- option ---#

    # xが属する集合の大きさを返す
    def group_size(self, x):
        return self.size[self.find(x)]

    # xが属する集合の要素を返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    # すべての根をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # 木の数を返す
    def group_count(self):
        return len(self.roots())

    # すべての要素を辞書で返す
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


#---usage---

# initialize

n = 10 # node
uf = UnionFind(n)
print(uf.parents) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(uf.rank)
# print(uf.size)

# unionによるグループの併合
uf.union(0, 2) # 要素0と要素2を併合
print(uf.parents) # [0, 1, 0, 3, 4, 5, 6, 7, 8, 9]

print(uf.find(0)) # 0
print(uf.find(2)) # 0
print(uf.same(0, 2)) # true

uf.union(1, 3)
uf.union(4, 5)
uf.union(1, 4)
# 親の要素、parents[5]は1ではなく4になっていることに注意
print(uf.parents) # [0, 1, 0, 1, 1, 4, 6, 7, 8, 9]

# すべての頂点について、その根を求める
print([uf.find(i) for i in uf.parents]) # [0, 1, 0, 1, 1, 1, 6, 7, 8, 9]

# group_size
print([uf.group_size(x) for x in uf.parents]) # [2, 4, 2, 4, 4, 4, 1, 1, 1, 1]