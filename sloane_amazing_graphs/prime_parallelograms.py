# Prime parallelograms
# https://oeis.org/A265326

# 31/aug/2020 | Guido Dipietro

import matplotlib.pyplot as plt

# CONSTANTS #

N_PRIMES = 2**15
COLOR = "#008000"

# SEQUENCE DEFINITION #

def primes(max):
	def prime(n):
		return all([n%d!=0 for d in range(2,int(n**0.5))])
	return [2] + [p for p in range(max) if prime(p)]

def seq(n):
	return n - int(bin(n)[-1:1:-1], 2)

# SEQUENCE GENERATION #

ps = primes(N_PRIMES)
y = [seq(n) for n in ps]

plt.scatter(ps, y, s=1, color=COLOR)
plt.show()