import socket
import json
import errno
from datetime import datetime
import sys
from pathlib import Path

#RED \033[91m
#ENDC \033[m
#GREEN \033[92m

clients = {}

try:
    with open(str(Path.home())+'/onlineList.json') as json_file:
        clients = json.load(json_file)
except:
    print("\033[91mOnline list cannot load from the file.\033[m")


def getInfo(ip):
    for x in clients:
        if(clients[str(x)]["ip_address"] == ip):
            global chatUser,chatIP
            chatUser = clients[str(x)]["username"]
            chatIP = clients[str(x)]["ip_address"]

def date():
    currentTime = datetime.now()
    dateFormat = str(currentTime.day) + "." + str(currentTime.month) + "." + str(currentTime.year) + " - " + str(currentTime.hour) + ":" + str(currentTime.minute) + ":" + str(currentTime.second)
    return dateFormat

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 5001
serverSocket.bind(("",PORT))
serverSocket.listen(1)
chatUser = ""
chatIP = ""

print("\033[92mI am waiting message!\033[m")
print("Chat log will be available on this location \033[91m"+str(Path.home())+"/\033[m after the conversation.")
while 1:

    try:
        connectionSocket, addr = serverSocket.accept()
        message = connectionSocket.recv(1024).decode()
        getInfo(addr[0])
        if(message == "exit"):
            print("\033[91m{} left the conversation.\033[m".format(chatUser))
        else:
            print("[{}] \033[91m{}\033[m: {}".format(date(),chatUser,message))
            try:
                home = str(Path.home())
                with open(home+"/"+chatUser +'_'+ chatIP +'.txt', 'a+') as chatLog:
                    chatLog.write("[{}] {}: {}\r\n".format(date(),chatUser,message))
            except:
                print("\033[91mChat log cannot write to file.\033[m")
        connectionSocket.close()
    except socket.error as e:
        if e.errno == errno.ECONNREFUSED:
            print("\033[91mConnection lost!\033[m")
        else:
            print("\033[91mThere is a problem, please try again.\033[m")
