#!/usr/bin/env python
import socket
import sys, tty, termios
import time

def getch():
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch

HOST, PORT = "swcai-desktop.sh.intel.com", 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
   sock.connect((HOST, PORT))
   while True:
      c = getch()
      print c
      if c == 'i':
         sock.sendall('up\n')
      if c == 'l':
         sock.sendall('left\n')
      if c == 'j':
         sock.sendall('right\n')
      if c == 'k':
         sock.sendall('down\n')
      if c == 'q':
         sock.sendall('bye\n')
         break
finally:
   sock.close()
