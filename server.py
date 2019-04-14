import socket
soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = "localhost"
PORT = 5000
soket.bind((HOST,PORT))

print ("Server is running on",PORT)
soket.listen(50)
baglanti,adres = soket.accept()
print ("Client is online:", adres)
msg = "Your connection is accepted."
msg = msg.encode()
baglanti.send(msg)
data = baglanti.recv(1024)
print (data)
