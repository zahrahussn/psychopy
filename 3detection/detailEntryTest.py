from psychopy import core, visual, gui, data, event, sound
from psychopy.tools.filetools import fromFile, toFile
import time, os, numpy as np
from PIL import Image
from psychopy.data import QuestPlusHandler
#from psychopy.visual import NoiseStim 
from scipy.ndimage import rotate, zoom
from scipy.io import loadmat
import matplotlib.pyplot as plt
import platform
from psychopy.hardware import keyboard

myPath = '/home/zahra/Documents/psychopy/detection/'

# global list to store details 
userDetails = {}

def runParamCollecting():
    
    if platform.platform()[0:5] == 'Linux': # if we're on Linux, then we're probably using the viewpixx monitor
        monitor = 'detectingMonitor'
        frameRate=120
        import ctypes
        xlib = ctypes.cdll.LoadLibrary("libX11.so")
        xlib.XInitThreads()
    else:   
        monitor = 'testMonitor'
        frameRate=60
    
    gamma = 2.2
    
    # create window and stimuli
    win = visual.Window([1000, 800], allowGUI=True, monitor='testMonitor', units='deg', checkTiming=False)
    #win.gamma=gamma
    kb = keyboard.Keyboard()

    intro = visual.TextStim(win, pos=[0, 0], text="press any key to begin")
    instru1 = visual.TextStim(win, pos=[0, 0], text="enter intials. 'return' when done")
    instru2 = visual.TextStim(win, pos=[0, 0], text="press left for 'grating' and right for 'texture'.")
    instru3 = visual.TextStim(win, pos=[0, 0], text="press left for '1' and right for '5'.")
    instru4 = visual.TextStim(win, pos=[0, 0], text="press left for 'fixed' and right for 'variable'.")

    intro.draw()
    win.flip()
    
    keys = kb.getKeys()
    while not keys:
        keys = kb.getKeys()
    
    # subject initials
    userDetails['initials'] = ""
    instru1.draw()
    win.flip()
    while True:
        keys = kb.getKeys()
        if keys:
            for key in keys:
                if key.name == 'return':  
                    if len(userDetails['initials']) > 0:
                        break
                elif key.name == 'backspace':
                    userDetails['initials'] = userDetails['initials'][:-1] 
                elif len(key.name) == 1: 
                    userDetails['initials'] += key.name

            # displaying typed keys on screen
            instru1.text = f"Initials: {userDetails['initials']}"
            instru1.draw()
            win.flip()
        
        if len(userDetails['initials']) > 0 and 'return' in keys:
            break  

    # stimulus type
    instru2.draw()
    win.flip()
    keys = kb.getKeys(keyList=['left', 'right'])
    while not keys:
        keys = kb.getKeys(keyList=['left', 'right'])

    if 'left' in keys:
        userDetails['stimulus'] = 'grating'
    else:
        userDetails['stimulus'] = 'texture'

    # no of stim
    instru3.draw()
    win.flip()
    keys = kb.getKeys(keyList=['left', 'right'])
    while not keys:
        keys = kb.getKeys(keyList=['left', 'right'])

    if 'left' in keys:
        userDetails['nStim'] = 1
    else:
        userDetails['nStim'] = 5

    # noise type
    instru4.draw()
    win.flip()
    keys = kb.getKeys(keyList=['left', 'right'])
    while not keys:
        keys = kb.getKeys(keyList=['left', 'right'])

    if 'left' in keys:
        userDetails['noiseType'] = 'fixed'
    else:
        userDetails['noiseType'] = 'dynamic'
    
    win.close()
    core.wait(1)

def detection():
    # getting user details from first fxn
    subject = userDetails['initials']
    stimulus = userDetails['stimulus']
    nStim = userDetails['nStim']
    noiseType = userDetails['noiseType']
    
    session_number='1'
    frameRate = 60
    stimDuration = 0.2
    isi = 1  # interstimulus interval
    fixate = 0.5
    gamma = 2.2
    
    # make a text file to save data
    fileName = f"{subject}_{stimulus}_{nStim}"
    dataFile = open(fileName + '.txt', 'w')
    dataFile.write('trial\tstimulus\tnStim\tstimID\tsignalInterval\tcontrast\tcorrect\n')
    
    thresholds = f"{subject}_{stimulus}_{nStim}_threshold "
    thresholdsData = open(thresholds + '.txt', 'w')
    
    # handling sound
    correctSound = sound.Sound(1800, octave=14, stereo=True, secs=0.01)
    incorrectSound = sound.Sound(700, octave=7, stereo=True, secs=0.01)
    
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
    win = visual.Window([1000, 800], allowGUI=True, monitor='testMonitor', units='deg', checkTiming=False)
    #win.gamma = gamma
    
    # create noise
    noiseSd = np.sqrt(0.1)
    noiseMean = 0
    noiseMatrix = np.random.normal(noiseMean, noiseSd, (256, 256))
    noise = visual.ImageStim(win, image=noiseMatrix, mask=None, size=4, interpolate=False, pos=(0, 0))
    
    if stimulus == "texture":
        # load and save textures
        textures = loadmat('theTextures.mat')
    #  images=textures['theStimulus4']
        image1 = textures['theStimulus4']['stim1'][0][0]
        image2 = textures['theStimulus4']['stim2'][0][0]
        image3 = textures['theStimulus4']['stim3'][0][0]
        image4 = textures['theStimulus4']['stim4'][0][0]
        image5 = textures['theStimulus4']['stim5'][0][0]
        textures = [image1, image2, image3, image4, image5]
    else: 
        array = np.linspace(0, 1, 256)
        grating = np.sin(1 * np.pi * 4 * array)
        grating = np.tile(grating, (256, 1))
        grating = grating * np.sqrt(1 / np.var(grating))
        oris = [0.0, 72.0, 144.0, 216.0, 288.0]  # 5 equally-spaced angles between 0 and 360 deg
    
    fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.2)
    fixation2 = visual.GratingStim(win, color='green', tex=None, mask='circle', size=0.2)
    message1 = visual.TextStim(win, pos=[0, +3], text='Hit any key when ready.')
    message2 = visual.TextStim(win, pos=[0, -3], 
                                text="Press left for interval 1 and right for interval 2.")
    
    # the parameters for quest+handler
    minContrast = 0.000001  # contrast variance
    maxContrast = 0.05
    intensityVals = np.logspace(np.log10(minContrast), np.log10(maxContrast), 50)  
    thresholdVals = np.logspace(np.log10(0.0000001), np.log10(0.1), 50)
    slopeVals = np.linspace(0.01, 10, 50)  
    lowerAsymptoteVals = [0.5]  # guess rate
    lapseRateVals = np.linspace(0, 0.05, 6)  
    responseVals = [1, 0]
    
    # create the quest+handler
    quest = data.QuestPlusHandler(intensityVals=intensityVals, thresholdVals=thresholdVals,
                                   slopeVals=slopeVals, lowerAsymptoteVals=lowerAsymptoteVals, startIntensity=intensityVals[30],
                                   lapseRateVals=lapseRateVals, responseVals=responseVals, paramEstimationMethod='mean', nTrials=20, stimScale='linear', dataFileName=None)
    
    # display instructions and wait
    win.mouseVisible = False
    message1.draw()
    message2.draw()
    fixation.draw()
    win.flip()
    
    # check for a keypress
    kb = keyboard.Keyboard()
    keys = kb.getKeys()
    while not keys:
        keys = kb.getKeys()
    
    for trials in range(quest.nTrials):  # will step through the staircase
        thisIncrement = quest.next()
        #print(thisIncrement)
    
        # set signal interval and identity
        signalInterval = np.random.choice([0, 1])
        stimNumber = np.random.choice(range(nStim))
    
        if stimulus == "grating":
            thisStim = rotate(grating, angle=oris[stimNumber], reshape=False)
        else:
            thisStim = textures[stimNumber]
            thisStim = thisStim * np.sqrt(1 / np.var(thisStim))
    
        # set stimulus contrast and add to noise
        noisyStim = np.clip((noiseMatrix + (np.sqrt(thisIncrement) * thisStim)), -1, 1)
        signalPlusNoise = visual.ImageStim(win, image=noisyStim, size=4, pos=(0, 0), mask=None, interpolate=False)
       
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
            allKeys = kb.getKeys(keyList=['escape', 'left', 'right'])
            for thisKey in allKeys:
                if thisKey == 'escape':
                    core.quit()
                elif thisKey in ['left', 'right']:
                    if thisKey == corresp:
                        thisResp = 1  # correct
                        correctSound.play()  
                        for frameN in range(int(round(fixate * frameRate))):
                            fixation2.draw()
                            win.flip()
                    else:
                        thisResp = 0  # incorrect
                        incorrectSound.play()
                kb.clearEvents('mouse')  # only really needed for pygame windows
    
        # add the response to the quest
        quest.addResponse(thisResp)
        core.wait(1)
        # print(f"Trial {trials}: Intensity={thisIncrement}, Threshold estimate={quest.paramEstimate('threshold')}")

        # dataFile.write('trial\tstimulus\tnStim\tstimID\tsignalInterval\tcontrast\tcorrect\n')
        dataFile.write('%i\t%s\t%i\t%i\t%i\t%.6f\t%i\n' % (trials + 1, stimulus, nStim, stimNumber + 1, signalInterval + 1, thisIncrement, thisResp))
    
    # staircase has ended
    threshold = quest.paramEstimate['threshold']
    slope = quest.paramEstimate['slope']
    thresholdsData.write('%s\t%s\t%i\tthreshold: %.4f\tslope: %.4f\n' % (subject, stimulus, nStim, threshold, slope))
    
    dataFile.close()
    #quest.saveAsPickle(fileName)  # save all the info
    
    savedFile = fileName + '.txt'
    #threshold = quest.mean()
    print('Estimated detection threshold:', quest.paramEstimate)

    win.close()
    core.wait(1)


runParamCollecting()

detection()
