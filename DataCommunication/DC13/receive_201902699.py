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


def hex_ip(data):
	ret = ''
	data = data.split('.')
	for x in data:
		x = hex(int(x))[2:]
		for i in range(2-len(x)):
			x = '0' + x
		ret += x
	return ret
	
	
def hex_(data, l):
	data = hex(int(data))[2:]
	for i in range(l-len(data)):
		data = '0' + data
	return data


def hex_d(data):
	return ''.join(hex(ord(x))[2:] for x in data)


def checksum(src_ip, dst_ip, zero, protocol, udplen, src_p, dst_p, cs, data):
	precs = hex_ip(src_ip)+hex_ip(dst_ip)+hex_(zero,2)+hex_(protocol,2)+hex_(udplen,4)+hex_(src_p,4)+hex_(dst_p,4)+hex_(udplen,4)+hex_(cs,4)+hex_d(data)
	
	total = 0
	for i in range(len(precs)//2):
		data = precs[2 * i:2 * i + 2]
		hex_data = hex(ord(data[0])) + hex(ord(data[1]))[2:]
		total = int(hex(total), 16) + int(hex_data, 16)
		
		if total > 0xffff:
			carry = (total & 0xf0000) >> 16
			sum = total & 0xffff
			total = sum + carry
			
	t = total
	total = ~total
	total = total & 0xffff
	
	return hex(total)


def check_checksum(cum):
	cs = checksum(cum[1] ,cum[2] ,cum[3] ,cum[4] ,cum[5] ,cum[6] ,cum[7] , '0', cum[10])
	if cs != cum[9]:
		print(">Checksum Error")
		s.close()
		sys.exit()
		
	return cs


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
        valid_data, addr = s.recvfrom(1024)
        exist_data, addr = s.recvfrom(1024)
        if valid_data.decode() == "valid list command" and exist_data.decode() == "file exist!":
            write_file = open(cmd[1], 'wb')
            chunk_size_l, addr = s.recvfrom(2048)
            chunk_size_l = chunk_size_l.decode().split('`')
            check_checksum(chunk_size_l)
            chunk_size = int(chunk_size_l[-1])
            
            s.sendto("READY".encode(), (host, int(port)))
            
            #receive data
            print("----------------------------")
            
            #error2
            #er = True
            write_data_l = []
            ark = '1'
            for i in range(chunk_size):
                while True:
                    try:
                        write_data_l, addr = s.recvfrom(2048)
                        write_data_l = write_data_l.decode().split('`')
                        ark_r = write_data_l[0]
                        if ark_r == '0':
                            ark = '1'
                        else:
                            ark = '0'
                        #good_cond
                        s.sendto(ark.encode(), (host, int(port)))
                        break
                        #error2
                        #if i == 0 and er:
                        #    s.sendto(ark.encode(), ('127.0.0.3', 6000))
                        #    er = False
                        #else:
                        #    s.sendto(ark.encode(), (host, int(port)))
                        #    break
                    except socket.timeout:
                        print("===============================================")
                        print("timeout! send to server NAK")
                        print("===============================================")
                        s.sendto('NAK'.encode(), (host, int(port)))
            
                cs = check_checksum(write_data_l)
                
                print("> received ack index", ark_r)
                print("    received checksum", write_data_l[-2])
                print("    new calculated checksum", cs)
                print("    received Packet : number", i + 1)
                print("> send ark index", ark)
                
                write_data = write_data_l[-1]
                write_file.write(write_data.encode())

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
        s.sendto(file_name.encode(), (host, int(port)))
        s.close()
        sys.exit()

