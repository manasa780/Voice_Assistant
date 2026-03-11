from speech_engine import listen, speak
from command_processor import process_command

def start_assistant():

    speak("Voice assistant started")

    while True:
        command = listen()

        if command != "":
            process_command(command)