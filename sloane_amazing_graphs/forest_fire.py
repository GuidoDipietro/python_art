# Forest Fire
# http://oeis.org/A229037

# 31/aug/2020 | Chai Wah Wu's generator listed in OEIS (my program was too slow!)

import matplotlib.pyplot as plt

# CONSTS #

POINTS = 100000 # this took a long while to compute, try a lower number perhaps!
COLOR = "#000000"

# SEQUENCE DEFINITION # (from Chai Wah Wu)

y = []
for n in range(POINTS):
	i, j, b = 1, 1, set()
	while n-2*i >= 0:
		b.add(2*y[n-i]-y[n-2*i])
		i += 1
	while j in b:
		b.remove(j)
		j += 1
	y.append(j)

# PLOT #
plt.scatter(range(POINTS), y, s=1, color=COLOR)
plt.show()