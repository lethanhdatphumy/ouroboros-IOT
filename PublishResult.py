from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
import gspread.exceptions


class PublishResult:
    def __init__(self, global_data):
        self.temperature = global_data[1]
        self.humidity = global_data[2]
        self.publish = global_data[4]
        print("Init publish result")
        self.number_of_seats = 3
        gc = gspread.service_account(
            filename="./client_secret_381278414659-0m31ivarqf8ugu4t3v39vaipu4q9j9ct.apps.googleusercontent.com.json")
        self.current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.sheet_name = "Ouroboros - history"

        try:  # Try to open today's sheet
            sheet = gc.open(self.sheet_name)
            self.work_sheet = sheet.sheet1
        except:  # Today's sheet does not exist
            # Create a new one
            sheet = gc.create(self.sheet_name)
            # Share to your account to view
            sheet.share('admin@trivie.com.vn', perm_type='user', role='writer')
            self.work_sheet = sheet.sheet1

            # Add titles to columns
            content = ["Temperature", "Humidity", "Time"]
            self.work_sheet.append_row(content, table_range="A1:C1")

    def PublishResult_run(self):
        from main import global_data
        if global_data[3] & global_data[2]:
            # content = [self.temperature, self.humidity, self.current_date]
            content = [12, 26.5, "lalalala"]

        if global_data[4]:
            self.work_sheet.append_row(content, table_range="A1:C1")
            global_data[4] = False
