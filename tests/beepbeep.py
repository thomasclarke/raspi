import sys
import os
import sys
sys.path.insert(0, '../')
import raspi as p
import RPi.GPIO as g
import time

bzr = 21
p.outpt(bzr)

btn = 26
p.btn_setup(btn)

while True:
	
	try:
		if g.input(btn) == True:
			p.on(bzr)
	except KeyboardInterrupt:
		print("KEYBOARD INTERRUPT")
		break
		
