#CLASS LIST
import socket
import json
import time
serviceSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serviceSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

ip = socket.gethostbyname(socket.gethostname()).split(".")
ip = "{}.{}.{}.255".format(ip[0],ip[1],ip[2])

HOST = ip
PORT = 5000

username = input("What is your username?: ")
client = {
    "username":username,
    "ip_address":ip
}
jsonData = json.dumps(client)
while True:
    print("You are online!")
    serviceSocket.sendto(jsonData.encode(),(HOST,PORT))
    time.sleep(60)