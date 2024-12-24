import RPi.GPIO as GPIO
import time

# Настройка GPIO
GPIO.setmode(GPIO.BCM)
servo_pin1 = 18
GPIO.setup(servo_pin1, GPIO.OUT)

GPIO.setmode(GPIO.BCM)
servo_pin2 = 26
GPIO.setup(servo_pin2, GPIO.OUT)

# Создаем объект PWM
pwm1 = GPIO.PWM(servo_pin1, 50)  # Частота 50 Гц
pwm1.start(0)

pwm2 = GPIO.PWM(servo_pin2, 50)  # Частота 50 Гц
pwm2.start(0)

def set_angle1(angle1):
    duty1 = angle / 18 + 2
    pwm1.ChangeDutyCycle(duty1)
    time.sleep(1)
    pwm1.ChangeDutyCycle(0)

def set_angle2(angle2):
    duty2 = angle2 / 18 + 2
    pwm2.ChangeDutyCycle(duty2)
    time.sleep(1)
    pwm2.ChangeDutyCycle(0)

try:
    while True:
        set_angle1(0)    # Устанавливаем угол поворота на 0 градусов
        time.sleep(1)   # Ждем 1 секунду

        set_angle1(90)   # Устанавливаем угол поворота на 90 градусов
        time.sleep(1)   # Ждем 1 секунду

        set_angle1(180)  # Устанавливаем угол поворота на 180 градусов
        time.sleep(1)

        set_angle2(0)  # Устанавливаем угол поворота на 0 градусов
        time.sleep(1)  # Ждем 1 секунду

        set_angle2(90)  # Устанавливаем угол поворота на 90 градусов
        time.sleep(1)  # Ждем 1 секунду

        set_angle2(180)  # Устанавливаем угол поворота на 180 градусов
finally:
    pwm.stop()
    GPIO.cleanup()
