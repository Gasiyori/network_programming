import socket
import struct
import binascii

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!HH', self.src_port, self.dst_port)
        packed += struct.pack('!HH', self.length, self.checksum)
        return packed

def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:8])
    return unpacked

def getSrcPort(unpacked_Udpheader):
    return unpacked_Udpheader[0]

def getDstPort(unpacked_Udpheader):
    return unpacked_Udpheader[1]
    
def getLength(unpacked_Udpheader):
    return unpacked_Udpheader[2]

def getChecksum(unpacked_Udpheader):
    return unpacked_Udphdr[3]

Udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_Udphdr = Udp.pack_Udphdr()
print(binascii.b2a_hex(packed_Udphdr)) # 이진 출력

unpacked_Udphdr = unpack_Udphdr(packed_Udphdr)
print(unpacked_Udphdr)
print(f"Source Port:{getSrcPort(unpacked_Udphdr)} Destination Port:{getDstPort(unpacked_Udphdr)} Length:{getLength(unpacked_Udphdr)} Checksum:{getChecksum(unpacked_Udphdr)}")