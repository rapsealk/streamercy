#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Message: ").encode("utf-8")
    total_amount = struct.pack(">I", len(message))
    sock.sendto(total_amount, ("127.0.0.1", 7000))
    sock.sendto(message, ("127.0.0.1", 7000))
    if message == "q".encode("utf-8"):
        break

print("Program will be terminated..")