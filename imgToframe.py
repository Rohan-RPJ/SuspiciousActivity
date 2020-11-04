'''
##To convert video to frames##
'''

import cv2
import os

path='/home/rohan/Desktop/SuspiciousDetection/'
tot=0
def getFrames(frameRate,vidcapt):
    count=0 
    sec=0
    while True:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        vidcapt.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcapt.read()
        if hasFrames:
            #Storing frames in Frames folder..Frames folder is to be created manually
            cv2.imwrite(path+"Frames/image"+str(tot+count)+".jpg", image)     # save frame as JPG file
        else:
            return count-1

# path to videos folder
os.chdir(path+"Videos")
print(os.listdir())
for filei in os.listdir():
    vidcapt = cv2.VideoCapture(filei)
    frameRate = 0.2 #//it will capture image in each 0.5 second
    count=getFrames(frameRate,vidcapt)
    tot+=count
print(tot)
