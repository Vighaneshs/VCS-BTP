import os
import numpy as np
import cv2




#shares for 2 out of 2 visual secret sharing problem scheme
shares = [[[[1,1],[0,0]], [[0,0],[1,1]]],  [[[1,0],[1,0]], [[0,1],[0,1]]],  [[[1,0],[0,1]], [[0,1],[1,0]]]]


# Load a color image in grayscale
img = cv2.imread('image1.jpg',cv2.IMREAD_GRAYSCALE)

#converting to binary by setting a threshold 
(thresh, imbw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
new_rows = 2*len(imbw)
new_cols = 2*len(imbw[0])

transparency1 = np.zeros((new_rows, new_cols))
transparency2 = np.zeros((new_rows, new_cols))



#Conversion to 2 transparencies
k = 0
l = 0
for i in range(len(imbw)):
    l = 0
    for j in range(len(imbw[0])):
        randInt1 = int.from_bytes(os.urandom(1), byteorder="big")%3
        randInt2 = int.from_bytes(os.urandom(1), byteorder="big")%2
        if imbw[i][j] == 255:
            transparency1[k][l] = shares[randInt1][randInt2][0][0]
            transparency1[k][l+1] = shares[randInt1][randInt2][0][1]
            transparency1[k+1][l] = shares[randInt1][randInt2][1][0]
            transparency1[k+1][l+1] = shares[randInt1][randInt2][1][1]
            
            transparency2[k][l] = shares[randInt1][randInt2][0][0]
            transparency2[k][l+1] = shares[randInt1][randInt2][0][1]
            transparency2[k+1][l] = shares[randInt1][randInt2][1][0]
            transparency2[k+1][l+1] = shares[randInt1][randInt2][1][1]
            
        elif imbw[i][j] == 0:    
            transparency1[k][l] = shares[randInt1][1^randInt2][0][0]
            transparency1[k][l+1] = shares[randInt1][1^randInt2][0][1]
            transparency1[k+1][l] = shares[randInt1][1^randInt2][1][0]
            transparency1[k+1][l+1] = shares[randInt1][1^randInt2][1][1]
            
            transparency2[k][l] = shares[randInt1][randInt2][0][0]
            transparency2[k][l+1] = shares[randInt1][randInt2][0][1]
            transparency2[k+1][l] = shares[randInt1][randInt2][1][0]
            transparency2[k+1][l+1] = shares[randInt1][randInt2][1][1]
        
        l = l + 2
    k = k + 2
            

decrypted_image =  np.zeros((new_rows, new_cols))

t1 = transparency1.astype(np.int8)
t2 = transparency2.astype(np.int8)

#decrypting image by taking and of 2 transparencies which is equivalent to aligning to transparencies and viewing with human eyes
for i in range(new_rows):
    for j in range(new_cols):
        decrypted_image[i][j] = (t1[i][j]) & (t2[i][j])
       


cv2.imshow('image',imbw)
cv2.imshow('transparency1',transparency1)
cv2.imshow('transparency2',transparency2)
cv2.imshow('decrypted', decrypted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()