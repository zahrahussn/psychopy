from __future__ import absolute_import, division, print_function
from psychopy import visual, event, core, gui, data, sound
from psychopy.tools.filetools import fromFile, toFile
from psychopy.hardware import keyboard
from random import shuffle, random
import random, copy, scipy
import os, shutil
import string, time
import platform
import csv
import time, numpy as np
from pathlib import Path
import datetime
debug = 1
dataPath = '/Users/zhussain1/Documents/psychopyData/preexposureLearning/'

subject = 'zh_test'
preexposureType = 'control' # preexposureType options: 'intermixed', 'blocked', 'control'
stimulusXType = 'fixed' # stimulusXType options: # 'fixed',  'variable'

if stimulusXType == 'fixed':
    stimSubfolder = 'preexp_fixed'
elif stimulusXType == 'variable':
    stimSubfolder = 'preexp_variable'
else:
    raise ValueError("stimulusXType must be 'fixed' or 'variable'")

stimFolder = Path('/Users/zhussain1/Documents/psychopy/2learning/stimuli/') / stimSubfolder
#stimFolder = Path('/Users/zhussain1/Dropbox/Research/Ongoing/preexposureLearning/code/stimuli/') / stimSubfolder
timestamp = datetime.datetime.now().strftime("%d_%m_%H%M")
dataFileName = (
    subject + '_textureCategorization'
    + '_' + preexposureType
    + '_' + stimulusXType
    + '_' + timestamp
)
dataFile = open(dataPath + dataFileName + '.csv', 'a')
dataFile.write(
    'phase, block, trial, preexposureType, stimulusXType, stim, sf, band, ref, texture, category, accuracy, rt\n'
)
dataFile.flush()

# === Load sounds ===
correctSound = sound.Sound(1800, octave=14, stereo=True, secs=0.01)
incorrectSound = sound.Sound(700, octave=7, stereo=True, secs=0.01)

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
    win = visual.Window([1600, 1000], allowGUI=True, monitor=monitor, units='deg', checkTiming=False, color='grey')
else:
    win = visual.Window(fullscr=True, allowGUI=True, monitor=monitor, units='deg', checkTiming=False, color='grey')
win.mouseVisible = False    

# === Stimulus parameters ===
texSize = 5
feedbackDuration = 1
fpduration = 1
stimulusduration = 1
blankduration = 0.1
trialsPerCondition = 1
sz = 256
noiseSd = np.sqrt(0.2)
noiseMean = 0

# preexposure timings
preBlankDuration = 1.0
preStimDuration = 0.7

# === Visual stimuli ===
fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.2)
fixationCorrect = visual.GratingStim(win, color='green', tex=None, mask='circle', size=0.2)
fixationIncorrect = visual.GratingStim(win, color='red', tex=None, mask='circle', size=0.2)
texStim = visual.ImageStim(win, size=texSize, units='deg', interpolate=True, mask=None)
noiseStim = visual.ImageStim(
    win,
    image=np.zeros((256, 256)),
    size=texSize,
    units='deg',
    interpolate=True,
    mask=None
)

# === Keyboard ===
kb = keyboard.Keyboard()

# --------------------------------------------------
# BLOCK DEFINITIONS
# --------------------------------------------------
blockConditions = [
    {'folder': 's7', 'sf': 'low', 'ref': 30, 'band': 30},
]

blocks = data.TrialHandler(
    trialList=blockConditions,
    nReps=1,
    method='random',
    name='blocks'
)

totalBlocks = len(blockConditions)
blockNum = 0
trialNum = 0
preTrialNum = 0

# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------
def wait_for_space_or_escape(kb_obj):
    kb_obj.clearEvents()
    waiting = True
    while waiting:
        keys = kb_obj.getKeys(['space', 'escape'])
        for key in keys:
            if key.name == 'escape':
                core.quit()
            elif key.name == 'space':
                waiting = False

def build_preexposure_list(stim_list, preexposure_type):
    ax_items = [s for s in stim_list if s['category'] == 'AX']
    bx_items = [s for s in stim_list if s['category'] == 'BX']

    random.shuffle(ax_items)
    random.shuffle(bx_items)

    if preexposure_type == 'blocked':
        if random.choice([True, False]):
            return ax_items + bx_items
        else:
            return bx_items + ax_items

    elif preexposure_type == 'intermixed':
        pre_list = []
        max_len = max(len(ax_items), len(bx_items))

        for i in range(max_len):
            if i < len(ax_items):
                pre_list.append(ax_items[i])
            if i < len(bx_items):
                pre_list.append(bx_items[i])

        return pre_list

    elif preexposure_type == 'control':
        control_list = []

        for i in range(2):
            control_list.append({
                'file': None,
                'category': 'noise',
                'texture': f'gaussian_noise_{i+1}'
            })

        return control_list

    else:
        raise ValueError("preexposureType must be 'intermixed', 'blocked', or 'control'")
    
def safe_quit():
    try:
        dataFile.flush()
        dataFile.close()
    except:
        pass
    try:
        win.close()
    except:
        pass

    core.quit()    
    ax_items = [s for s in stim_list if s['category'] == 'AX']
    bx_items = [s for s in stim_list if s['category'] == 'BX']

    random.shuffle(ax_items)
    random.shuffle(bx_items)

    if preexposure_type == 'blocked':
        if random.choice([True, False]):
            return ax_items + bx_items
        else:
            return bx_items + ax_items

    elif preexposure_type == 'intermixed':
        pre_list = []
        max_len = max(len(ax_items), len(bx_items))

        for i in range(max_len):
            if i < len(ax_items):
                pre_list.append(ax_items[i])
            if i < len(bx_items):
                pre_list.append(bx_items[i])

        return pre_list

    elif preexposure_type == 'control':
        control_list = []

        for i in range(60):
            control_list.append({
                'file': None,
                'category': 'noise',
                'texture': f'gaussian_noise_{i+1}'
            })

        return control_list

    else:
        raise ValueError("preexposureType must be 'intermixed', 'blocked', or 'control'")

# --------------------------------------------------
# BLOCK LOOP
# --------------------------------------------------
for thisBlock in blocks:

    blockNum += 1
    folderPath = stimFolder
    tex_files = sorted(
        [f.name for f in folderPath.glob('AX*.jpg')] +
        [f.name for f in folderPath.glob('BX*.jpg')]
    )
    if len(tex_files) == 0:
        raise RuntimeError(f"No AX/BX jpg files found in: {folderPath}")

    stimList = []
    for f in tex_files:
        category = 'AX' if f.startswith('AX') else 'BX'
        stimList.append({'file': f, 'category': category})

    # ==========================================
    # PREEXPOSURE PHASE
    # ==========================================
    preexposureList = build_preexposure_list(stimList, preexposureType)
    preMsgTitle = visual.TextStim(
        win,
        text='Pre-exposure phase',
        pos=[0, 2.2],
        height=0.6,
        wrapWidth=20,
        color='black'
    )
    
    preMsgBody = visual.TextStim(
        win,
        text=(
            'You will now see a series of images. Each image will appear briefly.\n\n'
            'After each image, press SPACE to continue.\n\n'
            'Press SPACE to begin.'
        ),
        pos=[0, 0],
        height=0.45,
        wrapWidth=18,
        color='black'
    )
    
    preMsgTitle.draw()
    preMsgBody.draw()
    win.flip()
    wait_for_space_or_escape(kb)
    
    for preStim in preexposureList:
    
        preTrialNum += 1
    
        category = preStim['category']
    
        # 1 s blank grey screen
        for _ in range(int(round(preBlankDuration * frameRate))):
            win.flip()
    
        # stimulus
        if preexposureType == 'control':
    
            seed1 = int(time.time() * 1000)
            random_state1 = np.random.default_rng(seed1)
            noiseMatrix = random_state1.normal(noiseMean, noiseSd, (256, 256))  # Store noise sample
            noiseMatrix = np.clip(noiseMatrix, -1, 1)
            noiseStim.image = noiseMatrix
            
            texture = preStim['texture']
    
            for _ in range(int(round(preStimDuration * frameRate))):
                noiseStim.draw()
                win.flip()
    
        else:
    
            img_file = preStim['file']
            full_path = folderPath / img_file
            texStim.image = str(full_path)
            texture = img_file.replace('.jpg', '')
    
            for _ in range(int(round(preStimDuration * frameRate))):
                texStim.draw()
                win.flip()
    
        # blank until spacebar
        win.flip()
        wait_for_space_or_escape(kb)
    
        dataFile.write(
            f"preexposure, {blockNum}, {preTrialNum}, {preexposureType}, {stimulusXType}, "
            f"{thisBlock['folder']}, {thisBlock['sf']}, {thisBlock['band']}, {thisBlock['ref']}, "
            f"{texture}, {category}, , \n"
        )
        dataFile.flush()
    # ==========================================
    # BREAK / WELCOME SCREEN BEFORE CATEGORIZATION
    # ==========================================

    msg1 = visual.TextStim(
        win,
        text='Categorization task: Press RIGHT for category A and LEFT for category B',
        pos=[0, 2],
        wrapWidth=200,
        height=0.45,
        color='black'
    )
    msg2 = visual.TextStim(
        win,
        text='Take a break if you want.\n\nPress SPACE when you are ready to begin the task.',
        height=0.45,
        pos=[0, 0],
        wrapWidth=20,
        color='black'
    )

    msg1.draw()
    msg2.draw()
    win.flip()
    wait_for_space_or_escape(kb)

    win.flip()
    core.wait(0.1)

    # ==========================================
    # CATEGORIZATION TRIALS
    # ==========================================
    trials = data.TrialHandler(
        trialList=stimList,
        nReps=trialsPerCondition,
        method='random',
        name='trials'
    )

    for thisTrial in trials:

        trialNum += 1

        img_file = thisTrial['file']
        category = thisTrial['category']

        full_path = folderPath / img_file
        texStim.image = str(full_path)

        texture = img_file.replace('.jpg', '')

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
        responseKey = ''
        rt = ''

        kb.clearEvents()
        clockRT = core.Clock()

        while thisResp is None:

            allKeys = kb.getKeys(keyList=['escape', 'left', 'right'], waitRelease=False)

            for thisKey in allKeys:

                if thisKey.name == 'escape':
                    safe_quit()

                elif thisKey.name in ['left', 'right']:

                    rt = thisKey.rt
                    responseKey = thisKey.name

                    if thisKey.name == corresp:
                        thisResp = 1
                        correctSound.play()
                        for frameN in range(int(round(feedbackDuration * frameRate))):
                            fixationCorrect.draw()
                            win.flip()
                    else:
                        thisResp = 0
                        incorrectSound.play()
                        for frameN in range(int(round(feedbackDuration * frameRate))):
                            fixationIncorrect.draw()
                            win.flip()

        core.wait(0.5)
        win.flip()

        dataFile.write(
            f"categorization, {blockNum}, {trialNum}, {preexposureType}, {stimulusXType}, "
            f"{thisBlock['folder']}, {thisBlock['sf']}, {thisBlock['band']}, {thisBlock['ref']}, "
            f"{texture}, {category}, {thisResp}, {round(rt, 3)}\n"
        )


        dataFile.flush()

    # ==========================================
    # END OF BLOCK SCREEN
    # ==========================================
    if blockNum < totalBlocks:

        blocksRemaining = totalBlocks - blockNum

        breakText = visual.TextStim(
            win,
            text=f"End of block {blockNum}\n\n{blocksRemaining} blocks to go\n\nPress SPACE to continue",
            height=0.8,
            color='black'
        )

        breakText.draw()
        win.flip()
        wait_for_space_or_escape(kb)
# ==========================================
# END OF EXPERIMENT SCREEN
# ==========================================
endText = visual.TextStim(
    win,
    text='All done!\n\nThank you for participating.',
    height=0.6,
    wrapWidth=20,
    color='black'
)

endText.draw()
win.flip()

core.wait(2.0)
dataFile.flush()
dataFile.close()
win.close()
core.quit()
