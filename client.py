import socket

# take the server name and port name
host = 'local host'
port = 5000

# create a socket at client side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect it to server and port 
# number on local computer.
s.connect(('127.0.0.1', port))

print('Received: ' + s.recv(1024).decode())

# send message to the client after 
# encoding into binary string
s.send(b"Mi secreto es que no me gusta la polenta.\n")

# disconnect the client
s.close()