import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

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

# Использование встроенного шрифта
font = ImageFont.load_default()

# Начальная координата для текста
y_position = 0

# Цикл для ввода текста
while True:
    # Ввод текста пользователем
    user_input = input("Введите текст для отображения на экране: ")

    # Если текст больше не помещается на экране, очищаем дисплей
    if y_position + 10 > HEIGHT:  # 10 пикселей - примерная высота строки
        draw.rectangle((0, 0, WIDTH, HEIGHT), fill=0)  # Очищ