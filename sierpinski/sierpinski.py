###########################
# Author: Guido Dipietro  #
# Date: 23/aug/2020		  #
###########################

# Method:

# 1)Draw a triangle
# 2) Pick a random point P anywhere
# 3) Pick a random vertex V of the triangle
# 4) Draw the midpoint P-V
# 5) Repeat from 2) using the new drawn point as P

###########################################

import numpy as np
import cv2
import random

###### CONSTANTS ######

T_SIDE = 480
WIN_H = 520
WIN_W = 520
P_COLOR = (0,0,255)
DOT_COLOR = (204, 255, 0)
DOT_RADIUS = 1
ITERATIONS = 10000

###### MISC ######

def midpoint(A, B):
	return ((A[0]+B[0])//2,(A[1]+B[1])//2)

def triangle_vertices(ts, ww, wh):
	th = int((ts**2 - (ts//2)**2)**(0.5))	# triangle height (vector norm)
	return [
		[ww//2 + ts//2, wh - (wh-th)//2], 	# base rightmost
		[ww//2 - ts//2, wh - (wh-th)//2], 	# base leftmost
		[ww//2, (wh-th)//2] 				# peak
	]

###### DRAWING ######

def iteration(img, vertices, point):
	pt = random.choice(vertices)
	mp = midpoint(pt, point)
	cv2.circle(img, mp, DOT_RADIUS, DOT_COLOR, -1)

	return mp

###### RUN ######

img = np.zeros((WIN_W, WIN_H, 3), np.uint8)					# blank

vertices = triangle_vertices(T_SIDE, WIN_W, WIN_H)
point = (random.randint(0,WIN_W), random.randint(0,WIN_H))	# starting point

cv2.circle(img, point, 5, P_COLOR, -1)

for i in range(ITERATIONS):
	point = iteration(img, vertices, point)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()