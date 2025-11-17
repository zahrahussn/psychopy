#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Demo of dot kinematogram
"""

from psychopy import visual, event, core
import platform
resx=1920

debug=0

if platform.platform()[0:5] == 'Linux': # if we're on Linux, then we're probably using the viewpixx monitor
    monitor = 'viewPixx'
    frameRate=120
    import ctypes
    xlib = ctypes.cdll.LoadLibrary("libX11.so")
    xlib.XInitThreads()
else:
    monitor = 'testMonitor'
    frameRate=60

win = visual.Window(monitor=monitor, fullscr=True, allowGUI=False, winType='pyglet', units='deg')


# Initialize some stimuli
dotPatch = visual.DotStim(win, color=(1.0, 1.0, 1.0), dir=90,
    nDots=100, fieldShape='circle', fieldPos=(0.0, 0.0), fieldSize=10,
    dotLife=8,  # number of frames for each dot to be drawn
    signalDots='same',  # are signal dots 'same' on each frame? (see Scase et al)
    noiseDots='direction',  # do the noise dots follow random- 'walk', 'direction', or 'position'
    speed=0.02, coherence=0.7, dotSize=5.85)

print(dotPatch)

message = visual.TextStim(win, text='Any key to quit', pos=(0, -6))
trialClock =core.Clock()
while not event.getKeys():
    dotPatch.draw()
    message.draw()
    win.flip()  # make the drawn things visible

    event.clearEvents('mouse')  # only really needed for pygame windows

print(win.fps())
win.close()
core.quit()

# The contents of this file are in the public domain.
