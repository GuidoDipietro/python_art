###########################
# Author: Guido Dipietro  #
# Date: 24/aug/2020		  #
###########################

import cv2
import numpy as np

###### CONSTANTS ######

N_SQUARES = 13
WIN_SCALE = 2
RECT_COLOR = (0,0,255)
RECT_WIDTH = 1
ARC_COLOR = (255,255,255)
ARC_THICKNESS = 2

###### MISC ######

def win_dimensions(n):
	return WIN_SCALE*fibo(n)+1,WIN_SCALE*fibo(n+1)+1 # height, width

def fibo(n): # only > 0
	return fibo(n-2)+fibo(n-1) if n>2 else 1

def get_pts(pt, leapsize, dir_modulo):
	sq_dirs = np.array([[1,1],[-1,1],[-1,-1],[1,-1]]) 	# Direction from point to sq 2nd vertex
	el_dirs = np.array([[1,0],[0,1],[-1,0],[0,-1]])		# Direction from point to arc center
	sq_vertex = tuple(pt+leapsize*sq_dirs[dir_modulo])
	el_center = tuple(pt+leapsize*el_dirs[dir_modulo])

	return sq_vertex, el_center 

###### DRAWING ######

def draw_arc(img, pt, iter_num, squares=False):
	mod = (iter_num - N_SQUARES) % 4 			# Where in the 4-cycle
	leap = fibo(iter_num)*WIN_SCALE				# Sq length
	newpt, el_center = get_pts(pt, leap, mod)	# Sq new vertex
	#angle = [270,0,90,180][mod]					# Arc angle (drawn as an ellipse arc)
	angle = [90, 180, 270, 0][mod]

	cv2.ellipse(img,el_center,(leap,leap),angle, 0, 90, ARC_COLOR, ARC_THICKNESS)
	if squares:
		cv2.rectangle(img, pt, newpt, RECT_COLOR, thickness=RECT_WIDTH)

	return newpt

###### RUN ######

img = np.zeros((*win_dimensions(N_SQUARES),3))
origin = (0,0)

for i in np.arange(N_SQUARES, 1, -1):
	origin = draw_arc(img, origin, i, squares=True)

cv2.imshow("Image", img)
#cv2.imwrite("Fibonacci2020.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()