import RPi.GPIO as GPIO
import time

# Настройка GPIO
GPIO.setmode(GPIO.BCM)
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)

# Создаем объект PWM
pwm = GPIO.PWM(servo_pin, 50)  # Частота 50 Гц
pwm.start(0)

def set_angle(angle):
    duty = angle / 18 + 2
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        set_angle(0)    # Устанавливаем угол поворота на 0 градусов
        time.sleep(1)   # Ждем 1 секунду

        set_angle(90)   # Устанавливаем угол поворота на 90 градусов
        time.sleep(1)   # Ждем 1 секунду

        set_angle(180)  # Устанавливаем угол поворота на 180 градусов
        time.sleep(1)   # Ждем 1 секунду
finally:
    pwm.stop()
    GPIO.cleanup()
d