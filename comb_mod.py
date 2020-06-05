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

MAXN = 2 * 10 ** 5 + 10
MOD = 10 ** 9 + 7

make_fact(MAXN, MOD)
print(comb_mod(100, 50, MOD)) # 538992043