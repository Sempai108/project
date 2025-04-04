from Adafruit_SSD1306 import SSD1306_128x64
from PIL import Image, ImageDraw

display = SSD1306_128x64()
display.begin()
display.clear()
display.display()

image = Image.new('1', (128, 64))
draw = ImageDraw.Draw(image)
draw.text((0, 0), 'Hello, OLED!', fill=255)
display.image(image)
display.display()

