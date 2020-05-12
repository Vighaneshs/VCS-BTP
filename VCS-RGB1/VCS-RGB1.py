import os
import numpy as np
import cv2




#Default scheme BGR

# Loading a color image
img = cv2.imread('image1.jpg', 1)


#Decomposing into 3
bi = img.copy() 
bi[:,:,1] = 0
bi[:,:,2] = 0

gi = img.copy() 
gi[:,:,0] = 0
gi[:,:,2] = 0

ri = img.copy() 
ri[:,:,0] = 0
ri[:,:,1] = 0


#Modifying image for implementation
for i in range(len(img)):
    for j in range(len(img[0])):
        if gi[i][j][1] >=128:
            gi[i][j][1] = 255
        else:
            gi[i][j][1] = 0
for i in range(len(img)):
    for j in range(len(img[0])):
        if bi[i][j][0] >=128:
            bi[i][j][0] = 255
        else:
            bi[i][j][0] = 0
for i in range(len(img)):
    for j in range(len(img[0])):
        if ri[i][j][2] >=128:
            ri[i][j][2] = 255
        else:
            ri[i][j][2] = 0

oimg = np.zeros((len(img),len(img[0]), 3), dtype = 'uint8')

oimg[:,:,0] = bi[:,:,0]
oimg[:,:,1] = gi[:,:,1]
oimg[:,:,2] = ri[:,:,2]




#Creating black and white mask
bwmask = np.zeros((2*len(img), 2*len(img[0]), 3), dtype = 'uint8')

for i in range(2*len(img)):
    for j in range(2*len(img[0])):
        if (i + j)%2 == 0:
            bwmask[i][j][0] = 0
            bwmask[i][j][1] = 0
            bwmask[i][j][2] = 0
        else:
            bwmask[i][j][0] = 255
            bwmask[i][j][1] = 255
            bwmask[i][j][2] = 255
         

#Making R G B transparencies
redtransparencies = np.zeros((2*len(img), 2*len(img[0]), 3), dtype = 'uint8')
greentransparencies = np.zeros((2*len(img), 2*len(img[0]), 3), dtype = 'uint8')
bluetransparencies = np.zeros((2*len(img), 2*len(img[0]), 3), dtype = 'uint8')

k = 0 
l = 0
for i in range(len(img)):
    l = 0
    for j in range(len(img[0])):
        if ri[i][j][2] == 255:
            redtransparencies[k][l][2] = 255
            redtransparencies[k][l+1][2] = 0        
            redtransparencies[k+1][l][2] = 0
            redtransparencies[k+1][l+1][2] = 255
        elif ri[i][j][2] == 0:
            redtransparencies[k][l][2] = 0
            redtransparencies[k][l+1][2] = 255        
            redtransparencies[k+1][l][2] = 255
            redtransparencies[k+1][l+1][2] = 0
        
        if gi[i][j][1] == 255:
            greentransparencies[k][l][1] = 255
            greentransparencies[k][l+1][1] = 0        
            greentransparencies[k+1][l][1] = 0
            greentransparencies[k+1][l+1][1] = 255
        elif gi[i][j][1] == 0:
            greentransparencies[k][l][1] = 0
            greentransparencies[k][l+1][1] = 255        
            greentransparencies[k+1][l][1] = 255
            greentransparencies[k+1][l+1][1] = 0

        if bi[i][j][0] == 255:
            bluetransparencies[k][l][0] = 255
            bluetransparencies[k][l+1][0] = 0        
            bluetransparencies[k+1][l][0] = 0
            bluetransparencies[k+1][l+1][0] = 255
        elif bi[i][j][0] == 0:
            bluetransparencies[k][l][0] = 0
            bluetransparencies[k][l+1][0] = 255        
            bluetransparencies[k+1][l][0] = 255
            bluetransparencies[k+1][l+1][0] = 0

        l = l + 2
    k = k + 2


#Decrypting the image using the R G B  transparencies
dimg = np.zeros((2*len(img), 2*len(img[0]), 3), dtype = 'uint8')
dimg[:,:,0] = bluetransparencies[:,:,0]
dimg[:,:,1] = greentransparencies[:,:,1]
dimg[:,:,2] = redtransparencies[:,:,2]

#Adding mask at the end
dimgf = dimg + bwmask

cv2.imshow('Original Image', oimg)
cv2.imshow('mask', bwmask)
cv2.imshow('Red transparencies', redtransparencies)
cv2.imshow('Green transparencies', greentransparencies)
cv2.imshow('Blue transparencies', bluetransparencies)
cv2.imshow('Decrypted image without BW MASK', dimg)
cv2.imshow('Decrypted image', dimgf)


cv2.waitKey(0)
cv2.destroyAllWindows()