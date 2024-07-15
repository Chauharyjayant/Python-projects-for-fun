#This is a small scale python project to automate the cctv's for the detection of the moments We will use openCv library in this project'''

import cv2 #starting by importing the library openCV
import winsound
cam = cv2.VideoCapture(0) #using the fucntion videocapture from the library, this fucntion will turn on the cameras,
#if there will be only one camera we will give 0 as the argument and if we have the multiple cameras we will give 1 as the argument'''

while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, x = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame1, contours, -1,(0,255,0) ,2) #This comment outed code is responsibel for the detection of even the eyelashes so we have created new code for that
    for c in contours:   #Now this will only form the counters when an object more than 5000 pixels will gonna move 
        if cv2.contourArea(c) < 5000:
            continue
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w , y+h),(0,0,255),2) #there will be a rectangle of red color will be shown with the 2px thickness
        winsound.Beep(500, 200)
    if cv2.waitKey(10) == ord("r"):
        break                       #Now this condition will wait for the user to  pressing r so that the break statement will get executed and cam stop'''
    cv2.imshow("Jayant's cam",frame1)#This statement shows the message that will be conveyed on the top left when the cam will be open'''

