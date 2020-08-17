from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
class Display(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,600)
        self.setWindowTitle("Monitor")
        self.lcd = QLCDNumber()
        slider = QSlider(Qt.Horizontal)
        slider.valueChanged.connect(self.updateLCD)
        layout = QVBoxLayout()
        layout.addWidget(self.lcd)
        layout.addWidget(slider)
        self.setLayout(layout)

    def updateLCD(self, event):
        self.lcd.display(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Display()
    demo.show()
    sys.exit(app.exec_())