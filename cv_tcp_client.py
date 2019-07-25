#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cv2
import sys
import socket
import struct
import time
from util import *
from functools import reduce

EXPECTED_BYTES = reduce(lambda x, y: x * y, IMAGE_SIZE)
HEADER = (HEADER_FLAG + '=' * (PACKET_SIZE - len(HEADER_FLAG))).encode("utf-8")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 7000))

cap = cv2.VideoCapture(0)

# Set camera properties
cap.set(cv2.CAP_PROP_FRAME_WIDTH, IMAGE_SIZE[1])
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, IMAGE_SIZE[0])
cap.set(cv2.CAP_PROP_FPS, 10)

if not cap.isOpened:
    cap.open()

last_timestamp = time.time()
while cap.isOpened():
    ret, frame = cap.read()

    cv2.imshow('cv_client', frame)

    #data = cv2.imencode(".jpg", frame)[1].tostring()#.encode("utf-8")
    data = frame.tostring()
    print("len(data):", len(data), "EXPECTED:", EXPECTED_BYTES)
    #assert(len(data) == EXPECTED_BYTES)

    sock.sendall(struct.pack(">I", len(data)) + data)
    #sock.sendall(data)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Program will be terminated..")
sock.close()
cap.release()
cv2.destroyAllWindows()