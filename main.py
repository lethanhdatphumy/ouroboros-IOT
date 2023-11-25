from scheduler import Scheduler
from OpenWeather import OpenWeather
from GetHumidityByLocation import GetHumidityByLocation
from Irrigation import IrrigationSystem
import time

global_data = ['ho chi minh', '', '', False, False]  # [city, temp, humanity, current status  , status change ]

scheduler = Scheduler()
scheduler.SCH_Init()

taskOpenWeather = OpenWeather(global_data)
getHumidityByLocation = GetHumidityByLocation(global_data)
irrigation_system = IrrigationSystem(global_data[0], global_data[3], global_data[4])

# Adding a task to run the IrrigationSystem


scheduler.SCH_Add_Task(taskOpenWeather.openWeather_Run, DELAY=1000, PERIOD=5000)
scheduler.SCH_Add_Task(getHumidityByLocation.GetHumidity_Run, DELAY=1000, PERIOD=5000)
scheduler.SCH_Add_Task(irrigation_system.IrrigationSystem_Run, DELAY=1000, PERIOD=5000)
while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)
