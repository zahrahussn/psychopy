from psychopy import core, visual, gui, data, event, sound
from psychopy.tools.filetools import fromFile, toFile
import time, numpy as np
from scipy.interpolate import interp1d
from psychopy.data import QuestPlusHandler
import os
import pandas as pd
from scipy.ndimage import rotate
from scipy.io import loadmat
import matplotlib.pyplot as plt
import platform
from psychopy.hardware import keyboard
import sys
# myPath = '/Users/zhussain1/Dropbox/Research/Ongoing/uncertainty_chinaecherem/calibration_bitStealing'
dataPath = '../../psychopyData/detection2024/sm_data/'
#dataPath = '/Users/zhussain1/Dropbox/Research/Ongoing/uncertainty_chinaecherem/psychopyData/test/'
#os.chdir(myPath)

debug=0
title='Detection under uncertainty'
subject = 'zh'
#subject = 'sm'
noiseType = 'variable'  # 'fixed', 'variable'
session_number = '4' # 1, 2, 3..., 12
stimIDs=np.random.choice(range(1,6),3, replace=False)

# data file
fileName = subject+'_'+noiseType+'_'+str(session_number)+'_quest_texture'
dataFile = open(dataPath+fileName + '.csv', 'a')
dataFile.write('trial,block,blockTrial,stimulus,nStim,stimID,noise,noiseSeed1,noiseSeed2,signalInterval,contrast,correct\n')
thresholdFile = subject+'_'+noiseType+'_'+'_'+str(session_number)+'_questThresholds_texture'
thresholdFile = open(dataPath+thresholdFile + '.csv', 'a')
thresholdFile.write('block,stimulus,nStim,stimID,noise,threshold,slope\n')

# create blocks: 3 x 2 x 2 = 12 blocks, at 50 trials per block - 2024
# create blocks: 3 x 1 x 2 = 6 blocks at 100 trials per block for keanu, 2025
stimList = []
for stimID in stimIDs: # 3 stim IDs so 3 reps per nStim
#    for stimulus in ['grating', 'texture']:
    for stimulus in ['grating']:   
        for nStim in [1, 5]:
            stimList.append({'stimulus': stimulus, 'nStim': nStim, 'stimID': stimID})
blocks = data.TrialHandler(stimList, 1,extraInfo={'subject': subject, 'noise': noiseType, 'session': session_number})

#creating block for practice
#stimList = [
#    #{'stimulus': 'grating', 'nStim': 1, 'stimID': 2} #,
#    {'stimulus': 'texture', 'nStim': 1, 'stimID': 2}
#]
#blocks = data.TrialHandler(stimList, 1,extraInfo={'subject': subject, 'noise': noiseType, 'session': session_number})

# trial parameters
# stim duration and isi changed from 0.2 and 1 to 0.15 and 0.5 for keanu
stimDuration = 0.15 
isi= 0.5
fixate = 0.5
textures=[1,2,3,4,5]
oris = [0.0, 72.0, 144.0, 216.0, 288.0] # 5 equally-spaced angles between 0 and 360 deg

# the parameters for quest+handler
minContrast=0.000001 # 0.000001 variance 
maxContrast=0.05 # 0.05
intensityVals = np.logspace(np.log10(minContrast), np.log10(maxContrast), 50)  
thresholdVals = np.logspace(np.log10(0.0000001), np.log10(0.1), 50) 
slopeVals = np.linspace(0.01, 10, 50)  
lowerAsymptoteVals = [0.5] # guess rate
lapseRateVals = np.linspace(0, 0.05, 6)  
responseVals = [1,0]
pThresholdVal=0.76 # d' = 1
numTrials=100

#  window 
gamma=2.2
if platform.platform()[0:5] == 'Linux': # if we're on Linux, then we're probably using the viewpixx monitor
    monitor = 'detectingMonitor'
    frameRate=120
    import ctypes
    xlib = ctypes.cdll.LoadLibrary("libX11.so")
    xlib.XInitThreads()
else:
    monitor = 'testMonitor'
    frameRate=60
if debug==1:
    win = visual.Window([1600, 1000], allowGUI=True, monitor=monitor, units='deg', checkTiming=False)
else:
    win = visual.Window(fullscr=True, allowGUI=True, monitor=monitor, units='deg', checkTiming=False)

# trial stuff
correctSound = sound.Sound(1800, octave=14, stereo=True, secs=0.01)
incorrectSound = sound.Sound(700, octave=7, stereo=True, secs=0.01)
fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.2)
fixationCorrect = visual.GratingStim(win, color='green', tex=None, mask='circle', size=0.2)
fixationIncorrect = visual.GratingStim(win, color='red', tex=None, mask='circle', size=0.2)
message1 = visual.TextStim(win, pos=[0, -1], text='Hit a key when ready')
message2 = visual.TextStim(win, pos=[0, -2.5], wrapWidth=200,
                            text="Press left for interval 1 and right for interval 2")
message3 = visual.TextStim(win, pos=[0, 0], text='End of block')                            

# start of block
trial=0
block=0
for thisBlock in blocks:
    
    block=block+1
    
    if thisBlock.nStim==1:
        stimName=thisBlock.stimID # for the quest threshold file
        if thisBlock.stimulus=="texture":
            stimulus="texture"
            stim_key = f'stim{thisBlock.stimID}' 
            #textures=loadmat('/home/zahra/Dropbox/psychopy/3detection/theTextures.mat')
            #textures=loadmat('/Users/zhussain1/Dropbox/Research/Ongoing/uncertainty_chinaecherem/psychopy/theTextures.mat')
            textures=loadmat('/home/zahra/Documents/psychopy/3detection/theTextures.mat')
            thisImage=textures['theStimulus4'][stim_key][0][0]
            thisImage=thisImage*np.sqrt(1/np.var(thisImage)) # for the clear images at the start of each block
            thisImage=thisImage-np.mean(thisImage)
            min_val = thisImage.min()
            max_val = thisImage.max()
            thisImage = 2 * ((thisImage- min_val) / (max_val - min_val)) - 1
            thisSignal = visual.ImageStim(win, image=np.clip(thisImage,-1,1), size=4, pos=(0, 2), mask=None, interpolate=True, contrast=1.25, opacity=1)
        else:
            stimulus="grating"
            array = np.linspace(0, 1, 512)
            bigGrating = np.sin(1 * np.pi * 8 * array)  # used to be 4 before scaling up and cropping grating
            bigGrating = np.tile(bigGrating, (512, 1))
            angle = oris[int(thisBlock.stimID) - 1]
            bigGrating=rotate(bigGrating, angle=angle, reshape=False)
            gratingCenter = 512 // 2
            thisGrating = bigGrating[gratingCenter-128:gratingCenter+128, gratingCenter-128:gratingCenter+128]
            thisSignal = visual.ImageStim(win, image=np.clip(thisGrating, -1,1), size=4, pos=(0, 2), mask=None, interpolate=True)
    else:
        stimName="all" # for quest threshold file
        if thisBlock.stimulus=="texture":
            stimulus="texture"
            #textures=loadmat('/home/zahra/Dropbox/psychopy/3detection/theTextures.mat')
            #textures=loadmat('/Users/zhussain1/Dropbox/Research/Ongoing/uncertainty_chinaecherem/psychopy/theTextures.mat')
            textures=loadmat('/home/zahra/Documents/psychopy/3detection/theTextures.mat')
            image1=textures['theStimulus4']['stim1'][0][0]
            image2=textures['theStimulus4']['stim2'][0][0]
            image3=textures['theStimulus4']['stim3'][0][0]
            image4=textures['theStimulus4']['stim4'][0][0]
            image5=textures['theStimulus4']['stim5'][0][0]
            textures = [image1, image2, image3, image4, image5]
            pad = np.zeros((256, 10))
            allImages = textures[0]
            for img in textures[1:]:
                allImages = np.hstack((allImages, pad, np.clip(img,-1,1)))
            thisSignal = visual.ImageStim(win, image=np.clip(allImages, -1,1), size=(20, 4), pos=(0, 2), mask=None, interpolate=True, contrast=1.25) 
        else:
            stimulus="grating"
            array = np.linspace(0, 1, 512)
            bigGrating = np.sin(1 * np.pi * 8 * array)  # used to be 4 before scaling up and cropping grating
            bigGrating = np.tile(bigGrating, (512, 1))
            oris = oris 
            pad = np.zeros((256, 10))
            gratingCenter = 512 // 2
            allImages = bigGrating[gratingCenter-128:gratingCenter+128, gratingCenter-128:gratingCenter+128]
            for angle in oris[1:]:
                bigGrating2=rotate(bigGrating, angle=angle, reshape=False)
                thisGrating = bigGrating2[gratingCenter-128:gratingCenter+128, gratingCenter-128:gratingCenter+128]
                allImages = np.hstack((allImages, pad, np.clip(thisGrating,-1,1)))
            thisSignal = visual.ImageStim(win, image=np.clip(allImages, -1,1), size=(20, 4), pos=(0, 2), mask=None, interpolate=True) 

    # create fixed noise; makes sense to do this outside the quest loop if fixed
    noiseSd = np.sqrt(0.1)
    noiseMean = 0
    seed1 = int(time.time() * 1000) 
    random_state = np.random.default_rng(seed1)
    noiseMatrix = random_state.normal(noiseMean, noiseSd, (256, 256))
    noiseMatrix = np.clip(noiseMatrix, -1, 1)
    seed2=seed1
            
    # create the quest+handler
    quest = data.QuestPlusHandler(intensityVals=intensityVals, thresholdVals=thresholdVals,
                             slopeVals=slopeVals, lowerAsymptoteVals=lowerAsymptoteVals, startIntensity=intensityVals[30],
                             lapseRateVals=lapseRateVals, responseVals=responseVals, paramEstimationMethod='mean', nTrials=numTrials, 
                             stimScale='linear') # , pThreshold=pThresholdVal
    
    # display instructions and wait
    win.mouseVisible = False
    message1.draw()
    message2.draw()
    thisSignal.draw()
    win.flip()
    
    # check for a keypress
    #event.waitKeys()
    kb = keyboard.Keyboard()
    keys = kb.getKeys()
    while not keys:
        keys = kb.getKeys()
    
    blockTrial = 0
    for trials in range(quest.nTrials):
        trial=trial+1
        blockTrial = blockTrial+1
        thisIncrement=quest.next()
        
        # do noise
        if noiseType=="fixed":
            noiseMatrix1=np.clip(noiseMatrix, -1, 1)
            noiseMatrix2=noiseMatrix1
        elif noiseType=="twin":
            seed1 = int(time.time() * 1000) + trial
            random_state = np.random.default_rng(seed1) 
            noiseMatrix1=np.random.normal(noiseMean, noiseSd, (256, 256))
            noiseMatrix1=np.clip(noiseMatrix1, -1, 1)
            noiseMatrix2=noiseMatrix1
            seed2=seed1
        else:
            seed1 = int(time.time() * 1000) + trial
            seed2 = int(time.time() * 1000) + trial + 1
            random_state1 = np.random.default_rng(seed1) 
            noiseMatrix1=random_state1.normal(noiseMean, noiseSd, (256, 256))
            noiseMatrix1=np.clip(noiseMatrix1, -1, 1)
            random_state2 = np.random.default_rng(seed2) 
            noiseMatrix2=random_state2.normal(noiseMean, noiseSd, (256, 256))
            noiseMatrix2=np.clip(noiseMatrix2, -1, 1)
        
        # set signal interval 
        signalInterval = np.random.choice([0, 1])
        
        # set stimulus index
        if thisBlock.nStim == 1:
            stimNumber=thisBlock.stimID
            if thisBlock.stimulus=="grating":
                thisStim=thisGrating
            else:
                thisStim=thisImage                
        else:
            stimNumber = np.random.choice(range(5))
            if thisBlock.stimulus=="grating":
                bigGrating=rotate(bigGrating, angle=oris[stimNumber], reshape=False)
                gratingCenter = 512 // 2
                thisStim = bigGrating[gratingCenter-128:gratingCenter+128, gratingCenter-128:gratingCenter+128]
            else:
                thisStim=textures[stimNumber]      
            stimNumber=stimNumber+1 # for the data file
             
        # set stimulus contrast and add to noise
        thisStim=thisStim*np.sqrt(1/np.var(thisStim))
        thisStim=np.sqrt(thisIncrement)*thisStim
        noisyStim=noiseMatrix1+thisStim
        noisyStimFinal=np.clip(noisyStim, -1, 1)
        
        noise = visual.ImageStim(win, image=noiseMatrix2, mask=None, size=4, interpolate=True, pos=(0,0))        
        signalPlusNoise = visual.ImageStim(win, image=noisyStimFinal, size=4, pos=(0, 0), mask=None, interpolate=True)
    
        if signalInterval == 0:
            stim1 = signalPlusNoise
            stim2 = noise
            corresp = 'left'
        else:
            stim2 = signalPlusNoise
            stim1 = noise
            corresp = 'right'
        
        # fixate
        for frameN in range(int(round(fixate * frameRate))):
            fixation.draw()
            win.flip()    
            
        # interval 1
        for frameN in range(int(round(stimDuration * frameRate))):  
            stim1.draw()
            win.flip()
    
        # inter-stimulus interval (ISI)
        for frameN in range(int(round(isi * frameRate))):
            win.flip()
    
        # interval 2
        for frameN in range(int(round(stimDuration * frameRate))):  
            stim2.draw()
            win.flip()
        # fixate
        for frameN in range(int(round(fixate * frameRate))):
            fixation.draw()
            win.flip()
            
        # get response
        thisResp = None
        clockRT = core.Clock() 
        while thisResp is None:
            allKeys = kb.getKeys(keyList=['escape','left','right'])
            for thisKey in allKeys:
                if thisKey == 'escape':
                    core.quit()
                elif thisKey in ['left','right']:
                    if thisKey == corresp:
                        thisResp = 1  # correct
                        correctSound.play()  
                        for frameN in range(int(round(fixate * frameRate))):
                            fixationCorrect.draw()
                            win.flip()
                    else:
                        thisResp = 0  # incorrect
                        incorrectSound.play()
                        for frameN in range(int(round(fixate * frameRate))):
                            fixationIncorrect.draw()
                            win.flip()           
                kb.clearEvents('mouse')  # only really needed for pygame windows
        
        # add the response to the quest
        quest.addResponse(thisResp)
        core.wait(1)
        dataFile.write(f"{trial},{block},{blockTrial},{stimulus},{thisBlock.nStim},{stimNumber},{noiseType},{seed1},{seed2},{signalInterval+1},{round(thisIncrement, 8)},{thisResp}\n")
    threshold = round(quest.paramEstimate['threshold'],8)
    slope = round(quest.paramEstimate['slope'],2)
    thresholdFile.write(f"{block},{stimulus},{thisBlock.nStim},{stimName},{noiseType},{threshold},{slope}\n")
    
    for frameN in range(int(round(2 * frameRate))):
            message3.draw()
            win.flip()
    
    #print(stimulus, nStim, threshold)
    
dataFile.close()
thresholdFile.close()

