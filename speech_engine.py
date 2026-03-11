import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

engine.setProperty('rate', 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("User:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("I did not understand. Please say again.")
        return ""

    except sr.RequestError:
        speak("Speech service is not available.")
        return ""