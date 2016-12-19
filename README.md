# RASPBERRY PI PROJECTS
Here is where I will put the code and info for my projects using the Raspberry Pi. I will lay out each of these like the demo below...

## <i>Title –</i> LED Project
This project is my first using the Raspberry Pi and GPIO ports. It is very simple: all that it does is turn on an LED at GPIO27 when a person types `on(27)`. This can be adapted to be triggered by buttons and sensors. Similar code also works for other components, like buzzers.

### <i>Diagram</i> [made in <i>Fritzing</i>]:
<img src="/sample/diagram1.png" length=400 width=400>

## Footnote
`raspi.py` is a module that I will probably use in most of my projects where I have done all of the setup necessary to use
python with the Pi, so I can get straight on with the task in hand. To use this in different directories I will have to put this at the top of my code...<br>
` import sys ` <br>
` sys.path.insert(0, '../') `<br>
` import raspi as p` <br>
This allows me to import the module from the parent directory.<br> 
Otherwise I could duplicate the `raspi.py` file into the directory.<br>

### A few things you can do with my `raspi` module...
<ul>
  <li>
  Avoid all of the labourous setup items like setting mode to BCM, turning off warnings and GPIO.cleanup. It is all done in the module.
  </li>
  <li> 
  Quick setup of components...<br>
  Setting up components is usually done by `GPIO.setup(gpio, GPIO.IN)` or `~~~GPIO.OUT` but with my `raspi` module, you can simply type `input(gpio)` or `output(gpio)`. Say GPIO21 was an led: `output(21)`. You can also set up pushbuttons quickly using `btn_setup(gpio)`.
  </li>
<ul><br>
The module is forever expanding!
