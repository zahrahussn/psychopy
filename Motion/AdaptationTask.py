from __future__ import absolute_import, division, print_function
from psychopy import visual, event, core, gui, data
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim
from random import shuffle
import string, time
import random, copy, scipy
import numpy 
from psychopy.hardware import keyboard
import platform


params = {'Subject':'001', 'Experimenter':'aa'}
frameRate=120
blank1=0.5
dotSpeed=8.25 #in degrees per second
fpDuration=0.5
blank2=0.1
stimDuration=1
resx=1920
speed=2.7
C99= 0.28 #insert oherence level at 99% performance accuracy here

blockTypes=[90,90,90,90,270,270,270,270]
random.shuffle(blockTypes)

#dlg = gui.DlgFromDict(params, title='MotionExp', fixed=['dateStr'])
#if dlg.OK:
toFile('lastParams.pickle', params) #save params to file for next time
#else:
#    core.quit()#the user hit cancel so exit

fileName = params['Experimenter']+'_'+params['Subject']+'_adaptation'
dataFile = open('../../psychopyData/Motion/'+fileName+'.csv', 'a')#a simple text file with 'comma-separated-values'
dataFile.write('trial, blocktrial, adapt_direction, coherence, direction, corresp, subjectResp, accuracy, RT\n') 
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
#win = visual.Window(fullscr=True, allowGUI = True, monitor = 'attentionExperimentsMonitor', units = 'deg')
win.mouseVisible=False
#creating stimuli
dot_stim = visual.DotStim(win, color=(1.0, 1.0, 1.0), dir=270,
    nDots=500, fieldShape='circle', fieldPos=(0.0, 0.0), fieldSize=10,
    dotLife=5,  # number of frames for each dot to be drawn
    signalDots='same',  
    noiseDots='direction',  
    speed=0.01, coherence=0.9)
fixation=visual.Circle(win, radius=0.1,  edges=60, units='deg', lineWidth=2, lineColor=[-1,-1,-1], fillColor=[-1,-1,-1], colorSpace='rgb', pos=(0, 0))
blankFrame=visual.TextStim(win, text='', pos=(0, 0))
instruction1=visual.TextStim(win, text="View the moving bars then look at the moving dots", pos=(0,5))
instruction2=visual.TextStim(win, text="If the dots generally move UP, press P. If they move DOWN, press Q", wrapWidth=19.5, pos=(0, 2))
instruction3 = visual.TextStim(win, text='Press the spacebar to continue', pos=(0,-3), height=0.6, wrapWidth=20, units='deg')
adapt_gabor = visual.GratingStim(win, tex="sqr", mask="sqr", texRes=256, 
           size=[15.0, 10.0], sf=[1, 0], ori = 90, name='gabor1')
fixationSqr= ShapeStim(win, vertices=((-0.25,-0.25),(-0.25,0.25),(0.25,0.25),(0.25,-0.25)), fillColor='black', pos=(0,0), lineColor=None)
breakscreen1 = visual.TextStim(win, text='End of block', pos=(0,2), height=0.6, wrapWidth=20, units='deg')
breakscreen2 = visual.TextStim(win, text='Press the spacebar to continue', pos=(0,0), height=0.6, wrapWidth=20, units='deg')
endscreen1 = visual.TextStim(win, text='End of experiment', pos=(0,2), height=0.6, wrapWidth=20, units='deg')
endscreen2 = visual.TextStim(win, text='Press space to exit', pos=(0,0), height=0.6, wrapWidth=20, units='deg')
kb = keyboard.Keyboard()

keys = kb.getKeys()
while 'space' not in keys:
    win.mouseVisible=False
    instruction1.draw()
    instruction2.draw()
    instruction3.draw()
    win.flip()
    #keyPress = event.waitKeys()
    keys = kb.getKeys()

trial=0;
for i in [0,1,2,3,4,5,6,7]:
    win.mouseVsible=False
    adapt_gabor = visual.GratingStim(win, tex="sqr", mask="sqr", texRes=256, 
           size=[15.0, 10.0], sf=[1, 0], ori = blockTypes[i], name='gabor1')
    #trials.data.addDataType('adapt_direction')

    if i in [1,2,3,4,5,6,7]:
        keys = kb.getKeys()
        while 'space' not in keys:
            breakscreen1.draw()
            breakscreen2.draw()
            win.mouseVisible=False
            win.flip()
            win.mouseVisible=False
            keys = kb.getKeys()
            win.mouseVisible=False
            
    # setup trial handler
    stimList=[]
    for direction in [90, 270]:
        for coherence in [C99, C99/2, C99/4]: #coherence at 99% performance, half and quarter of that
            stimList.append({'direction': direction, 'coherence': coherence})
    trials = data.TrialHandler(stimList, 1)
    trials.data.addDataType('adapt_direction')
    trials.data.addDataType('accuracy')
    trials.data.addDataType('RT')
    clockRT = core.Clock() 
    
    response=''
    responseField=''
    blockTrial=0
    #for frameN in range(int(round(stimDuration*frameRate))):
    #        instruction.draw()
    #        win.update()
    
    for thisTrial in trials:
        win.mouseVsible=False
        blockTrial=blockTrial+1
        trial=trial+1
        
        if trials.thisTrial.direction==90:
            corresp='p'
        else: corresp='q'
                
        
        dot_stim = visual.DotStim(win, color=(1.0, 1.0, 1.0), dir=trials.thisTrial.direction,
        nDots=100, fieldShape='circle', fieldPos=(0.0, 0.0), fieldSize=10, dotSize=5, 
        dotLife=5,  # number of frames for each dot to be drawn
        signalDots='same',  # are signal dots 'same' on each frame? (see Scase et al)
        noiseDots='direction',  # do the noise dots follow random- 'walk', 'direction', or 'position'
        speed=dotSpeed/frameRate, coherence=trials.thisTrial.coherence)
    #        
        #blank screen for 500ms
        win.mouseVisible=False
        for frameN in range(int(round(blank1*frameRate))):
            win.update()        
        #draw adaptor grating
        for frameN in range(int(round(stimDuration*2*frameRate))):
            adapt_gabor.phase += speed/frameRate
            adapt_gabor.draw()
            fixationSqr.draw()
            win.update()
        # show blank screen for 500 ms
        for frameN in range(int(round(blank1*frameRate))):
            win.update()
        # show fixation point for 500 ms
        for frameN in range(int(round(fpDuration*frameRate))):
            fixation.draw()
            win.update()
        thisResponse = None
        kb.clock.reset()
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
            keys = kb.getKeys(keyList=['escape','p','q'])
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

# keyPress = ['']
keys = kb.getKeys()
while 'space' not in keys:
    win.mouseVisible=False
    endscreen1.draw()
    endscreen2.draw()
    win.flip()
    keys = kb.getKeys()

core.quit()