import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) 	# BCM | BOARD


blink = True

# set pin
R1 = 8				# red
R2 = 22				# blue
R3 = 24				# button

GPIO.setwarnings(False)

# GPIO setup
GPIO.setup(R1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(R2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(R3, GPIO.IN)

try:
	while blink == True:
			
		if GPIO.input(R3):
			print "buuton"		

		dt = list(time.localtime())
                s = dt[5]
		
		if s % 2 == 0:	
			GPIO.output(R1, GPIO.HIGH)
			GPIO.output(R1, GPIO.LOW)
			time.sleep(.5)

		if s % 2 == 1:
			GPIO.output(R2, GPIO.HIGH)
	               	GPIO.output(R2, GPIO.LOW)
			time.sleep(.5)

#		print "red", GPIO.input(R1), "blue", GPIO.input(R2), "button", GPIO.input(R3)
finally:
	GPIO.cleanup()



