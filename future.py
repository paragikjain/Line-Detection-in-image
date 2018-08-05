# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 19:56:58 2018

@author: paragikjain
"""

import cv2
import numpy as np
img=cv2.imread("hand.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,75,150)
lines=cv2.HoughLinesP(edges,1,np.pi/180,50)
for line in  lines:
 x1,y1,x2,y2=line[0]
 
cv2.imshow("Edges",edges)
cv2.imshow("Image",img)
cv2.waitKey(0)