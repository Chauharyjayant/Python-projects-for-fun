#This is a small scale python project to automate the cctv's for the detection of the moments We will use openCv library in this project'''

import cv2 #starting by importing the library openCV

cam = cv2.VideoCapture(0) #using the fucntion videocapture from the library, this fucntion will turn on the cameras,
#if there will be only one camera we will give 0 as the argument and if we have the multiple cameras we will give 1 as the argument'''

while cam.isOpened():
    ret, frame = cam.read()
    if cv2.waitKey(10) == ord("r"):
        break                       #Now this condition will wait for the user to  pressing r so that the break statement will get executed and cam stop'''
    cv2.imshow("Jayant's cam",frame)#This statement shows the message that will be conveyed on the top left when the cam will be open'''

