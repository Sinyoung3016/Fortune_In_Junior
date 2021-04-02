import struct

ip_data = b'\xa8\xbc\x80\xff'

decode_number = struct.unpack("!4c", ip_data)
print("Origin Data :", ip_data)

ip_list = list()
for n in decode_number:
	ip_list.append(str(int(n.hex(), 16)))
print("Decode Data :", ". ".join(ip_list))
