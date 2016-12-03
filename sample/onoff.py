######################
# Thomas Clarke 2016 #
######################
__author__ = 'tclarke'

import sys
sys.path.insert(0, '../')
import raspi as p 


# components
led = 26
p.off(26)


print("ON or OFF?")
c = input("> ").upper()
if c == "ON":
    print("on")
    p.on(led)
