#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

import camera

PACKET_BYTES = 1024 * 4 # = 4096
TOTAL_BYTES = camera.IMAGE_WIDTH * camera.IMAGE_HEIGHT * 3
TOTAL_CHUNKS = math.ceil(TOTAL_BYTES / PACKET_BYTES)

HEADER_PACKET = "HEADER_PACKET"
HEADER_PACKET += "=" * (PACKET_BYTES - len(HEADER_PACKET))
HEADER_PACKET = HEADER_PACKET.encode("utf-8")