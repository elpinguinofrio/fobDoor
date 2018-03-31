#!/usr/bin/python3
import sys
import time
import urllib.request
import json
import datetime
from dateutil.parser import parse
import pygame
import os.path
import base64
from gtts import gTTS
import RPi.GPIO as GPIO

DOOR_PIN = 3

def init_the_door():
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(DOOR_PIN, GPIO.OUT) 

def open_the_door():
    GPIO.output(DOOR_PIN, GPIO.HIGH)
    time.sleep(1) # wait 1 second to be sure relay has enough time to switch
    GPIO.output(DOOR_PIN, GPIO.LOW) # External module imports


def play_sound(sound_file_name):
    pygame.mixer.init()
    #print("playing " + sound_file_name)
    pygame.mixer.music.load(sound_file_name)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    pygame.mixer.quit()


def generate_sound_by_text(text_to_say: str, language, sound_file_name):
    if os.path.exists(sound_file_name) == False:
        print("new phrase")
        tts = gTTS(text=text_to_say, lang=language)
        tts.save(sound_file_name)
    else:
        print("reading file from cache")

def say_text(text_to_say, language = "en"):
    # convert text to the uni
    sound_file_name = "/tmp/" + base64.b64encode(text_to_say.encode()).decode()
    generate_sound_by_text(text_to_say, language, sound_file_name)
    play_sound(sound_file_name)

DEFAULT_USER_NAME = "Fucker"


def reserve_copy(fob_number):
    # init reserve copy of db, very damn and temporary
    with open('/home/pi/fobDoor/db_snapshot.txt') as f:
        read_data = f.read()
    f.close()

    users = json.loads(read_data)
    for user in users:
        if user['fob'] == fob_number:
            return user
    return None

def get_user_info(fob_number):
    try:
        raw_json = urllib.request.urlopen("http://192.168.0.110:8003/state/members/" + str(fob_number)).read().decode('utf8')
        obj = json.loads(raw_json)
    except:
        say_text("can't connect to server!")
        obj = reserve_copy(fob_number)
    
    return obj

def user_get_duedate(user_info):
    return parse(user_info['membershipDue'])
    
def user_get_name(user_info):
    return user_info['name']

def check_can_the_user_get_in(user_code):
    user_info = get_user_info(user_code)
    if user_info == None:
        say_text("Access denied, " + "No user found!")
    else:
        name = user_get_name(user_info)
        #duedate = user_get_duedate(user_info)
        #now = datetime.datetime.now()
        #door_access = duedate.replace(tzinfo=None) >= now.replace(tzinfo=None)
        open_the_door()
        say_text("Access granted, " + name)
        

# usb fob reader
fp = open('/dev/hidraw0', 'rb')

def bytoToBDcode(code):
    if code == 40:
        return ""
    if code == 39:
        return "0"
    return chr(ord('1')+code-30)

if __name__ == "__main__":
    # init everything
    code = []
    init_the_door()
    say_text("Hello world!")
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
