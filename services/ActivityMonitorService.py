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
        activities = self.db.get_activities()
        self.activity_selection_screen = ActivitySelectionScreen(self, activities)
        self.activity_selection_screen.show()

    def create_activity(self, activity_type, cal_per_hour):
        self.activity = Activity(activity_type, cal_per_hour)
        self.activity_monitor_screen = ActivityMonitorScreen(self, self.activity.type)
        self.activity_monitor_screen.show()
        self.timer = self.create_timer()
        self.timer.start_timer()
        self.timer.timeout.connect(self.update_activity_monitor_screen)
        
    def update_activity_monitor_screen(self):
        self.smartwatch_reading = self.smartwatch.get_smartwatch_reading()
        self.current_time_elapsed = self.timer.time_elapsed()
        self.current_calories_burned = self.calories_burned(self.current_time_elapsed[1], self.activity.cal_per_hour)
        self.activity_monitor_screen.update(self.smartwatch_reading, self.current_time_elapsed[0]
                                            , self.current_calories_burned)
        
    def end_activity(self):
        self.timer.stop()
        self.db.store_activity(self.current_time_elapsed[0], self.current_calories_burned, 
                               self.smartwatch_reading)
        self.db.update_calorie_counter()
        self.activity_summary_screen = ActivitySummaryScreen(self, self.activity.type, 
                                                             self.current_time_elapsed[0], 
                                                             self.current_calories_burned)
        self.activity_summary_screen.show()

    def create_timer(self):
        return Timer()
    
    def calories_burned(self, seconds, cal_per_hour):
        return str(int(seconds*cal_per_hour/3600))
    
    