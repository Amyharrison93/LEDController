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
