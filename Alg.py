from bisect import bisect_left, bisect_right
from collections import Counter, deque
import sys
sys.setrecursionlimit(10 ** 7)

def is_power(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n != 1 # 1 のときは例外

# nまでの素数リスト
def prime_list(n):
    primes = set(range(2, n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        primes.difference_update(range(i * 2, n + 1, i))
    return list(primes)

# エラトステネスの篩
# nまでの整数([0,1,...,n])に対して、素数であるかのboolian配列
def prime_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    primes[0], primes[1] = False, False
    return primes

# 区間[a, b)内の素数の個数
def segment_sieve(a, b):
    res = []
    is_prime_small = [True] * (int(b ** 0.5) + 1)
    is_prime = [True] * (b - a)
    for i in range(2, int(b ** 0.5)):
        if is_prime_small[i]:
            j = 2 * i
            while j ** 2 < b:
                is_prime_small[j] = False
                j += i
            j = max(2 * i,((a + i - 1) // i) * i)
            while j < b:
                is_prime[j - a] = False
                j += i
        if a == 1:
            is_prime[0] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            res.append(a + i)
    return res