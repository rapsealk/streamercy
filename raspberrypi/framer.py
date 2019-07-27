#!/usr/bin/python3
# -*- coding: utf-8 -*-

import picamera
import picamera.array

IMAGE_WIDTH = 320
IMAGE_HEIGHT = 240

class PiCameraFramer:
    
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (IMAGE_WIDTH, IMAGE_HEIGHT)
        self.stream = picamera.array.PiRGBArray(self.camera)

    def capture(self):
        while True:
            self.camera.capture(self.stream, 'bgr', use_video_port=True)
            shape = self.stream.array.shape # (height, width, channel)
            yield self.stream.array
            self.stream.seek(0)
            self.stream.truncate()


if __name__ == "__main__":
    framer = PiCameraFramer()
    generator = framer.capture()
    for i in range(10):
        frame = next(generator)
        print(frame.shape)
