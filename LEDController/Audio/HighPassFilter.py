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
