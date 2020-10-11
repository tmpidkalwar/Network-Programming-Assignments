import socket

HOST = "94.142.241.111"
PORT = 23

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.bind((HOST, PORT))
s.listen(5)
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        rmsg = conn.recv(1024)
        if not rmsg:
            break
        print(rmsg.decode("ascii"))

        msg = "Hello Client, This is Server"
        conn.send(msg.encode("ascii"))

s.close()