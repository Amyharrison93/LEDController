#!/usr/bin/env python
import numpy as np
import cv2 as cv 

devIn = ""

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
	import pyaudio
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
if ret == True:
	devIn += "CAMERA"
b,g,r = cv.split(frame)
blank = b - b

#audio properties
intAudioRange = 20000 # 20KHz
intAlias = int(16777215/intAudioRange)

try:
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
		channels=CHANNELS,
		rate=RATE,
		input=True,
		frames_per_buffer=CHUNK)

	devIn += "AUDIO"

except:
	print("no audio device")

while True:
	if "CAMERA" in devIn:
		#read frame and split colour channels
		ret, frame = cam.read()
		imgBlue,imgGreen,imgRed = cv.split(frame)

		#average colour channels
		b = int(np.mean(imgBlue))
		g = int(np.mean(imgGreen))
		r = int(np.mean(imgRed))

	if "AUDIO" in devIn:
		#read audio device
		inAaudio = stream.read(CHUNK)

		hexColour = inAudio%intAlias
		#convert hex to RGB
		h = input('Enter hex: ').lstrip('#')
		R, G, B = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
	
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
		sh.set_pixels(backLight)
	
	backLight = np.array([
		[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
		[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
		[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
		[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
		[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
		[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
		[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],
		[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b]])
		
	try:
		#troubleshooting
		backlight = cv.merge((blank+b, blank+g, blank+r))
		cv.imshow('img', frame)
		cv.imshow('backlight', backlight)
	except:
		print("Cannot show troubleshooting")

	cv.waitKey(1)
