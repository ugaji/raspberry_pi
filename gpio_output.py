import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
numBlink=int(input('Blink: how many times?')) 
for x in range (0,numBlink):
	GPIO.output(7,True)
	time.sleep(1)
	GPIO.output(7,False)
	time.sleep(1)

