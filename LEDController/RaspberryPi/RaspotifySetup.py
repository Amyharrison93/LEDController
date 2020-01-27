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

