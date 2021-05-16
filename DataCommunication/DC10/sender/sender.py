import socket
import os
import sys
import hashlib

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", 8000))

except socket.error:
    print("failed to create socket")
    sys.exit()


def sender_send(file_name):
    s.sendto("valid list command".encode(), client_addr)

    if os.path.isfile(file_name):
        s.sendto("file exist!".encode(), client_addr)
        file_size = os.stat(file_name).st_size
        chunk_size = file_size // 4096 + 1
        s.sendto(str(chunk_size).encode(), client_addr)
        print("----------------------------")
        print(">File name :", file_name)
        print(">>>File Size :", file_size)

        s.recvfrom(4096)
        read_file = open(file_name, 'rb')
        for i in range(chunk_size):
            chunk_file = read_file.read(4096)
            s.sendto(chunk_file, client_addr)
            print(">>>Send Packet : number", i+1)
        print(">>Send All Packet")
        print("----------------------------")

    else:
        s.sendto("file not exist!".encode(), client_addr)
        print("----------------------------")
        print(">File name :", file_name)
        print(">File not exist!")
        print("----------------------------")


if __name__ == "__main__":

    try:
        data, client_addr = s.recvfrom(4096)
    except ConnectionResetError:
        print("error. port number not matching.")
        sys.exit()

    print(">Client와 연결되었습니다.")

    while True:
        text = data.decode('utf8')
        handler = text.split()

        if handler[0] == 'receive':
            sender_send(handler[1])

            try:
                data, client_addr = s.recvfrom(4096)
            except ConnectionResetError:
                print("error. port number not matching.")
                sys.exit()

        elif handler[0] == 'exit':
            s.close()
            sys.exit()


