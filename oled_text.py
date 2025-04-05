from PIL import Image, ImageDraw, ImageFont
import board
import busio
from adafruit_ssd1306 import SSD1306_I2C

# Настройка дисплея
i2c = busio.I2C(board.SCL, board.SDA)
display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

# Очистка экрана
display.fill(0)
display.show()

# Создание изображения
image = Image.new("1", (128, 64))
draw = ImageDraw.Draw(image)

# Использование кастомного шрифта
font = ImageFont.truetype("/path/to/Arial.ttf", 16)  # Замените путь

# Рисование текста
draw.text((0, 0), "Привет, OLED!", font=font, fill=255)

# Отображение на экране
display.image(image)
display.show()
