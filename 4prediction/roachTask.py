# Roach et al 2011 task
from psychopy import visual, core, event, sound, data
from psychopy.tools.filetools import fromFile, toFile
import numpy as np
import os, time, datetime, csv, random
import pandas as pd
import sys
import platform
from psychopy.hardware import keyboard
import sys
dataPath = '../../psychopyData/prediction/'
debug=0

# to quit the experiment at any point by pressing escape
event.globalKeys.add(key='escape', func=core.quit)

# === Participant info ===
subject= 'zh1'

# === File setup ===
timestamp = datetime.datetime.now().strftime("%d_%m_%H%M")
trialFileName = subject+'_prediction_trials'+'_'+timestamp
thresholdFileName = subject+'_prediction_thresholds'+'_'+timestamp
trialFile = open(dataPath+trialFileName + '.csv', 'a')
thresholdFile=open(dataPath+thresholdFileName + '.csv', 'a')
trialFile.write('trial, inducerLocation, phase, motion, edge, stimPos, log_contrast, contrast, correct\n')

# === Load sounds ===
correct_sound = sound.Sound(1200, octave=14, stereo=True, secs=0.05)
incorrect_sound = sound.Sound(400, octave=7, stereo=True, secs=0.05)

# === Experiment parameters ===
if platform.platform()[0:5] == 'Linux': # if we're on Linux, then we're probably using the viewpixx monitor
    monitor = 'detectingMonitor' # 'viewPixx' 'detectingMonitor'
    frameRate=120
    import ctypes
    xlib = ctypes.cdll.LoadLibrary("libX11.so")
    xlib.XInitThreads()
else:
    monitor = 'testMonitor'
    frameRate=120
if debug==1:
    win = visual.Window([1600, 1000], allowGUI=True, monitor=monitor, units='deg', checkTiming=False)
else:
    win = visual.Window(fullscr=True, allowGUI=True, monitor=monitor, units='deg', checkTiming=False)


inducer_logcontrast = 2
inducer_contrast = (10 ** inducer_logcontrast) / 100
noisesd = 0
noisepixelsize = 2
# F = 1 / 30       # spatial frequency (cycles/pixel approx)
TF = 5           # temporal frequency (Hz)
stimSize=1
inducerx = 2
inducery = 2
n_trials = 80  # total trials per block
phaseStep = TF / frameRate  # phase increment per frame
nframes = round(1 * frameRate)
blankframes = round(0.10 * frameRate)

fixation = visual.ShapeStim(win, vertices=((0, -0.15), (0, 0.15), (0,0), (-0.15,0), (0.15,0)),
                            lineWidth=2, closeShape=False, lineColor='black')
# Compute inducer height so that it abuts stimulus and reaches screen edge
stim_height = 1
win_height = win.size[1] * win.monitor.getPixelsPerDegree()[1] if hasattr(win.monitor, 'getPixelsPerDegree') else 30
inducer_height = (win_height / 2) - (stim_height / 2)
inducer_y_pos_top = (stim_height / 2) + (inducer_height / 2)
inducer_y_pos_bottom = - (stim_height / 2) - (inducer_height / 2)
                            
stim = visual.GratingStim(win, tex='sin', mask=None, size=(stimSize, stimSize), units="deg", sf=1, ori=270, phase=0.5)
inducer1 = visual.GratingStim(win, tex='sin', mask=None, size=(inducer_height, 1), units="deg", pos=(-inducerx, inducery), sf=1, ori=270, contrast=inducer_contrast, phase=0)
inducer2 = visual.GratingStim(win, tex='sin', mask=None, size=(inducer_height, 1), units="deg", pos=(inducerx, inducery), sf=1, ori=270, contrast=inducer_contrast, phase=0)

# === Experimental factors ===
locations = ['top', 'bottom']
phases = [0, 0.5]
motion = ['up', 'down']

# === Data storage ===
trial_data = []
msg1 = visual.TextStim(win, text='Press left  or right to report target location.', pos=[0, 3], wrapWidth=200)
msg2 = visual.TextStim(win, text='Press the space bar to begin', pos=[0, 0])

msg1.draw()
msg2.draw()
#fixation.draw()
win.flip()
# Wait for a keypress
kb = keyboard.Keyboard()
kb.clearEvents()
keys = []
while not keys:
    keys = kb.getKeys()

win.flip()  # flush buffer
core.wait(0.1)  # very short wait

# === Main experiment ===
trial_clock = core.Clock()
t_start = trial_clock.getTime()
win.mouseVisible = False
kb = keyboard.Keyboard()
kb.clearEvents()

blocks = [(loc, ph) for loc in locations for ph in phases]
random.shuffle(blocks)  # shuffle the block order
block_num = 0
total_blocks = len(locations) * len(phases)  # 4
trialNumber=0
#for location in locations:
#    for phase in phases:
for location, phase in blocks:
    block_num += 1
    print(f"\n=== Block start: Location={location}, Phase={phase} ===")
# === Balanced motion order ===
    motions_block = (['up'] * (n_trials // 2)) + (['down'] * (n_trials // 2))
    random.shuffle(motions_block)
    
                             
    stair = data.StairHandler(startVal=0.8, stepType='lin',
                              stepSizes=[0.4, 0.2, 0.1, 0.05], minVal=-2, maxVal=2,
                              nUp=1, nDown=3, 
                              nReversals=4, nTrials=n_trials)                         
    stair.extraInfo = {'location': location, 'phase': phase}
    
    # set inducer position
    if location=='top':
        inducer1.pos=(-inducerx, inducer_y_pos_top)
        inducer2.pos=(inducerx, inducer_y_pos_top)
    else:
        inducer1.pos=(-inducerx, inducer_y_pos_bottom)
        inducer2.pos=(inducerx, inducer_y_pos_bottom)
        
    # trials within block
    for motion, increment_logcontrast in zip(motions_block, stair):
        trialNumber +=1
        inducer1.phase = 0
        inducer2.phase = 0
        dir_sign = 1 if motion == 'up' else -1
        contrast = (10 ** increment_logcontrast) / 100
        stim.contrast = contrast
        log_contrast = round(increment_logcontrast, 2) # for data file
        contrast = round(contrast, 4) # for data file
        offset_deg = (stim.pos[1] - inducer1.pos[1])  # vertical distance from inducer center to stim center
        if stair.extraInfo['phase'] == 0:
            stim.phase = (-offset_deg / 1) % 1.0
        else:  # counterphase
            stim.phase = (0.5 - offset_deg / 1) % 1.0
       # stim.phase = stair.extraInfo['phase']
        side = np.random.choice([1, 2])
        stimSide =  ('left' if side == 1 else 'right')
        if (location == 'top' and motion == 'down') or (location == 'bottom' and motion == 'up'):
            edge = 'leading'
        else:
            edge = 'trailing'
        
        frame_times = []
        for frame in range(nframes):
            inducer1.phase += dir_sign * phaseStep
            inducer2.phase += dir_sign * phaseStep
            stim.phase += dir_sign * phaseStep
            stim.pos = (-inducerx if side == 1 else inducerx, 0)
            
            stim.draw()
            inducer1.draw()
            inducer2.draw()
            fixation.draw()
            win.flip()
            
        for frame in range(blankframes):
            fixation.draw()
            win.flip()   
    
        # === Get response ===
        thisResp = None
        clockRT = core.Clock() 
        keys = kb.waitKeys(keyList=['escape', 'left', 'right'])

        if 'escape' in keys:
            core.quit()

        resp_key = keys[0].name

        correct = int(
            (resp_key == 'left' and side == 1) or 
            (resp_key == 'right' and side == 2))
        stair.addResponse(correct)
        
        (correct_sound if correct else incorrect_sound).play()
        core.wait(0.3)
            
         # Save trial data
        trial_data.append({
        'trial': trialNumber,
        'location': location,
        'phase': phase,
        'motion': motion,
        'edge': edge,
        'stimSide': stimSide,
        'log_contrast': increment_logcontrast,
        'contrast': contrast,
        'correct': correct
        }) 
        trialFile.write(f"{trialNumber}, {location},{phase},{motion},{edge},{stimSide},{increment_logcontrast}, {contrast},{correct}\n")
  
# === Block break ===
    if block_num < total_blocks:
        msg_text = f"Block {block_num} complete.\nTake a short break.\nPress SPACE to continue."
    else:
        msg_text = "All done! Thank you.\nPress SPACE to exit."
    msg = visual.TextStim(win, text=msg_text,
                          color='black', height=0.5)
    msg.draw()
    win.flip()
    kb = keyboard.Keyboard()
    kb.clearEvents()
    keys = []
    while not keys:
        keys = kb.getKeys()

    core.wait(1)
    
# === Compute thresholds by edge type ===
df = pd.DataFrame(trial_data)
thresholds = []

for location in df['location'].unique():
    for phase in df['phase'].unique():
        for edge_type in ['leading', 'trailing']:
            subset = df[(df['location'] == location) &
                        (df['phase'] == phase) &
                        (df['edge'] == edge_type)]
            if len(subset) > 0:
                log_thr = round(np.mean(subset['log_contrast'].tail(8)),3)
                lin_thr = round((10 ** log_thr) / 100, 4)
                thresholdFile.write(f"{location},{phase},{edge_type},{log_thr}, {lin_thr}\n")

 #=== Print summary ===
print("\n=== Thresholds by condition ===")
for t in thresholds:
    print(f"{t['location']}, phase={t['phase']}, {t['edge']}: "
          f"log={t['threshold_log']:.2f}, "
          f"contrast={t['threshold_contrast']*100:.2f}%")

t_end = trial_clock.getTime()
print(f"\nExperiment complete. Duration: {(t_end - t_start)/60:.2f} min")

win.close()
core.quit()