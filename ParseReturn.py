# import blescan
import os
import sys
import struct
 # import bluetooth._bluetooth as blue

report_pkt_offset = 0

def packed_bdaddr_to_string(bdaddr_packed):
     return ':'.join('%02x'%i for i in struct.unpack("<BBBBBB", bdaddr_packed[::-1]))


print("help")
pkt = b'\x01\x00\x00\x89S\xa2?#\xac\x1e\x02\x01\x06\x1a\xffL\x00\x02\x15\xb9@\x7f0\xf5\xf8Fn\xaf\xf9%UkW\xfem\x00d\x00e\xe8\xcb'
#iIndex = iResult.find ("23", 0)
#print("found here %d", iIndex)

Adstring = packed_bdaddr_to_string(pkt[report_pkt_offset + 3:report_pkt_offset + 9])

pkt2 = b'\xac#?\xa2S\x89'
pkt = b'\x89S\xa2?#\xac'

Adstring = ':'.join('%02x'%i for i in struct.unpack("<BBBBBB", pkt[::-1]))
print('1 '+Adstring)

mfstr = ':'.join('%02x'%i for i in struct.unpack("<BBBBBB", pkt2[::]))
print('2 '+mfstr)

mfstr = ':'.join('%02x'%i for i in struct.unpack("<BBBBBB", pkt2[::-1]))
print('3 '+mfstr)

mfstr = struct.unpack("<BBBBBB", pkt2[::-1])

# print('%02x'%i for i in struct.unpack("<BBBBBB", pkt2[::]))

for i in struct.unpack("<BBBBBB", pkt2[::-1]):
    mfstr = '%02x'%i
    print('4 '+mfstr)

print("next test")
print("")
mfstr = ':'.join('%02x'%i for i in struct.unpack("<BBBBBB", pkt2[::-1]))
print('5 '+mfstr)
