#!/usr/bin/python3
# -*- coding: utf-8 -*-

from picamera import PiCamera
from time import sleep 
import Tkinter
from Tkinter import *
import tkMessageBox
import tkSimpleDialog
import tkMessageBox

root = Tkinter.Tk()
preTime = tkSimpleDialog.askinteger("Preview","Enter total preview time (seconds)")

#Initiate camera 
camera = PiCamera()
#camera.rotation = 180
camera.start_preview()
camera.led = True
print("Preview time: ",preTime)
sleep(preTime)

camera.stop_preview()
print("Preview completed")
