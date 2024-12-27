import cv2
import time
from PIL import Image, ImageChops


time.sleep(1)
camera = cv2.VideoCapture(0)
time.sleep(1)
count = 0
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