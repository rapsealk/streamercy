#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 7000))

while True:
    data, addr = sock.recvfrom(4)
    total_amount = struct.unpack(">I", data)[0]
    print("addr: %s, data: %d bytes" % (addr, total_amount))
    data, addr = sock.recvfrom(total_amount)
    data = data.decode("utf-8")
    print("addr: %s, data: %s" % (addr, data))
    if data == "q":
        break

print("Program will be terminated..")