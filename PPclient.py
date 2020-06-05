# coding: utf-8

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((socket.gethostbyname(socket.gethostname()), 0))
sock.setblocking(True)
server = ("192.168.0.17", 9002)

sock.sendto(("Postavte zachet)) Pojalusta...").encode("utf-8"), server)
data, addr = sock.recvfrom(1024)
data = data.decode("utf-8")
print(data)

f = open("/home/sm/.ssh/id_rsa.pub", 'r')
key = f.read()
sock.sendto(key.encode("utf-8"), server)
f.close()

for x in range(2):
	data, addr = sock.recvfrom(1024)
	data = data.decode("utf-8")
	print(data)

sock.close()
