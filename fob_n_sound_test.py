#!/usr/bin/python3
import sys
import time
import pygame
pygame.mixer.init()

fp = open('/dev/hidraw0', 'rb')

code = []

def play(soundFileName):
    print("play " + soundFileName)
    pygame.mixer.music.load(soundFileName)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

while True:
    buffer = fp.read(8)
    for c in buffer:
        if c > 0:
            code.append(c)
    if len(code) == 11:
        print(code)
        if code == [39, 39, 39, 35, 34, 33, 30, 36, 31, 37, 40]:
            play("access_granted.wav")
        elif code == [39, 39, 30, 32, 32, 32, 39, 31, 32, 31, 40]:
            play("el_pinguino_granted.mp3")
        elif code == [39, 39, 39, 36, 38, 32, 37, 38, 33, 33, 40]:
            play("jared_villian.mp3")
        elif code == [39, 39, 39, 35, 34, 33, 30, 36, 31, 37, 40]:
            play("test.mp3")
        else:
            play("access_denied2.wav")
        code = []

