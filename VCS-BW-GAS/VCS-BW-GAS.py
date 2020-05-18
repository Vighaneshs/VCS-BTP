import os
import numpy as np
import cv2
import itertools



# Load a color image in grayscale
img = cv2.imread('image1.jpg',cv2.IMREAD_GRAYSCALE)

#converting to binary by setting a threshold 
(thresh, imbw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
new_rows = 2*len(imbw)
new_cols = 2*len(imbw[0])

transparency1 = np.zeros((new_rows, new_cols))
transparency2 = np.zeros((new_rows, new_cols))
transparency3 = np.zeros((new_rows, new_cols))
transparency4 = np.zeros((new_rows, new_cols))




#Conversion to 2 transparencies
k = 0
l = 0


#For black
slist1 = [1,1,0,0]
slist2 = [0,0,0,1]
slist3 = [1,0,1,0]
slist4 = [0,1,1,0]

#For white
slist5 = [1,1,0,0]
slist6 = [1,0,0,0]
slist7 = [1,0,1,0]
slist8 = [1,0,0,1]


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


ccc = 0
for i in range(len(imbw)):
    l = 0
    for j in range(len(imbw[0])):
        rint = int.from_bytes(os.urandom(1), byteorder="big")%len(pslist5)
        rint1 = int.from_bytes(os.urandom(1), byteorder="big")%len(pslist1)
    
        

        if imbw[i][j] == 255:
            transparency1[k][l] = pslist5[rint][0]
            transparency1[k][l+1] = pslist5[rint][1]
            transparency1[k+1][l] = pslist5[rint][2]
            transparency1[k+1][l+1] = pslist5[rint][3]

            transparency2[k][l] = pslist6[rint][0]
            transparency2[k][l+1] = pslist6[rint][1]
            transparency2[k+1][l] = pslist6[rint][2]
            transparency2[k+1][l+1] = pslist6[rint][3]

            transparency3[k][l] = pslist7[rint][0]
            transparency3[k][l+1] = pslist7[rint][1]
            transparency3[k+1][l] = pslist7[rint][2]
            transparency3[k+1][l+1] = pslist7[rint][3]

            transparency4[k][l] = pslist8[rint][0]
            transparency4[k][l+1] = pslist8[rint][1]
            transparency4[k+1][l] = pslist8[rint][2]
            transparency4[k+1][l+1] = pslist8[rint][3]
            
        elif imbw[i][j] == 0:    
            transparency1[k][l] = pslist1[rint1][0]
            transparency1[k][l+1] = pslist1[rint1][1]
            transparency1[k+1][l] = pslist1[rint1][2]
            transparency1[k+1][l+1] = pslist1[rint1][3]

            transparency2[k][l] = pslist2[rint1][0]
            transparency2[k][l+1] = pslist2[rint1][1]
            transparency2[k+1][l] = pslist2[rint1][2]
            transparency2[k+1][l+1] = pslist2[rint1][3]

            transparency3[k][l] = pslist3[rint1][0]
            transparency3[k][l+1] = pslist3[rint1][1]
            transparency3[k+1][l] = pslist3[rint1][2]
            transparency3[k+1][l+1] = pslist3[rint1][3]

            transparency4[k][l] = pslist4[rint1][0]
            transparency4[k][l+1] = pslist4[rint1][1]
            transparency4[k+1][l] = pslist4[rint1][2]
            transparency4[k+1][l+1] = pslist4[rint1][3]
            
            

        ccc = ccc + 1
        l = l + 2
    k = k + 2
            

decerypted_12 =  np.zeros((new_rows, new_cols))
decerypted_23 =  np.zeros((new_rows, new_cols))
decerypted_24 =  np.zeros((new_rows, new_cols))
decerypted_134 =  np.zeros((new_rows, new_cols))

decrypted_14 = np.zeros((new_rows, new_cols))
decrypted_13 = np.zeros((new_rows, new_cols))
decrypted_34 = np.zeros((new_rows, new_cols))



t1 = transparency1.astype(np.int8)
t2 = transparency2.astype(np.int8)
t3 = transparency3.astype(np.int8)
t4 = transparency4.astype(np.int8)

#decrypting image by taking and of 2 transparencies which is equivalent to aligning to transparencies and viewing with human eyes
for i in range(new_rows):
    for j in range(new_cols):
        decerypted_12[i][j] = (t1[i][j]) & (t2[i][j])
        decerypted_23[i][j] = (t3[i][j]) & (t2[i][j])
        decerypted_24[i][j] = (t4[i][j]) & (t2[i][j])
        decerypted_134[i][j] = (t1[i][j]) & (t4[i][j]) & (t3[i][j])
        decrypted_14[i][j] = (t1[i][j]) & (t4[i][j])
        decrypted_13[i][j] = (t1[i][j]) & (t3[i][j])
        decrypted_34[i][j] = (t3[i][j]) & (t4[i][j])
       


cv2.imshow('image',imbw)
cv2.imshow('transparency1',transparency1)
cv2.imshow('transparency2',transparency2)
cv2.imshow('transparency3',transparency3)
cv2.imshow('transparency4',transparency4)
cv2.imshow('decrypted by 1 and 2', decerypted_12)
cv2.imshow('decrypted by 2 and 3', decerypted_23)
cv2.imshow('decrypted by 2 and 4', decerypted_24)
cv2.imshow('decrypted by 1, 3 and 4', decerypted_134)
cv2.imshow('can\'t be decrypted by 1 and 4', decrypted_14)
cv2.imshow('can\'t be decrypted by 1 and 3', decrypted_13)
cv2.imshow('can\'t be decrypted by 3 and 4', decrypted_34)
cv2.waitKey(0)
cv2.destroyAllWindows()