from PyQt6.QtWidgets import QWidget

# make this a popup 
class ConfirmScreen(QWidget):
    def __init__(self,service):
        self.service = service