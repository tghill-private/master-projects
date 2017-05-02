def fibo(n):
	a=b=1
	while b<n:
		yield b
		a, b = b, a+b


def prime_sieve(n):
	integer_set = set(range(n+1))
	j=1
	while j<=n+1:
		i=1
		while i<=j and (i+j+2*i*j)<=n+1:
			if (i+j+2*i*j) in integer_set:
				integer_set.remove(i+j+2*i*j)
			i+=1
		j+=1
	prime_list = map(lambda num: 2*num + 1,sorted(integer_set))
	return prime_list

def primes(n):
	n = int((n-1)//2)
	for prime in prime_sieve(n):
		yield prime

dict = {index:p for (index,p) in enumerate(primes(10000))}