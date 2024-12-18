import cv2  # Импортируем библиотеку OpenCV для работы с видео и изображениями
from PIL import Image, ImageChops  # Импортируем классы Image и ImageChops из библиотеки Pillow для работы с изображениями
import RPi.GPIO as GPIO  # Импортируем библиотеку для работы с GPIO
import time  # Импортируем библиотеку для работы с временем

from motors import set_angle

camera = cv2.VideoCapture(0)  # Инициализируем захват видео с камеры (номер 0)
count = 0  # Инициализируем счетчик пикселей

# Настройка GPIO для сервомотора
GPIO.setmode(GPIO.BCM)
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)
set_angle(90)

# Создаем объект PWM для сервомотора
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0) #Меня смущяет 0, потому что коэффициент заполнения 0 в контексте ШИМ-сигнала означает, что сигнал всегда находится
# в состоянии LOW, то есть его коэффициент заполнения равен 0%


def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

def yes_or_not():
    if count <= 30000:
        return 0
    else:
        return 1



def is_pixel_black_or_write(pixel):
    red, green, blue = pixel
    average = (red + green + blue) / 3
    if average >= 20:
        return 1
    else:
        return 0

def difference():
    old = 0
    human = 0
    global count
    while True:
        time.sleep(3)
        good, img = camera.read()
        cv2.imwrite('w1.png', img)
        cv2.imshow("Image", img)
        image_1 = Image.open("w.png")
        image_2 = Image.open("w1.png")

        result = ImageChops.difference(image_1, image_2)
        result.save('result.jpg')
        count = 0
        res = cv2.imread('result.jpg', cv2.IMREAD_GRAYSCALE)
        cv2.imshow('RES', res)
        image = Image.open('result.jpg')
        width, height = image.size
        for y in range(height):
            for x in range(width):
                pixel = image.getpixel((x, y))
                color = is_pixel_black_or_write(pixel)
                count = count + color
        print(count, width * height)

        human = yes_or_not()


        if old == 1 and human == 1:

            print("HUMAN")
            set_angle(90)  # Поворот на 90 градусов
            time.sleep(2)
            set_angle(0)  # Поворот на 0 градусов
            old = 0
            human = 0
        else:
            old = human
while True:
    good, img = camera.read()
    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('r'):
        good, image = camera.read()
        cv2.imwrite("w.png", image)
        difference()