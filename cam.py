import cv2
import time
import threading
import queue
import serial
q = queue.Queue()
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


url = "rtsp://admin:e@192.168.0.246:554/tmpfs/auto.jpg"
#cap = cv2.VideoCapture(url)
#url = "rtsp://admin:e@192.168.0.20:554/tmpfs/auto.jpg"
#cap = cv2.VideoCapture("udp://10.5.5.9:8554")
cap = cv2.VideoCapture(0)
def detection():
    ser = serial.Serial(int(input("port")), 9600)
    while True:
        try:
            if q.get() is not None:
                face = None
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
                        ser.write(input_value.encode(3))
                    if wi > face:
                        print("left")
                        ser.write(input_value.encode(1))
                    if wi - 20 < face and face < wi + 20:
                        print("middle, fire")
                        ser.write(input_value.encode(2))
                        face = None
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
#def servo():
    #need to work on this
x = threading.Thread(target=first)
x.start()
c = threading.Thread(target=detection)
c.start()

