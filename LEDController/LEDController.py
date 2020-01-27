#!/usr/bin/env python3
import numpy as np
import cv2 as cv
import subprocess as os
import numpy as np

strDevIn = ""

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
	arryLED ="","CMD656TVT2"
	strDevIn, intAlias, arryBlank = Setup("", arryDevice)

	strDevFlag = "AUDIO"
	strOutFlag = "BLUETOOTH"

	#start main loop
	while True:
		#hardware on/off flag
		if("GPIO" in strDevIn):
			if GPIO.event_detected(switch, GPIO.RISING):
				boolOnState = True
			if GPIO.event_detected(switch, GPIO.FALLING):
				boolOnState = False
		else:
			boolOnState = False

		#bluetooth on/off flag
		if("BLUETOOTH" in strDevIn):
			#check bluetooth packet
			boolOnState != boolOnState
		else:
			boolOnState = False

		#check if on 
		if boolOnState == true:
			if("BLUETOOTH" in strDevIn):
				#check connection with host
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
					hexCamColour = r << 32 | g << 16 | b << 0

				if("AUDIO" in strDevIn) and ("AUDIO" in strDevFlag):
					#read audio device
					inAaudio = stream.read(CHUNK)
				
					#filter into R, G, B values
					r = HighPass(inAudio) >> 32
					g = MidPass(inAudio) >> 16
					b = LowPass(inAudio) >> 0

					hexAudioColour = HighPass(inAudio) | MidPass(inAudio) | LowPass(inAudio)

				if "GPIO" in strDevIn:
					#change the duty cycle for different colours
					redCh.ChangeDutyCycle(r)
					greenCh.ChangeDutyCycle(g)
					blueCh.ChangeDutyCycle(b)
	
				if "BLUETOOTH" in strDevIn:
					#do bluetooth stuff plz
					print("")
	
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
