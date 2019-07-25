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

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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

    #ret, buffer = cv2.imencode(".jpg", frame)
    cv2.imshow('cv_client', frame)

    data = frame.tostring()
    print("len(data):", len(data), "EXPECTED:", EXPECTED_BYTES)
    assert(len(data) == EXPECTED_BYTES)
    sock.sendto((HEADER_FLAG + '=' * (PACKET_SIZE - len(HEADER_FLAG))).encode("utf-8"), ("127.0.0.1", 7000))
    for i in range(0, EXPECTED_BYTES, PACKET_SIZE):
        sock.sendto(data[i:i+PACKET_SIZE], ("127.0.0.1", 7000))
    """
    total_packet = 1 + int((len(buffer) - 1) / PACKET_SIZE)
    sys.stdout.write("cv_client::total_packet: %d\n" % total_packet)

    sock.sendto(struct.pack(">I", total_packet), ("127.0.0.1", 7000))
    for i in range(total_packet):
        sock.sendto(buffer[i*PACKET_SIZE:(i+1)*PACKET_SIZE], ("127.0.0.1", 7000))

    new_timestamp = time.time()
    duration = (new_timestamp - last_timestamp) / 1000
    sys.stdout.write("FPS: %f, kbps: %f\n" % (1 / duration, PACKET_SIZE / total_packet / duration / 1024 * 8))
    last_timestamp = new_timestamp
    """

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()