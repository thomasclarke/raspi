import time
import sys
sys.path.insert(0, '../')
import raspi as p 
import RPi.GPIO as g
leds = (17,18)
p.outpt(leds)
p.off(leds)

btn = 21
p.inpt(btn)

while True:
	if g.input(btn) == False:
		print("Button pressed")
		p.on(leds)
	else:
		print("Waiting...")
		p.off(leds)
	time.sleep(0.1)



