import cv2  # Импортируем библиотеку OpenCV для работы с видео и изображениями
from PIL import Image, \
    ImageChops  # Импортируем классы Image и ImageChops из библиотеки Pillow для работы с изображениями
import RPi.GPIO as GPIO  # Импортируем библиотеку для работы с GPIO
import time  # Импортируем библиотеку для работы с временем

camera = cv2.VideoCapture(0)  # Инициализируем захват видео с камеры (номер 0)
count = 0  # Инициализируем счетчик пикселей
# Настройка GPIO для сервомотора
GPIO.setmode(GPIO.BCM)
servo_pin1 = 18
GPIO.setup(servo_pin1, GPIO.OUT)

GPIO.setmode(GPIO.BCM)
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
    pwm2.ChangeDutyCycle(0)


def yes_or_not():
    if count <= 30000:
        value = 0
        return value
    else:
        value = 1
        return value


def is_pixel_black_or_write(pixel):
    red, green, blue = pixel
    average = (red + green + blue) / 3
    if average >= 30:
        return 1
    else:
        return 0


def difference():
    old = 0
    global count
    while True:
        time.sleep(3)
        good, img = camera.read()
        cv2.imwrite('w1.png', img)
        image_1 = Image.open("../w.png")
        image_2 = Image.open("../w1.png")

        result = ImageChops.difference(image_1, image_2)
        result.save('result.jpg')
        count = 0
        res = cv2.imread('result.jpg', cv2.IMREAD_GRAYSCALE)
        image = Image.open('../result.jpg')
        width, height = image.size
        for y in range(height):
            for x in range(width):
                pixel = image.getpixel((x, y))
                color = is_pixel_black_or_write(pixel)
                count = count + color
        print(count, width * height)
        human = yes_or_not()

        if old == 1 and human == 1:

            print("PERSON WAS DISCOVERED")
            set_angle1(0)  # Устанавливаем угол поворота на 0 градусов
            set_angle1(90)  # Устанавливаем угол поворота на 90 градусов
            set_angle1(180)  # Устанавливаем угол поворота на 180 градусов
            set_angle2(0)  # Устанавливаем угол поворота на 0 градусов
            set_angle2(90)  # Устанавливаем угол поворота на 90 градусов
            set_angle2(180)  # Устанавливаем угол поворота на 180 градусов
            human = 0
        else:
            old = human


while True:
    good, img = camera.read()
    if cv2.waitKey(1) == ord('r'):
        good, image = camera.read()
        cv2.imwrite("w.png", image)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()