#!/usr/bin/env python
# -*- coding: utf-8 -*-

from picamera import PiCamera
from time import sleep 
import Tkinter
from Tkinter import *
from datetime import datetime
import time
import tkMessageBox
import tkSimpleDialog
import tkMessageBox

#Setup GUI
root = Tk()
w=Label(root, text="Parameter Entry")
w.pack()

#defining user inputs
p = tkSimpleDialog.askinteger("Images","How many pictures do you want to take: ")
d = tkSimpleDialog.askinteger("Seconds","Enter time between pictures(seconds): ")

#Print total execution time to terminal
totTime=p*d
print("total time: ", totTime,"Seconds") 

#Set time variable to record timestamp
timStamp = (time.strftime("%b-%d-%Y-%H-%M-%S"))

#Initiate camera 
camera = PiCamera()
camera.start_preview(fullscreen=False,window=(100,20,640,480))
for i in range(p):
	print ("Capturing Images", i)
	camera.led = False
	sleep(d)
	camera.capture('/home/pi/Desktop/cam_images/images/image%s.jpg' % i)
	if i >= p-1:
		print ('loop limit reached')
		camera.stop_preview()
		print ('Images Captured:',i+1)
		camera.led = True
		break
else:
	i + 1
camera.stop_preview()
