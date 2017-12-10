#!/usr/bin/python3
import sys
import time
import pygame
pygame.mixer.init()

fp = open('/dev/hidraw0', 'rb')

code = []

def play(number):
    print("play " + str(number))
    if number == 1:
        pygame.mixer.music.load("access_granted.wav")
    if number == 0:
        pygame.mixer.music.load("access_denied2.wav") 
    if number == 2:
       pygame.mixer.music.load("el_pinguino_granted.mp3")
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
            play(1)
        elif code == [39, 39, 30, 32, 32, 32, 39, 31, 32, 31, 40]:
            play(2)
        else:
            play(0)
        code = []

