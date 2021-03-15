import tkinter as tk
root = tk.Tk()
import serial
import struct
stepstaken = 0
ardunioport = "COM" + str(input("Ardunio Port Number:")) # port number only
ser = serial.Serial(ardunioport, 9600)
wi = root.winfo_screenwidth() / 2
width = root.winfo_screenwidth()
hi = root.winfo_screenheight() / 2
height = root.winfo_screenheight()
sere = '\r\n' #still don't understand why but it does not work without this.
sender = sere.encode('utf_8')
pps = width / 200 #how many pixels are in 1 step
past = 0
sender = sere.encode('utf_8')
dir1 = str(400).encode('utf_8')
dir2 = str(400).encode('utf_8')
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
        if current != past:
                if steps > 0:
                        serialsteps = str(steps).encode('utf_8')
                        ser.write(dir1 + sender)
                        ser.write(serialsteps + sender)
                if steps < 0:
                        serialstepss = str(steps).encode('utf_8')
                        ser.write(dir2 + sender)
                        ser.write(serialstepss + sender)
        past = steps

while True:
        pos = root.winfo_pointerx() - wi
        steps = round(pos / pps)
        #print("Mouse Position " + str(pos) + " Steps Needed" + str(steps)) # shows cursor position
        send(steps)        
