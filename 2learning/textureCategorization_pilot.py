from __future__ import absolute_import, division, print_function
from psychopy import visual, event, core, gui, data, sound
from psychopy.tools.filetools import fromFile, toFile
from psychopy.hardware import keyboard
from random import shuffle, random 
import random, copy, scipy, numpy
import os, shutil
import string, time
import platform
import csv
from pathlib import Path
import datetime

subject = 'tmp'

debug = 0
#dataPath = '/Users/zhussain1/Documents/psychopyData/preexposureLearning/'
#stimFolder = Path('/Users/zhussain1/Dropbox/Research/Ongoing/preexposureLearning/code/stimuli/')
dataPath='../../psychopyData/learning/preex_pilot/'
stimFolder = Path('../../psychopy/2learning/stimuli/')

timestamp = datetime.datetime.now().strftime("%d_%m_%H%M")
dataFileName = subject+'_textureCategorization'+'_'+timestamp
dataFile = open(dataPath+dataFileName + '.csv', 'a')
dataFile.write('block, trial, stim, sf, band, ref, texture, accuracy, rt\n')
#dataFile.flush()   # forces it to disk
# PsychoPy experiment handler
thisExp = data.ExperimentHandler(
    name='textureCategorization',
    version='1.0',
    extraInfo={'participant':subject},
#    dataFileName=dataPath+dataFileName
)

# === Load sounds ===
corSnd = sound.Sound(1200, octave=14, stereo=True, secs=0.05)
incorSnd = sound.Sound(400, octave=7, stereo=True, secs=0.05)

# === Monitor setup ===
if platform.platform()[0:5] == 'Linux':
    monitor = 'detectingMonitor'
    frameRate = 120
    import ctypes
    xlib = ctypes.cdll.LoadLibrary("libX11.so")
    xlib.XInitThreads()
else:
    monitor = 'testMonitor'
    frameRate = 60

if debug == 1:
    win = visual.Window([1600,1000], allowGUI=True, monitor=monitor, units='deg', checkTiming=False)
else:
    win = visual.Window(fullscr=True, allowGUI=True, monitor=monitor, units='deg', checkTiming=False)

# === Stimulus parameters ===
texSize = 5
feedbackDuration = 1
fpduration = 1
stimulusduration = 1
blankduration = 0.2
trialsPerCondition = 1

# === Visual stimuli ===
fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.2)
fixationCorrect = visual.GratingStim(win, color='green', tex=None, mask='circle', size=0.2)
fixationIncorrect = visual.GratingStim(win, color='red', tex=None, mask='circle', size=0.2)
texStim = visual.ImageStim(win, size=texSize, units='deg', interpolate=True, mask=None)

# === Keyboard ===
kb = keyboard.Keyboard()

# === Welcome screen ===
win.mouseVisible = False
msg1 = visual.TextStim(win, text='Press right for category A and left for B', pos=[0,3], wrapWidth=200)
msg2 = visual.TextStim(win, text='Press the space bar to begin', pos=[0,1])

msg1.draw()
msg2.draw()
win.flip()

kb.clearEvents()
keys = []
while not keys:
    keys = kb.getKeys()

win.flip()
core.wait(0.1)

# --------------------------------------------------
# BLOCK DEFINITIONS (2 x 2 x 2 design)
# --------------------------------------------------

blockConditions = [
    {'folder':'s1','sf':'low','ref':20,'band':10},
    {'folder':'s2','sf':'high','ref':20,'band':10},
    {'folder':'s3','sf':'low','ref':20,'band':30},
    {'folder':'s4','sf':'high','ref':20,'band':30},
    {'folder':'s5','sf':'low','ref':30,'band':10},
    {'folder':'s6','sf':'high','ref':30,'band':10},
    {'folder':'s7','sf':'low','ref':30,'band':30},
    {'folder':'s8','sf':'high','ref':30,'band':30},
]

blocks = data.TrialHandler(
    trialList=blockConditions,
    nReps=2,
    method='random',
    name='blocks'
)

thisExp.addLoop(blocks)

totalBlocks = len(blockConditions)
blockNum = 0
trialNum = 0

# --------------------------------------------------
# BLOCK LOOP
# --------------------------------------------------

for thisBlock in blocks:

    blockNum += 1
    folderPath = stimFolder / thisBlock['folder']
    tex_files = sorted(
        [f.name for f in folderPath.glob('AX*.jpg')] +
        [f.name for f in folderPath.glob('BX*.jpg')]
    )

    stimList = []

    for f in tex_files:
        category = 'AX' if f.startswith('AX') else 'BX'
        stimList.append({'file':f,'category':category})

    trials = data.TrialHandler(
        trialList=stimList,
        nReps=trialsPerCondition,
        method='random',
        name='trials'
    )

    thisExp.addLoop(trials)

    # --------------------------------------------------
    # TRIAL LOOP
    # --------------------------------------------------

    for thisTrial in trials:

        trialNum += 1

        img_file = thisTrial['file']
        category = thisTrial['category']

        full_path = folderPath / img_file
        texStim.image = str(full_path)
        texture = img_file.replace('.jpg','')

        # fixation
        for _ in range(int(round(fpduration * frameRate))):
            fixation.draw()
            win.flip()

        # stimulus
        for _ in range(int(round(stimulusduration * frameRate))):
            texStim.draw()
            win.flip()

        # blank
        for _ in range(int(round(blankduration * frameRate))):
            win.flip()

        if category == 'AX':
            corresp = 'right'
        else:
            corresp = 'left'

        thisResp = None
        clockRT = core.Clock()

        while thisResp is None:

            allKeys = kb.getKeys(keyList=['escape','left','right'])
            rt = clockRT.getTime()

            for thisKey in allKeys:

                if thisKey.name == 'escape':
                    core.quit()

                elif thisKey.name in ['left','right']:

                    if thisKey.name == corresp:
                        thisResp = 1
                        corSnd.play()
                        for frameN in range(int(round(feedbackDuration * frameRate))):
                            fixationCorrect.draw()
                            win.flip()

                    else:
                        thisResp = 0
                        incorSnd.play()
                        for frameN in range(int(round(feedbackDuration * frameRate))):
                            fixationIncorrect.draw()
                            win.flip()

                    responseKey = thisKey.name

        core.wait(0.5)
        win.flip()
        # save data
        dataFile.write(f"{blockNum}, {trialNum},{thisBlock['folder']},{thisBlock['sf']}, {thisBlock['band']}, {thisBlock['ref']}, {texture},{thisResp},{round(rt,2)}\n")
        #dataFile.flush()   # forces it to disk

    # --------------------------------------------------
    # END OF BLOCK SCREEN
    # --------------------------------------------------

    if blockNum < totalBlocks:

        blocksRemaining = totalBlocks - blockNum

        breakText = visual.TextStim(
            win,
            text=f"End of block {blockNum}\n\n{blocksRemaining} blocks to go\n\nPress SPACE to continue",
            height=0.8
        )

        breakText.draw()
        win.flip()

        kb.clearEvents()

        waiting = True
        while waiting:

            keys = kb.getKeys(['space','escape'])

            for key in keys:

                if key.name == 'escape':
                    core.quit()

                if key.name == 'space':
                    waiting = False

thisExp.abort()
win.close()
core.quit()