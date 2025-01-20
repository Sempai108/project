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
        # Ввод угла поворота через терминал
        desired_angle = float(input("Введите угол поворота (0-180): "))
        if 0 <= desired_angle <= 180:
            set_angle(desired_angle)
        else:
            print("Пожалуйста, введите угол в диапазоне от 0 до 180.")
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
