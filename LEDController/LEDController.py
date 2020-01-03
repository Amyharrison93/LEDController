#!/usr/bin/env python3
import numpy as np
import cv2 as cv 

strDevIn = ""

#-----------------------------------------------------------------------
#      	bluetooth setup v0.2
# 		initialises bluetooth while checking if devices are accessable
#		started: 17/12/2019 updated: 03/01/2020 
#		Comp tested: 03/01/2020
#		Author: AH
#-----------------------------------------------------------------------
def BluetoothSetup(strDevIn):
	try:
		import bluetooth as bt
		arryDevices = bt.discover_devices(lookup_names = True)

		#compare with known device(create a config for this later)
		arryKnownDevice = "D4:11:A3:96:D0:AA", "What's a phone"

		#check if the known device is found
		for intCount in range(0, len(arryDevices)):
			if arryDevices[intCount] == arryKnownDevice:
			strDevIn += " BLUETOOTH"

	except:
		print("Bluetooth setup failed")
	return strDevIn

#-----------------------------------------------------------------------
#      	audio setup v0.2
# 		initialises the audio while checking if audio is accessable
#		started: 17/12/2019 updated: 03/01/2020 
#		comp tested:
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
		print("Audio setup failed")
	return strDevIn

#-----------------------------------------------------------------------
#      	GPIO setup v0.2
# 		initialises the GPIO while checking if GPIO are accessable
#		started: 17/12/2019 updated: 03/01/2020
#		comp tested:
#		Author: AH
#-----------------------------------------------------------------------
def GPIOSetup():
	try:
		import RPI.GPIO as gpio
		strDevIn += " GPIO"
		#set pins
		rCh = 12
		bCh = 13
		gCh = 18
		switch = 15
		#set mode out
		gpio.setup(rCh,GPIO.OUT)
		gpio.setup(gCh,GPIO.OUT)
		gpio.setup(bCh,GPIO.OUT)
		#set mode in 
		gpio.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		#set frequency of pwm
		pwmFreq = 255
		#define pwm for pins
		redCh   = gpio.PWM(rCh, pwmFreq)
		greenCh = gpio.PWM(gCh, pwmFreq)
		blueCh  = gpio.PWM(bCh, pwmFreq)
	except:
		print('GPIO setup failed')
	return strDevIn

#-----------------------------------------------------------------------
#      	sense Hat setup v0.2
# 		initialises the sense hat while checking if 
# 		devices are accessable
#		started: 17/12/2019 updated: 03/01/2020
#		comp tested:
#		Author: AH
#-----------------------------------------------------------------------
def SenseHatSetup(strDevIn):
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
		print('SenseHat setup failed')
	return strDevIn
#-----------------------------------------------------------------------
#      	Camera setup v0.1
# 		initialises camera and checks for connection 
#		started: 03/01/2020 updated:
#		comp tested:03/02/2020 
#		Author: AH
#-----------------------------------------------------------------------
def CameraSetup(strDevIn):
	try:
		cam = cv.VideoCapture(0)
		ret, frame = cam.read()
		if ret == True:
			strDevIn += " CAMERA"
	except:
		print("Camera setup failed")

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
if "CAMERA" in strDevIn:
	ret, frame = cam.read()
	b,g,r = cv.split(frame)
	blank = b - b

#audio properties 20 Hz - 20KHz to Hex
if "AUDIO" in strDevIn:
	intAudioRange = 20000 - 20
	intAlias = int(16777215/intAudioRange)

#bluetooth properties
if "BLUETOOTH" in strDevIn:
	print("bluetooth")


#-----------------------------------------------------------------------
#      	Main v0.3
# 		Main body for control software
#		started: 17/12/2019 updated: 03/01/2020
#		Author: AH
#-----------------------------------------------------------------------
while True:
	#on, off flag
	if "GPIO" in strDevIn:
		if GPIO.event_detected(switch, GPIO.RISING):
			boolOnState = True
		if GPIO.event_detected(switch, GPIO.FALLING):
			boolOnState = False
	else:
		boolOnState = False
	
	if "BLUETOOTH" in strDevIn:
		print("")

	if boolOnState == True:
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
			#pwm for analogue output (this is probably not correct)
			redCh.start(100)
			greenCh.start(1)
			blueCh.start(1)

			#change the duty cycle for different colours
			redCh.ChangeDutyCycle(r)
			greenCh.ChangeDutyCycle(g)
			blueCh.ChangeDutyCycle(b)
	
		if "BLUETOOTH" in strDevIn:
			#do bluetooth stuff plz
			print("")
			
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
	
		#troubleshooting only, not required for runtime (will likely fail in headless)
		try:
			backlight = cv.merge((blank+b, blank+g, blank+r))
			cv.imshow('image frame', frame)
			cv.imshow('backlight', backlight)
		except:
			print("Cannot show troubleshooting")
		print("loop complete")
	#adjust for higher/lower bitrates 
	cv.waitKey(1)
