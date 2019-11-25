import cv2
import numpy as np
import math


# load image with alpha channel
img = cv2.imread('floorWatermark.jpg')

# define desired brightness and contrast change values    
bri = 20
con = -40

# compute slope and intercept   
diffcon = (100 - con)
if diffcon <= 0.1: con=99.9

arg = math.pi * (((con * con) / 20000) + (3 * con / 200)) / 4
slope = 1 + (math.sin(arg) / math.cos(arg))
if slope < 0: slope=0

pivot = (100 - bri) / 200
intcpbri = bri / 100
intcpcon = pivot * (1 - slope)
intercept = (intcpbri + intcpcon)

# print slope and intercept
print(slope, intercept)

# apply slope and intercept
img = img/255.0
out = slope * img + intercept
out[out>1] = 1
out[out<0] = 0

# display IN and OUT images
cv2.imshow('IN', img)
cv2.imshow('OUT', out)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save output image
out = 255.0 * out
out = out.astype(int)
cv2.imwrite('floorWatermark.jpg', out)