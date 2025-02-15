import cv2
import time

# Открываем камеру (0 - это индекс камеры, при необходимости измените)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Не удалось открыть камеру")
    exit()

try:
    while True:
        # Захватываем кадр
        ret, frame = camera.read()

        if not ret:
            print("Не удалось получить кадр")
            break

        # Отображаем кадр
        cv2.imshow("Camera Feed", frame)

        # Задержка на 1 секунду
        time.sleep(1)

        # Выход из цикла при нажатии 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # Освобождаем ресурсы
    camera.release()
    cv2.destroyAllWindows()
