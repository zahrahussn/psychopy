1#from psychopy import *
from psychopy import visual, event, core, gui, data
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim, TextStim
from random import shuffle
import string, time
import random, copy, scipy, pygame
import numpy 
from psychopy import sound


params = {'ID number':'1',
	 'frameRate':60, 'ISI': 1, 'fp': 0.5,'task':'flankerLetterTask'}
   
# create window and stimuli
win = visual.Window(fullscr=True, allowGUI = True, monitor = 'attentionExperimentsMonitor', units = 'deg')
win.mouseVisible=False
targetLeftVert = [(0.1, -0.1),( -0.1, 0), (0.1, 0.1)] 
targetRightVert = [(-0.1, -0.1),( 0.1, 0), (-0.1, 0.1)] 
textCol= [-1, -1, -1]
linew=4
textSize=3

corSnd = sound.Sound(2400, octave=14, secs=0.1)
incorSnd = sound.Sound(800, octave=7, secs=0.1)
corSnd.setVolume(0.7)
incorSnd.setVolume(0.7)

# setup trial handler
stimList = []
for target in ['H', 'K', 'S', 'C']:
    for distractor in ['H', 'K', 'S', 'C']:
        stimList.append({'target': target, 'distractor':distractor})
trials = data.TrialHandler(stimList, 2)

trials.data.addDataType('accuracy')
trials.data.addDataType('RT')
clockRT = core.Clock() # initialize reaction times

for thisTrial in trials:
    
    if trials.thisTrial.target in ('H', 'K'):corresp=1
    elif trials.thisTrial.target in ('S', 'C'):corresp=2
    
    if trials.thisTrial.target in ('H', 'K') and trials.thisTrial.distractor in ('H', 'K'): congruence=1
    elif trials.thisTrial.target in ('H', 'K') and trials.thisTrial.distractor in ('S', 'C'): congruence=0
    elif trials.thisTrial.target in ('S', 'C') and trials.thisTrial.distractor in ('S', 'C'): congruence=1
    elif trials.thisTrial.target in ('S', 'C') and trials.thisTrial.distractor in ('H', 'K'): congruence=0
    
    targ = TextStim(win, text=trials.thisTrial.target, height=textSize,color=textCol,pos=[0,0])
    dist1 = TextStim(win, text=trials.thisTrial.distractor, height=textSize,color=textCol,pos=[-6,0])
    dist2 = TextStim(win, text=trials.thisTrial.distractor, height=textSize,color=textCol,pos=[-4,0])
    dist3 = TextStim(win, text=trials.thisTrial.distractor, height=textSize,color=textCol,pos=[-2,0])
    dist4 = TextStim(win, text=trials.thisTrial.distractor, height=textSize,color=textCol,pos=[2,0])
    dist5 = TextStim(win, text=trials.thisTrial.distractor, height=textSize,color=textCol,pos=[4,0])
    dist6 = TextStim(win, text=trials.thisTrial.distractor, height=textSize,color=textCol,pos=[6,0])
 
    # blank screen for 50 ms
    for frameN in range(int(round(params['ISI']*params['frameRate']))):
        win.update()
            
    thisResponse = None
    while thisResponse == None:

    # stimulus
#    for frameN in range(int(round(params['duration']*params['frameRate']))):
        clockRT.reset()
        targ.draw() 
        dist1.draw()
        dist2.draw()
        dist3.draw()
        dist4.draw()
        dist5.draw()
        dist6.draw()
        win.update()
    

    
    # start collecting response

        allKeys = event.waitKeys(timeStamped = clockRT)
        for keyTuple in allKeys:
            [thisKey, thisRT] = keyTuple
        for thisKey in allKeys:
            if thisKey in ['escape']:core.quit()
            elif int(thisKey[0]) == corresp:
                thisResponse=1
                accuracy = 1
                corSnd.play()
            else: 
                thisResponse=1
                accuracy = 0
                incorSnd.play()
            trials.data.add('accuracy', accuracy)

win.close()
core.quit()