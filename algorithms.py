# 素数判定 O(n ** 0.5)
def is_prime(n):
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return n != 1 # 1のときは例外

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
			is_print[0] = False
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
