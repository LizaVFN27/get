import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
light_sensor = 6


GPIO.setup(light_sensor, GPIO.IN)


print("Скрипт запущен.")

try:
    while True:
        sensor_state = GPIO.input(light_sensor)
           
        GPIO.output(led, not sensor_state)
        time.sleep(0.01)
except KeyboardInterrupt:
    print("\nРабота прервана пользователем")
finally:
    GPIO.cleanup()









