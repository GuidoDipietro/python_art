# Hofstadter's Sequence
# https://oeis.org/A005185

# a(n) = a(n-a(n-1)) + a(n-a(n-2)), with a(1)=1 and a(2)=1 initial conditions

# 5/sep/2020 | Guido Dipietro

import matplotlib.pyplot as plt
import numpy as np

# CONSTS #
COLOR = "#d4af37"
N_POINTS = 10000

# SEQ DEFINITION #

def a(arr, n): # holds for n>2
	arr[n] = arr[n-arr[n-1]]+arr[n-arr[n-2]]

# SEQ GENERATION #

y = np.zeros(N_POINTS, np.uint32)
y[0],y[1] = 1,1 # initial conditions (just to avoid an "if" statement in a())

for n in range(1,N_POINTS):
	a(y, n)

print(y)

# PLOT #

plt.scatter(range(N_POINTS), y, s=1, color=COLOR)
plt.show()