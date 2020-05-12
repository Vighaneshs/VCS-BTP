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

  

#Making R G B transparencies
t2 = np.zeros((2*len(img), 2*len(img[0]), 3), dtype = 'uint8')
t1 = np.zeros((2*len(img), 2*len(img[0]), 3), dtype = 'uint8')


k = 0 
l = 0
for i in range(len(img)):
    l = 0
    for j in range(len(img[0])):
        if ri[i][j][2] == 0:
            t1[k][l][2] = 255
            t1[k][l+1][2] = 0        
            t1[k+1][l][2] = 0
            t1[k+1][l+1][2] = 255

            t2[k][l][2] = 255
            t2[k][l+1][2] = 0        
            t2[k+1][l][2] = 0
            t2[k+1][l+1][2] = 255
        elif ri[i][j][2] == 255:
            t1[k][l][2] = 255
            t1[k][l+1][2] = 0        
            t1[k+1][l][2] = 0
            t1[k+1][l+1][2] = 255

            t2[k][l][2] = 0
            t2[k][l+1][2] = 255        
            t2[k+1][l][2] = 255
            t2[k+1][l+1][2] = 0
        
        if gi[i][j][1] == 0:
            t1[k][l][1] = 255
            t1[k][l+1][1] = 0        
            t1[k+1][l][1] = 0
            t1[k+1][l+1][1] = 255

            t2[k][l][1] = 255
            t2[k][l+1][1] = 0        
            t2[k+1][l][1] = 0
            t2[k+1][l+1][1] = 255
        elif gi[i][j][1] == 255:
            t1[k][l][1] = 255
            t1[k][l+1][1] = 0        
            t1[k+1][l][1] = 0
            t1[k+1][l+1][1] = 255

            t2[k][l][1] = 0
            t2[k][l+1][1] = 255        
            t2[k+1][l][1] = 255
            t2[k+1][l+1][1] = 0
        
        if bi[i][j][0] == 0:
            t1[k][l][0] = 255
            t1[k][l+1][0] = 0        
            t1[k+1][l][0] = 0
            t1[k+1][l+1][0] = 255

            t2[k][l][0] = 255
            t2[k][l+1][0] = 0        
            t2[k+1][l][0] = 0
            t2[k+1][l+1][0] = 255
        elif bi[i][j][0] == 255:
            t1[k][l][0] = 255
            t1[k][l+1][0] = 0        
            t1[k+1][l][0] = 0
            t1[k+1][l+1][0] = 255

            t2[k][l][0] = 0
            t2[k][l+1][0] = 255        
            t2[k+1][l][0] = 255
            t2[k+1][l+1][0] = 0
        
       

        l = l + 2
    k = k + 2


#Decrypting the image using the R G B  transparencies
dimg = t1 + t2



cv2.imshow('Original Image', oimg)
cv2.imshow('Share1', t1)
cv2.imshow('Share2', t2)
cv2.imshow('Decrypted image', dimg)


cv2.waitKey(0)
cv2.destroyAllWindows()