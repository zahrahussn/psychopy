from psychopy import core, visual, gui, data, event, sound
from psychopy.tools.filetools import fromFile, toFile
import time, numpy as np
from scipy.interpolate import interp1d
from psychopy.data import QuestPlusHandler
import os
import pandas as pd
# from psychopy.visual import NoiseStim 
from scipy.ndimage import rotate
from scipy.io import loadmat
import matplotlib.pyplot as plt
#myPath = '/Users/zhussain1/Dropbox/Research/Ongoing/uncertainty_chinaecherem/calibration_bitStealing'
#dataPath = '/Users/zhussain1/Dropbox/Research/Ongoing/uncertainty_chinaecherem/multObsData/'
dataPath = '../../psychopyData/detection2024/multObsData/sm/'
#os.chdir(myPath)
import sys
import platform
from psychopy.hardware import keyboard
import sys

debug=0# 1
#stimContrast=0.000065 # 0.00005 # 0.00008
stimContrast= 0.00009
nObs=4
title='Detection under uncertainty'
subject = 'sm'
#subject = 'gv_practice'
stimulus = 'grating' # 'grating', 'texture'
uncertainty = 'simple' # 'sse', 'simple', 'composite'
noiseType = 'fixed'  # 'fixed', 'variable'
session_number = '2' # 1, 2
stimID=2 # '1', '2', '3', '4', '5' only applies for the sse condition

#  window 
gamma=2.2
if platform.platform()[0:5] == 'Linux': # if we're on Linux, then we're probably using the viewpixx monitor
    monitor = 'detectingMonitor' # 'viewPixx' 'detectingMonitor'
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

#gamma=2.2
stimDuration =  0.15
isi= 0.5
fixate = 0.5
correctSound = sound.Sound(1800, octave=14, stereo=True, secs=0.01)
incorrectSound = sound.Sound(700, octave=7, stereo=True, secs=0.01)
noiseSd = np.sqrt(0.1)
noiseMean = 0

# data file
fileName = subject+'_'+stimulus+'_'+uncertainty+'_'+noiseType+'_multObs'
dataFile = open(dataPath+fileName + '.csv', 'a')
dataFile.write('trial,uncertainty, observation, stimulus,stimID,stimNumber,contrast,noise,noiseSeed1, noiseSeed2, signalInterval, correct\n')

if stimulus=="texture":
    #textures=loadmat('/Users/zhussain1/Dropbox/Research/Ongoing/uncertainty_chinaecherem/theTextures.mat')
    textures=loadmat('/home/zahra/Documents/psychopy/3detection/theTextures.mat')
    image1=textures['theStimulus4']['stim1'][0][0]
    image2=textures['theStimulus4']['stim2'][0][0]
    image3=textures['theStimulus4']['stim3'][0][0]
    image4=textures['theStimulus4']['stim4'][0][0]
    image5=textures['theStimulus4']['stim5'][0][0]
    textures = [image1, image2, image3, image4, image5]
    if uncertainty == "sse":
        selected_texture = textures[stimID]  # Choose a single orientation for SSE
        textures = [selected_texture]     
        #textures=textures[stimID]
        nStim=1
        trialsPerStimulus=100
    else:
        textures=textures
        nStim=5
        trialsPerStimulus=20
else:
    array = np.linspace(0, 1, 512)
    bigGrating = np.sin(1 * np.pi * 8 * array)  # used to be 4 before scaling up and cropping grating
    bigGrating = np.tile(bigGrating, (512, 1))
    gratingCenter = 512 // 2
    grating = bigGrating[gratingCenter-128:gratingCenter+128, gratingCenter-128:gratingCenter+128]
    oris = [0.0, 72.0, 144.0, 216.0, 288.0] # 5 equally-spaced angles between 0 and 360 deg
    if uncertainty == "sse":
        selected_ori = oris[stimID]  # Choose a single orientation for SSE
        oris = [selected_ori]     
        nStim=1
        trialsPerStimulus=100
    else:
        oris=oris
        nStim=5
        trialsPerStimulus=20

fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.2)
fixationCorrect = visual.GratingStim(win, color='green', tex=None, mask='circle', size=0.2)
fixationIncorrect = visual.GratingStim(win, color='red', tex=None, mask='circle', size=0.2)
message1 = visual.TextStim(win, pos=[0, +3], text='Hit a key when ready.')
message2 = visual.TextStim(win, pos=[0, -3], wrapWidth=200,
                            text="Press left for interval 1 and right for interval 2.")

# trial handler
stimList=[]
for image in range(nStim):
    stimList.append({'image': image})
trials = data.TrialHandler(stimList, trialsPerStimulus)#

# added 3rd nov to show stimulus example for sse
if stimulus=="grating":
        thisStim=rotate(grating, angle=oris[0], reshape=False)
else:
        thisStim=textures[0]
thisStim=visual.ImageStim(win, image=thisStim, size=4, pos=(0, 0), mask=None, interpolate=False)

# display instructions and wait
win.mouseVisible = False
message1.draw()
message2.draw()
fixation.draw()
thisStim.draw()
win.flip()

# check for a keypress
#event.waitKeys()
kb = keyboard.Keyboard()
keys = kb.getKeys()
while not keys:
    keys = kb.getKeys()

trialNumber = 0
for thisTrial in trials:  
    trialNumber = trialNumber+1
    
    # set signal interval and identity
    signalInterval = np.random.choice([0, 1])
    
    #    chinaecherem's change to the original code; may have resulted in invalid simple condition 
#    as condition was not applied to the stimulus inside the observation loop; zh 30 sept 2025
# moved these lines up from after the noise making, nov 3 2025; zh
    if uncertainty == "simple":
        UniqueStimNum = np.random.choice(range(nStim), size=nObs, replace=False)
    else:
        UniqueStimNum = [stimID] * nObs 
        
    for obs in range(nObs):
        stimNumber = UniqueStimNum[obs]
        stimID = stimNumber + 1
        
        if stimulus=="grating":
            bigGrating=rotate(bigGrating, angle=oris[stimNumber], reshape=False)
            gratingCenter = 512 // 2
            thisStim = bigGrating[gratingCenter-128:gratingCenter+128, gratingCenter-128:gratingCenter+128]
        else:
            thisStim=textures[stimID]
               
        # do noise
        noiseMatrix1 = np.zeros((256, 256, nObs))  # Initialize 256x256xnObs matrix
        noiseMatrix2 = np.zeros((256, 256, nObs))  # Initialize 256x256xnObs matrix
        seeds1 = np.zeros(nObs)
        seeds2 = np.zeros(nObs)
        if noiseType == "fixed":
            seed = int(time.time() * 1000)+trialNumber
            random_state = np.random.default_rng(seed)
            fixed_noise1 = random_state.normal(noiseMean, noiseSd, (256, 256))  # Single noise sample for signal+noise
            fixed_noise1 = np.clip(fixed_noise1, -1, 1)
            for obs in range(nObs):
                noiseMatrix1[:, :, obs] = fixed_noise1  # Store noise sample
                noiseMatrix2[:, :, obs] = fixed_noise1
                seeds1[obs]=seed
                seeds2[obs]=seed
        else:
            for obs in range(nObs):
                seed1 = int(time.time() * 1000) + obs
                seed2 = int(time.time() * 1000) + obs + 1
                random_state1 = np.random.default_rng(seed1)
                random_state2 = np.random.default_rng(seed2)
                noiseMatrix1[:, :, obs] = random_state1.normal(noiseMean, noiseSd, (256, 256))  # Store noise sample
                noiseMatrix2[:, :, obs] = random_state2.normal(noiseMean, noiseSd, (256, 256))  # Store noise sample
                seeds1[obs]=seed1
                seeds2[obs]=seed2
                noiseMatrix1 = np.clip(noiseMatrix1, -1, 1)
                noiseMatrix2 = np.clip(noiseMatrix2, -1, 1)
  
        # set stimulus contrast and add to noise
        thisStim=thisStim*np.sqrt(1/np.var(thisStim))
        thisStim=np.sqrt(stimContrast)*thisStim
        noisyStim=np.clip(noiseMatrix1[:,:,obs]+thisStim, -1, 1)
        noisyStimFinal=noisyStim
        noise = visual.ImageStim(win, image=noiseMatrix2[:,:,obs], mask=None, size=4, interpolate=False, pos=(0,0))        
        signalPlusNoise = visual.ImageStim(win, image=noisyStimFinal, size=4, pos=(0, 0), mask=None, interpolate=False)
      
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
                if thisKey == 'escape':core.quit()
                elif thisKey in ['left','right']:
                    if thisKey == corresp:
                        thisResp = 1  # correct
                        if obs==3:
                            correctSound.play()  
                            for frameN in range(int(round(fixate * frameRate))):
                                fixationCorrect.draw()
                                win.flip()                    
                    else:
                        thisResp = 0  
                        if obs==3:
                            incorrectSound.play()
                            for frameN in range(int(round(fixate * frameRate))):
                                fixationIncorrect.draw()
                                win.flip()                    
                kb.clearEvents('mouse')
        core.wait(1)
    
        dataFile.write(f"{trialNumber}, {uncertainty},{obs+1},{stimulus},{stimID},{stimNumber+1},{stimContrast},{noiseType},{seeds1[obs]}, {seeds2[obs]},{signalInterval+1},{thisResp}\n")
    
dataFile.close()
