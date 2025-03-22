from PIL import Image
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
    image = Image.open(image_path).convert("1")  # Преобразуем изображение в черно-белое
    print(f"Изображение {image_path} загружено успешно.")
except FileNotFoundError:
    print(f"Ошибка: Файл {image_path} не найден.")
    exit()
except Exception as e:
    print(f"Ошибка при загрузке изображения: {e}")
    exit()

# Отображение изображения на OLED-дисплее
try:
    device.clear()  # Очищаем экран перед отображением изображения
    device.display(image)
    print("Изображение отображено на экране.")
except Exception as e:
    print(f"Ошибка при отображении изображения: {e}")
    exit()

# Очистка экрана (опционально)
try:
    device.clear()
    print("Экран очищен.")
except Exception as e:
    print(f"Ошибка при очистке экрана: {e}")
