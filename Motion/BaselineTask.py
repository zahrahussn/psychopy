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


params = {'Subject':'INSERTSUB', 'Experimenter':'aa'}
nTrialsPerCondition = 10
frameRate=120
dotSpeed=8.25 #in degrees per second (calculated from 0.11 deg/frame speed from Winawer paper with 75Hz monitor)
dotsize=0.174 #dot size in degrees (calculated from 5pix dot size in aa's monitor with 1024px resolution and 30cm screen width, assuming viewing distance 57cm)
blank1=0.5
fpDuration=0.5
blank2=0.1
stimDuration=1
resx=1920
screenWidth=57.15 #screen width in cm

#dlg = gui.DlgFromDict(params, title='MotionExp', fixed=['dateStr'])
#if dlg.OK:
toFile('lastParams.pickle', params) #save params to file for next time
#else:
#    core.quit()#the user hit cancel so exit

fileName = params['Experimenter']+'_'+params['Subject']+'_baseline'
dataFile = open('../../psychopyData/Motion/'+fileName+'.csv', 'a') #a simple text file with 'comma-separated-values'
dataFile.write('trial\tcoherence\tdirection\tcorresp\tresponse\taccuracy\tRT\n') 
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
win = visual.Window(fullscr=True, allowGUI = True, monitor = monitor, units='deg', color=(-0.1,-0.1,-0.1), checkTiming=False)
#win = visual.Window(fullscr=True, allowGUI = True, monitor = 'testMonitor', winType='pyglet', units = 'deg', checkTiming=False)
win.mouseVisible=False
#creating stimuli
dot_stim = visual.DotStim(win, color=(1.0, 1.0, 1.0), dir=270,
    nDots=100, fieldShape='circle', fieldPos=(0.0, 0.0), fieldSize=10, opacity=1,
    dotSize=dotsize*resx/screenWidth,
    dotLife=5,  # number of frames for each dot to be drawn
    signalDots='same', noiseDots='direction',  
    speed=dotSpeed/frameRate, coherence=0.9)
fixation=visual.Circle(win, radius=0.1,  edges=60, units='deg', lineWidth=2, lineColor=[-1,-1,-1], fillColor=[-1,-1,-1], colorSpace='rgb', pos=(0, 0)) 
blankFrame=visual.TextStim(win, text='', pos=(0, 0))
instruction1=visual.TextStim(win, text="You will be shown a circular field of dots moving in different directions.", wrapWidth=20, pos=(0,3))
instruction2=visual.TextStim(win, text="If you can see that a portion of the dots are moving UP, press Q. If you can see them moving DOWN, press M", wrapWidth=25, pos=(0, 0))
instruction3 = visual.TextStim(win, text='Press the spacebar to continue', pos=(0,-3), height=0.6, wrapWidth=20, units='deg')
breakscreen1 = visual.TextStim(win, text='You are halfway through the task. You may now take a break.', pos=(0,2), height=0.6, wrapWidth=20, units='deg')
breakscreen2 = visual.TextStim(win, text='Press the spacebar when you wish to resume the task.', pos=(0,0), height=0.6, wrapWidth=20, units='deg')
endscreen1 = visual.TextStim(win, text='End of task', pos=(0,2), height=0.6, wrapWidth=20, units='deg')
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

# setup trial handler
stimList=[]
for direction in [90, 270]:
    for coherence in [0.05, 0.15, 0.25, 0.35, 0.45,  0.55, 0.65, 0.9 ]:
        stimList.append({'direction': direction, 'coherence': coherence})
trials = data.TrialHandler2(stimList, nTrialsPerCondition)
clockRT = core.Clock() 


for thisTrial in trials:
    if trials.thisN==96:
        keys = kb.getKeys()
        while 'space' not in keys:
            win.mouseVisible=False
            breakscreen1.draw()
            breakscreen2.draw()
            win.flip()
            #keyPress = event.waitKeys()
            keys = kb.getKeys()
    
    if trials.thisTrial.direction==90:
        corresp='q'
    else: corresp='m'
            
    dot_stim.dir=trials.thisTrial.direction
    dot_stim.coherence=trials.thisTrial.coherence

    #instructions
    win.mouseVisible=False
    # show blank screen for 500 ms
    for frameN in range(int(round(blank1*frameRate))):
        blankFrame.draw()
        win.update()
    # show fixation point for 500 ms
    for frameN in range(int(round(fpDuration*frameRate))):
        fixation.draw()
        win.update()
    thisResponse = None
    kb.clock.reset()
#show stimulus
    for frameN in range(int(round(stimDuration*frameRate))):
            dot_stim.draw()
            win.update()
    #blank screen
    for frameN in range(int(round(blank2*frameRate))):
        win.update()
        
    #kb.clock.reset()
    thisResponse = None
    while thisResponse == None:
        keys = kb.getKeys(keyList=['escape','q','m'])
        win.mouseVisible=False
        for thisKey in keys:
            if thisKey.name in ['escape']:
                dataFile.write('%d\t%s\t%s\t%s\t%s\t%s\t%s\n' %(trials.thisN,trials.thisTrial.coherence,trials.thisTrial.direction,corresp,'NA','NA',round(thisKey.rt,2)))
                core.quit()
            elif thisKey.name ==corresp:
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
    #print(thisKey.name)
    dataFile.write('%d\t%s\t%s\t%s\t%s\t%s\t%s\n' %(trials.thisN,trials.thisTrial.coherence, trials.thisTrial.direction, corresp, thisKey.name, accuracy, round(thisKey.rt,2)))
#        for thisKey in allKeys:
#            if thisKey[0] in ['escape']:core.quit()
#            elif thisKey[0] in ['up','down']:
#                if thisKey[0] == corresp:
#                    thisResponse=1
#                    accuracy = 1
#                    incorrect = 0
#                    #corSnd.play()
#                else: 
#                    thisResponse=1
#                    accuracy = 0
#                    incorrect = 1
#                    #incorSnd.play()
#    #while thisResponse == None: #could be put after
#    trials.addData('RT', thisRT)
#    trials.addData('corresp', corresp)
#    event.clearEvents()
#    dataFile.write('%s %s %s %s %s %s %s\n' %(trials.thisTrial.coherence, trials.thisTrial.direction, corresp, thisKey[0], accuracy, incorrect, round(thisRT,3)))

# save data file as pickle for processing
trials.saveAsPickle('../../psychopyData/Motion/'+fileName)

# keyPress = ['']
keys = kb.getKeys()
while 'space' not in keys:
    win.mouseVisible=False
    endscreen1.draw()
    endscreen2.draw()
    win.flip()
    keys = kb.getKeys()
    
core.quit()
