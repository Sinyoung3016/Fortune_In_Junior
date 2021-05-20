import socket
import random

game = ['rock','scissor','paper'] #rock, scissor, paper

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('',9000))
print("[Connecting..]")

data, addr = server_socket.recvfrom(2000)
msg = game.index(random.choice(game))
rec = data.decode().split("+")
print(rec[0], " : ", rec[1])
rec = rec[1]
answer = ''
if msg == 0: #rock
    if rec == 'a':
        answer = "DRAW"
    elif rec == 'b':
        answer = "LOSE"
    elif rec == 'c':
        answer = "WIN"
elif msg == 1: #scissor
    if rec == 'a':
        answer = "WIN"
    elif rec == 'b':
        answer = "DRAW"
    elif rec == 'c':
        answer = "LOSE"
elif msg == 2: #paper
    if rec == 'a':
        answer = "LOSE"
    elif rec == 'b':
        answer = "WIN"
    elif rec == 'c':
        answer = "DRAW"

print("[Finsh]")
server_socket.sendto(answer.encode(), (addr))
server_socket.close()                    
