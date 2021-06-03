import socket

ip_addr = "172.30.1.41"
port = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("[Connect]")

while True :
	msg = input(">>> ")
	client_socket.sendto(msg.encode(), (ip_addr, int(port)))

	data, addr = client_socket.recvfrom(2000)
	print(addr[0], " :: ", data.decode())

