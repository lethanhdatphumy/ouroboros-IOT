from datetime import datetime
import gspread
import gspread.exceptions


class PublishResult:
    def __init__(self, global_data):
        self.global_data = global_data
        print("Init publish result")
        gc = gspread.service_account(
            filename="./client_secret_381278414659-0m31ivarqf8ugu4t3v39vaipu4q9j9ct.apps.googleusercontent.com.json")
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

    def PublishResult_run(self):  # Start publish result to google sheet
        from main import global_data
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content = [global_data[1], global_data[2], current_date]
        print("Run Publish result to google sheet")

        if global_data[4]:
            print("Publishing result to google sheet")
            self.work_sheet.append_row(content, table_range="A1:C1")
            global_data[4] = False
