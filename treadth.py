import _thread, time, sys, serial, Ice, Comunication

from threading import Thread, Event, Lock


#variable gloval de comunicacion por protocolo serial con placa de comunicacion
global_ser = serial.Serial(port='COM7', baudrate=9600, timeout=0, write_timeout=0)

class Conection():

   def data_sender(self):

      while True:
         # se reciven los datos por comunicacion serial
         response = global_ser.readline()

         if response is not None:

            with Ice.initialize(sys.argv) as communicator:
               #local
               base = communicator.stringToProxy("SimplePrinter:default -p 11000")
               #torre
               #base = communicator.stringToProxy("SimplePrinter:tcp -h 25.89.209.150 -p 12000")
               #mac
               #base = communicator.stringToProxy("SimplePrinter:tcp -h 25.5.222.9 -p 12000")
               com_bilateral = Comunication.BirateralPrx.checkedCast(base)

               if not com_bilateral:
                  raise RuntimeError("Invalid proxy")

               # envio de los datos de sensoires
               # manda los valorores de los sensores por mediop de comunicacion serial con un foramto on@12@34
               com_bilateral.comunicationBilateral(str(response)[2:][:-5])
               #print(str(response)[2:][:-5])
               com_bilateral.comunicationBilateral("")
               # recive el dato y lo pasa a la placa por convercion a byte para la comunicacion serial
               global_ser.write(str(com_bilateral.comunicationBilateral("")).encode())


class main():

   try:
      #se crean hilos para paralelizar el trabajo
      t = Thread(target=Conection().data_sender)
      t.start()

   except:
      print("Error: unable to start thread")
   while 1:
      pass

if __name__ == '__main__':
    main()
