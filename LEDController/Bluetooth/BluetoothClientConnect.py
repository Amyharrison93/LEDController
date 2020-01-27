#-----------------------------------------------------------------------
#      	bluetooth Communication Client v0.1
# 		connects to discovered device as a client
#		started: 07/01/2020
#		Comp tested:
#		Author: AH
#-----------------------------------------------------------------------
def BluetootConnectClient(strMessage, strAddress , intPort = 1):
	#convert input to string
	strMessage = str(strMessage)
	#set socket status
	socket = bt.BluetoothSocket(bt.RFCOMM)
	socket.connect((strAddress, intPort))
	#send string to device
	socket.send(strMessage)
	#close socket connection
	socket.close()

	return strDevIn