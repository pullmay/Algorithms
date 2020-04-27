class UnionFind:
	def __init__(self, n):
		self.n = n
		self.parents = [i for i in range(n)] # parents
		self.rank = [1] * n # height of tree
		self.size = [1] * n # size[i] -> iをrootとするgroupのサイズ

	# 木の根を求める
	def find(self, x):
		if self.parents[x] == x:
			return x
		else:
			self.parents[x] = self.find(self.parents[x])
			return self.parents[x]

	# xとyの属する集合を併合
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
