import cv2
import sys
from  pycreate2 import Create2
import time
port = "COM7"  # where is your serial port?
bot = Create2(port)

# Start the Create 2

bot.start()
bot.safe()
#                bot.drive_direct(-100, -100)
#                time.sleep(5)
#                bot.drive_stop()
#                bot.close()
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)
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
        if x <= 240 and x >= 220:
            detected = True
            print('detected')
            bot.drive_stop()
        else:
            if detected != True:
                if x >= 200:
                    print("right")
                    bot.drive_direct(-25, 25)
                if x <= 165:
                    print("left")
                    bot.drive_direct(25, -25)
            if detected == True:
                on = False
                if on == True:
                    print("RAMM")
                    bot.drive_direct(-100, -100)
                    time.sleep(5)
                    bot.drive_stop()
                    bot.close()
                    break
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('FaceDetection', frame)
    if k%256 == 27: #ESC Pressed
        break
video_capture.release()
cv2.destroyAllWindows()
