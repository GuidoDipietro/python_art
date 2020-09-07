# Stern's Sequence
# https://oeis.org/A002487

# 5/sep/2020 | Guido Dipietro, image using Indranil Ghosh's generator

import matplotlib.pyplot as plt
import numpy as np

# CONSTS #

ROWS = 1000 # N of points = 2^(ROWS-1) + ROWS - 2
COLOR = "#b20000"

# SEQ DEFINITION #
# I'll use the definition as given by Sloane on the video, and constructing it exactly like that

def next_row(row):
	arr = np.empty((len(row)*2 - 1))
	sums = [x+y for x,y in zip(row,row[1:])]
	arr[0::2] = row
	arr[1::2] = sums

	return arr

# SEQ GENERATION #
# (there is a one-liner that generates it using a mathematical property of the sequence)
# def a(n): return n if n<2 else a(n/2) if n%2==0 else a((n - 1)/2) + a((n + 1)/2)
# I used that one to generate the image because it is way, way faster.
# Function by Indranil Ghosh

y = []
for i in range(16000):
	y.append(int(a(i)))

# y = [[1,1]]
# for _ in range(ROWS):
# 	y.append(next_row(y[-1]))
# y = [i for i in x for x in y]

# PLOT #
#plt.scatter(range(16000), y, s=1, color=COLOR)
plt.scatter(range(2**(ROWS-1)+ROWS-2), y, size=1, color=COLOR)
plt.show()