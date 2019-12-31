#!/usr/bin/env python
import numpy as np
import cv2 as cv 

try:
	import RPI.GPIO as gpio
	#really dumb
	gpioActive = True
	#set pins
	rCh = 20
	bCh = 21
	gCh = 22
	#set mode
	gpio.setup(rCh,gpio.OUT)
	gpio.setup(gCh,gpio.OUT)
	gpio.setup(bCh,gpio.OUT)
	#set frequency of pwm
	pwmFreq = 255
	#define pwm for pins
	redCh   = gpio.PWM(rCh, pwmFreq)
	greenCh = gpio.PWM(gCh, pwmFreq)
	blueCh  = gpio.PWM(bCh, pwmFreq)
	
except:
	print('could not find gpio library')
	gpioActive = False

try:
	from sense_hat import SenseHat
	sh = SenseHat()
	sh.clear
	hat = True
	gpioActive = False
	r,g,b = 0,0,0
	backLight = np.array([
	[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
	[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
	[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
	[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
	[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
	[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
	[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
	[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b]])
		
except:
	print('could not find senseHat library')
	hat = False

#change image to capture card location
cam = cv.VideoCapture(1)

#read image for framer size and create blank for troubleshooting
ret, frame = cam.read()
b,g,r = cv.split(frame)
blank = b - b

while True:
	#read frame and split colour channels
	ret, frame = cam.read()
	blue,green,red = cv.split(frame)
	
	#average colour channels
	b = int(np.mean(blue))
	g = int(np.mean(green))
	r = int(np.mean(red))
	#print red, green, blue
	
	#output average to LED controller
	if gpioActive == True:
		#pwm for analogue output
		redCh.start(100)
		greenCh.start(1)
		blueCh.start(1)
		#change the duty cycle for different colours
		redCh.ChangeDutyCycle(r)
		greenCh.ChangeDutyCycle(g)
		blueCh.ChangeDutyCycle(b)
	
	if hat == True:
		backLight = np.array([
			[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
			[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
			[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
			[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
			[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
			[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
			[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
			[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b]])
		sh.set_pixels(backLight)
		#print (r,g,b)
		
	
	#troubleshooting
	backlight = cv.merge((blank+b, blank+g, blank+r))
	cv.imshow('img', frame)
	cv.imshow('backlight', backlight)
	cv.waitKey(5)


