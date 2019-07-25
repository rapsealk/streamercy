#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cv2
import base64

cap = cv2.VideoCapture(0)

if not cap.isOpened:
    cap.open()

while True:
    ret, frame = cap.read()

    print(frame, frame.shape)
    ret, buffer = cv2.imencode(".jpg", frame)

    base64img = base64.b64encode(buffer)
    print("len(base64img):", len(base64img))
    print("base64img[:80]:", base64img[:80])
    #print("base64.decode:", int.from_bytes(base64.b64decode(base64img[:80]), byteorder="big"))

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()