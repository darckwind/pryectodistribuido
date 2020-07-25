import _thread, serial, time, sys

global_ser = serial.Serial( port='COM7', baudrate=9600, timeout=0, write_timeout=0)

def data_reciver():
   val = input("-->")
   print(val)
   sys.stdout.flush()

   #global_ser.write(input().encode())

def data_sender():
   while True:
      response = global_ser.readline()
      if response is not None:
         print(str(response)[2:][:-5])
         time.sleep(1)

def main():
   try:
      _thread.start_new_thread(data_reciver())
      _thread.start_new_thread(data_sender())

   except:
      print("Error: unable to start thread")
   while 1:
      pass

if __name__ == '__main__':
    main()
