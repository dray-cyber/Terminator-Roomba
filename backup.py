import cv2
from playsound import playsound
import time
import threading
import queue
q = queue.Queue()
url = "rtsp://admin:e@192.168.0.246:554/tmpfs/auto.jpg"
cap = cv2.VideoCapture(url)
#url = "rtsp://admin:e@192.168.0.20:554/tmpfs/auto.jpg"
#cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def detection():
    while True:
        try:
            if q.get() is not None:
                output = q.get()
                gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.5,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags=cv2.CASCADE_SCALE_IMAGE
                )   
                if faces is not None:
                    for (x, y, w, h) in faces:
                        face = x+w * .5
                        cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    (height, width) = output.shape[:2]
                    wi = width // 2 
                    if wi < face:
                        print("right")
                    if wi > face:
                        print("left")
                    if wi - 20 < face and face < wi + 20:
                        print("middle, fire")
                        playsound('beep.mp3')
        except:
            potato = "potato" 
def first():
    while True:
        ret, frame = cap.read()
        if frame is not None:
            width = int(frame.shape[1] * 70 / 100)
            height = int(frame.shape[0] * 70 / 100)
            dsize = (width, height)
            output = cv2.resize(frame, dsize)
            k = cv2.waitKey(1)
            q.put(output)
            cv2.imshow('FaceDetection', output)
x = threading.Thread(target=first)
x.start()
c = threading.Thread(target=detection)
c.start()

