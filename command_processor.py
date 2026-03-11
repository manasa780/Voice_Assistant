from speech_engine import speak
from weather_service import get_weather
import wikipedia

def process_command(command):

    if "hello" in command:
        speak("Hello Manasa, how can I help you")

    elif "weather" in command:
        weather = get_weather()
        speak(weather)

    elif "who is" in command:
        person = command.replace("who is", "")
        result = wikipedia.summary(person, 2)
        speak(result)

    elif "time" in command:
        from datetime import datetime
        time = datetime.now().strftime("%H:%M")
        speak("Current time is " + time)

    else:
        speak("Sorry, I didn't understand the command.")