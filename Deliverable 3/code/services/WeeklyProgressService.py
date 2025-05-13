from models.Progress import Progress
from models.Chart import Chart
from screens.WeeklyProgressScreen import WeeklyProgressScreen
from models.DBManager import  DBManager

class WeeklyProgressService:
    def __init__(self, db:DBManager):
        self.db = db

    def weekly_progress(self):
        weekly_data = self.db.get_weekly_data()
        self.sufficient_data()
        self.avg_daily_calories()
        self.total_activity_calories()
        self.daily_challenge_freq()
        self.progress = Progress()
        self.grade_progress()
        self.chart = Chart()
        self.weekly_progress_screen = WeeklyProgressScreen(self)
        self.weekly_progress_screen.show()

    def export(self):
        pass

    def sufficient_data(self):
        pass

    def avg_daily_calories(self):
        pass

    def total_activity_calories(self):
        pass

    def daily_challenge_freq(self):
        pass

    def grade_progress(self):
        pass

