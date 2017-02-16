import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) 	# BCM | BOARD


blink = True

# set pin
R1 = 8				# red
R2 = 22				# blue

GPIO.setwarnings(False)

# GPIO setup
GPIO.setup(R1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(R2, GPIO.OUT, initial=GPIO.LOW)

try:
	while blink == True:

		dt = list(time.localtime())
                s = dt[5]
		
		if s % 2 == 0:	
#			GPIO.output(R1, True)
#			time.sleep(.2)

			GPIO.output(R1, False)
			time.sleep(.2)

		if s % 2 == 1:
#			GPIO.output(R2, True)
#                	time.sleep(.2)

                	GPIO.output(R2, False)
                	time.sleep(.2)

	GPIO.output(R1, False)
	GPIO.output(R2, False)
	
finally:
	GPIO.cleanup()



