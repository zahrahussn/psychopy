from psychopy import visual, core, event
import platform
from psychopy.hardware import keyboard

# window setup
if platform.platform()[0:5] == 'Linux': # if we're on Linux, then we're probably using the viewpixx monitor
    monitor = 'detectingMonitor'
    frameRate=120
    import ctypes
    xlib = ctypes.cdll.LoadLibrary("libX11.so")
    xlib.XInitThreads()
else:   
    monitor = 'testMonitor'
    frameRate=60
    
win = visual.Window(size=[1920, 1080], color=[-1, -1, -1], monitor='detectingMonitor', units='deg', checkTiming=False)

#red
#patch = visual.Circle(win=win, radius=4, fillColor=[-1, 0, 0],  lineColor=None)
#patch = visual.Circle(win=win, radius=4, fillColor=[0, 0, 0],  lineColor=None)
#patch = visual.Circle(win=win, radius=4, fillColor=[1, 0, 0],  lineColor=None)

#green
#patch = visual.Circle(win=win, radius=4, fillColor=[0, -1, 0],  lineColor=None)
#patch = visual.Circle(win=win, radius=4, fillColor=[0, 0, 0],  lineColor=None)
#patch = visual.Circle(win=win, radius=4, fillColor=[0, 1, 0],  lineColor=None)

#blue
#patch = visual.Circle(win=win, radius=4, fillColor=[0, 0, -1],  lineColor=None)
#patch = visual.Circle(win=win, radius=4, fillColor=[0, 0, 0],  lineColor=None)
patch = visual.Circle(win=win, radius=4, fillColor=[0, 0, 1],  lineColor=None)

instruct = visual.TextStim(win=win, text="press any key to quit.", pos=(0, -5))

patch.draw()
instruct.draw()
win.flip()

kb = keyboard.Keyboard()
keys = kb.getKeys()
while not keys:
    keys = kb.getKeys()

win.close()
core.quit()