from __future__ import absolute_import, division, print_function
from psychopy import visual, event, core, data, sound
from psychopy.hardware import keyboard
from pathlib import Path
import numpy as np
import random, csv, os, platform

# ------------------ Experiment setup ------------------
debug = 1
idNumber = 1

if platform.platform().startswith('Linux'):
    monitor = 'viewPixx'
    frameRate = 120
else:
    monitor = 'testMonitor'
    frameRate = 60

if debug==1:
    win = visual.Window([1600, 800], allowGUI=True, monitor=monitor, units='deg', checkTiming=False)
else:
    win = visual.Window(fullscr=True, allowGUI=True, monitor=monitor, units='deg', checkTiming=False)

# ------------------ Parameters ------------------
feedback_duration = 1.0
fpduration = 2
stimulusduration = 0.15
blankduration = 1
trialsPerCondition = 3  # 3 repeats per mask x target

# ------------------ Stimuli setup ------------------
dataFileName = f'data/faceMatch_partial_{idNumber}'
os.makedirs('data', exist_ok=True)
if os.path.exists(dataFileName + '.csv'):
    i = 2
    while os.path.exists(f"{dataFileName}_{i}.csv"):
        i += 1
    dataFileName = f"{dataFileName}_{i}"

with open(dataFileName + '.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['trial', 'target', 'mask', 'response', 'accuracy', 'RT', 'stimDuration'])

folder = Path('/Users/zhussain1/Documents/psychopy/faceMatch/Stimuli/largerSet')
image_files = [f.name for f in folder.glob('*.jpeg')]
if len(image_files) < 50:
    raise ValueError("Expected 50 face images in Stimuli folder.")

# feedback sounds
corSnd = sound.Sound(1800, octave=14, stereo=True, secs=0.05)
incorSnd = sound.Sound(700, octave=7, stereo=True, secs=0.05)

# ------------------ Masks ------------------
faceWidth, faceHeight = 4.2, 4.2
faceStimulus = visual.ImageStim(win, size=(faceWidth, faceHeight))
noiseTexture = np.random.rand(128, 128) * 2.0 - 1
maskUpper = visual.GratingStim(win, tex=noiseTexture, size=(faceWidth, faceHeight / 2),
                               pos=(0, faceHeight / 4), interpolate=False)
maskLower = visual.GratingStim(win, tex=noiseTexture, size=(faceWidth, faceHeight / 2),
                               pos=(0, -faceHeight / 4), interpolate=False)

# ------------------ Choice screen setup ------------------
# 6 positions for 1-of-6 task
xcoords = [-7, -3.5, 0, 3.5, 7, 0]
ycoords = [4, 4, 4, 4, 4, -4]

faceWidthChoice, faceHeightChoice = 3, 3
faceStimuliList = [visual.ImageStim(win, size=(faceWidthChoice, faceHeightChoice)) for _ in range(6)]

# ------------------ Trial structure ------------------
stimList = []
for face_idx in range(50):  # 50 targets
    for mask in ['upper', 'lower', 'none']:
        for rep in range(trialsPerCondition):
            stimList.append({'target': face_idx, 'mask': mask})
trials = data.TrialHandler(stimList, nReps=1, method='random')

myMouse = event.Mouse(win=win)
fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.2)
msg = visual.TextStim(win, text='Press the space bar to begin')
frameFeedback = visual.ShapeStim(win, lineWidth=3.0)

# ------------------ Wait to start ------------------
key = event.waitKeys(keyList=['space'])

# ------------------ Trial loop ------------------
trialNum = 0
for trial in trials:
    trialNum += 1
    myMouse.setPos((0, 0))
    myMouse.clickReset()
    myMouse.setVisible(False)

    # select target and distractors
    available_faces = image_files.copy()
    target_image = available_faces[trial['target']]
    available_faces.remove(target_image)
    distractors = random.sample(available_faces, 5)
    all_faces = [target_image] + distractors
    random.shuffle(all_faces)

    correct_idx = all_faces.index(target_image)

    # prepare choice thumbnails
    for i in range(6):
        faceStimuliList[i].image = str(folder / all_faces[i])
        faceStimuliList[i].pos = (xcoords[i], ycoords[i])

    # choose mask
    if trial['mask'] == 'upper':
        mask = maskUpper
    elif trial['mask'] == 'lower':
        mask = maskLower
    else:
        mask = None

    # fixation
    for frameN in range(int(fpduration * frameRate)):
        fixation.draw()
        win.flip()

    # show target face
    faceStimulus.image = str(folder / target_image)
    for frameN in range(int(stimulusduration * frameRate)):
        faceStimulus.draw()
        if mask:
            mask.draw()
        win.flip()

    # blank
    for frameN in range(int(blankduration * frameRate)):
        win.flip()

    # choice screen
    myMouse.setVisible(True)
    rt_clock = core.Clock()
    clicked = False
    while not clicked:
        for stim in faceStimuliList:
            stim.draw()
        win.flip()

        buttons, times = myMouse.getPressed(getTime=True)
        if buttons[0]:
            clickPos = myMouse.getPos()
            for i, stim in enumerate(faceStimuliList):
                x, y = stim.pos
                half_w, half_h = stim.size[0] / 2, stim.size[1] / 2
                if (x - half_w < clickPos[0] < x + half_w) and (y - half_h < clickPos[1] < y + half_h):
                    clicked = True
                    rt = rt_clock.getTime()
                    accuracy = int(i == correct_idx)
                    frameColor = 'green' if accuracy == 1 else 'red'
                    frameFeedback.pos = stim.pos
                    frameFeedback.size = stim.size
                    frameFeedback.lineColor = frameColor
                    (corSnd if accuracy else incorSnd).play()
                    for f in range(int(frameRate * feedback_duration)):
                        for stim2 in faceStimuliList:
                            stim2.draw()
                        frameFeedback.draw()
                        win.flip()

                    with open(dataFileName + '.csv', 'a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow([
                            trialNum,
                            target_image,
                            trial['mask'],
                            all_faces[i],
                            accuracy,
                            round(rt, 3),
                            f"{stimulusduration}s"
                        ])
                    break

win.close()
core.quit()
