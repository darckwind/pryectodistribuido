import sys, Ice, time, Comunication
from threading import Thread, Event, Lock
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class SliceCoonection(Comunication.Birateral):

    action = False

    def __init__(self):
        super().__init__()
        self.data=""

    #actualiza el valor del parametro action
    def set_action(self,comand):
        SliceCoonection.action = comand


    def comunicationBilateral(self, s,current=None):
        self.data = s
        #envia la data formateada al updatelcd para actualizar la pantalla de monitoreo
        Display.updateLCD(self.data)
        #se utiliza una espera de tiempo para no saturar el buffer de serial en el lado del cliente.
        time.sleep(0.5)
        #retorna el valor correspondioente para la activacion del actuador al cliente,
        #apartir del valor existente en action, sindo por defecto falso donde el actuador no realiza ninguna accion
        if self.action:
            #retorna el valor que acciona el actuador
            return "1"
        else:
            #retorna el valor que desactiva el actuador
            return "2"

    @staticmethod
    def connector():
        with Ice.initialize(sys.argv) as communicator:
            adapter = communicator.createObjectAdapterWithEndpoints("SimplePrinterAdapter", "default -p 11000")
            object = SliceCoonection()
            adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
            adapter.activate()
            communicator.waitForShutdown()


    #inicia el metodo connector
    @staticmethod
    def starter():
        SliceCoonection.connector()

class Display(QWidget):



    #inicio de componentes para la pantalla de monitoreo y control
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
        #se fijan los componentes de la pantalla a un layout
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

    #encargada de actualizar la informacion de la pantalla que es resivida con formato value@value@value, para lo cual se hace split del string para asi obtener cada dato
    def updateLCD(event):
        if event != "" and len(str(event).split("@"))==3:
            lcd_humedad.display(str(event).split("@")[0])
            lcd_temp_hamb.display(str(event).split("@")[1])
            lcd_temp_camara.display(str(event).split("@")[2])

    #funciones encargadas de manejar el actuador, mediante el cambio del valor de una variable, el cual afecta el valor que retorna
    def launch(self):
        SliceCoonection().set_action(True)

    def stop_launch(self):
        SliceCoonection().set_action(False)


if __name__ == '__main__':


    #inicia el hilo de comunicacion del servidor
    tc = Thread(target=SliceCoonection.starter,daemon=True)
    tc.start()

    #se instancia de manera global los parametros basicos de la pantalla, para facilitar el trabajo con estos
    app = QApplication(sys.argv)
    lcd_humedad = QLCDNumber()
    lcd_temp_camara = QLCDNumber()
    lcd_temp_hamb = QLCDNumber()

    demo = Display()
    #se procede a lanzar la pantalla
    demo.show()


    #destruye el hilo al momento de cerrar la ventana
    if app.exec_() == 0:
        tc.stop()
        sys.exit(app.exec_())
