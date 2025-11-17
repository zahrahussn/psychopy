from __future__ import absolute_import, division, print_function
from psychopy import visual, event, core, gui, data, sound
from psychopy.tools.filetools import fromFile, toFile
from psychopy.hardware import keyboard
from random import shuffle, random #added this to track clicks
import random, copy, scipy, numpy
import os, shutil
import string, time
import platform
import csv
from pathlib import Path

debug=1
idNumber = 1

if platform.platform()[0:5] == 'Linux': # if we're on Linux, then we're probably using the viewpixx monitor
    monitor = 'viewPixx'
    frameRate=120
    print('hello')
else:
    monitor = 'testMonitor'
    frameRate=60
if debug==1:
    win = visual.Window([1600, 800], allowGUI=True, monitor=monitor, units='deg', checkTiming=False)
else:
    win = visual.Window(fullscr=True, allowGUI=True, monitor=monitor, units='deg', checkTiming=False)
   
feedback=1
fpduration=2
stimulusduration=0.15
blankduration=1
trialsPerCondition = 3

os.makedirs('data', exist_ok=True)
dataFileName = f'data/faceMatch_partial_{idNumber}'
if os.path.exists(dataFileName+'.csv'): # if datafile already exist, append a number
    ii=2
    while True:
        new_name = dataFileName + "_" + str(ii)
        if not os.path.exists(new_name+'.csv'):
            dataFileName = new_name
            break 
        ii += 1
with open(dataFileName+'.csv', 'a', newline='') as dataFile:
    writer = csv.writer(dataFile)
    writer.writerow(['trial', 'faceID', 'mask', 'response', 'accuracy', 'RT', 'stimDuration'])

folder = Path('/Users/zhussain1/Documents/psychopy/faceMatch/Stimuli/largerSet')
image_files = [f.name for f in folder.glob('*.jpeg')]

fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.2)
frameFeedback = visual.ShapeStim(win, color='green',lineWidth=1.5, vertices=((0, 0), (0, 0), (0, 0)))
myMouse = event.Mouse(win=win)

#Feedback sounds 
corSnd = sound.Sound(1800, octave=14, stereo=True, secs=0.05)
incorSnd = sound.Sound(700, octave=7, stereo=True, secs=0.05)

# Make face and noise stimuli
faceWidth=4.2
faceHeight=4.2
faceSize=(faceWidth,faceHeight)
facePos=(0,0)
faceStimulus= visual.ImageStim(win,size=faceSize) # create face stimulus without specifying the image or position
noiseTexture = numpy.random.rand(128, 128) * 2.0 - 1
half_height = faceHeight / 2.0
upper_center_y = facePos[1] + (faceHeight / 4.0)
lower_center_y = facePos[1] - (faceHeight / 4.0)
maskUpper = visual.GratingStim(win, tex=noiseTexture, size=(faceWidth, half_height), pos=(facePos[0], upper_center_y), units='deg', interpolate=False, autoLog=False)
maskLower = visual.GratingStim(win, tex=noiseTexture, size=(faceWidth, half_height), pos=(facePos[0], lower_center_y), units='deg', interpolate=False, autoLog=False)
zeroMask = None

# prepare face choice coordinates
faceWidthChoice = 3
faceHeightChoice = 3
faceSizeChoice = (faceWidthChoice, faceHeightChoice)
xcoords = [-6, 0, 6, -6, 0, 6]   # 3 on top, 3 below
ycoords = [4, 4, 4, -4, -4, -4]

# Create reusable face stimuli
faceStimuliList = [visual.ImageStim(win, size=faceSizeChoice) for _ in range(6)]

# ------------------- START SCREEN -------------------
msg = visual.TextStim(win, text='Press the space bar to begin')
keyPress = []
welcome_faces = random.sample(image_files, 6)
for i, stim in enumerate(faceStimuliList):
    stim.image = str(folder / welcome_faces[i])
    stim.pos = (xcoords[i], ycoords[i])
while 'space' not in keyPress:
    for stim in faceStimuliList:  # draw all 6 faces each frame
        stim.draw()
    msg.draw()
    win.flip()

    keyPress = event.getKeys(keyList=['space', 'escape'])
    if 'escape' in keyPress:
        core.quit()

# ------------------ Trial structure ------------------
stimList = []
for face_idx in range(50):  # 50 targets
    for mask in ['upper', 'lower', 'none']:
        for rep in range(trialsPerCondition):
            stimList.append({'target': face_idx, 'mask': mask})
trials = data.TrialHandler(stimList, nReps=1, method='random')

# ------------------- TRIAL LOOP -------------------
trialNum = 0
for thisTrial in trials:
    trialNum += 1
    myMouse.setPos((0, 0))
    myMouse.clickReset()

    # --- target and distractors ---
    available_faces = image_files.copy()
    target_image = available_faces[thisTrial['target']]
    available_faces.remove(target_image)
    distractors = random.sample(available_faces, 5)
    all_faces = [target_image] + distractors
    random.shuffle(all_faces)
    correct_idx = all_faces.index(target_image)

    # --- assign images to choice thumbnails ---
    for i in range(6):
        faceStimuliList[i].image = str(folder / all_faces[i])
        faceStimuliList[i].pos = (xcoords[i], ycoords[i])

    # --- set mask ---
    if thisTrial['mask'] == 'upper':
        mask = maskUpper
    elif thisTrial['mask'] == 'lower':
        mask = maskLower
    else:
        mask = zeroMask

    # --- fixation ---
    for _ in range(int(round(fpduration * frameRate))):
        fixation.draw()
        win.flip()

    # --- target ---
    faceStimulus.image = str(folder / target_image)
    for _ in range(int(round(stimulusduration * frameRate))):
        faceStimulus.draw()
        if mask is not None:
            mask.draw()
        win.flip()

    # --- blank ---
    for _ in range(int(round(blankduration * frameRate))):
        win.flip()

    # --- response phase ---
    myMouse.setVisible(True)
    clickedFace = None
    rt_clock = core.Clock()
    while clickedFace is None:
        for stim in faceStimuliList:
            stim.draw()
        fixation.draw()
        win.flip()

        if myMouse.getPressed()[0]:
            clickPos = myMouse.getPos()
            myMouse.setVisible(False)
            rt = rt_clock.getTime()

            for i, stim in enumerate(faceStimuliList):
                x, y = stim.pos
                half_w, half_h = stim.size[0] / 2, stim.size[1] / 2
                if (x - half_w < clickPos[0] < x + half_w) and (y - half_h < clickPos[1] < y + half_h):
                    clickedFace = i
                    accuracy = int(i == correct_idx)
                    frameColor = 'green' if accuracy else 'red'
                    (corSnd if accuracy else incorSnd).play()

                    # feedback rectangle (not triangle!)
                    vertices = [
                        (x - half_w, y - half_h),
                        (x + half_w, y - half_h),
                        (x + half_w, y + half_h),
                        (x - half_w, y + half_h),
                        (x - half_w, y - half_h)  # close shape
                    ]
                    frameFeedback = visual.ShapeStim(
                        win,
                        vertices=vertices,
                        lineColor=frameColor,
                        lineWidth=4,
                        fillColor=None,
                        closeShape=True
                    )

                    for _ in range(int(frameRate * feedback)):
                        for stim2 in faceStimuliList:
                            stim2.draw()
                        fixation.draw()
                        frameFeedback.draw()
                        win.flip()

                    # save data
                    with open(dataFileName + '.csv', 'a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow([
                            trialNum,
                            target_image,
                            thisTrial['mask'],
                            all_faces[i],
                            accuracy,
                            round(rt, 3),
                            f"{stimulusduration}s"
                        ])
                    break
win.close()
core.quit()
