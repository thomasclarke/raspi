# import Rasperry Pi GPIO module:
import RPi.GPIO as GPIO
# set GPIO layout to BroadCom:
GPIO.setmode(GPIO.BCM)
# disable debugging feedback to terminal:
GPIO.setwarnings(False)
# reset any existing settings for GPIOs:
GPIO.cleanup

# variables
outp = GPIO.OUT # output GPIO
inp = GPIO.IN # input GPIO
on = GPIO.HIGH # GPIO is turned on if this var is used
off = GPIO.LOW # GPIO is turned off if this var is used
 
# functions
def inpt(gpio): # set a GPIO to input
    GPIO.setup(gpio, inp)
def outp(gpio): # set a GPIO to output
    GPIO.setup(gpio, outp)
def on(gpio): # turn a GPIO on
    outp(gpio)
    GPIO.output(gpio, on)
def off(gpio): # turn a GPIO off
    outp(gpio)
    GPIO.output(gpio, off)
def cln(): # reset any existing settings for GPIOs:
	GPIO.cleanup
