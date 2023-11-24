from scheduler import Scheduler
from task.SmartHome import SmartHome
from task.OpenWeather import OpenWeather
from task.ProcessUserinfo import ProcessUserInformation
from task.FaceDetect import FaceDetectionSystem

import time


def delay_amount(ms):
    start_time = time.time()
    while (time.time() - start_time) * 1000 < ms:
        pass


'''
class CurrentUser:
    def __init__(self):
        self.name = ""
        self.id = 0
        self.destination = ""
        self.currentTime = 0



current_user = CurrentUser()
current_user.name = "Dat"
current_user.name = "Dat"
current_user.id = "003"
current_user.destination = "Biên Hòa"
current_user.currentTime = int(time.time())
        '''
data = {"name": "",
        "destination": "ho chi minh",
        "weatherData":
            {"city": "Ho Chi Minh City", "temperature": 29.0, "feels_like": 31.0}
        }
dateTest = ["",
            "ho chi minh",
            ["Ho Chi Minh City", 29.0, 31.0]
            ]

scheduler = Scheduler()
scheduler.SCH_Init()

taskFaceRecognizer = FaceDetectionSystem(0)
taskOpenWeather = OpenWeather(1, dateTest)
#taskProcessUserInfo = ProcessUserInformation(3, data["name"])

scheduler.SCH_Add_Task(taskFaceRecognizer.FaceRecog_Run(), DELAY=1000, PERIOD=5000)
scheduler.SCH_Add_Task(taskOpenWeather.openWeather_Run, DELAY=1000, PERIOD=5000)
#scheduler.SCH_Add_Task(taskProcessUserInfo, DELAY=1000, PERIOD=5000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)
