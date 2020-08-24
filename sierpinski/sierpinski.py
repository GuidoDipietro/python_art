# Method:

# Draw a triangle
# Draw a random point within it
# Pick a random vertex of the triangle
# Draw another point midway in between the chosen vertex and the first random point
# Repeat this using the new drawn point as your former "random point"

# 100K points used in all the 4 images

###########################################

import numpy as np
import cv2
import random

###### CONSTANTS ######

T_SIDE = 480
WIN_H = 520
WIN_W = 520
TRIANGLE_COLOR = (0,0,0)
POINT_COLOR = (0,0,255)
POINT_RADIUS = 1
ITERATIONS = 10000

###### MISC ######

def midpoint(A, B):
	return ((A[0]+B[0])//2,(A[1]+B[1])//2)

###### DRAWINGS ######

def draw_triangle(ts, ww, wh, color):
	th = (ts**2 - (ts//2)**2)**(0.5)
	pts = [
		[ww//2 + ts//2, wh - (wh-th)//2],
		[ww//2 - ts//2, wh - (wh-th)//2],
		[ww//2, (wh-th)//2]
	]
	pts = np.array(pts, np.int32)
	cv2.polylines(img,[pts],True,color)

	return pts

def iteration(img, vertices, point):
	pt = random.choice(vertices)
	mp = midpoint(pt, point)
	cv2.circle(img, mp, POINT_RADIUS, POINT_COLOR, -1)

	return mp

###### RUN ######

img = np.zeros((WIN_W, WIN_H, 3), np.uint8)

vertices = draw_triangle(T_SIDE, WIN_W, WIN_H, TRIANGLE_COLOR)
point = (250,250) #change to random within triangle

for i in range(ITERATIONS):
	point = iteration(img, vertices, point)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()