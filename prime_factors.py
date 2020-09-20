# Ref: https://qiita.com/rsk0315_h4x/items/ff3b542a4468679fb409

# ----- 前処理 ----- #
MAX = 10 ** 6 + 1000
dp = [i for i in range(MAX)]# dp[x]: xを割り切る最小の素数

for x in range(2, MAX):
    if dp[x] < x: continue
    for y in range(x + x, MAX, x):
        if dp[y] == y:
            dp[y] = x

# 試し割りをする必要がなくなる
def prime_factors(n):
    factors = []
    while n > 1:
        factors.append(dp[n])
        n //= dp[n]
    return factors

print(prime_factors(100))
print(prime_factors(101))
print(prime_factors(102))

# ----- 速度 ----- #
from time import time
start = time()
p_factors = [[] for _ in range(MAX)]
p_factors[0] = [0]
p_factors[1] = [1]
for i in range(2, MAX):
    p_factors[i] = prime_factors(i)
elapsed = time() - start
print(elapsed, '[sec]') # 1.22 sec くらい（Jupyter lab でやったら 868 ms ± 80.8 ms）
print(p_factors[:20])