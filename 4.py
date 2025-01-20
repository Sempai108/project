import RPi.GPIO as GPIO
import time

# Установка пинов
motor_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_pin, GPIO.OUT)

# Создание объекта PWM
pwm = GPIO.PWM(motor_pin, 50)  # Частота 50 Гц
pwm.start(0)

def set_angle(angle):
    duty_cycle = angle / 18 + 2
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)

try:
    while True:
        for angle in [0, 135, 0, 45]:
            set_angle(angle)
            time.sleep(2)  # Задержка перед следующим углом
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
