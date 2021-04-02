import struct
from pylibpcap.pcap import sniff
from pylibpcap import get_iface_list

using_iface = get_iface_list()[0]

def split_header(data):
	ethernet_header = data[0:14]
	eth_header_parser(ethernet_header)

def eth_header_parser(data):
	ethernet_header = struct.unpack("!14c", data)

	src_ethernet_addr = list()
	dst_ethernet_addr = list()
	for dst_i in ethernet_header[0:6]:
		dst_ethernet_addr.append(dst_i.hex())
	for src_i in ethernet_header[6:12]:
		src_ethernet_addr.append(src_i.hex())

	ip_header = ethernet_header[12:][0].hex() 

	dst_ethernet_addr = ":".join(dst_ethernet_addr)
	src_ethernet_addr = ":".join(src_ethernet_addr)

	print("###### [ Ethernet_header ] ######")
	print("dst_mac_address:", dst_ethernet_addr)
	print("src_mac_address:", src_ethernet_addr)
	print("ip_version:", "0x"+ip_header)


if __name__ == '__main__':
	for plen, t ,buf in sniff(using_iface, count=3):
		split_header(buf)
		print("==================================")
 
