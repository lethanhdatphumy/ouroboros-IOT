import requests
import json
import argparse
from simple_chalk import chalk

class OpenWeather:
    API_KEY = '3c110ac7e07818e06de1b8edee4e8917'
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

    def __init__(self, global_data):
        self.city_name = global_data[0]
        self.output = None
        print("Init OpenWeather")

    def get_weather(self):
        url = f"{self.BASE_URL}?q={self.city_name}&appid={self.API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code != 200:
            print(chalk.red("Error: Unable to retrieve weather information."))
            exit()
        self.data = response.json()

    def process_weather_data(self):
        temperature = self.data["main"]["temp"]
        feels_like = self.data["main"]["feels_like"]
        city = self.data["name"]

        self.output = {
            "city": city,
            "temperature": temperature,
            "feels_like": feels_like
        }

    def openWeather_Run(self):
        self.get_weather()
        self.process_weather_data()

        print(self.output["temperature"])
        from main import global_data
        global_data[1] = self.output["temperature"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get weather information for a destination.")
    parser.add_argument("destination", type=str, help="Destination city for weather information.")
    args = parser.parse_args()

    open_weather = OpenWeather(args.destination)
    open_weather.openWeather_Run()


