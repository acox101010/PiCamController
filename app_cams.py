#!/usr/bin/python3.4.2

import Tkinter
import cv2 

class App:
    def _init_(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.window.mainloop()
        

App(Tkinter.Tk(), "Tkinter and OpenCV")
