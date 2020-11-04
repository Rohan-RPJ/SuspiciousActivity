'''
##To label images and put it automatically to its respective folders##

'''


import os
import time 
import subprocess
import shutil

#Here all the frames are initially stored at path src in code
src="/home/rohan/Desktop/SuspiciousDetection/ResizedFrames/"

#dest1, dest2 and dest3 are empty foldes to be created manually inside src folder.. or u can give your own path
dest1="Safe/"
dest2="Potentially-Suspicious/"
dest3="Criminal-Activity/"

# l is number of image files which are initially there at path 'src'
l=1802

os.chdir(src)

# i used to put imagei.jpg to corresponding folderr
i=1
# loop to open images automatically, to be labelled manually by providing input as 1,2,3 or A 
# the labelled img moves autmatically to its corresponding number provided and next img is opened
while i<=l:
	img="image"+str(i)+".jpg"
	p = subprocess.Popen(["display", img])
	ch=input("1.Safe 2.Potentially-Suspicious 3.Criminal Activity A.Delete Image \n")
	if ch=="1":
		shutil.move(img, dest1)
	elif ch=="2":
		shutil.move(img, dest2)
	elif ch=="3":
		shutil.move(img, dest3)
	elif ch=="A":
		os.remove(img)
	else:
		print("Enter a valid option")
		i-=1
	
	p.kill()
	i+=1
	
