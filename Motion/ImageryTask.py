from __future__ import absolute_import, division, print_function
from psychopy import visual, event, core, gui, data
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim
from random import shuffle
import string, time
import random, copy, scipy
import numpy as np
from psychopy.hardware import keyboard
import platform

params = {'Subject':'INSERTSUB', 'Experimenter':'aa'}
C90= 3 #insert coherence at 99% performance here
nTrialsPerCondition=4
frameRate=120
resx=1920
speed=2.7
blank1=1
dotSpeed=8.25 #in degrees per second (calculated from 0.11 deg/frame speed from Winawer paper with 75Hz monitor)
dotsize=0.174 #dot size in degrees (calculated from 5pix dot size in aa's monitor with 1024px resolution and 30cm scrren width, assuming viewing distance 57cm)
screenWidth=57.15 #screen width in cm
fpDuration=0.5
blank2=0.1
stimDuration=1
cueDuration=1
gaborDuration=6
sqrDuration0=6
upVert=[(0.5,0),(0,0.5),(-0.5,0),(-0.125,0),(-0.125,-0.5),(0.125,-0.5),(0.125,0)]
downVert=[(0.5,0),(0,-0.5),(-0.5,0),(-0.125,0),(-0.125,0.5),(0.125,0.5),(0.125,0)]
blockTypes=['up','up','down','down']
random.shuffle(blockTypes)


toFile('lastParams.pickle', params) #save params to file for next time

fileName = params['Experimenter']+'_'+params['Subject']+'_imagery'
dataFile = open('../../psychopyData/Motion/'+fileName+'.csv', 'a')#a simple text file with 'comma-separated-values'
dataFile.write('trial\tblocktrial\timagery_direction\tcoherence\tdot_direction\tcorresp\tsubjectResp\taccuracy\tRT\n')

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

# Create a visual window:
win = visual.Window(fullscr=True, allowGUI = True, monitor = monitor, winType='pyglet', units='deg')
win.mouseVisible=False

#creating stimuli
adapt_gabor = visual.GratingStim(win, tex="sqr", mask="sqr", texRes=256, 
           size=[15.0, 10.0], sf=[1, 0], ori = 270, name='gabor1', pos=(0,0))
arrowVert = [(0.5,0),(0,0.5),(-0.5,0),(-0.125,0),(-0.125,-0.5),(0.125,-0.5),(0.125,0)]
arrow = ShapeStim(win, vertices=arrowVert, fillColor='white', lineWidth=2, lineColor='black', pos=(0,0))
dot_stim = visual.DotStim(win, units='deg', color=(1.0, 1.0, 1.0), dir=270, opacity=1,
    nDots=100, fieldShape='circle', fieldPos=(0.0, 0.0), fieldSize=10,
    dotLife=5,  # number of frames for each dot to be drawn
    signalDots='same', noiseDots='direction',  
    dotSize=dotsize*resx/screenWidth,
    speed=dotSpeed/frameRate, coherence=0.9)
fixation=visual.Circle(win, radius=0.1,  edges=60, units='deg', lineWidth=2, lineColor=[-1,-1,-1], fillColor=[-1,-1,-1], colorSpace='rgb', pos=(0, 0))
blankFrame=visual.TextStim(win, text='', pos=(0, 0))
clockRT = core.Clock()
instruction1=visual.TextStim(win, text='You will be shown striped patterns moving up or down.', pos=(0,3))
instruction2=visual.TextStim(win, text='Try to attend to the size, color, and speed of the stripes, so that later you can picture them clearly even when the screen is blank.', wrapWidth=25, pos=(0,-1))
instruction3=visual.TextStim(win, text='On the next screen, you will see an arrow on an image of the striped pattern. Remember the direction the arrow is pointing in.', wrapWidth=35, pos=(0,7))
instruction5=visual.TextStim(win, text='Once the arrow disappears, a flashing square will appear. Focus on it while imagining the moving stripes in the direction of the arro.w', wrapWidth=35, pos=(0,1))
instruction6=visual.TextStim(win, text='After that, you will see moving dots. If the dots generally move UP, press Q. If they move DOWN, press M.', pos=(0,-3), wrapWidth=35, units='deg')
breakscreen=visual.TextStim(win, text='Press the spacebar to continue', pos=(0,-7), wrapWidth=20, units='deg')
breakscreen1=visual.TextStim(win, text='End of block. You may now take a break.', pos=(0,-0), wrapWidth=20, units='deg')
endscreen1 = visual.TextStim(win, text='End of task', pos=(0,2), height=0.6, wrapWidth=20, units='deg')
endscreen2 = visual.TextStim(win, text='Press space to exit', pos=(0,0), height=0.6, wrapWidth=20, units='deg')
color = np.array([1, 1, 1])
sqrVert = [(-0.25,-0.25),(-0.25,0.25),(0.25,0.25),(0.25,-0.25)]
sqr = ShapeStim(win, vertices=sqrVert, fillColor=color, lineWidth=2, lineColor=None, pos=(0,0))
kb = keyboard.Keyboard()

keys = kb.getKeys()
while 'space' not in keys:
    win.mouseVisible=False
    instruction1.draw()
    instruction2.draw()
    breakscreen.draw()
    win.flip()
    keys = kb.getKeys()

trial=0;
for i in [0,1,2,3]:
    if blockTypes[i]=='up':
        arrow = ShapeStim(win, vertices=upVert, fillColor='white', lineWidth=2, lineColor='black', pos=(0,0))
    else: arrow = ShapeStim(win, vertices=downVert, fillColor='white', lineWidth=2, lineColor='black', pos=(0,0))
    
    if i in [0]:
        for frameN in range(int(round(fpDuration*frameRate))):
            blankFrame.draw()
            win.update()
    else:
        keys = kb.getKeys()
        while 'space' not in keys:
            breakscreen1.draw()
            breakscreen.draw()
            win.mouseVisible=False
            win.update()
#            win.mouseVisible=False/home/zahra/.local/lib/python3.10/site-packages/psychopy/demos/coder/experiment control
            keys = kb.getKeys()
            win.mouseVisible=False
    # setup trial handler
    stimList=[]
    for direction in [90, 270]:
        for coherence in [C90, C90/2, C90/4]: # coherence at 99% performance, half and then quarter of that
            stimList.append({'direction': direction, 'coherence': coherence})
    trials = data.TrialHandler2(stimList, nTrialsPerCondition)
    clockRT = core.Clock() 
    
    response=''
    responseField=''
    blockTrial=0
    #for frameN in range(int(round(stimDuration*frameRate))):
    #        instruction.draw()
    #        win.update()
    
    win.mouseVisible=False
    adapt_gabor.setOri(90)
    adapt_gabor.setOpacity(1)
    for frameN in range(int(round(gaborDuration*frameRate))):
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
    adapt_gabor.setOri(270)
    for frameN in range(int(round(gaborDuration*frameRate))):
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
    adapt_gabor.setOri(90)
    for frameN in range(int(round(gaborDuration*frameRate))):
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
    adapt_gabor.setOri(270)
    for frameN in range(int(round(gaborDuration*frameRate))):
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
    keys = kb.getKeys()
    while 'space' not in keys:
        instruction3.draw()
        instruction4.draw()
        instruction5.draw()
        instruction6.draw()
        breakscreen.draw()
        win.mouseVisible=False
        win.update()
        win.mouseVisible=False
        keys = kb.getKeys()
        win.mouseVisible=False
    
    for thisTrial in trials:
        win.mouseVsible=False
        blockTrial=blockTrial+1
        trial=trial+1
        
        if trials.thisN==0:
           sqrDuration=60
        else: sqrDuration=sqrDuration0
        print(sqrDuration)
        if trials.thisTrial.direction==90:
            corresp='q'
        else: corresp='m'
                
        dot_stim.dir=trials.thisTrial.direction
        dot_stim.coherence=trials.thisTrial.coherence
    
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
            keys = kb.getKeys(keyList=['escape','q','m'])
            win.mouseVisible=False
            for thisKey in keys:
                if thisKey.name in ['escape']: 
                    dataFile.write('%d%s\t\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %(trial,blockTrial,blockTypes[i],trials.thisTrial.coherence,trials.thisTrial.direction,corresp,'NA','NA',round(thisKey.rt,2)))
                    core.quit()
                elif thisKey.name==corresp:
                    thisResponse=1
                    accuracy=1
                    win.mouseVisible=False
                    win.update()
                    win.mouseVisible=False
                else:
                    thisResponse=1
                    accuracy=0 
                    win.mouseVisible=False
                    win.update()
                    win.mouseVisible=False
        trials.addData('RT', thisKey.rt)
        trials.addData('accuracy', accuracy)
        event.clearEvents()
        dataFile.write('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %(trial,blockTrial,blockTypes[i],trials.thisTrial.coherence,trials.thisTrial.direction,corresp,thisKey.name, accuracy,round(thisKey.rt,2)))

keys = kb.getKeys()
while 'space' not in keys:
    win.mouseVisible=False
    endscreen1.draw()
    endscreen2.draw()
    win.flip()
    keys = kb.getKeys()


win.close()
core.quit()
