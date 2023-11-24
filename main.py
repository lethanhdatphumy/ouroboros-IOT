from scheduler import Scheduler
from OpenWeather import OpenWeather
from GetHumidityByLocation import GetHumidityByLocation
import time

global_data = ['', '', '', ''] #[temp, humanity, tưới-ed ? , giờ tưới]

scheduler = Scheduler()
scheduler.SCH_Init()

taskOpenWeather = OpenWeather(global_data)
getHumidityByLocation = GetHumidityByLocation(global_data)

scheduler.SCH_Add_Task(taskOpenWeather.openWeather_Run, DELAY=1000, PERIOD=5000)
scheduler.SCH_Add_Task(getHumidityByLocation.GetHumidity_Run, DELAY=1000, PERIOD=5000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)
