#!/usr/bin/env python3
import numpy as np
import cv2 as cv 
import subprocess as os
import numpy as np

strDevIn = ""
#-----------------------------------------------------------------------
#      	High pass filter v0.1
# 		integrates filtering for colour channels 
#		started: 07/01/2020 
#		Comp tested: 
#		Author: AH
#-----------------------------------------------------------------------
def HighPass(inAudio):
	#filter the sinal
	if inAudio < (6340*2):
		inAudio = 0
	else:
		inAudio = inAudio - (6340*2)
	
	#calculate the hex colour 255
	if inAudio > 0:
		intHighPass = int(inAudio/24.862745098)
		if intHighPass > 255:
			intHighPass = 255
	#output hex value
	hexHighPass = intHighPass << 32

	return hexHighPass

#-----------------------------------------------------------------------
#      	mid pass filter v0.1
# 		integrates filtering for colour channels 
#		started: 07/01/2020 
#		Comp tested: 
#		Author: AH
#-----------------------------------------------------------------------
def MidPass(inAudio):
	if inAudio > 6340:
		inAudio = 0
	if inAudio > 6340:
		inAudio = 0
	
	#calculate the hex colour 255
	if(inAudio > 0) & (inAudio < 6340*2):
		intMidPass = int(inAudio/24.862745098)
		if intLowPass > 255:
			intLowPass = 255

	#output hex value
	hexMidPass = intMidPass << 16
	return hexMidPass

#-----------------------------------------------------------------------
#      	Low pass filter v0.1
# 		integrates filtering for colour channels 
#		started: 07/01/2020 
#		Comp tested: 
#		Author: AH
#-----------------------------------------------------------------------
def LowPass(inAudio):
	if inAudio > 6340:
		inAudio = 0
	
	#calculate the hex colour 255
	if inAudio > 0:
		intLowPass = int(inAudio/24.862745098)
		if intLowPass > 255:
			intLowPass = 255

	#output hex value
	hexLowPass = intLowPass << 0
	return hexLowPass

#-----------------------------------------------------------------------
#      	raspotify setup v0.2
# 		initialises rasppotify to ensure service is running
#		started: 03/01/2020 
#		Comp tested: 03/01/2020
#		Author: AH
#-----------------------------------------------------------------------
def ServiceStart(strService = "raspotify"):
	try:
		status = os.system('service {} status'.format(strService))

		strCommand = "sudo systemctl restart {0}".format(strService)
		os.system(strCommand)

		print("RASPOTIFY setup Seccess")
	except:
		print("service failed to start")

#-----------------------------------------------------------------------
#      	bluetooth setup v0.2
# 		initialises bluetooth while checking if devices are accessable
#		started: 17/12/2019 updated: 03/01/2020 
#		Comp tested: 03/01/2020
#		Author: AH
#-----------------------------------------------------------------------
def BluetoothSetup(strDevIn, arryKnownDevice):
	try:
		import bluetooth as bt
		arryDevices = bt.discover_devices(lookup_names = True)		

		#check if the known device is found
		for intCount in range(0, len(arryDevices)):
			if arryDevices[intCount] == arryKnownDevice:
				strDevIn += " BLUETOOTH"
				
				break
		if not (" BLUETOOTH" in strDevIn):
			print("no bluetooth devices found")
		print("BLUETOOTH setup Seccess")
	except:
		print("Bluetooth setup failed")
	return strDevIn

#-----------------------------------------------------------------------
#      	bluetooth connect to device v0.1
# 		connects to discovered device
#		started: 07/01/2020
#		Comp tested:
#		Author: AH
#-----------------------------------------------------------------------
def BluetootConnect():
		
	socketServer.bind(("",port))
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
		print("AUDIO setup Seccess")
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
def GPIOSetup(strDevIn):
	try:
		import RPI.GPIO as gpio
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
		strDevIn += " GPIO"
		print("GPIO setup Seccess")
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
		strDevIn += " SENSE-HAT"
		print("SENSE-HAT setup Seccess")
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
	cam = 0
	try:
		cam = cv.VideoCapture(0)
		ret, frame = cam.read()
		if ret == True:
			strDevIn += " CAMERA"
			print("CAMERA setup Seccess")
	except:
		print("Camera setup failed")

	return strDevIn, cam

#-----------------------------------------------------------------------
#      	setup v0.1
# 		initialises all
#		started: 03/01/2020 updated: 
#		Author: AH
#-----------------------------------------------------------------------
def Setup(strDevIn, arryKnownDevice):

	intAlias = 0
	arryBlank = [0,0]

	print("Running Startup")
	ServiceStart()
	strDevIn = BluetoothSetup(strDevIn, arryKnownDevice)
	strDevIn = AudioSetup(strDevIn)
	strDevIn = GPIOSetup(strDevIn)
	strDevIn = SenseHatSetup(strDevIn)
	strDevIn, cam = CameraSetup(strDevIn)
	print("Startup finished devices available: {}".format(strDevIn))

		#frame properties
	if "CAMERA" in strDevIn:
		ret, frame = cam.read()
		arryBlank = frame[:,:,0] - frame[:,:,0]

	#audio properties 20 Hz - 20KHz to Hex
	if "AUDIO" in strDevIn:
		intAudioRange = 20000 - 20

	#bluetooth properties
	if "BLUETOOTH" in strDevIn:
		#connect to device
		BluetootConnect()

		print("bluetooth")

	return strDevIn, intAlias, arryBlank

#-----------------------------------------------------------------------
#      	Main v0.3
# 		Main body for control software
#		started: 17/12/2019 updated: 07/01/2020
#		Author: AH
#-----------------------------------------------------------------------
def main(args):
	print("Entering Main")
	#start service
	arryDevice = "D4:11:A3:96:D0:AA", "What's a phone"
	strDevIn, intAlias, arryBlank = Setup("", arryDevice)

	#start main loop
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

				#average colour channels
				b = int(np.mean(frame[:,:,0]))
				g = int(np.mean(frame[:,:,1]))
				r = int(np.mean(frame[:,:,2]))

				#shift bits to make hex value
				hexColour = r << 32 | g << 16 | b << 0

			if "AUDIO" in strDevIn:
				#read audio device
				inAaudio = stream.read(CHUNK)
				
				#filter into R, G, B values
				r = HighPass(inAudio) >> 32
				g = MidPass(inAudio) >> 16
				b = LowPass(inAudio) >> 0

				hexColour = HighPass(inAudio) | MidPass(inAudio) | LowPass(inAudio)

			if "GPIO" in strDevIn:
				#pwm for analogue output (this is probably not correct)
				redCh.start(1)
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
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
