import struct
from pylibpcap.pcap import sniff
from pylibpcap import get_iface_list

using_iface = get_iface_list()[0]

def split_header(data):
	ethernet_header = data[0:14]
	eth_header_parser(ethernet_header)
	ip_header = data[14:34]   
	seg = ip_header_parser(ip_header)
	if seg == '06':
		tcp_header = data[34:54]
		tcp_header_parser(tcp_header)
	elif seg == '11':
		udp_header = data[34:42]
		udp_header_parser(udp_header)


def eth_header_parser(data):
	ethernet_header = struct.unpack("!14c", data)

	src_ethernet_addr = list()
	dst_ethernet_addr = list()
	type_ethernet = list()
	for dst_i in ethernet_header[0:6]:
		dst_ethernet_addr.append(dst_i.hex())
	for src_i in ethernet_header[6:12]:
		src_ethernet_addr.append(src_i.hex())
	for type_i in ethernet_header[12:]:
		type_ethernet.append(type_i.hex())
 

	dst_ethernet_addr = ":".join(dst_ethernet_addr)
	src_ethernet_addr = ":".join(src_ethernet_addr)
	type_ethernet = "".join(type_ethernet)

	print("###### [ Ethernet_Header ] ######")
	print("Destination Address:", dst_ethernet_addr)
	print("Source Address:", src_ethernet_addr)
	print("Type:", "0x"+ type_ethernet)


def ip_header_parser(data):
	ip_header = struct.unpack("!20c", data)
	
	ip_total_len = list()
	ip_checksum = list()
	dst_ip_addr = list()
	src_ip_addr = list()
	
	for len_i in ip_header[2:4]:
		ip_total_len.append(len_i.hex())
	for sum_i in ip_header[10:12]:
		ip_checksum.append(sum_i.hex())
	for dst_i in ip_header[12:16]:
		dst_ip_addr.append(str(int(dst_i.hex(),16)))
	for src_i in ip_header[16:]:
		src_ip_addr.append(str(int(src_i.hex(),16)))

	dst_ip_addr = ":".join(dst_ip_addr)
	src_ip_addr = ":".join(src_ip_addr)
	ip_total_len = "".join(ip_total_len)
	ip_checksum = "".join(ip_checksum)


	print("###### [ Ip_Header ] ######")
	print("Version:", (int(ip_header[0].hex())//10))
	print("IHL (Header Length):", (int(ip_header[0].hex())%10))
	print("Total Length:",int(ip_total_len,16))
	print("Protocol:", ip_header[9].hex())
	print("Header Checksum:", "0x"+ip_checksum)
	print("Source Address:", src_ip_addr)
	print("Destination Address:", dst_ip_addr)

	return ip_header[9].hex()


def tcp_header_parser(data):
	tcp_header = struct.unpack("!20c", data)

	src_tcp_port = list()
	dst_tcp_port = list()
	tcp_seqno = list()
	tcp_acknowno = list()
	tcp_checksum = list()

	for dst_i in tcp_header[2:4]:
		dst_tcp_port.append(dst_i.hex())
	for src_i in tcp_header[0:2]:
		src_tcp_port.append(src_i.hex())
	for type_i in tcp_header[4:8]:
		tcp_seqno.append(type_i.hex())
	for type_i in tcp_header[8:12]:
		tcp_acknowno.append(type_i.hex())
	for type_i in tcp_header[16:18]:
		tcp_checksum.append(type_i.hex())
 
	dst_tcp_port = "".join(dst_tcp_port)
	src_tcp_port = "".join(src_tcp_port)
	tcp_seqno = "".join(tcp_seqno)
	tcp_acknowno = ''.join(tcp_acknowno)
	tcp_checksum = "".join(tcp_checksum)

	print("###### [TCP_Header] ######")
	print("Source Port:", int(src_tcp_port, 16))
	print("Destination Port:", int(dst_tcp_port, 16))
	print("Sequence Number:", int(tcp_seqno, 16))
	print("Acknowledgement Number:", int(tcp_acknowno, 16))
	print("Checksum:", "0x" + tcp_checksum)


def udp_header_parser(data):
	udp_header = struct.unpack("!8c", data)

	src_udp_port = list()
	dst_udp_port = list()
	udp_len = list()
	udp_checksum = list()

	for dst_i in udp_header[2:4]:
		dst_udp_port.append(dst_i.hex())
	for src_i in udp_header[0:2]:
		src_udp_port.append(src_i.hex())
	for type_i in udp_header[4:6]:
		udp_len.append(type_i.hex())
	for type_i in udp_header[6:]:
		udp_checksum.append(type_i.hex())
 
	dst_udp_port = "".join(dst_udp_port)
	src_udp_port = "".join(src_udp_port)
	udp_len = "".join(udp_len)
	udp_checksum = "".join(udp_checksum)

	print("###### [UDP_Header] ######")
	print("Source Port:", int(src_udp_port, 16))
	print("Destination Port:", int(dst_udp_port, 16))
	print("Length:", int(udp_len, 16))
	print("Checksum:", "0x" + udp_checksum)



if __name__ == '__main__':
	for plen, t ,buf in sniff(using_iface, count=3):
		split_header(buf)
		print("==================================")
 
