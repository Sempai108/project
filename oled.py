from PIL import Image, ImageDraw
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306

# Настройка интерфейса I2C и OLED-дисплея
try:
    serial = i2c(port=1, address=0x3C)  # Убедитесь, что адрес соответствует вашему дисплею
    device = ssd1306(serial)
    print("Устройство подключено успешно.")
except Exception as e:
    print(f"Ошибка подключения к OLED-дисплею: {e}")
    exit()

# Создание изображения с текстом
try:
    # Настройки дисплея
    width = device.width
    height = device.height

    # Создаем пустое изображение
    text_image = Image.new("1", (width, height), "black")
    draw = ImageDraw.Draw(text_image)

    # Пишем текст на экране
    draw.text((10, 10), "Привет, Кирилл!", fill="white")  # Ваш текст и координаты

    # Отображение текста на экране
    device.display(text_image)
    print("Текст успешно отображен.")
except Exception as e:
    print(f"Ошибка при выводе текста: {e}")
    exit()

# Очистка экрана отключена, текст останется отображённым
# Удалите или закомментируйте строку ниже, если она у вас есть:
# device.clear()
