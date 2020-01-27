#-----------------------------------------------------------------------
#      	GPIO setup v0.2
# 		initialises the GPIO while checking if GPIO are accessable
#		started: 17/12/2019 updated: 03/01/2020
#		comp tested:
#		Author: AH
#-----------------------------------------------------------------------
def GPIOSetup(strDevIn, arryPins):
	try:
		import RPI.GPIO as gpio
		#set pins
		intCount = 0
		intNoPins = len(arryPins)

		for intCount in range(0, intNoPins):
			if "OUT" in arryPins[intCount][1]: 
				#set mode out
				gpio.setup(arryPins[0] ,GPIO.OUT)
			if "IN" in arryPins[intCount][1]:
				#set mode in 
				gpio.setup(arryPins[0], GPIO.IN, pull_up_down=GPIO.PUD_UP)

		strDevIn += " GPIO"
		print("GPIO setup Seccess")
	except:
		print('GPIO setup failed')
	return strDevIn
