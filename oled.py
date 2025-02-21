from PIL import Image
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306

# Настройка интерфейса I2C и OLED-дисплея
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

# Загрузка вашего изображения
image_path = "C:\\Users\\1\\Documents\\ПР\\было зачем-то нужно\\загруженное (1).png"
image = Image.open(image_path).convert("1")  # Преобразуем изображение в черно-белое

# Отображение изображения на экране
device.display(image)

# Очистка экрана
device.clear()
