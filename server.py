import socket
soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = "localhost"
PORT = 5000
soket.bind((HOST,PORT))

print ("Kullanıcı bekleniyor.")
soket.listen(1)
baglanti,adres = soket.accept()
print ("Bir bağlantı kabul edildi.", adres)
baglanti.send("Hoşgeldiniz efendim , hoşgeldiniz.")
data = baglanti.recv(1024)
print (data)
print(tes)
soket.close()