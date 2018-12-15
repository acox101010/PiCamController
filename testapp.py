#!/usr/bin/python3.4.2
# -*- coding: utf-8 -*-
#POC: Andrew Cox; acox3@mmm.com

import Tkinter
from Tkinter import *
import tkMessageBox
import tkSimpleDialog
import tkMessageBox
import cv2
import os
import sys

#Specifying Frame GUI
top = Tkinter.Tk()
top.title("PiCamera Controller")
top.configure(bg="#ffffff")
top.geometry("500x400")
canvas = Canvas(top, width = 300, height = 250, bg="white")
canvas.pack()
img = PhotoImage(file="/home/pi/Desktop/cam_images/icons/piInside.gif")
canvas.create_image(30,30, anchor=NW, image=img)
frame = Tkinter.Frame(top,)
frame.pack()


#Function button 1 & 3 to execute camera.py and camsRecord.py respectively
def helloCallBack():
	os.system('python /home/pi/Desktop/cam_images/camera.py') #connects to picamera script in same directory
try:
	b1 = Tkinter.Button(frame, text ="Run Cam", fg="green", bg="white", command = helloCallBack) #calls camera.py when button is pressed
except(KeyboardInterrupt, SystemExit):
	print ('Images Captured:',i+1)
		
def recordCallBack():
	os.system('python /home/pi/Desktop/cam_images/camsRecord.py') #connects to picamera to record
try:
	b3 = Tkinter.Button(frame, text ="Run Video", fg="orange", bg="white", command = recordCallBack) #calls camsRecord.py when button is pressed
except(KeyboardInterrupt, SystemExit):
	print ('Video Captured')
		
#Function button 2 to close application
def killsCallBack():
    sys.exit("application closed by user")
b2 = Tkinter.Button(frame, text="Exit App", fg="blue", bg="white", command = killsCallBack)

#Preview Camera
def prwCallBack():
	os.system('python /home/pi/Desktop/cam_images/preview.py')	
b4 = Tkinter.Button(frame, text="Quick Preview", fg="black", bg ="white", command = prwCallBack)

#Live View
def lviewCallBack():
	os.system('sudo modprobe bcm2835-v4l2')
	os.system('qv4l2')
try:
	b5 = Tkinter.Button(frame, text="Live View", fg="black", bg ="white", command = lviewCallBack)
	print ('qv4l2 loaded, change pixel aspect rat to NTSC/PAL-M/PAL-60')
except(KeyboardInterrupt, SystemExit):
	print ('Live view closed')
	
#button padding and orientation
b1.pack(side=Tkinter.LEFT)
b2.pack(side=Tkinter.RIGHT)
b3.pack(side=Tkinter.TOP)
b4.pack(side=Tkinter.TOP)
b5.pack(side=Tkinter.TOP)

#App Notes 
Label(top, text="Live View: Allows you to view remotely through VNC", font="Calibri").pack(side=Tkinter.BOTTOM)
Label(top, text="Quick Preview: Previews camera for specified time in xwindow", font="Calibri").pack(side=Tkinter.BOTTOM)

top.mainloop()
