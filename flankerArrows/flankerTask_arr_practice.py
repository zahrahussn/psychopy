1#from psychopy import *
from psychopy import visual, event, core, gui, data
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim
from random import shuffle
import string, time
import random, copy, scipy, pygame
import numpy 
from psychopy import sound


params = {'ID number':'1',
	 'frameRate':60, 'ISI': 1, 'fp': 0.5,'task':'flankerTask', 'computer':'raylan'}

# create window and stimuli
win = visual.Window(fullscr=True, allowGUI = True, monitor = 'attentionExperimentsMonitor', units = 'deg')
win.mouseVisible=False
targetLeftVert = [(0.1, -0.1),( -0.1, 0), (0.1, 0.1)] 
targetRightVert = [(-0.1, -0.1),( 0.1, 0), (-0.1, 0.1)] 
arrowCol= [-1, -1, -1]
linew=4
arrowSize=6
targetLeft = ShapeStim(win, vertices=targetLeftVert, size=arrowSize, lineColor=arrowCol, lineWidth=linew, closeShape=False, pos=[0,0])
targetRight = ShapeStim(win, vertices=targetRightVert, size=arrowSize,lineColor=arrowCol,lineWidth=linew,  closeShape=False, pos=[0,0])
arrow2 = ShapeStim(win, vertices=targetLeftVert, size=arrowSize,lineColor=arrowCol,lineWidth=linew,  closeShape=False, pos=[2,0])
arrow3 = ShapeStim(win, vertices=targetLeftVert, size=arrowSize,lineColor=arrowCol,lineWidth=linew,  closeShape=False, pos=[4,0])
arrow4 = ShapeStim(win, vertices=targetLeftVert,size=arrowSize, lineColor=arrowCol, lineWidth=linew, closeShape=False, pos=[-4,0])
arrow5 = ShapeStim(win, vertices=targetLeftVert, size=arrowSize,lineColor=arrowCol,lineWidth=linew, closeShape=False, pos=[-2,0])
fixation = visual.PatchStim(win, color=-1, tex=None, mask='circle',size=0.2, units='deg', pos=[0,0])


corSnd = sound.Sound(2400, octave=14, secs=0.1)
incorSnd = sound.Sound(800, octave=7, secs=0.1)
corSnd.setVolume(0.7)
incorSnd.setVolume(0.7)

# setup trial handler
stimList = []
for dir in [1,2]:
    for con in [1,2]:
        stimList.append({'dir': dir, 'con':con})
trials = data.TrialHandler(stimList, 2)

trials.data.addDataType('accuracy')
trials.data.addDataType('RT')
clockRT = core.Clock() # initialize reaction times

for thisTrial in trials:
    # set arrow direction depending on trial type
    # target points left
    if trials.thisTrial['dir']==1:
        target=targetLeft
        if trials.thisTrial['con']==1:
            arrow2.setOri(0)
            arrow3.setOri(0)
            arrow4.setOri(0)
            arrow5.setOri(0)
        else:
            arrow2.setOri(180)
            arrow3.setOri(180)
            arrow4.setOri(180)
            arrow5.setOri(180)
    
    # target points right
    else:
        target=targetRight
        if trials.thisTrial['con']==1:
            arrow2.setOri(180)
            arrow3.setOri(180)
            arrow4.setOri(180)
            arrow5.setOri(180)
        else:
            arrow2.setOri(0)
            arrow3.setOri(0)
            arrow4.setOri(0)
            arrow5.setOri(0)

    # blank screen for 50 ms
    for frameN in range(int(round(params['ISI']*params['frameRate']))):
        win.update()
            
    thisResponse = None
    while thisResponse == None:

    # stimulus
#    for frameN in range(int(round(params['duration']*params['frameRate']))):
        clockRT.reset()
        target.draw() 
        arrow2.draw()
        arrow3.draw()
        arrow4.draw()
        arrow5.draw()
        win.update()
    

    
    # start collecting response

        allKeys = event.waitKeys(timeStamped = clockRT)
        for keyTuple in allKeys:
            [thisKey, thisRT] = keyTuple
        for thisKey in allKeys:
            if thisKey in ['escape']:core.quit()
            elif int(thisKey[0]) == int(trials.thisTrial['dir']):
                thisResponse=1
                accuracy = 1
                corSnd.play()
            else: 
                thisResponse=1
                accuracy = 0
                incorSnd.play()
            trials.data.add('accuracy', accuracy)


    event.clearEvents()
    

win.close()
core.quit()