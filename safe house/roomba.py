import cv2
import numpy as np
from time import time
import socket
from goprocam import GoProCamera
from goprocam import constants
import cv2
import sys
from  pycreate2 import Create2
import time as te
from time import time
import requests
import random as rand
from playsound import playsound
port = "COM7"  # what is your serial port?
bot = Create2(port)
# Start the Create 2
bot.start()
bot.safe()
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gpCam = GoProCamera.GoPro()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
t=time()
gpCam.livestream("start")
cap = cv2.VideoCapture("udp://10.5.5.9:8554")
thereface = True
img_counter = 0
detected = False
onetime = True
def speak(text, filename, speed = 1, lang = 'en-US'):
        speed = str(speed)
        url = u"https://translate.google.com/translate_tts?ie=UTF-8&q=" + text + "%21&tl=" + lang + "&ttsspeed=" + speed + "&total=1&idx=0&client=tw-ob&textlen=14&tk=594228.1040269"
        r = requests.get(url)
        with open(filename, 'wb') as test:
            test.write(r.content)
while True:
    if time() - t >= 2.5:
        sock.sendto("_GPHD_:0:0:2:0.000000\n".encode(), ("10.5.5.9", 8554))
        t=time()
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
        if x <= 185 and x >= 175:
            detected = True
            print('detected')
            bot.drive_stop()
        else:
            if detected != True or x <= 185 and x >= 175:
                if x >= 185:
                    print("left")
                    #turn print("right")
                    bot.drive_direct(-25, 25)
                if x <= 175:
                    print("right")
                    #turn print("left")
                    bot.drive_direct(25, -25)
            if detected == True:
                on = True
                if on == True:
                    wordchoice = rand.randrange(0, 5)
                    if wordchoice == 1:
                        playsound('words.mp3')
                        wordchoice = 0
                    if wordchoice == 2:
                        playsound('words1.mp3')
                        wordchoice = 0
                    if wordchoice == 3:
                        playsound('words2.mp3')
                        wordchoice = 0
                    if wordchoice == 4:
                        playsound('words3.mp3')
                        wordchoice = 0
                    print("RAMM")
                    bot.drive_direct(500, 500)
                    break
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('FaceDetection', frame)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('FaceDetection', frame)
    if k%256 == 27: #ESC Pressed
        break
video_capture.release()
cv2.destroyAllWindows()
