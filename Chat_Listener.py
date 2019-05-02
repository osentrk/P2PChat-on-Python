import socket
import json

clients = {}

with open('onlineList.json') as json_file:
    clients = json.load(json_file)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 5001
serverSocket.bind(("",PORT))
serverSocket.listen(1)

chatUser = ""
chatIP = ""
def getInfo(ip):
    for x in clients:
        if(clients[str(x)]["ip_address"] == ip):
            global chatUser,chatIP
            chatUser = clients[str(x)]["username"]
            chatIP = clients[str(x)]["ip_address"]

while 1:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024)
    getInfo(addr[0])
    print("{}: {}".format(chatUser,message.decode()))
    connectionSocket.close()