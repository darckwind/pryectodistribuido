import _thread, time, sys, serial, Ice, Demo

from threading import Thread, Event, Lock

global_ser = serial.Serial(port='COM7', baudrate=9600, timeout=0, write_timeout=0)

def data_sender():

   while True:
      response = global_ser.readline()
      if response is not None:

         with Ice.initialize(sys.argv) as communicator:
            base = communicator.stringToProxy("SimplePrinter:default -p 12000")
            printer = Demo.PrinterPrx.checkedCast(base)

            if not printer:
               raise RuntimeError("Invalid proxy")

            #envio de los datos de sensoires
            #manda los valorores de los sensores por mediop de comunicacion serial con un foramto on@12@34
            printer.printString(str(response)[2:][:-5])
            #recive el dato y lo pasa a la placa por convercion a byte para la comunicacion serial
            global_ser.write(str(printer.printString("")).encode())

def main():
   try:
      #se crean hilos para paralelizar el trabajo
      t = Thread(target=data_sender())
      t.start()
   except:
      print("Error: unable to start thread")
   while 1:
      pass

if __name__ == '__main__':
    main()
