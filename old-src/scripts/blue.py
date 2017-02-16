import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) 	# BCM | BOARD


blink = True

# set pin
R1 = 22				# blue

GPIO.setwarnings(False)

GPIO.setup(R1, GPIO.OUT)

try:
	while blink == True:
			
		GPIO.output(R1, True)
		time.sleep(.2)

		GPIO.output(R1, False)
		time.sleep(.2)
	
finally:
	GPIO.cleanup()



