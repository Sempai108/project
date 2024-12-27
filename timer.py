import time
def countdown_timer (seconds):
    while seconds >= 0:
        time.sleep(1)
        print(seconds)
        seconds -= 1
countdown_timer(5)