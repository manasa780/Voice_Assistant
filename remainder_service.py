import schedule
import time
from speech_engine import speak

def set_reminder(message, delay):

    def reminder():
        speak(message)

    schedule.every(delay).seconds.do(reminder)

    while True:
        schedule.run_pending()
        time.sleep(1)