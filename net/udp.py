#!/usr/bin/python3
# -*- coding: utf-8 -*-

__all__ = ["Client"]

import socket
import struct

class Server:

    def __init__(self, port):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(("0.0.0.0", self.port))

    def run(self):
        while True:
            try:
                divmod
            except Exception as e:
                print(e)
                break
        print("UDP Server is going to terminated..")

class Client:

    def __init__(self, addr):
        self.addr = addr
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, message):
        if type(message) == str:
            message = message.encode("utf-8")
        assert(type(message) == bytes)

        # FIXME: Right way to use UDP?
        # 4-bytes message size header
        #header = struct.pack(">I", len(message))
        #self.socket.sendto(header, self.addr)
        self.socket.sendto(message, self.addr)