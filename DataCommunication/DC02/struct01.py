import struct

number = 36 
number_bytes = number.to_bytes(4, byteorder="big")

decode_number = struct.unpack("!i", number_bytes)

print("Origin Data : ", number_bytes)
print("Decode Data : ", decode_number[0])
