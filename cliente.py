import sys, Ice, time
import Demo

with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("SimplePrinter:default -p 10000")
    printer = Demo.PrinterPrx.checkedCast(base)
    if not printer:
        raise RuntimeError("Invalid proxy")


    mensaje="conectando"
    print(printer.printString(mensaje))
    while mensaje!="quit":
        mensaje = input()
        print(printer.printString("usuario -> " + mensaje))
        time.sleep(.3)
