import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw

# Настройка I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Инициализация дисплея
WIDTH = 128
HEIGHT = 64
display = SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

# Очистка дисплея
display.fill(0)
display.show()

# Создание изображения
image = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)

# Рисуем текст
draw.text((0, 0), "Hello, OLED!", fill=255)

# Отображаем на экране
display.image(image)
display.show()
