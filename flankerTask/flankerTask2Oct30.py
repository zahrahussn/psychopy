1#from psychopy import *
from psychopy import visual, event, core, gui, data
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim
from random import shuffle
import string, time, strop
import random, copy, scipy, pygame
import numpy as np
from psychopy import sound


params = {'ID number':'1',
	 'frameRate':60,'duration':0.2, 'ISI': 0.02, 'fp': 1,'task':'Flanker_Task'}

dlg = gui.DlgFromDict(params, title='Flanker_Task', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', params)#save params to file for next time
else:
    core.quit()#the user hit cancel so exit
    
fileName = params['ID number'] 
dataFile = open(fileName+'.txt', 'a')#a simple text fil e with 'comma-separated-values'
dataFile.write('dir, con, accuracy, RT\n') 

# create window and stimuli
win = visual.Window(fullscr=True, allowGUI = True, monitor = 'boyd', units = 'deg')
arrowVert = [(-0.4,0.05),(-0.4,-0.05),(-.2,-0.05),(-.2,-0.1),(0,0),(-.2,0.1),(-.2,0.05)]
arrowCol= [-1, -1, -1]
arrowRGB = ShapeStim(win, vertices=arrowVert, fillColor=arrowCol, size=5, lineColor=arrowCol)
fixation = visual.PatchStim(win, color=-1, tex=None, mask='circle',size=0.2, units='deg')
arrow2 = ShapeStim(win, vertices=arrowVert, fillColor=arrowCol, size=5, lineColor=arrowCol)
arrow3 = ShapeStim(win, vertices=arrowVert, fillColor=arrowCol, size=5, lineColor=arrowCol)
arrow4 = ShapeStim(win, vertices=arrowVert, fillColor=arrowCol, size=5, lineColor=arrowCol)
arrow5 = ShapeStim(win, vertices=arrowVert, fillColor=arrowCol, size=5, lineColor=arrowCol)
arrowRGB.pos=1,0
arrow2.pos=5,0
arrow3.pos=2.5,0
arrow4.pos=-5, 0
arrow5.pos=-2.5,0
corSnd = sound.Sound(2400, octave=14, secs=0.1)
incorSnd = sound.Sound(800, octave=7, secs=0.1)
corSnd.setVolume(0.7)
incorSnd.setVolume(0.7)

# setup trial handler
stimList = []
for dir in [1,2]:
    for con in [1,2]:
        stimList.append({'dir': dir, 'con':con})
trials = data.TrialHandler(stimList, 20)

trials.data.addDataType('accuracy')
trials.data.addDataType('RT')
clockRT = core.Clock() # initialize reaction times

for thisTrial in trials:
    direction = trials.thisTrial['dir']
    
    # set arrow direction depending on trial type
    # target points right
    if trials.thisTrial['dir']==2:
        arrowRGB.setOri(0)
        if trials.thisTrial['con']==1:
            arrowRGB.pos = 1, 0
            arrow2.pos=6,0
            arrow3.pos=3.5,0
            arrow4.pos=-4, 0
            arrow5.pos=-1.5,0
            arrow2.setOri(0)
            arrow3.setOri(0)
            arrow4.setOri(0)
            arrow5.setOri(0)
        else:
            arrowRGB.pos = 1,0
            arrow2.pos=4,0
            arrow3.pos=1.5,0
            arrow4.pos=-6, 0
            arrow5.pos=-3.5,0
            arrow2.setOri(180)
            arrow3.setOri(180)
            arrow4.setOri(180)
            arrow5.setOri(180)
    
    # target points left
    else:
        arrowRGB.setOri(180)
        if trials.thisTrial['con']==1:
            arrowRGB.pos = -1, 0
            arrow2.pos=4,0
            arrow3.pos=1.5,0
            arrow4.pos=-6, 0
            arrow5.pos=-3.5,0
            arrow2.setOri(180)
            arrow3.setOri(180)
            arrow4.setOri(180)
            arrow5.setOri(180)
        else:
            arrowRGB.pos = -1,0
            arrow2.pos=6,0
            arrow3.pos=3.5,0
            arrow4.pos=-4, 0
            arrow5.pos=-1.5,0
            arrow2.setOri(0)
            arrow3.setOri(0)
            arrow4.setOri(0)
            arrow5.setOri(0)
        
    # show fixation point for one second
    for frameN in range(int(round(params['fp']*params['frameRate']))):
        fixation.draw()
        win.update()

    # show arrow for 200 ms
    for frameN in range(int(round(params['duration']*params['frameRate']))):
        arrowRGB.draw() 
        arrow2.draw()
        arrow3.draw()
        arrow4.draw()
        arrow5.draw()
        win.update()
    
    # show blank screen for 500 ms
    for frameN in range(int(round(params['ISI']*params['frameRate']))):
        win.update()
            
    clockRT.reset()
    
    # collect response
    thisResponse = None
    while thisResponse == None:
        allKeys = event.waitKeys(timeStamped = clockRT)
        for keyTuple in allKeys:
            [thisKey, thisRT] = keyTuple
        for thisKey in allKeys:
            if thisKey in ['escape']:core.quit()
            elif int(thisKey[0]) == int(trials.thisTrial['dir']):
                #print(int(thisKey[1]))
                thisResponse=1
                accuracy = 1
                corSnd.play()
            else: 
                thisResponse=1
                accuracy = 0
                incorSnd.play()
            trials.data.add('accuracy', accuracy)
    

    trials.addData('RT', thisRT)
    event.clearEvents()
    dataFile.write('%s %s %s %s\n' %(trials.thisTrial['dir'], trials.thisTrial['con'], accuracy, thisRT))
    

#df = trials.saveAsWideText(fileName = outputFile)
#dataFile.write('%s %s %s %s' %(dir, con, accuracy, RT))
win.close()
core.quit()