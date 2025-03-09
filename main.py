from PyQt6.QtWidgets import QApplication
from mywindow import CalculatorModel
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorModel()
    window.show()
    app.exec()
