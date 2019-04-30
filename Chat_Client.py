import socket
import json

clients = {}

with open('onlineList.json') as json_file:
    clients = json.load(json_file)


def onlineList():
    print("ONLINE LIST")
    for i in clients:
        print(i)
        print("{} {}".format(clients[str(i)]["username"],clients[str(i)]["ip_address"]))
    print("----------------------------------")

def control(u):
    isOnline = False
    for x in clients:
        if(clients[str(x)]["username"] == u):
            print("IP bulundu {}".format(u))
            connect(clients[str(x)]["ip_address"])
            isOnline = True
    if(isOnline == False):
        print("{} is not online.".format(u))

def connect(ip):

    TCPHost = ip
    print(TCPHost)
    TCPPort = 5001
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSocket.settimeout(5.0)
    try:
        tcpSocket.connect((TCPHost, TCPPort))
        print("You will chat with {}".format(ip))
        while 1:
            tm = input("> ")
            if (tm == "exit"):
                break;
            tcpSocket.send(tm.encode())
            tcpSocket.close()
    except:
        print("User is offline!")
        tcpSocket.close()


if __name__ == '__main__':
    while True:
        onlineList()
        getUsername = input("Connect to: ")
        control(getUsername)










# import socket
#
# s = socket.socket()
# s.settimeout(5)   # 5 seconds
# try:
#     s.connect(('123.123.123.123', 12345))         # "random" IP address and port
# except socket.error, exc:
#     print "Caught exception socket.error : %s" % exc