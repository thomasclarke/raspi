	import time
import os
import sys
sys.path.insert(0, '../')
import raspi as p 
import RPi.GPIO as g


bzr = 21
p.outpt(bzr)
p.off(bzr)

btn = 17
p.btn_setup(btn)

print('Waiting to be pressed')
print('>>')

while True:
	try:	
		if g.input(btn) == True:
			p.on(bzr)
			print("<< Button pressed >>")
		else:
			#print("Push button")
			time.sleep(0.02)
			os.system('clear')
			p.off(bzr)
	except KeyboardInterrupt:
		print()
		print("<< Process ended by CTRL-C >>")
		break


