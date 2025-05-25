import time
from PyQt6.QtCore import QTimer

class Timer(QTimer):
    def __init__(self):
        super().__init__()
        self.seconds_elapsed = 0

    def start_timer(self):
        self.start(1000)

    def time_elapsed(self):
        self.seconds_elapsed += 1
        hours = self.seconds_elapsed // 3600
        minutes = (self.seconds_elapsed % 3600) // 60
        seconds = self.seconds_elapsed % 60
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        return [ time_str, seconds ]


