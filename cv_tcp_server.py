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

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 7000))
sock.listen(1)

conn, addr = sock.accept()

last_timestamp = time.time()
while True:
    chunk = conn.recv(4)
    total_amount = struct.unpack(">I", chunk)[0]
    print("cv_tcp_server::total_amount:", total_amount)
    received_amount = 0
    buffer = b''
    while received_amount < total_amount:
        chunk = conn.recv(total_amount - received_amount)
        received_amount += len(chunk)
        #chunk = np.fromstring(chunk, np.uint8)
        #buffer += cv2.imdecode(chunk, cv2.CV_LOAD_IMAGE_COLOR)
        buffer += chunk
    print("buffer:", buffer)
    #buffer = b''.join(buffer)
    frame = np.frombuffer(buffer, dtype=np.uint8).reshape(IMAGE_SIZE[0], IMAGE_SIZE[1], IMAGE_SIZE[2])
    cv2.imshow('cv_server', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Program will be terminated..")
conn.close()
sock.close()
cv2.destroyAllWindows()