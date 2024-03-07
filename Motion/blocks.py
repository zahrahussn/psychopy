from __future__ import absolute_import, division, print_function
from psychopy import visual, event, core, gui, data
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim
from random import shuffle
import string, time
import random, copy, scipy
import numpy 
from psychopy import sound


params = {'participant ID':'1','condition':'test'}
frameRate=60
blank1=0.5
fpDuration=0.5
blank2=0.1
stimDuration=1
blockTypes=[90, 270]

dlg = gui.DlgFromDict(params, title='MotionExp', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', params) #save params to file for next time
else:
    core.quit()#the user hit cancel so exit

fileName = params['participant ID']+'_blocks'
dataFile = open(fileName+'.csv', 'a')#a simple text file with 'comma-separated-values'
dataFile.write('trialNo, adapt_direction, coherence, direction, corresp, subjectResp, accuracy, incorrect, RT\n') 

# Create a visual window:
win = visual.Window(fullscr=False, allowGUI = True, monitor = 'testMonitor', winType='pyglet', units='deg')
#win = visual.Window(fullscr=True, allowGUI = True, monitor = 'attentionExperimentsMonitor', units = 'deg')
win.mouseVisible=False
#fixation = visual.PatchStim(win, color=-1, tex=None, mask='circle',size=0.2, units='deg')
dot_stim = visual.DotStim(win, color=(1.0, 1.0, 1.0), dir=270,
    nDots=500, fieldShape='circle', fieldPos=(0.0, 0.0), fieldSize=1,
    dotLife=5,  # number of frames for each dot to be drawn
    signalDots='same',  # are signal dots 'same' on each frame? (see Scase et al)
    noiseDots='direction',  # do the noise dots follow random- 'walk', 'direction', or 'position'
    speed=0.01, coherence=0.9)
fixation=visual.Circle(win, radius=0.1,  edges=128, units='deg', lineWidth=2, lineColor=[-1,-1,-1], fillColor=False, colorSpace='rgb', pos=(0, 0)) 
blankFrame=visual.TextStim(win, text='', pos=(0, 0))
instruction=visual.TextStim(win, text="Press p for up and q for down", pos=(0, 0))
adapt_gabor = visual.GratingStim(win, tex="sqr", mask="sqr", texRes=256, 
           size=[15.0, 10.0], sf=[1, 0], ori = 90, name='gabor1')
#corSnd = sound.Sound(2200, octave=14, secs=0.01) # auditory feedback
#incorSnd = sound.Sound(800, octave=7, secs=0.01) # auditory feedback

for i in [0,1]:
    adapt_gabor = visual.GratingStim(win, tex="sqr", mask="sqr", texRes=256, 
           size=[15.0, 10.0], sf=[1, 0], ori = blockTypes[i], name='gabor1')

    # setup trial handler
    stimList=[]
    for direction in [90, 270]:
        for coherence in [0.07, 0.14, 0.28]: # 0 is vertical; 10 is 10deg clockwise (to the right)
            stimList.append({'direction': direction, 'coherence': coherence})
    trials = data.TrialHandler(stimList, 3)
    trials.data.addDataType('accuracy')
    trials.data.addDataType('RT')
    clockRT = core.Clock() 
    
    #for frameN in range(int(round(stimDuration*frameRate))):
    #        instruction.draw()
    #        win.update()
    
    for thisTrial in trials:
        
        if trials.thisTrial.direction==90:
            corresp='p'
        else: corresp='q'
                
        
        dot_stim = visual.DotStim(win, color=(1.0, 1.0, 1.0), dir=trials.thisTrial.direction,
        nDots=100, fieldShape='circle', fieldPos=(0.0, 0.0), fieldSize=10, dotSize=5, 
        dotLife=5,  # number of frames for each dot to be drawn
        signalDots='same',  # are signal dots 'same' on each frame? (see Scase et al)
        noiseDots='direction',  # do the noise dots follow random- 'walk', 'direction', or 'position'
        speed=0.11, coherence=trials.thisTrial.coherence)
    #        
        #instructions
        win.mouseVisible=False
        
        for frameN in range(int(round(stimDuration*2*frameRate))):
            adapt_gabor.phase += 0.045
            adapt_gabor.draw()
            win.update()
        # show blank screen for 500 ms
        for frameN in range(int(round(blank1*frameRate))):
            win.update()
        # show fixation point for 500 ms
        for frameN in range(int(round(fpDuration*frameRate))):
            fixation.draw()
            win.update()
        thisResponse = None
        clockRT.reset()
    #    circleLeft.draw()
    #    circleRight.draw()
        for frameN in range(int(round(stimDuration*frameRate))):
            dot_stim.draw()
            win.update()
        #blank screen
        for frameN in range(int(round(blank2*frameRate))):
            win.update()
        while thisResponse == None: #could be put after
        # collect response
            allKeys = event.getKeys(keyList=['escape','p','q'],timeStamped = clockRT)
            for keyTuple in allKeys:
                [thisKey, thisRT] = keyTuple
            for thisKey in allKeys:
                if thisKey[0] in ['escape']:core.quit()
                elif thisKey[0] in ['p','q']:
                    if thisKey[0] == corresp:
                        thisResponse=1
                        accuracy = 1
                        incorrect = 0
                        #corSnd.play()
                    else: 
                        thisResponse=1
                        accuracy = 0
                        incorrect = 1
                        #incorSnd.play()
        #while thisResponse == None: #could be put after
        trials.addData('RT', thisRT)
        trials.addData('corresp', corresp)
        event.clearEvents()
        dataFile.write('%s %s %s %s %s %s %s %s %s\n' %(trials.thisTrialN, blockTypes[i], trials.thisTrial.coherence, trials.thisTrial.direction, corresp, thisKey[0], accuracy, incorrect, round(thisRT,3)))
        
win.close()
core.quit()