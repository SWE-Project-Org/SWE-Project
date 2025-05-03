from ui_classes import ActivitySelectionScreen, ActivityMonitorScreen, ActivitySummaryScreen
from support_classes import Activity, Timer, SmartWatch, DBManager

smartwatch = SmartWatch()
dbmanager = DBManager()

class ActivityMonitorService():

    def monitor_activity(self):
        self.activities = self.get_activities()
        self.activity_selection_screen = ActivitySelectionScreen(self)
        self.activity_selection_screen.show()
        
    def create_activity(self):
        self.activity = Activity()
        self.timer = self.create_timer()
        self.activity_monitor_screen = ActivityMonitorScreen(self)
        self.activity_monitor_screen.show()
        self.timer.StartTimer()
        self.smartwatch_reading = smartwatch.get_smartwatch_reading()
        self.current_calories_burned = self.calories_burned()
        self.current_time_elapsed = self.timer.time_elapsed()
        self.update_activity_monitor_screen()
        
    def end_activity(self):
        dbmanager.store_activity()
        dbmanager.update_calorie_counter()
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
    


    

    
        



    
