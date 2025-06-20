from models.Progress import Progress
from models.Chart import Chart
from screens.WeeklyProgressScreen import WeeklyProgressScreen
from models.DBManager import  DBManager

class WeeklyProgressService:
    def __init__(self, db:DBManager):
        self.db = db
        self.weekly_data = None
        self.progress = None
        self.chart = None

    def weekly_progress(self):
        self.weekly_data = self.db.get_weekly_data()
        self.sufficient_data()
        self.avg_daily_calories()
        self.total_activity_calories()
        self.daily_challenge_freq()
        self.progress = Progress()
        self.grade_progress()
        self.chart = Chart()
        self.chart.fig.savefig("ui/weekly_progress.png", dpi=300, bbox_inches='tight')
        self.weekly_progress_screen = WeeklyProgressScreen(self)
        self.weekly_progress_screen.show()

    def export(self):
        self.chart.fig.savefig("weekly_progress.pdf", bbox_inches='tight')

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

