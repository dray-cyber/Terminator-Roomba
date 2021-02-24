import cv2
import sys
from  pycreate2 import Create2 as meme
import time
from playsound import playsound
import requests
import random as rand
port = "COM7"
#bot = meme(port)
#bot.start()
#bot.safe()
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)
def speak(text, filename, speed = 1, lang = 'en-US'):
        speed = str(speed)
        url = u"https://translate.google.com/translate_tts?ie=UTF-8&q=" + text + "%21&tl=" + lang + "&ttsspeed=" + speed + "&total=1&idx=0&client=tw-ob&textlen=14&tk=594228.1040269"
        r = requests.get(url)
        with open(filename, 'wb') as test:
            test.write(r.content)
thereface = True
img_counter = 0
detected = False
onetime = True
while True:
    ret, frame = video_capture.read()
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
        if x <= 280 and x >= 270:
            detected = True
            print('detected')
            #bot.drive_stop()
        else:
            if detected != True:
                if x >= 280:
                    print("left")
                    #turn print("right")
                    #bot.drive_direct(-25, 25)
                if x <= 270:
                    print("right")
                    #turn print("left")
                    #bot.drive_direct(25, -25)
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
                    #bot.drive_direct(-100, -100)
                    #bot.drive_stop()
                    #bot.close()
                    break
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('FaceDetection', frame)
    if k%256 == 27: #ESC Pressed
        break
video_capture.release()
cv2.destroyAllWindows()

