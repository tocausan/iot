import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) 	# BCM | BOARD


day = [6, 21]
goodmorning = [6, 9]
goodnight = [21, 24]

# set pin
R1 = 8				# red
R2 = 10				# blue
R3 = 12				# button

GPIO.setwarnings(False)

# GPIO setup
GPIO.setup(R1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(R2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(R3, GPIO.IN)

try:
	while True:

		# button state		
		state = GPIO.input(R3)

		# get date
		dt = list(time.localtime())
		h = dt[3]
		
		# button
		if not state:
        			
			GPIO.output(R1, False)
			time.sleep(1)
			GPIO.output(R2, False)
			time.sleep(1)

		# day -> redlight
		if h >= day[0] and h < day[1]:

			# Alarm
			if h >= goodmorning[0] and h < goodmorning[1]:
				GPIO.output(R1, True)
				time.sleep(.2)
				GPIO.output(R1, False)
				time.sleep(.2)

                        else:
				GPIO.output(R1, True)
				time.sleep(.5)
				GPIO.output(R1, False)
				time.sleep(0)

		# night -> bluelight
		else:

			# Alarm
                        if h >= goodnight[0] and h < goodnight[1]:
                                GPIO.output(R2, True)
                                time.sleep(.2)
                                GPIO.output(R2, False)
                                time.sleep(.2)

                        else:
                                GPIO.output(R2, True)
                                time.sleep(.5)
                                GPIO.output(R2, False)
                                time.sleep(0)

#		print "red", GPIO.gpio_function(R1), "blue", GPIO.gpio_function(R2), "button", GPIO.gpio_function(R3)
	
finally:
	GPIO.cleanup()



