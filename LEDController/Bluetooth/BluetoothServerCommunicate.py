#-----------------------------------------------------------------------
#      	Bluetooth communication server v0.1
# 		communicate information over bluetooth as server
#		started: 13/01/2020 updated: 
#		Author: AH
#-----------------------------------------------------------------------
def BtCommunicateServer(strMessage, intPort = 1):
	#set socket status
	socket = bt.BluetoothSocket(bt.RFCOMM)
	socket.bind(("", intPort))
	socket.listen(1)

	#find client details 
	strClientSock, strAddress = socket.accept()

	#receive message from client
	strMessage = socket.recv(1024)

	return strMessage
