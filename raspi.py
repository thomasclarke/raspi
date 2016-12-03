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
hi = GPIO.HIGH # GPIO is turned on if this var is used
lo = GPIO.LOW # GPIO is turned off if this var is used
 
# functions
def inpt(gpio): # set a GPIO to input
    GPIO.setup(gpio, inp)
def outpt(gpio): # set a GPIO to output
    GPIO.setup(gpio, outp)
def on(gpio): # turn a GPIO on
    outpt(gpio)
    GPIO.output(gpio, hi)
def off(gpio): # turn a GPIO off
    outpt(gpio)
    GPIO.output(gpio, lo)
def cln(): # reset any existing settings for GPIOs:
	GPIO.cleanup
