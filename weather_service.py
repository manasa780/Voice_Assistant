import requests
from config import WEATHER_API_KEY, CITY

def get_weather():

    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    return f"The temperature is {temperature}°C with {description}"