import RPi.GPIO as GPIO
import time

# Настройка GPIO
GPIO.setmode(GPIO.BCM)
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)

# Создаем объект PWM
pwm = GPIO.PWM(servo_pin, 50)  # 50 Гц (период 20 мс)
pwm.start(0)

def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        set_angle(90)  # Поворот на 90 градусов
        time.sleep(2)
        set_angle(0)   # Поворот на 0 градусов
        time.sleep(2)
finally:
    pwm.stop()
    GPIO.cleanup()
