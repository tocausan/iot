import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)        # BCM | BOARD

blinkCount = 3
count = 4
blink = True

# set pin
R1 = 8                          # red
R2 = 22                         # blue

GPIO.setwarnings(False)

GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)

try:
        while blink == True:

                dt = list(time.localtime())
                h = dt[3]
                min = dt[4]
                sec = dt[5]

                R = ""


                if sec < 30:
                        R = "red"

                        GPIO.output(R2, False)

                        GPIO.output(R1, True)
                        time.sleep(.2)

                        GPIO.output(R1, False)
                        time.sleep(.2)

                elif sec >= 30:
                        R = "blue"

                        GPIO.output(R1, False)

                        GPIO.output(R2, True)
                        time.sleep(.2)

                        GPIO.output(R2, False)
                        time.sleep(.2)

                print sec, R
                time.sleep(.2)
finally:
        GPIO.cleanup()
