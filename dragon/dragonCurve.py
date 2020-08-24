# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:02:35 2019

@author: dipie
"""

import copy
import cv2
import numpy as np

step = 20
iterations = 7
h,w = 350,400
originx, originy = 150,250
linepx = 3

# list of moves in x,y axes. Start with (1,0) (straight line to right)
moves = [[step,0]]

def rotate(t):
    t[0],t[1] = -1*t[1],t[0]
    return t

def turtleLines(coords,x,y):
    turtleCoords = []
    for i,point in enumerate(coords):
        lineCoords = [(x,y),(x+point[0],y+point[1])]
        x,y = x+point[0],y+point[1]
        turtleCoords.append(lineCoords)
    return turtleCoords

for i in range(0,iterations):
    copia = list(map(rotate,copy.deepcopy(moves)[::-1]))
    moves += copia
    
turtleCoords = turtleLines(moves,originx,originy)

img = np.zeros((h,w,3), np.uint8)

for each in turtleCoords:
    cv2.line(img,each[0],each[1],(51,170,18),linepx)
    
cv2.imshow('Dragon',img)
#cv2.imwrite("Dragon5.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
