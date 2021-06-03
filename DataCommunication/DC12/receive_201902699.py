import socket
import os
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setblocking(0)
    s.settimeout(15)
except socket.error:
    print("failed to create socket")
    sys.exit()

if len(sys.argv) == 3:
    host = sys.argv[1]
    port = sys.argv[2]
else:
    print(">입력이 잘못되었습니다.")
    sys.exit()

file_name = input("enter a command: \n1.receive [filed_name] \n2.exit\n")

while True:
    cmd = file_name.split()
    if cmd[0] == 'receive':
        s.sendto(file_name.encode(), (host, int(port)))
        valid_data, addr = s.recvfrom(4096)
        exist_data, addr = s.recvfrom(4096)
        if valid_data.decode() == "valid list command" and exist_data.decode() == "file exist!":
            write_file = open(cmd[1], 'wb')
            chunk_size, addr = s.recvfrom(4096)
            chunk_size = int(chunk_size.decode())
            print("----------------------------")
            s.sendto("ready".encode(), (host, int(port)))
            for i in range(chunk_size):
                write_data, addr = s.recvfrom(4096)
                print(">>>Received Packet : number", i + 1)
                write_file.write(write_data)

            write_file.close()
            print(">>Receive All Packet")
            print(">>New File (", cmd[1], ")")
            print("----------------------------")
        else:
            print("----------------------------")
            print(">>Invalid Command")
            print("----------------------------")
        file_name = input("Enter a command: \n1.receive [filed_name] \n2.exit\n")

    elif cmd[0] == 'exit':
        print(">종료합니다.")
        s.close()
        sys.exit()

