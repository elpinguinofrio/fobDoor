import pygame
testfile = "/tmp/temp.mp3"
pygame.mixer.init()
pygame.mixer.music.load(testfile)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
