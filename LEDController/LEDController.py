#!/usr/bin/env python
import numpy as np
import cv2 as cv 


#initialise the device list 
strDevIn = ""
#-----------------------------------------------------------------------
#      	bluetooth setup v0.2
# 		initialises bluetooth while checking if devices are accessable
#		started: 17/12/2019 updated: 03/01/2020
#		Author: AH
#-----------------------------------------------------------------------
def BluetoothSetup(strDevIn):
	try:
		import pybluez
		strstrDevIn += " BLUETOOTH"
	except:
		print("bluetooth library not found")
	return strDevIn

#-----------------------------------------------------------------------
#      	audio setup v0.2
# 		initialises the audio while checking if audio is accessable
#		started: 17/12/2019 updated: 03/01/2020
#		Author: AH
#-----------------------------------------------------------------------
def AudioSetup(strDevIn):
	try:
		import pyaudio
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

		strDevIn += " AUDIO"
	except:
		print("no audio device")
	return strDevIn

#-----------------------------------------------------------------------
#      	GPIO setup v0.2
# 		initialises the GPIO while checking if GPIO are accessable
#		started: 17/12/2019 updated: 03/01/2020
#		Author: AH
#-----------------------------------------------------------------------
def GPIOSetup():
	try:
		import RPI.GPIO as gpio
		strDevIn += " GPIO"
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
	return strDevIn

#-----------------------------------------------------------------------
#      	sense Hat setup v0.2
# 		initialises the sense hat while checking if 
# 		devices are accessable
#		started: 17/12/2019 updated: 03/01/2020
#		Author: AH
#-----------------------------------------------------------------------
def SenseHatSetup(strDevIn)
	try:
		from sense_hat import SenseHat
		sh = SenseHat()
		sh.clear
		strDevIn += " SENSE-HAT"
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
	return strDevIn
#-----------------------------------------------------------------------
#      	Camera setup v0.1
# 		initialises camera and checks for connection 
#		started: 03/01/2020 updated: 
#		Author: AH
#-----------------------------------------------------------------------
def CameraSetup(strDevIn):
	cam = cv.VideoCapture(0)
	ret, frame = cam.read()
	if ret == True:
		strDevIn += " CAMERA"
	return strDevIn

#-----------------------------------------------------------------------
#      	setup v0.1
# 		initialises all
#		started: 03/01/2020 updated: 
#		Author: AH
#-----------------------------------------------------------------------
def Setup(strDevIn):
	strDevIn = BluetoothSetup(strDevIn)
	strDevIn = AudioSetup(strDevIn)
	strDevIn = GPIOSetup(strDevIn)
	strDevIn = SenseHatSetup(strDevIn)
	strDevIn = CameraSetup(strDevIn)

	return strDevIn

#frame properties
if "CAMERA" in devIn:
	ret, frame = cam.read()
	b,g,r = cv.split(frame)
	blank = b - b

#audio properties 20 Hz - 20KHz to Hex
if "AUDIO" in devIn:
	intAudioRange = 20000 - 20
	intAlias = int(16777215/intAudioRange)

#-----------------------------------------------------------------------
#      	Main v0.1
# 		Main body for control software
#		started: 17/12/2019 updated: 03/01/2020
#		Author: AH
#-----------------------------------------------------------------------
while True:
	if "CAMERA" in strDevIn:
		#read frame and split colour channels
		ret, frame = cam.read()
		imgBlue,imgGreen,imgRed = cv.split(frame)

		#average colour channels
		b = int(np.mean(imgBlue))
		g = int(np.mean(imgGreen))
		r = int(np.mean(imgRed))

	if "AUDIO" in strDevIn:
		#read audio device
		inAaudio = stream.read(CHUNK)

		hexColour = inAudio%intAlias
		#convert hex to RGB
		h = input('Enter hex: ').lstrip('#')
		R, G, B = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
	

	if "GPIO" in strDevIn:
		#pwm for analogue output
		redCh.start(100)
		greenCh.start(1)
		blueCh.start(1)

		#change the duty cycle for different colours
		redCh.ChangeDutyCycle(r)
		greenCh.ChangeDutyCycle(g)
		blueCh.ChangeDutyCycle(b)
	
	if "BLUETOOTH" in strDevIn:
		#do bluetooth stuff plz
	
	if "SENSE-HAT" in strDevIn:
		#output colour to sense hat LED matrix 
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
		cv.imshow('image frame', frame)
		cv.imshow('backlight', backlight)
	except:
		print("Cannot show troubleshooting")
	#adjust for higher/lower bitrates 
	cv.waitKey(1)
