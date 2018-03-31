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

say_text("hello DCTRL!")