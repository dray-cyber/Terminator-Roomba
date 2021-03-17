import tkinter as tk
root = tk.Tk()
import serial
import struct
import time
stepstaken = 0
ardunioport = "COM" + str(input("Ardunio Port Number:")) # port number only
#ser = serial.Serial(ardunioport, 9600)
wi = root.winfo_screenwidth() / 2
width = root.winfo_screenwidth()
hi = root.winfo_screenheight() / 2
height = root.winfo_screenheight()
sere = '\r\n' #still don't understand why but it does not work without this.
sender = sere.encode('utf_8')
ppsx = width / 200 #how many pixels are in 1 step in side to side
ppsy = height / 200 #how many pixels are in 1 step in up and down
past = 0
sender = sere.encode('utf_8')
dir1 = str(400).encode('utf_8')
dir2 = str(401).encode('utf_8')
dir3 = str(500).encode('utf_8')
dir4 = str(501).encode('utf_8')
def send(steps):
        global past
        global current
        global sender
        global dir1
        global dir2
        global stepstaken
        global working
        #need overcome overstepping
        sere = '\r\n'
        current = steps
        neg = past - 5 # tolerance 
        pos = past + 5 # tolerance
        needed = current - past
        print(needed, steps)
        if working == False:
                if needed > 0:
                        working = True
                        serialsteps = str(needed).encode('utf_8')
                        ser.write(dir1 + sender)
                        ser.write(serialsteps + sender)
                        working = False
                if needed < 0 :
                        working = True
                        needed = needed * -1
                        serialstepss = str(needed).encode('utf_8')
                        ser.write(dir2 + sender)
                        ser.write(serialstepss + sender)
                        working = False
        past = steps
def sendy(steps):
        global past
        global current
        global sender
        global dir1
        global dir2
        global stepstaken
        global working
        #need overcome overstepping
        sere = '\r\n'
        current = steps
        neg = past - 5 # tolerance 
        pos = past + 5 # tolerance
        needed = current - past
        print(needed, steps)
        if working == False:
                if needed > 0:
                        working = True
                        needed = needed + 600
                        serialsteps = str(needed).encode('utf_8')
                        ser.write(dir3 + sender)
                        ser.write(serialsteps + sender)
                        working = False
                if needed < 0:
                        working = True
                        needed = needed * -1 + 600
                        serialstepss = str(needed).encode('utf_8')
                        ser.write(dir4 + sender)
                        ser.write(serialstepss + sender)
                        working = False
                past = steps

while True:
        pos = root.winfo_pointerx() - wi
        sop = root.winfo_pointery() - hi
        steps = round(pos / ppsx)
        stepy = round(sop / ppsy)
        #print("Mouse Position " + str(pos) + " Steps Needed" + str(steps)) # shows cursor position
        send(steps)
        sendy(stepy)
