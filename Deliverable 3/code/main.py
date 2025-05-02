# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import QApplication
import ui_classes

app = QApplication(sys.argv)
main_menu = ui_classes.MainMenuWindow()
app.exec()
