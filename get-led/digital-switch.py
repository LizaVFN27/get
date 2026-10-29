import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
button = 13


GPIO.setup(button, GPIO.IN)
state = 0


GPIO.output(led, state)
print("Скрипт запкщен.")

try:
    while True:
        if GPIO.input(button):
            state = 1 - state
            GPIO.output(led, state)
            while GPIO.input(button) == 1:
                time.sleep(0.05)
            time.sleep(0.2)
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nРабота прервана пользователем")
finally:
    GPIO.cleanup()









