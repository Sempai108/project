import cv2  # Импортируем библиотеку OpenCV для работы с видео и изображениями
from PIL import Image, ImageChops  # Импортируем классы Image и ImageChops из библиотеки Pillow для работы с изображениями

camera = cv2.VideoCapture(0)  # Инициализируем захват видео с камеры (номер 0)
count = 0  # Инициализируем счетчик пикселей

def yes_or_not():
    global count
    return 1 if count > 30000 else 0


def is_pixel_black_or_white(pixel):
    red, green, blue = pixel
    average = (red + green + blue) / 3
    return 1 if average >= 30 else 0


def difference():
    old = 0
    global count


    try:
        while True:
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
                    color = is_pixel_black_or_white(pixel)
                    count += color
            print(count, width * height)
            human = yes_or_not()

            if old == 1 and human == 1:
                print("PERSON WAS DISCOVERED")
                human = 0
            else:
                old = human
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        print("Прерывание программы. Освобождение ресурсов...")
    finally:
        camera.release()
        cv2.destroyAllWindows()


# Снимаем начальное изображение и сохраняем его как 'w.png'
good, image = camera.read()
cv2.imwrite("w.png", image)


# Запускаем функцию для вычисления разницы
difference()
