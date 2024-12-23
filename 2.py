import cv2  # Импортируем библиотеку OpenCV для работы с видео и изображениями
from PIL import Image, ImageChops  # Импортируем классы Image и ImageChops из библиотеки Pillow для работы с изображениями
import RPi.GPIO as GPIO  # Импортируем библиотеку для работы с GPIO
import time  # Импортируем библиотеку для работы с временем

camera = cv2.VideoCapture(0)  # Инициализируем захват видео с камеры (номер 0)
count = 0  # Инициализируем счетчик пикселей

# Настройка GPIO для сервомотора
GPIO.setmode(GPIO.BCM)
servo_pin1 = 18
servo_pin2 = 19
GPIO.setup(servo_pin1, GPIO.OUT)
GPIO.setup(servo_pin2, GPIO.OUT)

# Создаем объект PWM для сервомотора
pwm1 = GPIO.PWM(servo_pin1, 50) # 50 Гц (период 20 мс)
pwm2 = GPIO.PWM(servo_pin2, 50) # 50 Гц (период 20 мс)
pwm1.start(2)
pwm2.start(2)

def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

def yes_or_not():
    if count <= 30000:
        return 0
    else:
        return 1
ч1

def is_pixel_black_or_write(pixel):
    red, green, blue = pixel
    average = (red + green + blue) / 3
    if average >= 30:
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
        image_1 = Image.open("w.png")
        image_2 = Image.open("w1.png")

        result = ImageChops.difference(image_1, image_2)
        result.save('result.jpg')
        count = 0
        res = cv2.imread('result.jpg', cv2.IMREAD_GRAYSCALE)
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
            set_angle(pwm1, 0)
            set_angle(pwm1, 90)
            set_angle(pwm2, 0)
            set_angle(pwm2, 90)
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