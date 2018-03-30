import random
import primefac
import itertools
import time

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m

def coprime(a, b):
	return egcd(a, b) == 1

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Unused
def encipher(M, n, e):
	e_b = list(map(int, list("{0:b}".format(e))))
	C = 1
	for i in e_b:
		C = C**2 % n
		if (i == 1):
			C = (C * M) % n
	return C

# Unused
def decipher(M, n, d):
	d_b = list(map(int, list("{0:b}".format(d))))
	C = 1
	for i in d_b:
		C = C**2 % n
		if (i == 1):
			C = (C * M) % n
	return C

if __name__ == "__main__":
	i = 10**7
	while i < 10**9:
		# Calculate time required to compute the numbers for enciphering
		nums_start_time = time.time()
		# Calculate p
		p = random.randint(i - 1000, i)
		while not (primefac.isprime(p)):
			p = random.randint(i - 1000, i)

		# Calculate q
		q = random.randint(i - 1000, i)
		while not (primefac.isprime(q)):
			q = random.randint(i - 1000, i)

		# Calculate n and phi(n)
		n = p * q
		phi = (p-1)*(q-1)

		# Calculate d
		d = max(p, q)
		while not primefac.isprime(d):
			d += 1

		# Calculate e
		e = modinv(d, phi)
		nums_stop_time = time.time()

		# Calculate time required to factorize n
		fact_start_time = time.time()
		p = prime_factors(n)
		fact_stop_time = time.time()
                
                file = open("rsa.csv", "a")
		file.write(str(i) + "," + str(nums_stop_time - nums_start_time) + "," + str(fact_stop_time - fact_start_time) + "\n")
                file.close()
		i += 1000000
