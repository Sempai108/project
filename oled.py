import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image

# Настройка I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Инициализация дисплея
WIDTH = 128
HEIGHT = 64
display = SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

# Очистка дисплея
display.fill(0)
display.show()

# Загрузка изображения
# Убедитесь, что изображение 128x64 пикселей и черно-белое (1-bit mode)
image = Image.open("eye.bmp").convert("1")

# Отображение изображения на экране
display.image(image)
display.show()
