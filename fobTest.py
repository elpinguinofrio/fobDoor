#!/usr/bin/python3
import sys
import time

fp = open('/dev/hidraw0', 'rb')

dict(a="A",
	 b="B",
	 c="C",
	 )

def bytoToBDcode(code):
	if code == 40:
		return ""
	if code == 39:
		return "0"
	return chr(ord('1')+code-30)

code = []

while True:
	buffer = fp.read(1)
	for c in buffer:
		if c > 0:
			code.append(c)
	if len(code) == 11:
		fobNumber = ""
		for c in code:
			fobNumber += bytoToBDcode(c)
		print(fobNumber)
		code = []
