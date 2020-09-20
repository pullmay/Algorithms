# \binom{n}{k} mod p の値を前処理 O(N) の下で O(1) で求める

def comb_mod(n, k, p):
    if k < 0 or n < k:
        return 0
    k = min(k, n - k)
    return fact[n] * factinv[k] * factinv[n - k] % p

# 前処理
def make_fact(n, p):
    for k in range(2, n + 1):
        fact.append((fact[-1] * k) % p)
        inv.append((-inv[p % k]) * (p // k) % p)
        factinv.append((factinv[-1] * inv[-1]) % p)
    return

fact = [1, 1]
inv = [0, 1]
factinv = [1, 1]

MAXN = 2 * 10 ** 5 + 10 # 必要な数を設定
MOD = 10 ** 9 + 7 # 剰余

make_fact(MAXN, MOD) # O(N)
print(comb_mod(100, 50, MOD)) # 538992043


# ----- 2020/9/20 ----- #

MOD = 10 ** 9 + 7
N = 10 ** 5

fact = [1] * (N + 1)
inv_fact = [1] * (N + 1)

for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact[N] = pow(fact[N], MOD - 2, MOD)
for i in range(N, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % MOD

def perm(n, k):
    return fact[n] * inv_fact[n - k] % MOD

def comb(n, k):
    return fact[n] * inv_fact[k] * inv_fact[n - k] % MOD

print(fact[:20])
print(inv_fact[:20])