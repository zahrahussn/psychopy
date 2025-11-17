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
#import ctypes
#myPath = '/Users/zhussain1/Dropbox/Research/Ongoing/leftObjectBias/psychoPyCode/nov2024'
#os.chdir(myPath)

# REMEMBER TO ASSIGN THE CORRECT ID AND EXPERIMENTER!
# REMEMBER TO ASSIGN THE SAME GROUP AS DAY 1!
params = {'Subject':'13', 'Group':'TextureA ', 'Experimenter': 'id'}

#######
fileName = params['Experimenter']+params['Subject']+'_'+params['Group']+'_'+'bias'
dataFile = open('../../psychopyData/bias2024/bias/'+fileName+'.csv', 'a') #a simple text file with 'comma-separated-values'
dataFile.write('trial, blocktrial, stimulus, stimulusNumber, IM, LLlocation, corresponse, response, bias, RT\n') 

if platform.platform()[0:5] == 'Linux': # if we're on Linux, then we're probably using the viewpixx monitor
    monitor = 'viewPixx'
    frameRate=120
    import ctypes
    xlib = ctypes.cdll.LoadLibrary("libX11.so")
    xlib.XInitThreads()
else:
    monitor = 'testMonitor'
    frameRate=60
duration=0.3
ISI1=0.2
ISI2=0.5
fp=1
faceWidth=6
faceHeight=6
faceSize=(faceWidth,faceHeight)
posLVF=(-10,0)
posRVF=(10,0)

faceAPath='stimuli/faceA/'
faceBPath='stimuli/faceB/'
texAPath='stimuli/texA/'
texBPath='stimuli/texB/'
stimuli=['faceA','faceB', 'textureA', 'textureB']
random.shuffle(stimuli)

# Create a visual window:
win = visual.Window(fullscr=True, allowGUI = True, monitor = monitor, units = 'deg',checkTiming=False)
win.mouseVisible=False
fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.3, interpolate=True)
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
for i in [0,1,2,3]: 
    win.mouseVisible=False
    if stimuli[i]=='faceA':
        stimPath=faceAPath
    elif stimuli[i]=='faceB':
        stimPath=faceBPath
    elif stimuli[i]=='textureA':
        stimPath=texAPath
    else:
        stimPath=texBPath
    
    if i in [1,2,3]:
        keys = kb.getKeys()
        while 'space' not in keys:
            breakscreen1.draw()
            breakscreen2.draw()
            win.mouseVisible=False
            win.flip()
            win.mouseVisible=False
            #keyPress = event.waitKeys()
            keys = kb.getKeys()
            win.mouseVisible=False
                        
    imageO = sorted([os.path.join(stimPath, file) for file in os.listdir(stimPath) if file.endswith("O.jpeg")])
    imageM = sorted([os.path.join(stimPath, file) for file in os.listdir(stimPath) if file.endswith("M.jpeg")])
    imageL = sorted([os.path.join(stimPath, file) for file in os.listdir(stimPath) if file.endswith("L.jpeg")])
    imageR = sorted([os.path.join(stimPath, file) for file in os.listdir(stimPath) if file.endswith("R.jpeg")])
   
    # setup trial handler
    win.mouseVisible=False
    stimList=[]
    for image in range (0,len(imageO)):
        for intact in [1,0]: # intact vs mirror
            for field in [1,0]: # LVF
                stimList.append({'intact': intact, 'field':field, 'image':image}) # setting trial sequence
    trials = data.TrialHandler(stimList, 2)
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
                    image_LVF = visual.ImageStim(win, image=imageL[trials.thisTrial.image], pos=posLVF,size=faceSize, interpolate=True)
                    image_Cent = visual.ImageStim(win, image=imageO[trials.thisTrial.image], pos=(0,0),size=faceSize, interpolate=True) 
                    image_RVF = visual.ImageStim(win, image=imageR[trials.thisTrial.image], pos=posRVF,size=faceSize, interpolate=True)
                    LL_location='LVF'
                    corresp=1
            else: # if LL in RVF 
                    image_LVF = visual.ImageStim(win, image=imageR[trials.thisTrial.image], pos=posLVF,size=faceSize, interpolate=True)
                    image_Cent = visual.ImageStim(win, image=imageO[trials.thisTrial.image], pos=(0,0),size=faceSize, interpolate=True) 
                    image_RVF = visual.ImageStim(win, image=imageL[trials.thisTrial.image], pos=posRVF,size=faceSize, interpolate=True)
                    LL_location='RVF'
                    corresp=0
        else: # if mirror face
            IM='M'
            if trials.thisTrial.field==1: # if LL in LVF trial
                    image_LVF = visual.ImageStim(win, image=imageR[trials.thisTrial.image], pos=posLVF,size=faceSize, interpolate=True)
                    image_Cent = visual.ImageStim(win, image=imageM[trials.thisTrial.image], pos=(0,0),size=faceSize, interpolate=True) 
                    image_RVF = visual.ImageStim(win, image=imageL[trials.thisTrial.image], pos=posRVF,size=faceSize, interpolate=True)
                    LL_location='LVF'
                    corresp=1
            else: # if LL in RVF 
                    image_LVF = visual.ImageStim(win, image=imageL[trials.thisTrial.image], pos=posLVF,size=faceSize, interpolate=True)
                    image_Cent = visual.ImageStim(win, image=imageM[trials.thisTrial.image], pos=(0,0),size=faceSize, interpolate=True) 
                    image_RVF = visual.ImageStim(win, image=imageR[trials.thisTrial.image], pos=posRVF,size=faceSize, interpolate=True)
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
        thisResponse = None
        while thisResponse == None:
            clockRT.reset()
            win.mouseVisible=False
            image_Cent.draw()
            image_LVF.draw()
            image_RVF.draw()
            win.update()
            
    # collect response
            #allKeys = event.waitKeys(keyList=['escape','1','0'],timeStamped = clockRT)
            keys = kb.getKeys(keyList=['escape','1','0'])
            win.mouseVisible=False                
            for thisKey in keys:
                if thisKey.name in ['escape']:
                    bias=0
                    dataFile.write(f"{trial},{blockTrial},{stimuli[i]},{stimName},{IM},{LL_location},{corresp}, {'escape'}, {bias}, {round(thisKey.rt,2)}\n")
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
#        trials.addData('RT', thisRT)
#        trials.addData('bias', bias)
        event.clearEvents()
        dataFile.write(f"{trial},{blockTrial},{stimuli[i]},{stimName},{IM},{LL_location},{corresp}, {thisKey.name}, {bias}, {round(thisKey.rt,2)}\n")
       
#keyPress = ['']
keys = kb.getKeys()
while 'space' not in keys:    
    win.mouseVisible=False
    endscreen1.draw()
    endscreen2.draw()
    win.flip()
    keys = kb.getKeys()

core.quit()