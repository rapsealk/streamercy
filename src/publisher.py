#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import argparse

import camera
import constant


class Publisher:

    def __init__(self, type="udp"):
        self.address = ("127.0.0.1", 7001)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.camera = camera.get_camera()
        self.generator = self.camera.capture()

    def run(self):
        while True:
            frame = next(self.generator)
            data = frame.tostring()
            print(frame.shape, len(data))
            self.socket.sendto(constant.HEADER_PACKET, self.address)
            for i in range(0, constant.TOTAL_BYTES, constant.PACKET_BYTES):
                self.socket.sendto(data[i:i+constant.PACKET_BYTES], self.address)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", dest="type", type=str, default="udp")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    publisher = Publisher()
    publisher.run()