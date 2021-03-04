import cv2
import time
import threading
import queue
import serial
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
def send(drive, ser):
        s = ser
        s.write(drive.encode())
        #does final checks and some changes before sending it through serial to a ardunio
def detection():
    #ser = serial.Serial("COM11", 9600)
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
                        face = y+h * .5
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
                    spp = height // 200
                    if face > hi:
                        #tell how many pixels above
                        needed = face-hi
                        rotate = needed * 1.8
                        drive = round(rotate)
                        print("-" + str(drive))
                        #stepper go down
                        #send(drive, ser)
                    if face < hi:
                        #tell how many pixels below
                        needed = hi-face
                        rotate = needed * 1.8
                        drive = round(rotate)
                        print("+" + str(drive))
                        #send(drive, ser)
                        #stepper go up
                    
        except:
            potato = "potato"
x = threading.Thread(target=first)
x.start()
c = threading.Thread(target=detection)
c.start()

