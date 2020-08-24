###########################
# Author: Guido Dipietro  #
# Date: 3/mar/2020        #
###########################

import numpy as np
import cv2
import random
import math

###### GENERATING THE BOARD ######

board_size = 61
center_cell = (board_size//2)
cell_width = 10
board = np.zeros([board_size,board_size], np.int32)

# array that looks like 1,1,2,2,3,3,4,4,5,5,...
# try making a spiral around a grid's center and count the leap size
leaps = np.array([(x,x) for x in range(1,board_size+1)], np.int32)
leaps = np.resize(leaps,leaps.size)
leaps = leaps[:-1]

# spiral turns
direction = np.array([[0,1],[-1,0],[0,-1],[1,0]])

# steering (where to move in each step)
steering = np.zeros([sum(leaps),2], np.int32)
count = 0
for i in range(len(leaps)):
	for times in range(leaps[i]):
		steering[count] = direction[i%4]
		count += 1

# tiling
pos = (center_cell,center_cell) # we begin in the center
count = 1
for turn in steering:
	board[tuple(pos)] = count
	count += 1
	pos += turn

# checking neighbors
def check_nbros(pos, board, limit):
	nbors = np.array([[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]) #relative position of nbors
	nbors_pos = np.tile(pos, (8,1)) #repeat pos 8 times
	nbors_pos = nbors_pos + nbors #move each pos to where the nbor is
	nbors_pos = np.array([x for x in nbors_pos if (x[0]>=0 and x[1]>=0 and x[0]<=limit-1 and x[1]<=limit-1)]) #delete overflow
	#I don't think this method of removing unwanted data is efficient at all, but I'm not sure how to use masking here
	nbors_pos = np.array([x for x in nbors_pos if board[tuple(x)]!=limit**2+1]) #another not efficient thing
	nbors_values = np.array([board[tuple(x)] for x in nbors_pos]) #take the numbers

	if len(nbors_pos>0):
		return nbors_pos[np.argmin(nbors_values)]
	else:
		return pos

# calculating path
pos = (center_cell,center_cell) #resetting pos
path = np.zeros([board_size**2,2],np.uint32)
for i in range(board_size**2):
	path[i] = pos
	board[tuple(pos)] = board_size**2+1
	pos = check_nbros(pos, board, board_size)

###### ACTUAL DRAWING ######
img = np.zeros((board_size*cell_width,board_size*cell_width,3), np.uint8) #black image

path = path*cell_width
color = [0,255,0]
for n,coord in enumerate(path[:-1]):
	#color = tuple([random.randint(0,255) for x in range(3)])
	if(n%10 == 0):
		color[1] -= 1
	if(n%5 ==0):
		color[2] += 2
	img = cv2.line(img, tuple(coord), tuple(path[n+1]), color, 2)

cv2.imshow("Knight",img)
#cv2.imwrite("horse1427.png",img)
cv2.waitKey()
print(board)
