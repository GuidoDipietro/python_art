# Wisteria
# http://oeis.org/A299741

# 31/aug/2020 | Guido Dipietro

import matplotlib.pyplot as plt
import numpy as np

# CONSTS #

POINTS = 1000
COLOR = "#967bb6"

# SEQUENCE DEFINITION #

def wisterize(n):
	return n - np.prod([int(d) for d in str(n)])

# SEQUENCE GENERATION #
y = []
for i in range(POINTS):
	y.append(wisterize(i))

# PLOT #
plt.scatter(range(POINTS), y, s=3, color=COLOR)
plt.show()