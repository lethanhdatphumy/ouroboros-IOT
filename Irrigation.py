import random
import time
import json
with open('weather_data.json', 'r') as file:
    weather_data = json.load(file)
current_temperature = weather_data.get('temperature', 0)
class SoilMoistureSensor:
    def __init__(self):
        self.moisture_level = random.randint(0, 100)
    def read_moisture(self):
        self.moisture_level = random.randint(0, 100)
        return self.moisture_level
class IrrigationSystem:
    def __init__(self):
        self.sensor = SoilMoistureSensor()
        self.is_on = False
    def check_and_update(self):
        moisture = self.sensor.read_moisture()
        print(f"Current Temperature: {current_temperature}°C")
        print(f"Soil moisture level: {moisture}%")
        if current_temperature > 30 and moisture < 30:
            self.is_on = True
            print("Irrigation system turned ON")
        else:
            self.is_on = False
            print("Irrigation system turned OFF")
def main():
    system = IrrigationSystem()
    while True:
        system.check_and_update()
        time.sleep(1)
if __name__ == "__main__":
    main()