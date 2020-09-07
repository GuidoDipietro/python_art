# Balanced Ternary
# https://oeis.org/A117966

# 31/aug/2020 | Guido Dipietro

import matplotlib.pyplot as plt

# CONSTS #

POINTS = 19650
COLOR = "#0000b2"

# SEQUENCE DEFINITION #

# This function is not "too Pythonic", but I don't mind; it's short enough and it works
def balanced_ternary(n):
	num, ind = 0, 0
	while n:
		n, r = divmod(n, 3)
		if r==2: r=-1
		num += (r*3**ind)
		ind += 1
	return num

# SEQUENCE GENERATION #

y = []
for i in range(POINTS):
	y.append(balanced_ternary(i))

# PLOT #
plt.scatter(range(POINTS), y, s=1, color=COLOR)
plt.show()
