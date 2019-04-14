import socket
soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = "192.168.1.23"
PORT = 5000
soket.bind((HOST,PORT))

print ("Server is running on",PORT)
soket.listen(50)
baglanti,adres = soket.accept()
print ("Client is online:", adres) #information to server
msg = "Your connection is accepted." #info msg
msg = msg.encode()
baglanti.send(msg)
def getMsg():
    data = baglanti.recv(1024).decode()
    print("{}: {}".format(adres,data))

while True:
    getMsg()
