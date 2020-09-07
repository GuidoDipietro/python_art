# Remy's Sequence
# https://oeis.org/A279125

# 6/sep/2020 | Guido Dipietro

import matplotlib.pyplot as plt
import numpy as np

# CONSTS #

COLOR = "#FFFFFF"
FACECOLOR = "#000000"
N_POINTS = 3000

# SEQ DEFINITION #

def seq(arr, n):
	# I'll find all numbers where the index has an "overlapping" bit (x AND n != 0)
	people = arr[[x for x in range(1,n) if x&n!=0]]

	# Now find the smallest number that doesn't belong to that set
	taotry = 0 # Start with this
	while taotry in people:
		taotry+=1

	# The sequence is defined to have that as the number for index n
	arr[n] = taotry

# SEQ GENERATION #

y = np.zeros(N_POINTS)
for n in range(1,N_POINTS):
	seq(y,n)

# PLOT #

fig, ax = plt.subplots(nrows=1, ncols=1)
plt.scatter(range(N_POINTS), y, s=1, color=COLOR)
ax.set_facecolor(FACECOLOR) # using this to make the "night sky"

plt.show()