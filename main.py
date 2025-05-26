import sys
from PyQt6.QtWidgets import QApplication
import main_menu
app = QApplication(sys.argv)
main_menu = main_menu.MainMenuScreen()
app.exec()
