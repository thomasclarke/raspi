import time
import os
import sys
sys.path.insert(0, '../')
import raspi as p 
import RPi.GPIO as g


led = 26
p.outpt(led)
p.off(led)

btn = 17
p.btn_setup(btn)

while True:
	try:	
		print(">> ")
		if g.input(btn) == True:
			print("<< Button pressed >>")
			p.on(led)
		else:
			print("Push button")
			p.off(led)
		time.sleep(0.5)
	except KeyboardInterrupt:
		print()
		print("<< Process ended by CTRL-C >>")
		break


