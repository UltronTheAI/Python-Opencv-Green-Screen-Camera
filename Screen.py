#green screen camera
'''
This Tk App Use Is You Can Record Screen And You Can Choose Bg Transparent And X, Y. It Is Green Screen Camera
'''
import os
from tkinter import *
import numpy as np
import cv2
screen = Tk()
#color
trans = 'green'
screen.config(bg=trans)
screen.attributes('-fullscreen', True)
screen.wm_attributes('-transparentcolor',    trans)

#camera num
cap = cv2.VideoCapture(0)
camlab = Label(padx=200, pady=200, bg=trans, image=None)
camlab.place(x=0, y=0)

while True:
	screen.update()
	screen.update_idletasks()
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    cv2.imwrite('img.png', frame)
    imgp = PhotoImage(file='img.png')
    camlab['image'] = imgp
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
