#!/usr/bin/python3
import sys
import time

# usb fob reader
fp = open('/dev/hidraw0', 'rb')

def bytoToBDcode(code):
    if code == 40:
        return ""
    if code == 39:
        return "0"
    return chr(ord('1')+code-30)

if __name__ == "__main__":
    code = []
    while True:
        buffer = fp.read(1)
        for c in buffer:
            if c > 0:
                code.append(c)
        if len(code) == 11:
            # conver array "code" to strong fob code which server understands
            fobNumber = ""
            for c in code:
                fobNumber += bytoToBDcode(c)

            # todo something when you read the fob
            print(fobNumber)
            
            # clear
            code = []
