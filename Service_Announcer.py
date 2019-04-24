import socket
import json
import time
serviceSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serviceSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
HOST = "192.168.1.255"
PORT = 5000

username = input("What is your username?: ")
client = {
    "username":username,
    "ip_address":"192.168.1.15"
}
jsonData = json.dumps(client)
while True:
    print("You are online!")
    serviceSocket.sendto(jsonData.encode(),(HOST,PORT))
    time.sleep(60)