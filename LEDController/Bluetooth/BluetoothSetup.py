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
