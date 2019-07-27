#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import numpy as np
from framer import PiCameraFramer

IMAGE_WIDTH = 1280
IMAGE_HEIGHT = 720
IMAGE_SIZE = (IMAGE_WIDTH, IMAGE_HEIGHT)

PACKET_BYTES = 4096
DESTINATION = ("192.168.35.9", 7000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
f = PiCameraFramer(size=IMAGE_SIZE)
generator = f.capture()

while True:
    frame = next(generator)
    frame = np.array(frame)
    frame = frame.tostring()
    total_bytes = len(frame)
    print("total_bytes: %d, packet_bytes: %d" % (total_bytes, PACKET_BYTES))
    for i in range(total_bytes // PACKET_BYTES):
        sock.sendto(frame[i*PACKET_BYTES:(i+1)*PACKET_BYTES], DESTINATION)
    #sock.sendto(frame.tostring(), ("192.168.35.9", 7000))

print("Close")
