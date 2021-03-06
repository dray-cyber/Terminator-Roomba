import cv2
import time
import threading
import queue
import serial
import struct
global direction
direction = 1
home = 180
past = 0
sere = '\r\n'
sender = sere.encode('utf_8')
q = queue.Queue()
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#url = "rtsp://admin:e@192.168.0.246:554/tmpfs/auto.jpg"
#cap = cv2.VideoCapture(url)
#url = "rtsp://admin:e@192.168.0.20:554/tmpfs/auto.jpg"
cap = cv2.VideoCapture(0)
#gpCam = GoProCamera.GoPro()
#gpCam.stream("udp://127.0.0.1:10000")

#gpCam.livestream("start")
#cap = cv2.VideoCapture("udp://localhost:10000")
#cap = cv2.VideoCapture("udp://10.5.5.100:8554")
print("capture initiated")
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
sere = '\r\n' #still don't understand why but it does not work without this.
sender = sere.encode('utf_8')
dir1 = str(400).encode('utf_8')
dir2 = str(401).encode('utf_8')
def send(steps):
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
                if needed > 0:
                        serialsteps = str(needed).encode('utf_8')
                        ser.write(dir1 + sender)
                        ser.write(serialsteps + sender)
                if needed < 0:
                        needed = needed * -1
                        serialstepss = str(needed).encode('utf_8')
                        ser.write(dir2 + sender)
                        ser.write(serialstepss + sender)
        past = steps
        #does final checks and some changes before sending it through serial to a ardunio
def detection():
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
                        face = w+x * .5
                    (height, width) = output.shape[:2]
                    wi = width // 2
                    hi = height // 2
                    #stepper will be at 180 degrees
                    #add more to raise up
                    #take away to go down
                    #hi = 180
                    #to get stepper rotation per pixel,
                    #divide height by the total number of steps
                    #thats how many steps you have to take for pixel
                    pps = width / 198
                    if face is not None:
                            if face > wi:
                                #tell how many pixels above
                                needed = face-hi
                                steps = round(face / pps)
                                drive = round(steps)
                                print("-" + str(drive))
                                #stepper go down
                                send(drive)
                            if face < wi:
                                #tell how many pixels below
                                needed = hi-face
                                steps = round(face / pps)
                                drive = round(steps)
                                print("+" + str(drive))
                                send(drive)
                                #stepper go up
x = threading.Thread(target=first)
x.start()
c = threading.Thread(target=detection)
c.start()

