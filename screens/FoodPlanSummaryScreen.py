from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QFileDialog, QMessageBox
from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtGui import QPainter, QPageSize
from ui_py import (food_plan_summary_ui)
import main_menu


def placeholder():
    pass

class FoodPlanSummaryScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = food_plan_summary_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.label_4.setText('Greek Yogurt with Honey and Berries')
        self.ui.label_5.setText('Greek Salad with Grilled Chicken')
        self.ui.label_6.setText('Grilled Salmon with Quinoa and Steamed Broccoli')
        self.ui.tableWidget.setRowCount(3)
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Quantity', 'Price'])
        self.populate_table()
        
        # self.ui.label_4 is the breakfast label
        # self.ui.label_5 is the lunch label
        # self.ui.label_6 is the dinner label
        # self.ui.tableWidget is the food plan table find how to insert items
        self.ui.pushButton_9.clicked.connect(self.export_to_pdf) #export to pdf
        self.ui.pushButton_10.clicked.connect(self.show_main_menu_screen) #main menu

    def populate_table(self):
        food_names = [
        'Food1',
        'Food2', 
        'Food3'
        ]
    
        self.ui.tableWidget.setVerticalHeaderLabels(food_names)

        foods = [
            ('500g', '$5.99'),  
            ('700g', '$12.99'), 
            ('400g', '$18.99')   
        ]

        for row, (quantity, price) in enumerate(foods):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(quantity))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(price))

    def placeholder(self):
        self.deleteLater()
        pass

    def export_to_pdf(self):
        try:
            
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save PDF",
                "food_plan_summary.pdf",
                "PDF Files (*.pdf)"
            )
            
            if file_path:
                
                printer = QPrinter(QPrinter.PrinterMode.HighResolution)
                printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
                printer.setOutputFileName(file_path)
                printer.setPageSize(QPageSize(QPageSize.PageSizeId.A4))
                
                
                painter = QPainter()
                if painter.begin(printer):
                    
                    widget_rect = self.rect()
                    page_rect = printer.pageRect(QPrinter.Unit.DevicePixel)
                    
                    
                    scale_x = page_rect.width() / widget_rect.width()
                    scale_y = page_rect.height() / widget_rect.height()
                    scale = min(scale_x, scale_y)  
                    
                    
                    painter.scale(scale, scale)
                    
                    
                    self.render(painter)
                    painter.end()
                    
                    
                    QMessageBox.information(
                        self,
                        "Export Successful",
                        f"Food plan exported to:\n{file_path}"
                    )
                else:
                    QMessageBox.critical(
                        self,
                        "Export Error",
                        "Failed to initialize PDF painter"
                    )
            else:
                print("No file selected")
                
        except Exception as e:
            QMessageBox.critical(
                self,
                "Export Error",
                f"Failed to export PDF:\n{str(e)}"
            )
            print(f"PDF export error: {e}")
    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()
