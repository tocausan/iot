# GPIO
## Script
```python
# import gpio library
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print('Error importing RPi.GPIO.')
    print('This is probably because you need superuser privileges.')

# import other libraries
import time

# mode
# mode = BCM | BOARD
# channel = name (BCM) | number (BOARD)
GPIO.setmode(GPIO.[mode])
GPIO.getmode()

# warnings
GPIO.setwarnings([boolean])

# channels
# channel = channel | channel list
# type = GPIO.IN | GPIO.OUT
# resistor = (empty) | pull_up_down=GPIO.PUD_UP | pull_up_down=GPIO.PUD_DOWN
GPIO.setup([channel], [type], [resistor])

# input
# channel = channel | channel list
GPIO.input([channel])

# output
# channel = channel | channel list
# state = 0 | 1 | GPIO.LOW | GPIO.HIGH | Fasle | True | (GPIO.HIGH, GPIO.LOW)
GPIO.output([channel], [state])

# interrupt and edge detection
# channel = channel | channel list
# type =  GPIO.RISING | GPIO.FALLING | GPIO.BOTH
# timeout = timeout=[milliseconds]
# callback = [function]
# bounce = bouncetime=[milliseconds]
GPIO.wait_for_edge([channel], [type], [timeout])
GPIO.add_event_detect([channel], [type], [callback], [bounce])
GPIO.event_detect([channel])
GPIO.remove_event_detect([channel])

# pulse width modulation
# dc = 0.0 <= dc <= 100.0
# frequency = [Hz]
p = GPIO.PWM([channel], [frequency])
p.start([dc])
p.ChangeFrequency([frequency])
p.ChangeDutyCycle([dc])
p.stop()

# gpio function
# returns: GPIO.IN | GPIO.OUT | GPIO.SPI | GPIO.I2C | GPIO.HARD_PWM | GPIO.SERIAL | GPIO.UNKNOWN
GPIO.gpio_function([channel])

# cleanup
# channel = (empty) | channel | channel list
GPIO.cleanup([channel])

# rpi info
GPIO.RPI_INFO
GPIO.RPI_INFO['PI_REVISION']
```

## Pin
```
Pi Model B/B+ 
BOARD   BCM         BOARD   BCM
1       3V3         2   5V
3       GPIO 2      4   5v
5       GPIO 3      6   ground
7       GPIO 4      8   GPIO 14
9       GROUND      10  GPIO 15
11      GPIO 17     12  GPIO 18
13      GPIO 27     14  ground
15      GPIO 22     16  GPIO 23
17      3V3         18  GPIO 24
19      GPIO 10     20  ground
21      GPIO 9      22  GPIO 25
23      GPIO 11     24  GPIO 8
25      GROUND      26  GPIO 7
27      ID_SD       28  ID_SC
29      GPIO 5      30  GROUND
31      GPIO 6      32  GPIO 12
33      GPIO 13     34  GROUND
35      GPIO 19     36  GPIO 16
37      GPIO 26     38  GPIO 20
39      GROUND      40  GPIO 21
```