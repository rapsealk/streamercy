#!/usr/bin/python3
# -*- coding: utf-8 -*-

#__all__ = ["IMAGE_SIZE"]

import sys

HEADER_BYTES = 4
HEADER_FLAG = "HEADER"

if sys.platform == "darwin":
    IMAGE_SIZE = (720, 1280, 3)
elif sys.platform == "win32":
    IMAGE_SIZE = (480, 360, 3)
elif sys.platform == "linux":
    IMAGE_SIZE = (None, None, None)

FRAME_HEIGHT = 720
FRAME_WIDTH = 1280
FRAME_INTERVAL = int(1000 / 30)
PACKET_SIZE = 4096  # OSX limits < 8100 bytes
ENCODE_QUALITY = 80