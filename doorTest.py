#!/usr/bin/python3
import sys
import time
import urllib.request
import json
import datetime
from dateutil.parser import parse
import pygame
pygame.mixer.init()

def play(soundFileName):
    print("play " + soundFileName)
    pygame.mixer.music.load(soundFileName)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def read_user_info(code):
    raw_json = urllib.request.urlopen("http://192.168.0.110:8003/state/members/" + str(code)).read().decode('utf8')
    obj = json.loads(raw_json)
    return obj

def user_get_duedate(user_info):
    raw_date = user_info['membershipDue']
    date = parse(raw_date)
    return date


def checkTheCode(user_code):
    try:
        # try to read date from DB
        duedate = user_get_duedate(read_user_info(user_code))
    except:
        # yesterday
        duedate = datetime.datetime.now() - datetime.timedelta(1)
    now = datetime.datetime.now()

    print(str(now))
    print(str(duedate))

    door_access = duedate.replace(tzinfo=None) >= now.replace(tzinfo=None)
    if door_access:
        play("access_granted.wav")
    else:
        play("access_denied2.wav")


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
            checkTheCode(fobNumber)
            # clear
            code = []
