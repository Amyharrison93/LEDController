#-----------------------------------------------------------------------
#      	audio setup v0.2
# 		initialises the audio while checking if audio is accessable
#		started: 17/12/2019 updated: 03/01/2020 
#		comp tested:
#		Author: AH
#-----------------------------------------------------------------------
def AudioSetup(strDevIn, intChunk = 1024, intChannels = 2, intRate = 44100):
	try:
		import pyaudio
		FORMAT = pyaudio.paInt16
		p = pyaudio.PyAudio()

		stream = p.open(format=FORMAT,
			channels=intChannels,
			rate=intRate,
			input=True,
			frames_per_buffer=intChunk)

		strDevIn += " AUDIO"
		print("AUDIO setup Seccess")
	except:
		print("Audio setup failed")
	return strDevIn