import socket

# take the server name and port name
host = 'local host'

# create a socket at server side
# using TCP / IP protocol
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print ("> Socket successfully created")
except socket.error as err: 
    print ("> Socket creation failed with error %s" %(err))

port = 5000

# bind the socket with server
# and port number
s.bind(('', port))
print ("> Socket binded to %s" %(port)) 

# allow maximum 1 connection to
# the socket
s.listen(1)
print ("> Socket is listening")            

while True: 
 
    # Establish connection with client. 
    c, addr = s.accept()     
    print ('> Got connection from', addr )
    
    # Say hello
    c.send('Gracias por conectarse a Lachiwa. Sientase segurx de contarnos sus secretos.'.encode()) 

    # receive message string from
    # server, at a time 1024 B
    msg = c.recv(1024)
    
    print("")

    # repeat as long as message
    # string are not empty
    while msg:
        print('Received: ' + msg.decode())
        msg = c.recv(1024)
 
    # Close the connection with the client 
    c.close()   
    
    # Breaking once connection closed
    # break