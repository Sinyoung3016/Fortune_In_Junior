from pylibpcap.pcap import sniff
from pylibpcap import get_iface_list

using_iface = get_iface_list()[0]

for plen, t, buf in sniff(using_iface, filters='ip src naver.com', count=10):
	print("[+]: Payload len=", plen)
	print("[+]: Time", t)
	print("[+]: Payload", buf)



