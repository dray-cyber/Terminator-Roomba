import cv2
from playsound import playsound
url = "rtsp://admin:password@192.168.0.20:554/tmpfs/auto.jpg"
#ip cam
#cap = cv2.VideoCapture(url)
#web cam

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    ret, frame = cap.read()
    if frame is not None:
        scale_percent = 70
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dsize = (width, height)
        output = cv2.resize(frame, dsize)
        (h, w) = output.shape[:2]
        k = cv2.waitKey(1)
        gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.5,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        left = w / 2 + 25
        right = w / 2 - 25
        middle = (300, 200)
        for (x, y, w, h) in faces:
            face = x+w * .5
            (height, width) = output.shape[:2]
            wi = width // 2
            #-------------------------
            #100                   200
            if wi < face:
                    print("right")
            if wi > face:
                    print("left")
            if wi - 20 < face and face < wi + 20:
                print("middle, fire")
                playsound('beep.mp3')
        for (x, y, w, h) in faces:
            middle = x+w * .5
            cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow('FaceDetection', output)
    if k%256 == 27: #ESC Pressed
        break
video_capture.release()
cv2.destroyAllWindows()
