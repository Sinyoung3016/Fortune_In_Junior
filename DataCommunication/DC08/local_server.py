import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('',8000))
print("[Connecting..]")

data, addr = server_socket.recvfrom(2000)
print(addr[0], " :: ", data.decode())

while True :
	msg = input(">>> ")
	server_socket.sendto(msg.encode(), (addr))

	data, addr = server_socket.recvfrom(2000)
	print(addr[0], " :: ", data.decode())

