from __future__ import absolute_import, division, print_function
from psychopy import visual, event, core, gui, data, sound
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim
from random import shuffle
import string, time
import random, copy, scipy 
import os
from psychopy.hardware import keyboard
import platform
import ctypes
xlib = ctypes.cdll.LoadLibrary("libX11.so")
xlib.XInitThreads()


params = {'Subject':'1', 'Experimenter': 'zh'}
#dlg = gui.DlgFromDict(params, title='leftBias', fixed=['dateStr'])
#if dlg.OK:
toFile('lastParams.pickle', params) #save params to file for next time
#else:
#    core.quit()#the user hit cancel so exit
fileName = params['Experimenter']+'_'+params['Subject']

dataFile = open('../../psychopyData/leftBias/'+fileName+'.csv', 'a') #a simple text file with 'comma-separated-values'
dataFile.write('trial, blocktrial, stimulus, stimulusNumber, IM, LLlocation, corresponse, response, bias, RT\n') 
debug=1

if platform.platform()[0:5] == 'Linux': # if we're on Linux, then we're probably using the viewpixx monitor
    monitor = 'viewPixx'
    frameRate=120
else:
    monitor = 'testMonitor'
    frameRate=60

duration=0.3
ISI1=0.2
ISI2=0.5
fp=1
faceWidth=4.5 # equivalent of 5 dg of visual angle in pixels according to screen dimension
faceHeight=4.5
faceSize=(faceWidth,faceHeight)
posLVF=(-8,0)
posRVF=(8,0)

facePath='stimuli/faces/renamedFaces/'
texPath='stimuli/textures/renamedTextures/'
outlinePath='stimul/outlines/renamedOutlines/'

stimuli=['face','texture', 'outline']
random.shuffle(stimuli)

# Create a visual window:
# win = visual.Window(fullscr=True, allowGUI = True, monitor = 'testMonitor', units = 'deg',checkTiming=False)
win = visual.Window(fullscr=True, allowGUI = True, monitor = monitor, units = 'deg',checkTiming=False)
win.mouseVisible=False
fixation = visual.PatchStim(win, color=-1, tex=None, mask='circle',size=(0.25,0.25))
instruction1 = visual.TextStim(win, text=u'Judge whether the left image or right image looks more like the target in the middle', 
pos=(0,4), height=0.6, wrapWidth=30, units='deg')
instruction2 = visual.TextStim(win, text=u'Press 1 if the left image looks more like the target', pos=(0,2), height=0.6, wrapWidth=20, units='deg')
instruction3 = visual.TextStim(win, text=u'Press 0 if the right image looks more like the target', pos=(0,0), height=0.6, wrapWidth=20, units='deg')
instruction4 = visual.TextStim(win, text=u'Press the spacebar to begin', pos=(0,-2), height=0.6, wrapWidth=20, units='deg')
breakscreen1 = visual.TextStim(win, text='End of block', pos=(0,2), height=0.6, wrapWidth=20, units='deg')
breakscreen2 = visual.TextStim(win, text='Press the spacebar to continue', pos=(0,0), height=0.6, wrapWidth=20, units='deg')
endscreen1 = visual.TextStim(win, text='End of experiment', pos=(0,2), height=0.6, wrapWidth=20, units='deg')
endscreen2 = visual.TextStim(win, text='Press space to exit', pos=(0,0), height=0.6, wrapWidth=20, units='deg')
kb = keyboard.Keyboard()

# keyPress = ['']
keys = kb.getKeys()
while 'space' not in keys:
    win.mouseVisible=False
    instruction1.draw()
    instruction2.draw()
    instruction3.draw()
    instruction4.draw()
    win.flip()
    #keyPress = event.waitKeys()
    keys = kb.getKeys()

trial=0;
for i in [0,1,2]: 
    win.mouseVisible=False
    if stimuli[i]=='face':
        stimPath='stimuli/faces/renamedFaces/'
    elif stimuli[i]=='texture':
        stimPath='stimuli/textures/renamedTextures/'
    else:
        stimPath='stimuli/outlines/renamedOutlines/'
    
    if i in [1,2]:
        keys = kb.getKeys()
        while 'space' not in keys:
            breakscreen1.draw()
            breakscreen2.draw()
            win.mouseVisible=False
            win.flip()
            win.mouseVisible=False
            keys = kb.getKeys()
            win.mouseVisible=False
    if debug==1:
        imageO = [os.path.join(stimPath +'O1')]
        imageM = [os.path.join(stimPath +'M1')]
        imageL = [os.path.join(stimPath +'LL1')]
        imageR = [os.path.join(stimPath  +'RR1')]
    else:    
        imageO = [os.path.join(stimPath +'O1'), os.path.join(stimPath +'O2'),os.path.join(stimPath +'O3'),os.path.join(stimPath +'O4'),os.path.join(stimPath +'O5'),
            os.path.join(stimPath +'O6'),os.path.join(stimPath +'O7'), os.path.join(stimPath +'O8'),os.path.join(stimPath +'O9'),os.path.join(stimPath +'O10'),
            os.path.join(stimPath  +'O11'),os.path.join(stimPath  +'O12'),os.path.join(stimPath  +'O13'),os.path.join(stimPath +'O14'),os.path.join(stimPath +'O15'),
            os.path.join(stimPath +'O16'),os.path.join(stimPath +'O17'),os.path.join(stimPath +'O18'),os.path.join(stimPath  +'O19'),os.path.join(stimPath +'O20')]
        
        imageM = [os.path.join(stimPath +'M1'), os.path.join(stimPath +'M2'),os.path.join(stimPath +'M3'),os.path.join(stimPath +'M4'),os.path.join(stimPath +'M5'),
            os.path.join(stimPath +'M6'),os.path.join(stimPath +'M7'), os.path.join(stimPath +'M8'),os.path.join(stimPath +'M9'),os.path.join(stimPath +'M10'),
            os.path.join(stimPath +'M11'),os.path.join(stimPath +'M12'),os.path.join(stimPath +'M13'),os.path.join(stimPath +'M14'),os.path.join(stimPath +'M15'),
            os.path.join(stimPath +'M16'),os.path.join(stimPath +'M17'),os.path.join(stimPath +'M18'),os.path.join(stimPath +'M19'),os.path.join(stimPath +'M20')]
        
        imageL = [os.path.join(stimPath +'LL1'), os.path.join(stimPath +'LL2'),os.path.join(stimPath +'LL3'),os.path.join(stimPath +'LL4'),os.path.join(stimPath +'LL5'),
            os.path.join(stimPath +'LL6'),os.path.join(stimPath +'LL7'), os.path.join(stimPath +'LL8'),os.path.join(stimPath +'LL9'),os.path.join(stimPath +'LL10'),
            os.path.join(stimPath  +'LL11'),os.path.join(stimPath +'LL12'),os.path.join(stimPath +'LL13'),os.path.join(stimPath +'LL14'),os.path.join(stimPath +'LL15'),
            os.path.join(stimPath +'LL16'),os.path.join(stimPath +'LL17'),os.path.join(stimPath +'LL18'),os.path.join(stimPath +'LL19'),os.path.join(stimPath +'LL20')]
        
        imageR = [os.path.join(stimPath  +'RR1'), os.path.join(stimPath +'RR2'),os.path.join(stimPath +'RR3'),os.path.join(stimPath +'RR4'),os.path.join(stimPath  +'RR5'),
            os.path.join(stimPath +'RR6'),os.path.join(stimPath +'RR7'), os.path.join(stimPath +'RR8'),os.path.join(stimPath +'RR9'),os.path.join(stimPath  +'RR510'),
            os.path.join(stimPath +'RR11'),os.path.join(stimPath +'RR12'),os.path.join(stimPath +'RR13'),os.path.join(stimPath +'RR14'),os.path.join(stimPath +'RR15'),
            os.path.join(stimPath +'RR16'),os.path.join(stimPath +'RR17'),os.path.join(stimPath +'RR18'),os.path.join(stimPath +'RR19'),os.path.join(stimPath +'RR20')]
    
    # setup trial handler
    win.mouseVisible=False
    stimList=[]
    for image in range (0,len(imageO)):
        for intact in [1,0]: # intact vs mirror
            for field in [1,0]: # LVF
                stimList.append({'intact': intact, 'field':field, 'image':image}) # setting trial sequence
    trials = data.TrialHandler(stimList, 1)
    trials.data.addDataType('RT')
    trials.data.addDataType('bias')
    clockRT = core.Clock() 
    
    response=''
    responseField=''
    blockTrial=0
    
    for thisTrial in trials:
        win.mouseVisible=False
        blockTrial=blockTrial+1
        trial=trial+1
        
        stimName=os.path.split(imageO[trials.thisTrial.image])[1]
        if trials.thisTrial.intact==1: # if intact face
            IM='I'
            if trials.thisTrial.field==1: # if LL in LVF trial
                    image_LVF = visual.ImageStim(win, image=imageL[trials.thisTrial.image], pos=posLVF,size=faceSize)
                    image_Cent = visual.ImageStim(win, image=imageO[trials.thisTrial.image], pos=(0,0),size=faceSize) 
                    image_RVF = visual.ImageStim(win, image=imageR[trials.thisTrial.image], pos=posRVF,size=faceSize)
                    LL_location='LVF'
                    corresp=1
            else: # if LL in RVF 
                    image_LVF = visual.ImageStim(win, image=imageR[trials.thisTrial.image], pos=posLVF,size=faceSize)
                    image_Cent = visual.ImageStim(win, image=imageO[trials.thisTrial.image], pos=(0,0),size=faceSize) 
                    image_RVF = visual.ImageStim(win, image=imageL[trials.thisTrial.image], pos=posRVF,size=faceSize)
                    LL_location='RVF'
                    corresp=0
        else: # if mirror face
            IM='M'
            if trials.thisTrial.field==1: # if LL in LVF trial
                    image_LVF = visual.ImageStim(win, image=imageR[trials.thisTrial.image], pos=posLVF,size=faceSize)
                    image_Cent = visual.ImageStim(win, image=imageM[trials.thisTrial.image], pos=(0,0),size=faceSize) 
                    image_RVF = visual.ImageStim(win, image=imageL[trials.thisTrial.image], pos=posRVF,size=faceSize)
                    LL_location='LVF'
                    corresp=1
            else: # if LL in RVF 
                    image_LVF = visual.ImageStim(win, image=imageL[trials.thisTrial.image], pos=posLVF,size=faceSize)
                    image_Cent = visual.ImageStim(win, image=imageM[trials.thisTrial.image], pos=(0,0),size=faceSize) 
                    image_RVF = visual.ImageStim(win, image=imageR[trials.thisTrial.image], pos=posRVF,size=faceSize)
                    LL_location='RVF'
                    corresp=0
        
        # show blank screen for 500 ms
        for frameN in range(int(round(ISI2*frameRate))):
            win.mouseVisible=False
            win.update()
    
        # show fixation point for one second
        for frameN in range(int(round(fp*frameRate))):
            fixation.draw()
            win.mouseVisible=False
            win.update()
            
        # show stimuli
        # kb = keyboard.Keyboard()
        kb.clock.reset()
        thisResponse = None
        while thisResponse == None:
            #clockRT.reset()
            win.mouseVisible=False
            image_Cent.draw()
            image_LVF.draw()
            image_RVF.draw()
            win.update()
            
    # collect response
            #allKeys = event.waitKeys(keyList=['escape','1','0'],timeStamped = clockRT)
            keys = kb.getKeys(keyList=['escape','1','0'])
            win.mouseVisible=False
#            for keyTuple in keys:
#                [key.name, key.rt] = keyTuple
#                
            for thisKey in keys:
                if thisKey.name in ['escape']:
                    dataFile.write('%d%s\t\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %(trial,blockTrial,stimuli[i],stimName,IM, LL_location,corresp,response, 'NA',round(thisKey.rt,2)))
                    core.quit()
                elif int(thisKey.name)==corresp:
                    thisResponse=1
                    bias=1
                    win.mouseVisible=False
                    win.update()
                    win.mouseVisible=False
                else:
                    thisResponse=1
                    bias=0 
                    win.mouseVisible=False
                    win.update()
                    win.mouseVisible=False
        trials.addData('RT', thisKey.rt)
        trials.addData('bias', bias)
        event.clearEvents()
        dataFile.write('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %(trial,blockTrial,stimuli[i],stimName,IM, LL_location,corresp,thisKey.name, bias,round(thisKey.rt,2)))

# keyPress = ['']
keys = kb.getKeys()
while 'space' not in keys:
    win.mouseVisible=False
    endscreen1.draw()
    endscreen2.draw()
    win.flip()
    keys = kb.getKeys()

core.quit()