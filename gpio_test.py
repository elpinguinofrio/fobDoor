# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
beerPin = 3 # Broadcom pin 17 (P1 pin 11)

# Pin Setup:
GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme
GPIO.setup(beerPin, GPIO.OUT) # 17 pin set as output

GPIO.output(beerPin, GPIO.HIGH)
time.sleep(1) # wait 1 second to be sure relay has enough time to switch
GPIO.output(beerPin, GPIO.LOW) # External module imports
