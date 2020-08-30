import sys, Ice, time, Comunication
from threading import Thread, Event, Lock
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class SliceCoonection(Comunication.Birateral):
    action = False
    stop_threads = False
    def __init__(self):
        super().__init__()
        self.data=""

    def set_action(self,comand):
        SliceCoonection.action = comand
        print(self.action)


    def comunicationBilateral(self, s,current=None):
        self.data = s
        print(self.action)
        Display.updateLCD(self.data)
        time.sleep(0.5)
        if self.action:
            return "2"
        else:
            return "1"

    @staticmethod
    def connector():
        with Ice.initialize(sys.argv) as communicator:
            adapter = communicator.createObjectAdapterWithEndpoints("SimplePrinterAdapter", "default -p 11000")
            object = SliceCoonection()
            adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
            adapter.activate()
            communicator.waitForShutdown()
    @staticmethod
    def starter():
        SliceCoonection.connector()
        while True:
            if SliceCoonection.stop_threads:
                break

class Display(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(600, 200)
        self.setWindowTitle("Monitor")
        self.button = QPushButton("Launch")
        self.lable_temp_cam = QLabel("Temperatura Camara")
        self.lable_hume_ham = QLabel("Humedad Ambiente")
        self.lable_temp_ham = QLabel("Temperatura Ambiente")
        self.button = QPushButton("Launch")
        self.button_stop = QPushButton("Stop")

        layout = QGridLayout()
        layout.setSpacing(10)
        layout.addWidget(self.lable_temp_ham,1,0)
        layout.addWidget(self.lable_hume_ham,1,1)
        layout.addWidget(self.lable_temp_cam,1,2)
        layout.addWidget(lcd_temp_hamb,2,0)
        layout.addWidget(lcd_humedad,2,1)
        layout.addWidget(lcd_temp_camara,2,2)
        layout.addWidget(self.button,3,1)
        layout.addWidget(self.button_stop,3,2)
        self.button.clicked.connect(self.launch)
        self.button_stop.clicked.connect(self.stop_launch)
        self.setLayout(layout)

    def updateLCD(event):
        if event != "" and len(str(event).split("@"))==3:
            lcd_humedad.display(str(event).split("@")[0])
            lcd_temp_hamb.display(str(event).split("@")[1])
            lcd_temp_camara.display(str(event).split("@")[2])

    def launch(self):
        SliceCoonection().set_action(True)

    def stop_launch(self):
        SliceCoonection().set_action(False)


if __name__ == '__main__':



    tc = Thread(target=SliceCoonection.starter,daemon=True)
    tc.start()

    app = QApplication(sys.argv)
    lcd_humedad = QLCDNumber()
    lcd_temp_camara = QLCDNumber()
    lcd_temp_hamb = QLCDNumber()

    demo = Display()
    demo.show()
    if app.exec_() == 0:
        SliceCoonection().stop_threads = True
        sys.exit(app.exec_())
