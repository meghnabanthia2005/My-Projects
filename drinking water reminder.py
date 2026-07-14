import time
import winsound

interval = 3600  # 1 hour

while True:
    print("💧 Time to drink water!")
    winsound.Beep(1000, 1000)  # frequency, duration
    time.sleep(interval)