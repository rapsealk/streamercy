#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import argparse

import cv2
import numpy as np

import camera
import constant


class Subscriber:

    def __init__(self, type="udp"):
        self.address = ("0.0.0.0", 7000)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(self.address)

    def run(self):
        while True:
            chunk, addr = self.socket.recvfrom(constant.PACKET_BYTES)
            if chunk != constant.HEADER_PACKET:
                print("chunk: %s\nchunk == constant.HEADER_PACKET: %r" % (chunk, chunk == constant.HEADER_PACKET))
                continue
            buffer = [self.socket.recv(constant.PACKET_BYTES) for _ in range(constant.TOTAL_CHUNKS)]
            buffer = b''.join(buffer)
            frame = np.frombuffer(buffer, dtype=np.uint8).reshape(camera.IMAGE_HEIGHT, camera.IMAGE_WIDTH, 3)
            
            cv2.imshow("Subscriber", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", dest="type", type=str, default="udp")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    subscriber = Subscriber()
    subscriber.run()