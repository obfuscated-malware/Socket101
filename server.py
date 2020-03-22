#usr/bin/python

#Learning 101 - AnkushJain(Obfuscated_Malware) Simple Socket Server Echo Program can be connected using Netcat.

import socket
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpSocket.bind(("0.0.0.0", 8000))

tcpSocket.listen(2)

print ("Waiting for a client....")

(client, (ip,soc)) = tcpSocket.accept()

print ("Receiveed Connection from: ", ip)
print ("Starting Server....")
data = 'dummy'

while len(data):
	data = client.recv(2048)
	print ("Client sent: ",data)
	client.send(data)

print ("Closing Connection....")
client.close()
