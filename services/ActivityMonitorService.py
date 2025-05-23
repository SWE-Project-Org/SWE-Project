from screens.ActivitySelectionScreen import ActivitySelectionScreen
from screens.ActivityMonitorScreen import ActivityMonitorScreen
from screens.ActivitySummaryScreen import ActivitySummaryScreen
from screens.Notification import NotificationScreen
from models.DBManager import  DBManager
from models.SmartWatch import SmartWatch
from models.Timer import Timer
from models.Activity import Activity

class ActivityMonitorService():
    def __init__(self, db:DBManager, smartwatch:SmartWatch):
        self.db = db
        self.smartwatch = smartwatch
        self.timer = None
        self.activity = None

    def monitor_activity(self):
        self.activities = self.get_activities()
        self.activity_selection_screen = ActivitySelectionScreen(self)
        self.activity_selection_screen.show()

    def create_activity(self):
        self.activity = Activity()
        self.timer = self.create_timer()
        self.activity_monitor_screen = ActivityMonitorScreen(self)
        self.activity_monitor_screen.show()
        self.timer.start_timer()
        self.smartwatch_reading = self.smartwatch.get_smartwatch_reading()
        self.current_calories_burned = self.calories_burned()
        self.current_time_elapsed = self.timer.time_elapsed()
        self.update_activity_monitor_screen()
        
    def end_activity(self):
        self.db.store_activity()
        self.db.update_calorie_counter()
        self.activity_summary_screen = ActivitySummaryScreen(self)
        self.activity_summary_screen.show()
    
    def get_activities(self):
        pass
    
    def create_timer(self):
        return Timer()
    
    def calories_burned(self):
        pass
    
    def update_activity_monitor_screen(self):
        self.activity_monitor_screen.update()