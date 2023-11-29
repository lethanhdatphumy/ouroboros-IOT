import argparse

from GetHumidityByLocation import GetHumidityByLocation
from OpenWeather import OpenWeather


class SoilMoistureSensor:
    def __init__(self, humidity):
        self.moisture_level = humidity

    def read_moisture(self):
        return self.moisture_level


class IrrigationSystem:
    def __init__(self, city_name, sprinkler_status, write_to_sheet):
        self.city_name = city_name
        self.sprinkler_status = sprinkler_status
        self.write_to_sheet = write_to_sheet
        self.weather_fetcher = OpenWeather([self.city_name])
        self.humidity_fetcher = GetHumidityByLocation([])
        self.current_temperature = None
        self.current_humidity = None
        self.is_on = False

    def fetch_weather_data(self):
        self.weather_fetcher.openWeather_Run()
        self.humidity_fetcher.GetHumidity_Run()
        self.current_temperature = self.weather_fetcher.output["temperature"]
        self.current_humidity = float(self.humidity_fetcher.output["humidity"])  # Convert to float

    def IrrigationSystem_Run(self):
        self.fetch_weather_data()
        if self.current_temperature is None or self.current_humidity is None:
            print("Could not fetch weather data. Skipping irrigation check.")
            return

        # self.current_temperature = 29
        # self.current_humidity = 49

        print(f"Current Temperature: {self.current_temperature}°C")
        print(f"Soil moisture level: {self.current_humidity}%")
        if self.current_temperature > 30:
            self.is_on = False

        else:
            if self.current_humidity < 50:
                self.is_on = True
                self.sprinkler_status = self.is_on

            else:
                self.is_on = False
                self.sprinkler_status = self.is_on

        if self.is_on is False:
            print("Irrigation system turned OFF")

        else:
            print("Irrigation system turned ON")
            self.write_to_sheet = True

        from main import global_data
        if global_data[3] != self.sprinkler_status:
            global_data[4] = self.write_to_sheet
            print(global_data[4])
            global_data[4] = True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the irrigation system for a specific city.")
    parser.add_argument("city", type=str, help="Destination city for weather information.")
    args = parser.parse_args()

    irrigation_system = IrrigationSystem(args.city)
    irrigation_system.IrrigationSystem_Run()
