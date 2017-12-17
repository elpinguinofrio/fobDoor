#!/usr/bin/python3
import sys
import time
import urllib.request
import json
import datetime
from dateutil.parser import parse
import pygame
pygame.mixer.init()
from gtts import gTTS

def play_sound(sound_file_name):
    print("playing " + sound_file_name)
    pygame.mixer.music.load(sound_file_name)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

TEMP_FILE = "/tmp/temp.mp3"

def generate_sound_by_text(text_to_say, language = "en"):
    tts = gTTS(text=text_to_say, lang=language)
    tts.save(TEMP_FILE)

def say_text(text_to_say, language = "en"):
    generate_sound_by_text(text_to_say, language)
    play_sound(TEMP_FILE)

DEFAULT_USER_NAME = "Fucker"

def get_user_info(user_code):
    raw_json = urllib.request.urlopen("http://192.168.0.110:8003/state/members/" + str(user_code)).read().decode('utf8')
    obj = json.loads(raw_json)
    return obj

def user_get_duedate(user_info):
    return parse(user_info['membershipDue'])
    
def user_get_name(user_info):
    return user_info['name']

def check_can_the_user_get_in(user_code):
    try:
        # try to read date from DB
        user_info = get_user_info(user_code)
        duedate = user_get_duedate(user_info)
        name = user_get_name(user_info)
    except:
        # yesterday
        duedate = datetime.datetime.now() - datetime.timedelta(1)
        name = DEFAULT_USER_NAME
    now = datetime.datetime.now()

    #print(str(now))
    print(str(duedate))

    door_access = duedate.replace(tzinfo=None) >= now.replace(tzinfo=None)
    if door_access:
        say_text("Access granted, " + name)
    else:
        say_text("Access denied, " + name)

    '''
    generate_sound_by_text(name)
    if door_access:
        play_sound("access_granted.wav")
    else:
        play_sound("access_denied2.wav")
    play_sound(TEMP_FILE)
    '''

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
            check_can_the_user_get_in(fobNumber)
            # clear
            code = []
