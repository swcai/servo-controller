#!/usr/bin/env python
import serial
import SocketServer
import time
import daemon

HOST = 'swcai-desktop.sh.intel.com'
PORT = 1234
ADDR = (HOST, PORT)
BUFSIZE = 4096

# ms = serial.Serial('/dev/ttyUSB0', 115200)

class myHandler(SocketServer.StreamRequestHandler):
   def setup(self):
      print 'setup()'
      self.ms = serial.Serial('/dev/ttyUSB0', 115200)

   def finish(self):
      print 'finish()'
      self.ms.close()

   def handle(self):
      while True:
         self.data = self.request.recv(1024).strip()
         print self.data
         if self.data.startswith('left'):
            self.ms.write('left\n')
         if self.data.startswith('right'):
            self.ms.write('right\n')
         if self.data.startswith('up'):
            self.ms.write('up\n')
         if self.data.startswith('down'):
            self.ms.write('down\n')
         if self.data.startswith('bye'):
            break

def main():
   server = SocketServer.TCPServer(ADDR, myHandler)
   server.serve_forever()

if __name__ == "__main__":
   with daemon.DaemonContext():
      main()
