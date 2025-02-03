import pygame  # Импортируем библиотеку pygame для воспроизведения аудио

# Инициализация pygame
pygame.mixer.init()

# Загрузка и воспроизведение MP3-файла
pygame.mixer.music.load("C:\\Users\\1\\Documents\\ПР\\TTS\\TTS_1.mp3")
pygame.mixer.music.play()
с
# Задержка для воспроизведения аудио до конца
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
