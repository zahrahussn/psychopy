from __future__ import absolute_import, division, print_function
from psychopy import visual, core, gui, data, sound
from psychopy.hardware import keyboard, mouse
import numpy as np
import os
import csv
import platform

# ----------------------------- #
# Experiment parameters
# ----------------------------- #
debug = 1
params = {'ID number': '1'}

dlg = gui.DlgFromDict(params, title='Face Match', fixed=['dateStr'])
if dlg.OK == False:
    core.quit()

# Monitor setup
if platform.platform()[0:5] == 'Linux':
    monitor = 'viewPixx'
    frameRate = 120
else:
    monitor = 'testMonitor'
    frameRate = 60

win = visual.Window([1000, 800] if debug else [1920, 1080],
                    fullscr=not debug, allowGUI=True,
                    monitor=monitor, units='deg', checkTiming=False)

# ----------------------------- #
# Global keys
# ----------------------------- #
#event.globalKeys.add(key='escape', func=core.quit)

# ----------------------------- #
# Timing
# ----------------------------- #
fixate = 0.5
fpduration = 1.0
stimulusduration = 0.3
maskduration = 0.1
blankduration = 0.2

# ----------------------------- #
# Data file
# ----------------------------- #
os.makedirs('data', exist_ok=True)
dataFileName = f"data/FaceMatch{params['ID number']}_partial"
if os.path.exists(dataFileName + '.csv'):
    ii = 2
    while True:
        new_name = f"{dataFileName}_{ii}"
        if not os.path.exists(new_name + '.csv'):
            dataFileName = new_name
            break
        ii += 1

with open(dataFileName + '.csv', 'a', newline='') as dataFile:
    writer = csv.writer(dataFile)
    writer.writerow(['trial', 'faceID', 'mask', 'response', 'accuracy', 'RT', 'stimDuration'])

# ----------------------------- #
# Fixation stimuli
# ----------------------------- #
fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.2)
fixationCorrect = visual.GratingStim(win, color='green', tex=None, mask='circle', size=0.2)
fixationIncorrect = visual.GratingStim(win, color='red', tex=None, mask='circle', size=0.2)

# ----------------------------- #
# Feedback sounds
# ----------------------------- #
corSnd = sound.Sound(1800, octave=14, stereo=True, secs=0.05)
incorSnd = sound.Sound(700, octave=7, stereo=True, secs=0.05)

# ----------------------------- #
# Stimuli
# ----------------------------- #
facePath = 'Stimuli/'
imageM = ['M1','M2','M3','M4','M5']
imageF = ['F1','F2','F3','F4','F5']

faceWidth, faceHeight = 4.2, 4.2
faceSize = (faceWidth, faceHeight)
facePos = (0, 0)
faceStimulus = visual.ImageStim(win, size=faceSize)

# Gaussian noise mask
noiseTexture = np.random.rand(128, 128) * 2.0 - 1
half_height = faceHeight / 2.0
maskUpper = visual.GratingStim(win, tex=noiseTexture, size=(faceWidth, half_height),
                               pos=(facePos[0], facePos[1]+half_height/2), units='deg',
                               interpolate=False, autoLog=False)
maskLower = visual.GratingStim(win, tex=noiseTexture, size=(faceWidth, half_height),
                               pos=(facePos[0], facePos[1]-half_height/2), units='deg',
                               interpolate=False, autoLog=False)
maskPost = visual.GratingStim(win, tex=noiseTexture, size=faceSize, pos=facePos, units='deg',
                              interpolate=False, autoLog=False)
zeroMask = None  # no mask

# ----------------------------- #
# Face choice screen
# ----------------------------- #
faceWidthChoice, faceHeightChoice = 3, 3
xcoords = [-10,-5,0,5,10,-10,-5,0,5,10]
ycoords = [5,5,5,5,5,-5,-5,-5,-5,-5]

faceStimuluslist = []
for i in range(10):
    if i < 5:
        faceStimuluslist.append(visual.ImageStim(win, image=f"{facePath}{imageM[i]}.jpg",
                                                 pos=(xcoords[i], ycoords[i]),
                                                 size=(faceWidthChoice, faceHeightChoice)))
    else:
        faceStimuluslist.append(visual.ImageStim(win, image=f"{facePath}{imageF[i-5]}.jpg",
                                                 pos=(xcoords[i], ycoords[i]),
                                                 size=(faceWidthChoice, faceHeightChoice)))
faceBuffer = visual.BufferImageStim(win, stim=faceStimuluslist, rect=(-1,1,1,-1))

# ----------------------------- #
# Trial handler
# ----------------------------- #
stimList = []
for image in range(len(imageM)):
    for mask in ['upper','lower','none']:
        for gender in [0,1]:
            stimList.append({'gender':gender,'mask':mask,'image':image})
trials = data.TrialHandler(stimList, 10)

# ----------------------------- #
# Mouse and keyboard
# ----------------------------- #
myMouse = mouse.Mouse(win=win)
myMouse.setVisible(False)
kb = keyboard.Keyboard()

# ----------------------------- #
# Wait for space bar to start
# ----------------------------- #
msg = visual.TextStim(win, text='Press the space bar to begin')
keyPress = []
while 'space' not in keyPress:
    faceBuffer.draw()
    msg.draw()
    win.flip()
    keyPress = kb.getKeys(['space'], waitRelease=False)

# ----------------------------- #
# Trial loop
# ----------------------------- #
trial = 0
for thisTrial in trials:
    trial += 1

    # recenter mouse
    myMouse.setPos((0,0))
    myMouse.setVisible(False)

    # choose face image
    if thisTrial['gender'] == 1:
        image = imageM[thisTrial['image']]
        correctFace = thisTrial['image']
    else:
        image = imageF[thisTrial['image']]
        correctFace = thisTrial['image'] + 5
    faceStimulus.image = f"{facePath}{image}.jpg"

    # select mask
    if thisTrial['mask'] == 'upper':
        mask = maskUpper
    elif thisTrial['mask'] == 'lower':
        mask = maskLower
    else:
        mask = zeroMask

    # fixation
    for _ in range(int(round(fpduration*frameRate))):
        fixation.draw()
        win.flip()

    # stimulus + mask
    for _ in range(int(round(stimulusduration*frameRate))):
        faceStimulus.draw()
        if mask is not None:
            mask.draw()
        win.flip()

    # post-mask
    for _ in range(int(round(maskduration*frameRate))):
        fixation.draw()
        maskPost.draw()
        win.flip()

    # blank
    for _ in range(int(round(blankduration*frameRate))):
        win.flip()

    # ----------------------------- #
    # Response collection
    # ----------------------------- #
    clickedFace = None
    myMouse.setVisible(True)
    trialStart = core.getTime()  # for RT

    while clickedFace is None:
        faceBuffer.draw()
        fixation.draw()
        win.flip()

        # --- check escape key every frame ---
        keys = kb.getKeys(['escape'], waitRelease=False)
        if 'escape' in keys:
            core.quit()

        # --- get mouse press ---
        buttons, times, positions = myMouse.getPressedPos()
        if buttons[0] and positions is not None:
            pos = positions[0]
            if isinstance(pos, (list, tuple, np.ndarray)) and len(pos) == 2:
                clickcoords = np.array(pos)
                RT = core.getTime() - trialStart

                # check which face was clicked
                for i in range(10):
                    x_min = xcoords[i] - faceWidthChoice/2
                    x_max = xcoords[i] + faceWidthChoice/2
                    y_min = ycoords[i] - faceHeightChoice/2
                    y_max = ycoords[i] + faceHeightChoice/2

                    if x_min < clickcoords[0] < x_max and y_min < clickcoords[1] < y_max:
                        clickedFace = i

                        # Feedback
                        if clickedFace == correctFace:
                            accuracy = 1
                            corSnd.play()
                            for _ in range(int(round(fixate*frameRate))):
                                fixationCorrect.draw()
                                win.flip()
                        else:
                            accuracy = 0
                            incorSnd.play()
                            for _ in range(int(round(fixate*frameRate))):
                                fixationIncorrect.draw()
                                win.flip()

                        clickedImage = imageM[clickedFace] if clickedFace < 5 else imageF[clickedFace-5]

                        # Save data
                        with open(dataFileName+'.csv','a',newline='') as dataFile:
                            writer = csv.writer(dataFile)
                            writer.writerow([trial, thisTrial['image'], thisTrial['mask'],
                                             clickedImage, accuracy, RT, f"{stimulusduration} s"])

                        myMouse.setVisible(False)
                        break  # exit for-loop

win.close()
core.quit()
