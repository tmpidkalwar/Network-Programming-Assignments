import socket

HOST = "94.142.241.111"  # The server's hostname or IP address
PORT = 23        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    msg = "Hello Server, This is the message from Client"
    s.send(msg.encode('ascii'))

    rmsg = s.recv(1024)
    print(rmsg.decode('ascii'))

s.close()