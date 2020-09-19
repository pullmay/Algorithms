from bisect import bisect_left, bisect_right
from collections import Counter, deque
import sys
sys.setrecursionlimit(10 ** 7)

def is_prime(n):
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

# 1 から n までの約数の個数
def count_divisors(n):
    cnt_div = [0] * (n + 1)
    for x in range(1, n + 1):
        for y in range(x, n + 1):
            cnt_div[y] += 1
    return cnt_div

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

# 約数の列挙 O(n ** 0.5)
def divisible(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            # nが約数dをもつとき、n/dも約数
            if i != n // i:
                divisors.append(n // i)
    # divisors.sort()
    return divisors

# 素因数分解 O(n ** 0.5)
def prime_factor(n):
    factor = []
    for i in range(2, int(n ** 0.5) + 1):
        while (n % i == 0):
            factor.append(i)
            n //= i
    if n != 1:
        factor.append(n)
    return factor

# 約数の個数
def divisible_count(n):
    divisors = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors += 1
            if i != n // i:
                divisors += 1
    return divisors

# 約数の総和
def divisible_sum(n):
    divisors = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors += i
            if i != n // i:
                divisors += n // i
    return divisors

# 約数の総積
def divisible_product(n):
    divisors = 1
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors *= i
            if i != n // i:
                divisors *= n // i
    return divisors

# 互いに素なものの総数
# Euler's phi function
def Euler_phi(n):
    divisors = prime_factor(n)
    divisors = set(divisors)
    res = n
    for factor in divisors:
        res = res * (factor - 1) // factor
    return res

# squareかどうか判定
def is_square(n):
    return n >= 0 and n ** 0.5 % 1 == 0

# LIS
def LIS(arr):
    dp = [arr[0]]
    for i in arr[1:]:
        if dp[-1] < i:
            dp.append(i)
        else:
            dp[bisect_left(dp, i)] = i
    return len(dp)

# nのk進数表現(k=-2)
# リストで返るので、文字列として出力したい場合は
# print(*Convert_To_Another_Base(n), sep='')とする
def Convert_To_Another_Base(n):
    res = []
    while (n != 0):
        r = n % 2
        if r < 0: # 剰余が負になった場合の処理
            r += 2
        n = (n - r) // (-2)
        res.append(r)
    if res == []:
        res.append(0)
    res = res[::-1] # 逆順になっているので反転させる
    return res

# 繰り返し二乗法
# a^n mod p を高速に計算
# 実際はpow(a, n, p)でよい
def modpow(a, n, mod):
    res = 1
    while n > 0:
        # if n % 2:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n = n >> 1
    return res

# 最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)

# Counter
# 2つのリストの共通要素の個数
def joint(lst1, lst2):
    d1 = dict(Counter(lst1))
    d2 = dict(Counter(lst2))
    cnt = 0
    for k in d1:
        if k in d2:
            cnt += min(d1[k], d2[k])
    return cnt

# 累積和
def cumsum(lst):
    res = [0]
    for v in lst:
        res.append(res[-1] + v)
    return res

# fib
# メモ化再帰
def fib_memo(n):
    dp = [-1] * (n + 1)

    def fib(n):
        if n == 0 or n == 1:
            return 1
        if dp[n] != -1:
            return dp[n]
        dp[n] = fib(n - 1) + fib(n - 2)
        return dp[n]
    return fib(n)

# fib
# loop
def fib_loop(n):
    F = [-1] * (n + 1)
    F[0], F[1] = 1, 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]

# fib 配列
def fib_array(n):
    F = [-1] * (n + 1)
    F[0], F[1] = 1, 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F

# 選択ソート
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minj = i
        for j in range(i, n):
            if arr[j] < arr[minj]:
                minj = j
        arr[i], arr[minj] = arr[minj], arr[i]
    return arr

# 挿入ソート
def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        v = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > v:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = v
    return arr

# バブルソート
def bubble_sort(arr):
    n = len(arr)
    flag = True
    i = 0
    while flag:
        flag = False
        for j in range(n - 1, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                flag = True
        i += 1
    return arr
    
# マージソート
def merge_sort(arr, left, right):
    # merge_sort(lst, 0, len(lst))
    if right - left == 1:
        return 
    mid = left + (right - left) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)
    a = [arr[i] for i in range(left, mid)] \
        + [arr[i] for i in range(right - 1, mid - 1, -1)]
    iterator_left = 0
    iterator_right = len(a) - 1
    for i in range(left, right):
        if a[iterator_left] <= a[iterator_right]:
            arr[i] = a[iterator_left]
            iterator_left += 1
        else:
            arr[i] = a[iterator_right]
            iterator_right -= 1

# 線型探索 O(N)
def linearSearch(A, key):
    n = len(A) - 1
    i = 0
    A[n] = key # 番兵
    while (A[i] != key):
        i += 1
    return i != n

# 二部探索 O(logN)
def binarySearch(A, key):
    left, right = 0, len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] == key:
            return True
        elif key < A[mid]:
            right = mid
        else:
            left = mid + 1
    return False

# Partition
def partiton(A, p, r):
    # partiton(A, 0, len(A)-1)
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

# Quick Sort O(NlogN)
def quick_sort(A, p, r):
    #  quick_sort(A, 0, len(A)-1)
    if p < r:
        q = partiton(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

# fact mod
def factorial_mod(n, mod):
    a = 1
    for i in range(1, n + 1):
        a *= i
        a %= mod
    return a

# combination mod
def comb_mod(n, k, mod):
    if k > n:
        return 0
    fact_n = factorial_mod(n, mod)
    fact_k = factorial_mod(k, mod)
    fact_n_k = factorial_mod(n - k, mod)
    return (fact_n * pow(fact_k, mod - 2, mod) * pow(fact_n_k, mod - 2, mod)) % mod

# 迷路探索，queue による幅優先探索
# 入力に壁あり（壁なしにも対応）
def bfs():
    H, W = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    field = [list(input()) for _ in range(H)]

    sy, sx, gy, gx = sy - 1, sx - 1, gy - 1, gx - 1

    dyx = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    q.append((sy, sx, 0))

    while q:
        cy, cx, ct = q.popleft()
        for dy, dx in dyx:
            # 移動
            ny, nx = cy + dy, cx + dx
            # 範囲外に行ってしまった場合
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
            # ゴールに辿り着いた場合
            if (ny, nx) == (gy, gx):
                return ct + 1
            # 壁の場合
            if field[ny][nx] == '#':
                continue
            # queue に追加
            q.append((ny, nx, ct + 1))
            field[ny][nx] = '#'

# しゃくとり法
def shakutori(n, k, a:list):
    res = n + 1
    right, subsum = 0, 0
    for left in range(n):
        while right < n and subsum < k:
            subsum += a[right]
            right += 1
        if subsum < k:
            break
        res = min(res, right - left)
        subsum -= a[left]

        if res > n: # 解なし
            res = 0

    return res

# ランレングス圧縮
def rle(s):
    tmp, cnt, res = s[0], 1, ''
    for i in range(1, len(s)):
        if tmp == s[i]:
            cnt += 1
        else:
            res += tmp + str(cnt)
            tmp = s[i]
            cnt = 1
    res += tmp + str(cnt)
    return res