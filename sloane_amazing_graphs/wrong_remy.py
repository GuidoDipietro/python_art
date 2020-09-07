# Wrong Remy's
# Accidentally created when coding Remy's sequence

# This one seems to be constructed like this:
#	-) Array full of 0s
#	-) Loop from 1 to the array length (i)
#	-) Add 1 to every position (n) to the right that has i AND n != 0

# 6/sep/2020 | Guido Dipietro

import matplotlib.pyplot as plt
import numpy as np

# CONSTS #

COLOR = "#000000"
FACECOLOR = "#000000"
N_POINTS = 5000

# SEQ DEFINITION #

def seq(arr):
	taotry = 0
	for i in range(1,len(arr)):
		for d in range(i,len(arr)):
			if d&i!=0: arr[d]+=1

# SEQ GENERATION #

y = np.zeros(N_POINTS)
seq(y)

# PLOT #

plt.scatter(range(N_POINTS), y, s=1, color=COLOR, facecolor=FACECOLOR)
plt.show()