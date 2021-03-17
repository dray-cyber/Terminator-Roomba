import cv2
import time
import threading
import queue
import serial
import struct
past = 0
current = 0
q = queue.Queue()
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
print("capture initiated")
global ser
ser = serial.Serial("COM8", 9600)
def first():
        while True:
            ret, frame = cap.read()
            if frame is not None:
                width = int(frame.shape[1] * 70 / 100)
                height = int(frame.shape[0] * 70 / 100)
                hi = int(frame.shape[0] / 2)
                dsize = (width, height)
                output = cv2.resize(frame, dsize)
                k = cv2.waitKey(1)
                gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.5,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags=cv2.CASCADE_SCALE_IMAGE
                )   
                for (x, y, w, h) in faces:
                    cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)
                hi = int(height / 2)
                cv2.line(output, (0,hi), (width,hi),(0,255,0),1) 
                cv2.imshow('FaceDetection', output)
                q.put(output)
past = 0
sere = '\r\n' 
sender = sere.encode('utf_8')
dir1 = str(400).encode('utf_8')
dir2 = str(401).encode('utf_8')
def prep(steps):
        global past
        global current
        global sender
        global dir1
        global dir2
        global stepstaken
        #need overcome overstepping
        sere = '\r\n'
        current = steps
        neg = past - 5 # tolerance 
        pos = past + 5 # tolerance
        needed = current - past
        print(needed, steps)
        if current != past:
                if steps > 0:
                        serialsteps = str(needed).encode('utf_8')
                        ser.write(dir1 + sender)
                        ser.write(serialsteps + sender)
                if steps < 0:
                        needed = needed * -1
                        serialstepss = str(needed).encode('utf_8')
                        ser.write(dir2 + sender)
                        ser.write(serialstepss + sender)
        past = steps

def detection():
    global past
    global current
    global facex
    facex = None
    global facey
    facey = None
    #b'200\r\n'
    #ser = 1
    #supposed recipe for sending
    #    sere = '\r\n'
    #    sender = sere.encode('utf_8')
    #    e = str(200).encode('utf_8')
    #    ser.write(e + sender)
    while True:
        if q.get() is not None:
                face = None
                output = q.get()
                (height, width) = output.shape[:2]
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
                        facex = w+x * .5
                        facey = h+y * .5
                    if facex is not None:
                        wi = width // 2
                        spp = height // 200 / 4
                        if wi < facex:
                            needed = wi-facex
                            rotate = needed * spp
                            steps = round(rotate)
                            prep(int(steps))
                            print(facex)
                        if facex < wi:
                            needed = wi-facex
                            rotate = needed * spp
                            steps = round(rotate)
                            prep(int(steps))
                            print(facex)
x = threading.Thread(target=first)
x.start()
c = threading.Thread(target=detection)
c.start()

