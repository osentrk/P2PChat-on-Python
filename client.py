import socket
soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = "192.168.1.23"
PORT = 5000

soket.connect((HOST,PORT))
data = soket.recv(1024)
data = data.decode()
print(data)
while True:


    k_msg = input("-> ")
    k_msg = k_msg.encode()
    soket.send(k_msg)

soket.close()

