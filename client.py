import socket

soket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
soket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

username = input("Username: ")

HOST = "192.168.1.255"
PORT = 5000

while True:
    k_msg = input("{}: ".format(username))
    k_msg = k_msg.encode()
    soket.sendto(k_msg,(HOST,PORT))
