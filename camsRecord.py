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
import wx


#Setup GUI
root = Tk()
w=Label(root, text="Parameter Entry")
w.pack()

#defining user input
y = tkSimpleDialog.askinteger("Seconds","Enter total video time (seconds): ")

#Set time variable to record timestamp
timStamp = (time.strftime("%b-%d-%Y-%H-%M-%S"))

camera = PiCamera()
camera.start_preview(fullscreen=False,window=(100,20,640,480))		
camera.led = False
print ("Now recording")
camera.start_recording('/home/pi/Desktop/cam_images/video/Video%s.h264'% timStamp)
sleep(y)
camera.stop_recording()
camera.led = True
print ("video successfully captured")
print ("!!!Convert to MP4 using *MP4Box -add file.h264 file.mp4*!!!")
print ("!!!View using *omxplayer file.mp4*!!!")
print ("Total Recording Time:", y)
camera.stop_preview()
