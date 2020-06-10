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