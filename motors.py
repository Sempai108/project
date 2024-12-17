import cv2  # Импортируем библиотеку OpenCV для работы с видео и изображениями
from PIL import Image, ImageChops  # Импортируем классы Image и ImageChops из библиотеки Pillow для работы с изображениями
import RPi.GPIO as GPIO  # Импортируем библиотеку для работы с GPIO
import time  # Импортируем библиотеку для работы с временем

camera = cv2.VideoCapture(0)  # Инициализируем захват видео с камеры (номер 0)
count = 0  # Инициализируем счетчик пикселей

# Настройка GPIO для сервомотора
GPIO.setmode(GPIO.BCM)
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)

# Создаем объект PWM для сервомотора
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0) 


def set_angle(pwm, angle):
    duty = angle / 18 + 2
    GPIO.output(pwm, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(pwm, False)
    pwm.ChangeDutyCycle(0)


def is_pixel_black_or_white(pixel):
    red, green, blue = pixel
    average = (red + green + blue) / 3
    return 1 if average >= 20 else 0


def yes_or_not():
    global count
    if count >= 30000:
        print('Yes_or_not: True')
        # Поворачиваем сервомотор на 90 градусов
        set_angle(pwm, 90)
    else:
        print('Yes_or_not: False')
        # Поворачиваем сервомотор на 0 градусов
        set_angle(pwm, 0)


def process_image():
    global count
    good, img = camera.read()  # Захватываем кадр с камеры
    if not good:
        print("Failed to read from camera")
        return

    cv2.imwrite('w1.png', img)  # Сохраняем захваченное изображение в файл

    try:
        image_1 = Image.open("w.png")  # Открываем базовое изображение
    except FileNotFoundError:
        print("File w.png not found")
        return

    image_2 = Image.open("w1.png")  # Открываем захваченное изображение

    result = ImageChops.difference(image_1, image_2)
    result.save('result.jpg')

    count = 0
    res = cv2.imread('result.jpg', cv2.IMREAD_GRAYSCALE)

    if res is None or res.size == 0:
        print("Error: Result image is empty or not valid")
        return

    image = Image.open('result.jpg')
    width, height = image.size
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            count += is_pixel_black_or_white(pixel)

    print(count, width * height)
    yes_or_not()


try:
    # Захват и сохранение базового изображения при запуске
    good, image = camera.read()
    if good:
        cv2.imwrite("w.png", image)

    while True:
        process_image()

        # Отображение изображений w.png и w1.png
        try:
            img1 = cv2.imread("w.png")
            cv2.imshow('Base Image', img1)

            img2 = cv2.imread("w1.png")
            cv2.imshow('Captured Image', img2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except Exception as e:
            print(f"Failed to display image: {e}")
finally:
    camera.release()
    cv2.destroyAllWindows()
    pwm.stop()
    GPIO.cleanup()
