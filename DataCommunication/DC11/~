import socket
import random

ip_addr = "3.35.21.46"
port = 9000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("[Connect] Game Start")

print("> Write : student_id + a(rock), b(scissor), c(paper)")
msg = input(">>>")
client_socket.sendto(msg.encode(), (ip_addr, int(port)))

data, addr = client_socket.recvfrom(2000)
print("> Result : ", data.decode())
client_socket.close()

