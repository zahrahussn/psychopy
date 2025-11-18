# Roach et al 2011 task
from psychopy import visual, core, event, sound, data
import numpy as np
import os, time, datetime, csv, random
import pandas as pd

# === Participant info ===
name = 'zh1'
while len(name) != 3:
    name = input('Initials (3 letters): ')

# === File setup ===
timestamp = datetime.datetime.now().strftime("%d_%m_%H%M")
outfolder = os.path.join(os.getcwd(), "zhData", name)
os.makedirs(outfolder, exist_ok=True)
trialfile = os.path.join(outfolder, f"{timestamp}_trials.csv")
thresholdfile = os.path.join(outfolder, f"{timestamp}_thresholds.csv")
with open(trialfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        'inducerLocation', 'phase','motion', 'edge', 'stimPos', 'log_contrast', 'contrast', 'correct'
    ])

# === Load sounds ===
correct_sound = sound.Sound(1800, octave=14, stereo=True, secs=0.01)
incorrect_sound = sound.Sound(700, octave=7, stereo=True, secs=0.01)

# === Experiment parameters ===
win = visual.Window(size=[800, 600], units="deg", color=[0, 0, 0], fullscr=False, monitor='testMonitor', checkTiming=False)
#actual_frame_rate = win.getActualFrameRate(nIdentical=60, nMaxFrames=200)

inducer_logcontrast = 2
inducer_contrast = (10 ** inducer_logcontrast) / 100
noisesd = 0
noisepixelsize = 2
# F = 1 / 30       # spatial frequency (cycles/pixel approx)
TF = 5           # temporal frequency (Hz)
stimSize=1
frameRate = 60
phaseStep = TF / frameRate  # phase increment per frame
inducerx = 2
inducery = 2
n_trials = 10  # total trials per block
nframes = round(5 * frameRate)
blankframes = round(0.20 * frameRate)

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

# === Main experiment ===
trial_clock = core.Clock()
t_start = trial_clock.getTime()
win.mouseVisible = False

block_num = 0
total_blocks = len(locations) * len(phases)  # 4

for location in locations:
    for phase in phases:
        block_num += 1
        print(f"\n=== Block start: Location={location}, Phase={phase} ===")
  # === Balanced motion order ===
        motions_block = (['up'] * (n_trials // 2)) + (['down'] * (n_trials // 2))
        random.shuffle(motions_block)
        
        stair = data.StairHandler(startVal=0.8, stepType='lin',
                                  stepSizes=[0.4], minVal=-2, maxVal=2,
                                  nReversals=8, nTrials=n_trials)
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
#            TF_actual=phaseStep*actual_frame_rate
#            print(f"Actual frame rate: {actual_frame_rate:.2f} Hz")
#            print(f"Measured temporal frequency: {TF_actual:.2f} Hz")
            
            event.clearEvents()
            keys = event.waitKeys(keyList=['left', 'right', 'escape'])
            if 'escape' in keys:
                win.close()
                core.quit()
        
            correct = int(
                (keys[0] == 'left' and side == 1) or (keys[0] == 'right' and side == 2)
            )
            stair.addResponse(correct)
        
            (correct_sound if correct else incorrect_sound).play()
            core.wait(0.3)
            
            # Save trial data
            trial_data.append({
                'participant': name,
                'location': location,
                'phase': phase,
                'motion': motion,
                'edge': edge,
                'stimPos': stimSide,
                'log_contrast': increment_logcontrast,
                'stim_contrast': contrast,
                'correct': correct
            })
            
            with open(trialfile, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                location, phase, motion, edge, stimSide, 
                log_contrast,   
                contrast,                        
                correct
                ])
  
  # === Block break ===
        if block_num < total_blocks:
            msg_text = f"Block {block_num} complete.\nTake a short break.\nPress SPACE to continue."
        else:
            msg_text = "All done! Thank you.\nPress SPACE to exit."
        msg = visual.TextStim(win, text=msg_text,
                              color='black', height=0.5)
        msg.draw()
        win.flip()
        event.waitKeys(keyList=['space'])
        
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
                thresholds.append({
                    'participant': name,
                    'location': location,
                    'phase': phase,
                    'edge': edge_type,
                    'threshold_log': log_thr,
                    'threshold_contrast': lin_thr
                })

# Save files
df.to_csv(trialfile, index=False)
pd.DataFrame(thresholds).to_csv(thresholdfile, index=False)

# === Print summary ===
print("\n=== Thresholds by condition ===")
for t in thresholds:
    print(f"{t['location']}, phase={t['phase']}, {t['edge']}: "
          f"log={t['threshold_log']:.2f}, "
          f"contrast={t['threshold_contrast']*100:.2f}%")

t_end = trial_clock.getTime()
print(f"\nExperiment complete. Duration: {(t_end - t_start)/60:.2f} min")

win.close()
core.quit()