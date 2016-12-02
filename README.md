# RASPBERRY PI PROJECTS
Here is where I will put the code and info for my projects using the Raspberry Pi. I will lay out each of these like the demo below...

## <i>Title –</i> LED Project
This project is my first using the Raspberry Pi and GPIO ports. It is very simple: all that it does is turn on an LED at GPIO27 when a person types on(27). This can be adapted to be triggered by buttons and sensors. Similar code also works for other components, like buzzers.

### <i>Diagram</i> [made in <i>Fritzing</i>]:
<i> I apologise for any imperfections - I'm just starting out!</i><br>
<img src="/sample/diagram1.png" length=400 width=400>

## Footnote
`raspi.py` is a module that I will probably use in most of my projects where I have done all of the setup necessary to use
python with the Pi, so I can get straight on with the task in hand. To use this in different directories I will have to put this at the top of my code...
` # some_file.py
import sys
sys.path.insert(0, '/')
import raspi `
