import sys, Ice, time
import Demo


class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        if(s == "conectando"):
            return "coneccion establecida"

        elif(s == "usuario -> quit"):

            return "bey bye"
        else:
            print(s)
            respuesta = str(input("-->"))
            time.sleep(0.3)
            return (respuesta)


with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("SimplePrinterAdapter", "default -p 10000")
    object = PrinterI()
    adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
    adapter.activate()
    communicator.waitForShutdown()