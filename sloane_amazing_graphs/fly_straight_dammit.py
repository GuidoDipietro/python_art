# Fly straight, dammit!
# https://oeis.org/A133058

# 31/aug/2020 | Guido Dipietro

import matplotlib.pyplot as plt

# CONSTS #

COLOR = "#b20000"
POINTS = 1200

# SEQUENCE DEFINITION #

def divs(n):
	return set([x for x in range(2,n+1) if n%x==0])

def genner(ind, n):
	div = divs(n) & divs(ind)
	if ind<2: num = 1
	else:
		num = ind+n+1 if div==set() else n//max(div)
	return ind+1, num

# SEQUENCE GENERATION #

y = []
ind, n = 0, 1
for _ in range(POINTS):
	ind, n = genner(ind, n)
	y.append(n)

# PLOT #

plt.scatter(range(POINTS), y, s=1, color=COLOR)
plt.show()