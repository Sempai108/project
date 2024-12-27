import cv2  # Импортируем библиотеку OpenCV для работы с видео и изображениями
from PIL import Image, ImageChops  # Импортируем классы Image и ImageChops из библиотеки Pillow для работы с изображениями
import RPi.GPIO as GPIO  # Импортируем библиотеку для работы с GPIO
import time  # Импортируем библиотеку для работы с временем

camera = cv2.VideoCapture(0)  # Инициализируем захват видео с камеры (номер 0)
count = 0  # Инициализируем счетчик пикселей

# Настройка GPIO для сервомотора
GPIO.setmode(GPIO.BCM)
servo_pin1 = 18
GPIO.setup(servo_pin1, GPIO.OUT)

servo_pin2 = 26
GPIO.setup(servo_pin2, GPIO.OUT)

# Создаем объект PWM для сервомотора
pwm1 = GPIO.PWM(servo_pin1, 50)  # Частота 50 Гц
pwm1.start(0)

pwm2 = GPIO.PWM(servo_pin2, 50)  # Частота 50 Гц
pwm2.start(0)

def set_angle1(angle1):
    duty1 = angle1 / 18 + 2
    pwm1.ChangeDutyCycle(duty1)
    time.sleep(1)
    pwm1.ChangeDutyCycle(0)

def set_angle2(angle2):
    duty2 = angle2 / 18 + 2
    pwm2.ChangeDutyCycle(duty2)
    time.sleep(1)
    pwm