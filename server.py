#communicate with client
import socket
import sys
import storage
import inference

TCP_IP = '127.0.0.1'#localhost
TCP_PORT = 5000
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))
sock.listen(1)
connection, client_address = sock.accept()
while(1):
	data = connection.recv(BUFFER_SIZE)
	if not data: break
	print("received data: "+str(data))
	
	connection.send("do we have your consent to store the data?".encode())
	
	consent = connection.recv(BUFFER_SIZE)
	print(consent)

	if(consent):
		storage.store(str(data))

	response = inference.infer(data)
	
	connection.send(bytes(response))
connection.close()
