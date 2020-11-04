'''
##To resize img to particular dimension##
'''

import cv2
import os

path='/home/rohan/Desktop/SuspiciousDetection/'

count=1
def resizeImg(imgi,width,height):
    img = cv2.imread(imgi)
    #print('original image shape:', img.shape) 
    resized_img = cv2.resize(img, (width, height))
    #print('resized to 128x256 image shape:', resized_img.shape)
    cv2.imwrite(path+"ResizedFrames/image"+str(count)+".jpg", resized_img)     # save frame as JPG file


# path were frames are stored
os.chdir(path+"Frames")
l=len(os.listdir())

#size of frames
height,width=299,299
try:
    for i in range(1,l+1):
        resizeImg("image"+str(i)+".jpg",width,height)
        count+=1
    print("Success")
except:
    print("Exception occured")
