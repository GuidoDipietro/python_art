# -*- coding: utf-8 -*-
"""
Created on Sun May 12 19:55:44 2019

@author: dipie
"""

import cv2
import numpy as np

def firstNFibonacci(n):
    out = []
    a,b = 0,1
    while(n>0):
        out.append(b)
        a,b = b,a+b
        n = n-1
    return out[::-1]

def returnCoords(l,x,y):
    original = [x for x in l]
    
    l = l[3:] #Now we can go
    a = -1
    original.pop(0)
    yield [x,y],original[0]
    while(a<len(l)-1):
        if a%4==0:
            original.pop(0)
            a+=1
            x = x-l[a]
            yield [x,y],original[0]
        elif a%4==1:
            original.pop(0)
            a+=1
            y = y-l[a]
            yield [x,y],original[0]
        elif a%4==2:
            original.pop(0)
            a+=1
            x = x+l[a]
            yield [x,y],original[0]
        elif a%4==3:
            original.pop(0)
            a+=1
            y = y+l[a]
            yield [x,y],original[0]

depth = 17
numbers = firstNFibonacci(depth)
h,w = numbers[1],numbers[0]
centers = returnCoords(numbers,w-h,0)

img = np.zeros((h,w), np.uint8)

angle = 270
for each in centers:
    angle = (angle+90)%360
    centerx,centery = each[0][0],each[0][1]
    radius = each[1]
    print(angle,centerx,centery,radius,sep=' ')
    cv2.ellipse(img,(centerx,centery),(radius,radius),
                angle, 0, 90, (255,0,0),1)

#cv2.ellipse(img,(233,0),(377,377),0,0,90,(255,255,0),3)
#cv2.ellipse(img,(233,144),(233,233),90,0,90,(255,255,0),3)

cv2.imshow('narnia',img)
#cv2.imwrite("narnia.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()