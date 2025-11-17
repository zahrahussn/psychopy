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
import platform
from psychopy.hardware import keyboard
# myPath = '/Users/zhussain1/Dropbox/Research/Ongoing/uncertainty_chinaecherem/calibration_bitStealing'
dataPath = '../../psychopyData/detection2024/'
#os.chdir(myPath)
import sys
# sys.path.append('/Users/zhussain1/Dropbox/Research/Ongoing/uncertainty_chinaecherem/calibration_bitStealing')
#import findBackgroundIndex
#import pbLum2BS
#import pbBitStealing2RGB

# calibration file and other stuff needed for bit-stealing
#doBitStealing=0
#calData = pd.read_excel("/Users/zhussain1/Dropbox/Research/Ongoing/uncertainty_Chinaecherem/calibration_bitStealing/calibration_data.xlsx")
#backgroundRGB = np.array([160,160,160])
#backgroundIndex=findBackgroundIndex.find_Background_Index(calData, backgroundRGB)
#maxminaveIndices=[1786,1,backgroundIndex[0]]
#interpolator = interp1d(calData['RGB Number'], calData['Luminance'], kind='linear', fill_value="extrapolate")
#maxminave = interpolator(maxminaveIndices)
#avgLum=maxminave[2]
#cmin=(maxminave[1]-maxminave[2])/maxminave[2]
#cmax=(maxminave[0]-maxminave[2])/maxminave[2]
#L=calData['Luminance']
#B=calData['RGB Number']
#rgbMat=calData[['R', 'G', 'B']]

# present a dialogue to change params
#dlg = gui.Dlg(title="Detection under uncertainty")
#dlg.addField('Subject', 'zh') #0
#dlg.addField('Stimulus', choices=['grating', 'texture']) #1       
#dlg.addField('nStim', choices=['1', '5']) #2
#dlg.addField('Noise type', choices=['fixed', 'twin', 'variable'])  #3
#dlg.addField('Session number', choices=[1,2,3,4,5]) #4
#dlg.addField('Stim ID', choices=[1, 2, 3, 4, 5]) #5
#user_input = dlg.show()
#if dlg.OK:
#  print("good to go")
#  #  toFile('lastParams.pickle', params)  # save params to file for next time
#else:
#    core.quit()  # the user hit cancel so exit

#subject = user_input[0]  
#stimulus = user_input[1]  
#nStim= int(user_input[2])  
#noiseType = user_input[3]  
#session_number = user_input[4]
#stimID=int(user_input[5])

title='Detection under uncertainty'

subject = 'KF'

noiseType = 'fixed'  # 'fixed', 'variable'

stimulus = 'texture' # 'grating', 'texture'

nStim = 1  # 1, 5

stimID='2' # 1, 2, 3, 4, 5

session_number = '12' # 1, 2, 3..., 12

gamma=2.2
#frameRate = 60
stimDuration = 0.2
isi= 0.5 #remember to change back to 1
fixate = 0.5
textures=[1,2,3,4,5]
oris = [0.0, 72.0, 144.0, 216.0, 288.0] # 5 equally-spaced angles between 0 and 360 deg
if nStim==1:
    if stimulus=='texture':
        stimName=stimID
    else:
        stimName=stimID
else:
    stimName="all"
        

correctSound = sound.Sound(1800, octave=14, stereo=True, secs=0.01)
incorrectSound = sound.Sound(700, octave=7, stereo=True, secs=0.01)

# data file
fileName = subject+'_'+stimulus+'_'+str(nStim)+'_'+str(stimName)+'_'+noiseType+'_'+str(session_number)+'_quest'
dataFile = open(dataPath+fileName + '.csv', 'a')
dataFile.write('trial,stimulus,nStim,noise,noiseSeed1, noiseSeed2, stimID,signalInterval,contrast, correct\n')

thresholdFile = subject+'_'+stimulus+'_'+str(nStim)+'_'+str(stimName)+'_'+noiseType+'_'+'_'+str(session_number)+'_questThreshold '
thresholdData = open(dataPath+thresholdFile + '.csv', 'a')

# create window and stimuli
if platform.platform()[0:5] == 'Linux': # if we're on Linux, then we're probably using the viewpixx monitor
    monitor = 'detectingMonitor'
    frameRate=120
    import ctypes
    xlib = ctypes.cdll.LoadLibrary("libX11.so")
    xlib.XInitThreads()
else:
    monitor = 'testMonitor'
    frameRate=60

# create window and stimuli
#win = visual.Window([1600, 1000], allowGUI=True, monitor=monitor, units='deg', checkTiming=False)
win = visual.Window(fullscr=True, allowGUI=True, monitor=monitor, units='deg', checkTiming=False)

# create fixed noise
noiseSd = np.sqrt(0.1)
noiseMean = 0
seed1 = int(time.time() * 1000) 
random_state = np.random.default_rng(seed1)
noiseMatrix = random_state.normal(noiseMean, noiseSd, (256, 256))
noiseMatrix = np.clip(noiseMatrix, -1, 1)
seed2=seed1

if stimulus=="texture":
    textures=loadmat('/home/zahra/Documents/psychopy/3detection/theTextures.mat')
    image1=textures['theStimulus4']['stim1'][0][0]
    image2=textures['theStimulus4']['stim2'][0][0]
    image3=textures['theStimulus4']['stim3'][0][0]
    image4=textures['theStimulus4']['stim4'][0][0]
    image5=textures['theStimulus4']['stim5'][0][0]
    textures = [image1, image2, image3, image4, image5]
else:
    array = np.linspace(0, 1, 256)
    grating = np.sin(1 * np.pi * 4 * array)  
    grating = np.tile(grating, (256, 1))
    oris = oris 

if nStim == 1:
    if stimulus == "texture":
        textures = [textures[int(stimID) - 1]]  # Adjust for 0-based indexing
    else:
        oris = [oris[int(stimID) - 1]] 
        
fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.2)
fixationCorrect = visual.GratingStim(win, color='green', tex=None, mask='circle', size=0.2)
fixationIncorrect = visual.GratingStim(win, color='red', tex=None, mask='circle', size=0.2)
message1 = visual.TextStim(win, pos=[0, +3], text='Hit a key when ready.')
message2 = visual.TextStim(win, pos=[0, -3], wrapWidth=200,
                            text="Press left for interval 1 and right for interval 2.")

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

# create the quest+handler
quest = data.QuestPlusHandler(intensityVals=intensityVals, thresholdVals=thresholdVals,
                         slopeVals=slopeVals, lowerAsymptoteVals=lowerAsymptoteVals, startIntensity=intensityVals[30],
                         lapseRateVals=lapseRateVals, responseVals=responseVals, paramEstimationMethod='mean', nTrials=50, 
                         stimScale='linear', dataFileName=None, pThreshold=pThresholdVal)

# display instructions and wait
win.mouseVisible = False
message1.draw()
message2.draw()
fixation.draw()
win.flip()

# check for a keypress
#event.waitKeys()
kb = keyboard.Keyboard()
keys = kb.getKeys()
while not keys:
    keys = kb.getKeys()

trialNumber = 0
for trials in range(quest.nTrials):  
    trialNumber = trialNumber+1
    thisIncrement=quest.next()
    
    # do noise
    if noiseType=="fixed":
        noiseMatrix1=np.clip(noiseMatrix, -1, 1)
        noiseMatrix2=noiseMatrix1
    elif noiseType=="twin":
        seed1 = int(time.time() * 1000) + trialNumber
        random_state = np.random.default_rng(seed1) 
        noiseMatrix1=np.random.normal(noiseMean, noiseSd, (256, 256))
        noiseMatrix1=np.clip(noiseMatrix1, -1, 1)
        noiseMatrix2=noiseMatrix1
        seed2=seed1
    else:
        seed1 = int(time.time() * 1000) + trialNumber
        seed2 = int(time.time() * 1000) + trialNumber + 1
        random_state1 = np.random.default_rng(seed1) 
        noiseMatrix1=random_state1.normal(noiseMean, noiseSd, (256, 256))
        noiseMatrix1=np.clip(noiseMatrix1, -1, 1)
        random_state2 = np.random.default_rng(seed2) 
        noiseMatrix2=random_state2.normal(noiseMean, noiseSd, (256, 256))
        noiseMatrix2=np.clip(noiseMatrix2, -1, 1)
    
    # set signal interval 
    signalInterval = np.random.choice([0, 1])
    
    # set stimulus index
    if nStim == 1:
        stimNumber = 0
    else:
        stimNumber = np.random.choice(range(nStim))
    
    if stimulus=="grating":
        thisStim=rotate(grating, angle=oris[stimNumber], reshape=False)
    else:
        thisStim=textures[stimNumber]
       
    # set stimulus contrast and add to noise
    thisStim=thisStim*np.sqrt(1/np.var(thisStim))
    thisStim=np.sqrt(thisIncrement)*thisStim
    noisyStim=noiseMatrix1+thisStim
#    if doBitStealing==1:
#        noisyStimLum=avgLum*(1+noisyStim)
#        noisyStimBS=pbLum2BS.pbLum_2_BS(noisyStimLum, L, B)
#        noisyStimFinal=pbBitStealing2RGB.pb_BitStealing_2_RGB(noisyStimBS, rgbMat,0)
#        noisyStimFinal = 2 * (noisyStimFinal - noisyStimFinal.min()) / (noisyStimFinal.max() - noisyStimFinal.min()) - 1
#    else:
#         noisyStimFinal=np.clip(noisyStim, -1, 1)   
    noisyStimFinal=np.clip(noisyStim, -1, 1)
    
    noise = visual.ImageStim(win, image=noiseMatrix2, mask=None, size=4, interpolate=False, pos=(0,0))        
    signalPlusNoise = visual.ImageStim(win, image=noisyStimFinal, size=4, pos=(0, 0), mask=None, interpolate=False)
    #signalPlusNoise.setColor(noisyStimFinal, 'rgb255')
    
#    print(trialNumber)
#    print(thisIncrement)
#    print(np.var(thisStim))
#    print(np.min(noiseMatrix))
#    print(np.max(noiseMatrix))

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

#    # get response
#    thisResp = None
#    clockRT = core.Clock() 
#    while thisResp is None:
#        allKeys = event.getKeys(keyList=['escape','left','right'],timeStamped = clockRT)
#        for keyTuple in allKeys:
#            [thisKey, thisRT] = keyTuple
#        for thisKey in allKeys:
#            if thisKey[0] in ['escape']:core.quit()
#            elif thisKey[0] in ['left','right']:
#                if thisKey[0] == corresp:
#                    thisResp = 1  # correct
#                    correctSound.play()  
#                    for frameN in range(int(round(fixate * frameRate))):
#                        fixationCorrect.draw()
#                        win.flip()                    
#                else:
#                    thisResp = 0  # incorrect
#                    incorrectSound.play()
#                    for frameN in range(int(round(fixate * frameRate))):
#                        fixationIncorrect.draw()
#                        win.flip()           
#            event.clearEvents('mouse')  
#    quest.addResponse(thisResp)
#    core.wait(1)

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
    
    dataFile.write(f"{trialNumber},{stimulus},{nStim},{noiseType},{seed1},{seed2},{stimNumber+1},{signalInterval+1},{thisIncrement},{thisResp}\n")
    
dataFile.close()
threshold = quest.paramEstimate['threshold']
slope = quest.paramEstimate['slope']
thresholdData.write('%s\t%s\t%i\tthreshold: %.6f\tslope: %.6f\n' % (subject, stimulus, nStim, threshold, slope))

savedFile = fileName + '.csv'
print('Estimated detection threshold:', quest.paramEstimate)
