import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [24, 22, 23, 27, 17, 25, 5, 16]

for pin in leds:
    GPIO.setup(pin, GPIO.OUT)
GPIO.output(leds, GPIO.LOW)

try:
    for pin in leds:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(pin, GPIO.LOW)


except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()




















