import _thread, time, sys, serial, Ice, Demo

global_ser = serial.Serial(port='COM7', baudrate=9600, timeout=0, write_timeout=0)

def data_reciver():

   with Ice.initialize(sys.argv) as communicator:
      base = communicator.stringToProxy("SimplePrinter:default -p 10000")
      printer = Demo.PrinterPrx.checkedCast(base)
      if not printer:
         raise RuntimeError("Invalid proxy")
      while True:
         printer.printString("2")
         global_ser.write(str("s").encode())

   #global_ser.write(input().encode())

def data_sender():
   while True:
      response = global_ser.readline()
      if response is not None:

         with Ice.initialize(sys.argv) as communicator:
            base = communicator.stringToProxy("SimplePrinter:default -p 10000")
            printer = Demo.PrinterPrx.checkedCast(base)

            if not printer:
               raise RuntimeError("Invalid proxy")

            #envio de los datos de sensoires
            mensaje = "conectado"
            #manda los valorores de los sensores por mediop de comunicacion serial con un foramto on@12@34
            printer.printString(str(response)[2:][:-5])
            time.sleep(1)
            #recive el dato y lo pasa a la placa por convercion a byte para la comunicacion serial
            global_ser.write(str(printer.printString(mensaje)).encode())

def main():
   try:
      #se crean hilos para paralelizar el trabajo
      #_thread.start_new_thread(data_reciver())
      _thread.start_new_thread(data_sender())

   except:
      print("Error: unable to start thread")
   while 1:
      pass

if __name__ == '__main__':
    main()
