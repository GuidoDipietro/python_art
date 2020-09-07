# Fly straight, dammit!
# https://oeis.org/A133058

# 31/aug/2020 | Guido Dipietro

import matplotlib.pyplot as plt

# CONSTS #

POINTS = 1200
COLOR = "#b20000"

# MISC #

def divs(n):
	return set([x for x in range(2,n+1) if n%x==0])

# GENNER #

def genner(ind, n):
	div = divs(n) & divs(ind)
	if ind<2: num = 1
	else:
		num = ind+n+1 if div==set() else n//max(div)
	return ind+1, num
		
# PLOT #

y = []
ind, n = 0, 1
for _ in range(POINTS):
	ind, n = genner(ind, n)
	y.append(n)

plt.scatter(range(POINTS), y, s=1, color=COLOR)
plt.show()