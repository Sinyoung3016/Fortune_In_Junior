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
		#print("[a]", data,  ">" , hex_data)
		total = int(hex(total), 16) + int(hex_data, 16)
		#print("[b]", hex(total), "+" , hex_data, "=", hex(total))
		
		if total > 0xffff:
			carry = (total & 0xf0000) >> 16
			sum = total & 0xffff
			total = sum + carry
			#print("[c]", hex(carry) , "+" , hex(sum), "=", total)
			
	t = total
	total = ~total
	total = total & 0xffff
	#print("[e]" , hex(t), ">", hex(total))
	
	return hex(total)
			                                                
	
def sender_send(file_name,client_addr):
    s.sendto("valid list command".encode(), client_addr)
    if os.path.isfile(file_name):
        s.sendto("file exist!".encode(), client_addr)
        
        #chunk size
        file_size = os.stat(file_name).st_size
        chunk_size = file_size // 1024 + 1
        data = str(chunk_size)
        src_ip = s.getsockname()[0]
        dst_ip = client_addr[0]
        src_p = '8000'
        dst_p = str(client_addr[1])
        
        cs = checksum(str(src_ip) ,str(dst_ip) ,'0' ,'17' ,str(8+len(data)) ,src_p ,dst_p ,'0' ,str(data))
        data = '0' + '`' + src_ip+'`'+dst_ip+'`'+'0'+'`'+'17'+'`'+str(8+len(data))+'`'+src_p+'`'+dst_p+'`'+str(8+len(data))+'`'+cs+'`'+str(data)
        s.sendto(data.encode(), client_addr)
        print("----------------------------")
        print(">File name :", file_name)
        print(">> File Size :", file_size)
        s.recvfrom(1024)
        
		#send data
        read_file = open(file_name, 'rb')
        
        ark = '0'
        for i in range(chunk_size):
            data = read_file.read(1024)
            cs = checksum(str(src_ip) ,str(dst_ip) ,'0' ,'17' ,str(8+len(data)) ,src_p ,dst_p ,'0' ,str(data))
            data = ark + '`' + src_ip+'`'+dst_ip+'`'+'0'+'`'+'17'+'`'+str(8+len(data))+'`'+src_p+'`'+dst_p+'`'+str(8+len(data))+'`'+cs+'`'+str(data)
            #good_cond
            s.sendto(data.encode(), client_addr)
            #error1
            #if i == 0:
            #    s.sendto(data.encode(), ('127.0.0.1',6000))
            #else:
            #    s.sendto(data.encode(), client_addr)
            ###
            print(">  send ack index :", ark)
            while True:
                try:
                    ark_r, client_addr = s.recvfrom(1024)
                    if ark_r.decode() == 'NAK':
                        raise 
                    elif ark_r.decode() == '1':
                        ark = '1'
                    else:
                        ark = '0'
                    print(">  received ack index :", ark_r.decode())
                    break
                except socket.timeout:
                    print("===============================================")
                    print("timeout! not received packet! resend about prev packet!")
                    print("===============================================")
                    s.sendto(data.encode(), client_addr)
                    print(">  send ack index :", ark)
                except : #nak
                    s.sendto(data.encode(), client_addr)
                    print(">  send ack index :", ark)
                	
            print(">  Send Packet : number", i+1)
			
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
        data, client_addr = s.recvfrom(1024)
    except ConnectionResetError:
        print("error. port number not matching.")
        sys.exit()

    print(">Client와 연결되었습니다.")

    while True:
        text = data.decode('utf8')
        handler = text.split()

        if handler[0] == 'receive':
            sender_send(handler[1], client_addr)
            try:
                data, client_addr = s.recvfrom(1024)
            except ConnectionResetError:
                print("error. port number not matching.")
                sys.exit()

        elif handler[0] == 'exit':
            s.close()
            sys.exit()


