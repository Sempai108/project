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

# Загрузка изображения
image_path = "/home/promrobo/project/w1.png"
try:
    # Загружаем изображение и преобразуем его в черно-белое
    image = Image.open(image_path).convert("1")
    # Масштабируем изображение под разрешение дисплея (например, 128x64)
    image = image.resize((128, 64))  # Убедитесь, что размеры совпадают с вашим дисплеем
    print(f"Изображение {image_path} загружено успешно.")
except FileNotFoundError:
    print(f"Ошибка: Файл {image_path} не найден.")
    exit()
except Exception as e:
    print(f"Ошибка при загрузке изображения: {e}")
    exit()

# Отображение изображения на OLED-дисплее
try:
    device.clear()  # Очищаем экран перед отображением
    device.display(image)
    print("Изображение успешно отображено на экране.")
except Exception as e:
    print(f"Ошибка при отображении изображения: {e}")
    exit()

# Тестовое сообщение (опционально)
try:
    # Создаем пустое изображение для вывода текста
    test_image = Image.new("1", (128, 64), "black")
    draw = ImageDraw.Draw(test_image)
    draw.text((10, 10), "Привет, OLED!", fill="white")  # Пример текста
    device.display(test_image)
    print("Тестовый текст успешно отображён.")
except Exception as e:
    print(f"Ошибка при отображении тестового сообщения: {e}")

# Очистка экрана (опционально)
try:
    device.clear()
    print("Экран очищен.")
except Exception as e:
    print(f"Ошибка при очистке экрана: {e}")
