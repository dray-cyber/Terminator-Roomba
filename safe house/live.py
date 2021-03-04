from goprocam import GoProCamera
from goprocam import constants
import cv2
import sys
import numpy as np
import socket
from  pycreate2 import Create2 as roomba
import time as te
from time import time
port = "COM7"
#bot = roomba(port)
#bot.start()
#bot.safe()
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gpCam = GoProCamera.GoPro()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
t=time()
gpCam.livestream("start")
cap = cv2.VideoCapture("udp://10.5.5.9:8554")




while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    k = cv2.waitKey(1)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        if x >= 200:
                #turn print("right")
                bot.drive_direct(-25, 25)
        if x <= 170:
                #turn print("left")
                bot.drive_direct(25, -25)
        if x >= 170 and x <= 200:
                bot.drive_direct(0, 0)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('FaceDetection', frame)
    if time() - t >= 2.5:
        sock.sendto("_GPHD_:0:0:2:0.000000\n".encode(), ("10.5.5.9", 8554))
        t=time()
    if k%256 == 27: #ESC Pressed
        break
video_capture.release()
cv2.destroyAllWindows()
