#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cv2
import sys
import socket
import struct
import numpy as np
import time
from util import *
from functools import reduce

EXPECTED_BYTES = reduce(lambda x, y: x * y, IMAGE_SIZE)
NUMBER_OF_CHUNKS = int(EXPECTED_BYTES / PACKET_SIZE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 7000))

last_timestamp = time.time()
while True:
    chunk, addr = sock.recvfrom(PACKET_SIZE)
    if not chunk.startswith(HEADER_FLAG.encode("utf-8")):
        sys.stdout.write("chunk: %s\n" % chunk)
        continue
    buffer = [sock.recv(PACKET_SIZE) for _ in range(NUMBER_OF_CHUNKS)]
    buffer = b''.join(buffer)
    frame = np.frombuffer(buffer, dtype=np.uint8).reshape(IMAGE_SIZE[0], IMAGE_SIZE[1], IMAGE_SIZE[2])
    cv2.imshow('cv_server', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Program will be terminated..")
cv2.destroyAllWindows()