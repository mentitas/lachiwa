import socket
from mail_server import send_email

# take the server name and port name
host = 'local host'

# mail variables
sender_email   = "mail-server@lachiwa.com"
receiver_email = "client@example.com"

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
    msg = "Gracias por confiar en Lachiwa. Sientase segurx de contarnos sus secretos"
    print("Sent: " + msg)

    c.send(msg.encode())

    # receive message string from
    # server, at a time 1024 B
    msg = c.recv(1024)
    
    print("")

    whole_msg = "Se recibió un secreto desde la IP " + str(addr[0]) + ":\n"

    # repeat as long as message
    # string are not empty
    while msg:
        print('Received: ' + msg.decode())
        whole_msg += msg.decode()
        msg = c.recv(1024)

    send_email(sender_email, receiver_email, "Hemos recibido un secreto desde la IP " + str(addr[0]), whole_msg)

    # Close the connection with the client 
    c.close()   
    
    # Breaking once connection closed
    break