#!/usr/bin/python3
import sys
import time

fp = open('/dev/hidraw0', 'rb')

code = []

while True:
    buffer = fp.read(8)
    for c in buffer:
        if c > 0:
            code.append(c)
    if len(code) == 11:
        print(code)
        code = []
