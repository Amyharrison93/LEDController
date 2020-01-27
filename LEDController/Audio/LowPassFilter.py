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
