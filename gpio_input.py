import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

inPin=36
GPIO.setup(inPin,GPIO.IN)
readValue=GPIO.input(inPin)
print(readValue)
time.sleep(1)
print("End of code")
GPIO.cleanup()


