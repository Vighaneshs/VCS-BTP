import os
import numpy as np
import cv2
import itertools



#For black
slist1 = [255,255,0,0]
slist2 = [0,0,0,255]
slist3 = [255,0,255,0]
slist4 = [0,255,255,0]

#For white
slist5 = [255,255,0,0]
slist6 = [255,0,0,0]
slist7 = [255,0,255,0]
slist8 = [255,0,0,255]


pslist1 = itertools.permutations(slist1)
pslist1 = list(pslist1)


pslist2 = itertools.permutations(slist2)
pslist2 = list(pslist2)


pslist3 = itertools.permutations(slist3)
pslist3 = list(pslist3)


pslist4 = itertools.permutations(slist4)
pslist4 = list(pslist4)


pslist5 = itertools.permutations(slist5)
pslist5 = list(pslist5)


pslist6 = itertools.permutations(slist6)
pslist6 = list(pslist6)


pslist7 = itertools.permutations(slist7)
pslist7 = list(pslist7)


pslist8 = itertools.permutations(slist8)
pslist8 = list(pslist8)






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
t3 = np.zeros((2*len(img), 2*len(img[0]), 3), dtype = 'uint8')
t4 = np.zeros((2*len(img), 2*len(img[0]), 3), dtype = 'uint8')


k = 0 
l = 0
for i in range(len(img)):
    l = 0
    for j in range(len(img[0])):
        rint = int.from_bytes(os.urandom(1), byteorder="big")%len(pslist5)
        rint1 = int.from_bytes(os.urandom(1), byteorder="big")%len(pslist1)

        if ri[i][j][2] == 0:
            t1[k][l][2] = pslist5[rint][0]
            t1[k][l+1][2] = pslist5[rint][1]        
            t1[k+1][l][2] = pslist5[rint][2]
            t1[k+1][l+1][2] = pslist5[rint][3]

            t2[k][l][2] = pslist6[rint][0]
            t2[k][l+1][2] = pslist6[rint][1]        
            t2[k+1][l][2] = pslist6[rint][2]
            t2[k+1][l+1][2] = pslist6[rint][3]

            t3[k][l][2] = pslist7[rint][0]
            t3[k][l+1][2] = pslist7[rint][1]        
            t3[k+1][l][2] = pslist7[rint][2]
            t3[k+1][l+1][2] = pslist7[rint][3]

            t4[k][l][2] = pslist8[rint][0]
            t4[k][l+1][2] = pslist8[rint][1]        
            t4[k+1][l][2] = pslist8[rint][2]
            t4[k+1][l+1][2] = pslist8[rint][3]


        elif ri[i][j][2] == 255:
            t1[k][l][2] = pslist1[rint][0]
            t1[k][l+1][2] = pslist1[rint][1]        
            t1[k+1][l][2] = pslist1[rint][2]
            t1[k+1][l+1][2] = pslist1[rint][3]

            t2[k][l][2] = pslist2[rint][0]
            t2[k][l+1][2] = pslist2[rint][1]        
            t2[k+1][l][2] = pslist2[rint][2]
            t2[k+1][l+1][2] = pslist2[rint][3]

            t3[k][l][2] = pslist3[rint][0]
            t3[k][l+1][2] = pslist3[rint][1]        
            t3[k+1][l][2] = pslist3[rint][2]
            t3[k+1][l+1][2] = pslist3[rint][3]

            t4[k][l][2] = pslist4[rint][0]
            t4[k][l+1][2] = pslist4[rint][1]        
            t4[k+1][l][2] = pslist4[rint][2]
            t4[k+1][l+1][2] = pslist4[rint][3]




        
        if gi[i][j][1] == 0:
            t1[k][l][1] = pslist5[rint][0]
            t1[k][l+1][1] = pslist5[rint][1]        
            t1[k+1][l][1] = pslist5[rint][2]
            t1[k+1][l+1][1] = pslist5[rint][3]

            t2[k][l][1] = pslist6[rint][0]
            t2[k][l+1][1] = pslist6[rint][1]        
            t2[k+1][l][1] = pslist6[rint][2]
            t2[k+1][l+1][1] = pslist6[rint][3]

            t3[k][l][1] = pslist7[rint][0]
            t3[k][l+1][1] = pslist7[rint][1]        
            t3[k+1][l][1] = pslist7[rint][2]
            t3[k+1][l+1][1] = pslist7[rint][3]

            t4[k][l][1] = pslist8[rint][0]
            t4[k][l+1][1] = pslist8[rint][1]        
            t4[k+1][l][1] = pslist8[rint][2]
            t4[k+1][l+1][1] = pslist8[rint][3]


        elif gi[i][j][1] == 255:
            t1[k][l][1] = pslist1[rint][0]
            t1[k][l+1][1] = pslist1[rint][1]        
            t1[k+1][l][1] = pslist1[rint][2]
            t1[k+1][l+1][1] = pslist1[rint][3]

            t2[k][l][1] = pslist2[rint][0]
            t2[k][l+1][1] = pslist2[rint][1]        
            t2[k+1][l][1] = pslist2[rint][2]
            t2[k+1][l+1][1] = pslist2[rint][3]

            t3[k][l][1] = pslist3[rint][0]
            t3[k][l+1][1] = pslist3[rint][1]        
            t3[k+1][l][1] = pslist3[rint][2]
            t3[k+1][l+1][1] = pslist3[rint][3]

            t4[k][l][1] = pslist4[rint][0]
            t4[k][l+1][1] = pslist4[rint][1]        
            t4[k+1][l][1] = pslist4[rint][2]
            t4[k+1][l+1][1] = pslist4[rint][3]
        




        if bi[i][j][0] == 0:
            t1[k][l][0] = pslist5[rint][0]
            t1[k][l+1][0] = pslist5[rint][1]        
            t1[k+1][l][0] = pslist5[rint][2]
            t1[k+1][l+1][0] = pslist5[rint][3]

            t2[k][l][0] = pslist6[rint][0]
            t2[k][l+1][0] = pslist6[rint][1]        
            t2[k+1][l][0] = pslist6[rint][2]
            t2[k+1][l+1][0] = pslist6[rint][3]

            t3[k][l][0] = pslist7[rint][0]
            t3[k][l+1][0] = pslist7[rint][1]        
            t3[k+1][l][0] = pslist7[rint][2]
            t3[k+1][l+1][0] = pslist7[rint][3]

            t4[k][l][0] = pslist8[rint][0]
            t4[k][l+1][0] = pslist8[rint][1]        
            t4[k+1][l][0] = pslist8[rint][2]
            t4[k+1][l+1][0] = pslist8[rint][3]


        elif bi[i][j][0] == 255:
            t1[k][l][0] = pslist1[rint][0]
            t1[k][l+1][0] = pslist1[rint][1]        
            t1[k+1][l][0] = pslist1[rint][2]
            t1[k+1][l+1][0] = pslist1[rint][3]

            t2[k][l][0] = pslist2[rint][0]
            t2[k][l+1][0] = pslist2[rint][1]        
            t2[k+1][l][0] = pslist2[rint][2]
            t2[k+1][l+1][0] = pslist2[rint][3]

            t3[k][l][0] = pslist3[rint][0]
            t3[k][l+1][0] = pslist3[rint][1]        
            t3[k+1][l][0] = pslist3[rint][2]
            t3[k+1][l+1][0] = pslist3[rint][3]

            t4[k][l][0] = pslist4[rint][0]
            t4[k][l+1][0] = pslist4[rint][1]        
            t4[k+1][l][0] = pslist4[rint][2]
            t4[k+1][l+1][0] = pslist4[rint][3]
        
       

        l = l + 2
    k = k + 2


#Decrypting the image using the R G B  transparencies
dimg12 = t1 + t2
dimg23 = t2 + t3
dimg24 = t2 + t4
dimg134 = t1 + t3 + t4
udimg13 = t1 + t3
udimg14 = t1 + t4
udimg34 = t3 + t4


cv2.imshow('Original Image', oimg)
cv2.imshow('Share1', t1)
cv2.imshow('Share2', t2)
cv2.imshow('Share3', t3)
cv2.imshow('Share4', t4)
cv2.imshow('Decrypted image by 1 and 2', dimg12)
cv2.imshow('Decrypted image by 2 and 3', dimg12)
cv2.imshow('Decrypted image by 2 and 4', dimg12)
cv2.imshow('Decrypted image by 1, 3 and 4', dimg12)
cv2.imshow('Can\'t be Decrypted by 1 and 3', udimg13)
cv2.imshow('Can\'t be Decrypted by 1 and 4', udimg14)
cv2.imshow('Can\'t be Decrypted by 3 and 4', udimg34)


cv2.waitKey(0)
cv2.destroyAllWindows()