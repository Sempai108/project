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

# Очистка экрана
display.fill(0)
display.show()

# Цикл для ввода текста
while True:
    # Запрос текста от пользователя
    user_input = input("Введите текст для отображения на экране: ")

    # Создание изображения
    image = Image.new("1", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)

    # Загрузка шрифта (можно заменить стандартным)
    # Убедитесь, что у вас есть файл шрифта 'font.ttf' или используйте встроенный шрифт
    # font = ImageFont.truetype("/path/to/font.ttf", 16)
    font = ImageFont.load_default()

    # Рисование текста
    draw.text((0, 0), user_input, font=font, fill=255)

    # Отображение на экране
    display.image(image)
    display.show()
