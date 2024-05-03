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


params = {'Subject':'test', 'Experimenter':'aa'}
C90= 0.5 #insert coherence level at 90% performance accuracy here
nTrialsPerCondition=8
frameRate=120
blank1=0.5
dotSpeed=8.25 #in degrees per second (calculated from 0.11 deg/frame speed from Winawer paper with 75Hz monitor)
fpDuration=0.5
blank2=0.1
adaptDuration0=6
stimDuration=1
resx=1920
speed=2.7
dotsize=0.174 #dot size in degrees (calculated from 5pix dot size in aa's monitor with 1024px resolution and 30cm scrren width, assuming viewing distance 57cm)
screenWidth=57.15 #screen width in cm

blockTypes=[90,90,270,270]
random.shuffle(blockTypes)

#dlg = gui.DlgFromDict(params, title='MotionExp', fixed=['dateStr'])
#if dlg.OK:
toFile('lastParams.pickle', params) #save params to file for next time
#else:
#    core.quit()#the user hit cancel so exit

fileName = params['Experimenter']+'_'+params['Subject']+'_adaptation'
dataFile = open('../../psychopyData/Motion/'+fileName+'.csv', 'a')#a simple text file with 'comma-separated-values'
dataFile.write('trial\tblocktrial\tadapt_direction\tcoherence\tdot_direction\tcorresp\tsubjectResp\taccuracy\tRT\n') 
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
    nDots=100, fieldShape='circle', fieldPos=(0.0, 0.0), fieldSize=10,
    dotLife=5,  # number of frames for each dot to be drawn
    signalDots='same', noiseDots='direction',  
    dotSize=dotsize*resx/screenWidth,
    speed=dotSpeed/frameRate, coherence=0.9)
fixation=visual.Circle(win, radius=0.1,  edges=60, units='deg', lineWidth=2, lineColor=[-1,-1,-1], fillColor=[-1,-1,-1], colorSpace='rgb', pos=(0, 0))
blankFrame=visual.TextStim(win, text='', pos=(0, 0))
instruction1=visual.TextStim(win, text="View the striped pattern and focus on the black square in front of them.", pos=(0,5))
instruction2=visual.TextStim(win, text="After that, look at the moving dots. If the dots generally move UP, press Q. If they move DOWN, press M", wrapWidth=19.5, pos=(0, 2))
instruction3 = visual.TextStim(win, text='Press the spacebar to continue', pos=(0,-3), height=0.6, wrapWidth=20, units='deg')
adapt_gabor = visual.GratingStim(win, tex="sqr", mask="sqr", texRes=256, 
           size=[15.0, 10.0], sf=[1, 0], ori = 90, name='gabor1')
fixationSqr= ShapeStim(win, vertices=((-0.25,-0.25),(-0.25,0.25),(0.25,0.25),(0.25,-0.25)), fillColor='black', pos=(0,0), lineColor=None)
breakscreen1 = visual.TextStim(win, text='End of block. You may now take a break.', pos=(0,2), height=0.6, wrapWidth=20, units='deg')
breakscreen2 = visual.TextStim(win, text='Press the spacebar to continue', pos=(0,0), height=0.6, wrapWidth=20, units='deg')
endscreen1 = visual.TextStim(win, text='End of task.', pos=(0,2), height=0.6, wrapWidth=20, units='deg')
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
for i in [0,1,2,3]:
    win.mouseVsible=False
    adapt_gabor = visual.GratingStim(win, tex="sqr", mask="sqr", texRes=256, 
           size=[15.0, 10.0], sf=[1, 0], ori = 360 - blockTypes[i], #coded like this since direction of motion is the opposite of the gabor orientation, (if ori=90, direction=270)
           name='gabor1')
    #trials.data.addDataType('adapt_direction')

    if i in [1,2,3]:
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
        for coherence in [C90, C90/2, C90/4]: #coherence at 99% performance, half and quarter of that
            stimList.append({'direction': direction, 'coherence': coherence})
    trials = data.TrialHandler2(stimList, nTrialsPerCondition)
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
        
        if trials.thisN==0:
            adaptDuration=60
        else: adaptDuration=adaptDuration0
        if trials.thisTrial.direction==90:
            corresp='q'
        else: corresp='m'
                
        
        dot_stim.dir=trials.thisTrial.direction
        dot_stim.coherence=trials.thisTrial.coherence
        
    #        
        #blank screen for 500ms
        win.mouseVisible=False
        for frameN in range(int(round(blank1*frameRate))):
            win.update()        
        #draw adaptor grating
        for frameN in range(int(round(adaptDuration*frameRate))):
            adapt_gabor.phase += speed/frameRate
            adapt_gabor.draw()
            fixationSqr.draw()
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

# keyPress = ['']
keys = kb.getKeys()
while 'space' not in keys:
    win.mouseVisible=False
    endscreen1.draw()
    endscreen2.draw()
    win.flip()
    keys = kb.getKeys()

core.quit()
