# coding: utf-8

import socket
from fcntl import ioctl
from struct import pack

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        pack('256s', bytes(ifname[:15], 'utf-8'))
    )[20:24])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((get_ip_address("eth0"), 0))
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
