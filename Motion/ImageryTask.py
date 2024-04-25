from __future__ import absolute_import, division, print_function
from psychopy import visual, event, core, gui, data
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim
from random import shuffle
import string, time
import random, copy, scipy
import numpy as np

params = {'participant ID':'1','condition':'test'}
frameRate=60
speed=2.7
blank1=1
dotSpeed=0.11 #2deg/s, to be converted to 2deg/frame
fpDuration=0.5
blank2=0.1
stimDuration=1
cueDuration=1
sqrDuration0=6
upVert=[(0.5,0),(0,0.5),(-0.5,0),(-0.125,0),(-0.125,-0.5),(0.125,-0.5),(0.125,0)]
downVert=[(0.5,0),(0,-0.5),(-0.5,0),(-0.125,0),(-0.125,0.5),(0.125,0.5),(0.125,0)]
blockTypes=['up','up','down','down']
random.shuffle(blockTypes)
C99= 0.5 #insert coherence at 99% performance here

fileName = params['participant ID']+'_blocks'
dataFile = open(fileName+'.csv', 'a')#a simple text file with 'comma-separated-values'
dataFile.write('trial, blocktrial, adapt_direction, coherence, direction, corresp, subjectResp, accuracy, incorrect, RT\n')

win = visual.Window(monitor='testMonitor', units='deg', checkTiming=False)

# The fill color to start with.
#color = np.array([1, 1, 1])

adapt_gabor = visual.GratingStim(win, tex="sqr", mask="sqr", texRes=256, 
           size=[10.0, 7.0], sf=[1, 0], ori = 270, name='gabor1', pos=(0,0))
arrowVert = [(0.5,0),(0,0.5),(-0.5,0),(-0.125,0),(-0.125,-0.5),(0.125,-0.5),(0.125,0)]
arrow = ShapeStim(win, vertices=arrowVert, fillColor='white', lineWidth=2, lineColor='black', pos=(0,0))
dot_stim = visual.DotStim(win, color=(1.0, 1.0, 1.0), dir=270,
    nDots=500, fieldShape='circle', fieldPos=(0.0, 0.0), fieldSize=1,
    dotLife=5,  # number of frames for each dot to be drawn
    signalDots='same', 
    noiseDots='direction',  
    speed=dotSpeed, coherence=0.9)
fixation=visual.Circle(win, radius=0.1,  edges=128, units='deg', lineWidth=2, lineColor=[-1,-1,-1], fillColor=False, colorSpace='rgb', pos=(0, 0)) 
blankFrame=visual.TextStim(win, text='', pos=(0, 0))
clockRT = core.Clock()
instruction1=visual.TextStim(win, text='You will be shown striped patterns moving up or down.', pos=(0,3))
instruction2=visual.TextStim(win, text='Try to attend to the size, color, and speed of the stripes, so that later you can picture them clearly even when the screen is blank.', wrapWidth=20, pos=(0,0))
instruction3=visual.TextStim(win, text='On the next screen, you will see an arrow indicating the direction to imagine the striped pattern. If the arrow points UP, you need to imagine the stripes moving upwards with the same speed as seen earlier. If the arrow points DOWN, you need to imagine the stripes moving downward. Focus on the arrow until it is gone, then imagine the motion when you see a flashing square.', wrapWidth=20, pos=(0,1))
breakscreen=visual.TextStim(win, text='Press the spacebar to continue', pos=(0,-3), height=0.6, wrapWidth=20, units='deg')
breakscreen1=visual.TextStim(win, text='End of block', pos=(0,-0), wrapWidth=20, units='deg')
color = np.array([1, 1, 1])
sqrVert = [(-0.25,-0.25),(-0.25,0.25),(0.25,0.25),(0.25,-0.25)]
sqr = ShapeStim(win, vertices=sqrVert, fillColor=color, lineWidth=2, lineColor=None, pos=(0,0))
#kb = keyboard.Keyboard()

keys = event.getKeys()
while 'space' not in keys:
    win.mouseVisible=False
    instruction1.draw()
    instruction2.draw()
    breakscreen.draw()
    win.flip()
    #keyPress = event.waitKeys()
    keys = event.getKeys()

for i in [0,1,2,3]:
    if blockTypes[i]=='up':
        arrow = ShapeStim(win, vertices=upVert, fillColor='white', lineWidth=2, lineColor='black', pos=(0,0))
    else: arrow = ShapeStim(win, vertices=downVert, fillColor='white', lineWidth=2, lineColor='black', pos=(0,0))
    
    if i in [0]:
        for frameN in range(int(round(fpDuration*frameRate))):
            blankFrame.draw()
            win.update()
    else:
        keys = event.getKeys()
        while 'space' not in keys:
            if thisKey[0] in ['escape']:core.quit()
            breakscreen1.draw()
            breakscreen.draw()
            win.mouseVisible=False
            win.update()
            win.mouseVisible=False
            keys = event.getKeys()
            win.mouseVisible=False
    # setup trial handler
    stimList=[]
    for direction in [90, 270]:
        for coherence in [C99, C99/2, C99/4]: # coherence at 99% performance, half and then quarter of that
            stimList.append({'direction': direction, 'coherence': coherence})
    trials = data.TrialHandler(stimList, 1)
    trials.data.addDataType('accuracy')
    trials.data.addDataType('RT')
    clockRT = core.Clock() 
    
    #for frameN in range(int(round(stimDuration*frameRate))):
    #        instruction.draw()
    #        win.update()
    
    for frameN in range(int(round(stimDuration*2*frameRate))):
        adapt_gabor.setOri(90)
        adapt_gabor.setOpacity(1)
        adapt_gabor.phase += speed/frameRate
        adapt_gabor.draw()
        p=np.cos((frameN*speed/frameRate)*2*np.pi)
        #print(p)
        sqr.setFillColor([p,p,p])
        # Draw the stimulus and display it.
        sqr.draw()
        win.update()
    # show blank screen for 1s
    for frameN in range(int(round(blank1*frameRate))):
        blankFrame.draw()
        win.update()
    for frameN in range(int(round(stimDuration*2*frameRate))):
        adapt_gabor.setOri(270)
        adapt_gabor.setOpacity(1)
        adapt_gabor.phase += speed/frameRate
        adapt_gabor.draw() 
        p=np.cos((frameN*speed/frameRate)*2*np.pi)
        #print(p)
        sqr.setFillColor([p,p,p])
        # Draw the stimulus and display it.
        sqr.draw()
        win.update()
    # show blank screen for 1s
    for frameN in range(int(round(blank1*frameRate))):
        blankFrame.draw()
        win.update()
    for frameN in range(int(round(stimDuration*2*frameRate))):
        adapt_gabor.setOri(90)
        adapt_gabor.phase += speed/frameRate
        adapt_gabor.draw()
        p=np.cos((frameN*speed/frameRate)*2*np.pi)
        #print(p)
        sqr.setFillColor([p,p,p])
        # Draw the stimulus and display it.
        sqr.draw()
        win.update()
    # show blank screen for 1s
    for frameN in range(int(round(blank1*frameRate))):
        blankFrame.draw()
        win.update()
    for frameN in range(int(round(stimDuration*2*frameRate))):
        adapt_gabor.setOri(270)
        adapt_gabor.phase += speed/frameRate
        adapt_gabor.draw()
        p=np.cos((frameN*speed/frameRate)*2*np.pi)
        #print(p)
        sqr.setFillColor([p,p,p])
        # Draw the stimulus and display it.
        sqr.draw()
        win.update()
    # show blank screen for 1s
    for frameN in range(int(round(blank1*frameRate))):
        blankFrame.draw()
        win.update()
    # instructions for trials
    keys = event.getKeys()
    while 'space' not in keys:
        instruction3.draw()
        breakscreen.draw()
        win.mouseVisible=False
        win.update()
        win.mouseVisible=False
        keys = event.getKeys()
        win.mouseVisible=False
    
    for thisTrial in trials:
        
        if trials.thisTrialN==0:
           sqrDuration=10
        else: sqrDuration=sqrDuration0
        print(sqrDuration)
        if trials.thisTrial.direction==90:
            corresp='p'
        else: corresp='q'
                
        
        dot_stim = visual.DotStim(win, color=(1.0, 1.0, 1.0), dir=trials.thisTrial.direction,
        nDots=100, fieldShape='circle', fieldPos=(0.0, 0.0), fieldSize=10, dotSize=5, 
        dotLife=5,  # number of frames for each dot to be drawn
        signalDots='same',  # are signal dots 'same' on each frame? (see Scase et al)
        noiseDots='direction',  # do the noise dots follow random- 'walk', 'direction', or 'position'
        speed=dotSpeed, coherence=trials.thisTrial.coherence)
    #        
        #instructions
        win.mouseVisible=False
        
        for frameN in range(int(round(blank1*frameRate))):
            win.update()
        for frameN in range(int(round(cueDuration*frameRate))):
            # Draw the stimulus and display it.
            adapt_gabor.setOpacity(1 - frameN/frameRate)
            arrow.setOpacity(1 - frameN/frameRate)
            adapt_gabor.draw()
            arrow.draw()
            win.update()
        # show blank screen for 1s
        for frameN in range(int(round(blank1*frameRate))):
            win.update()
        # show fixation guide for 60/6s
        for frameN in range(int(round(sqrDuration*frameRate))):
            p=np.cos((frameN*speed/frameRate)*2*np.pi)
            sqr.setFillColor([p,p,p])
        # Draw the stimulus and display it.
            sqr.draw()
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