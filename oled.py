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

# Конвертация изображения в 1-bit
image = Image.open("/home/promrobo/project/eye.bmp")
image = image.convert("1")  # Преобразование в чёрно-белый формат
image.save("/home/promrobo/project/eye_converted.bmp")  # Сохранение конвертированного файла

# Загрузка и отображение конвертированного изображения
image = Image.open("/home/promrobo/project/eye_converted.bmp")
display.image(image)
display.show()
