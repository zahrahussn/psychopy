# Prediction_counterphase (PsychoPy version)
# Converted from MATLAB + VSG to PsychoPy
# Uses current working directory for saving data and sound files

from psychopy import visual, core, event, sound, data
import numpy as np
import os, time, datetime#, json

# === Participant info ===
name = 'zh1'
while len(name) != 3:
    name = input('Initials (3 letters): ')

# === File setup ===
timestamp = datetime.datetime.now().strftime("%d_%m_%H%M")
#folder = os.path.join(os.getcwd(), "counterphase_data", name)
#os.makedirs(folder, exist_ok=True)
#outfile = os.path.join(folder, f"{timestamp}.json")

# === Load sounds ===
correct_sound = sound.Sound(1800, octave=14, stereo=True, secs=0.01)
incorrect_sound = sound.Sound(700, octave=7, stereo=True, secs=0.01)
#correct_sound = sound.Sound(os.path.join(os.getcwd(), "correct.wav"))
#incorrect_sound = sound.Sound(os.path.join(os.getcwd(), "incorrect.wav"))

# === Experiment parameters ===
inducer_logcontrast = 2
inducer_contrast = (10 ** inducer_logcontrast) / 100
noisesd = 0
noisepixelsize = 2
F = 1 / 30       # spatial frequency (cycles/pixel approx)
TF = 5           # temporal frequency (Hz)
nframes = round(1000 / TF)
#testsize = 60 // 2
#adaptorsize = 400 // 2
testsize=1
adaptorsize=2
phases = [0, 0.5]
frameRate = 60.0
phaseStep = TF / frameRate  # phase increment per frame

win = visual.Window(size=[800, 600], units="deg", color=[0, 0, 0], fullscr=False, monitor='testMonitor')
fixation = visual.ShapeStim(win, vertices=((0, -0.25), (0, 0.25), (0,0), (-0.25,0), (0.25,0)),
                            lineWidth=2, closeShape=False, lineColor='white')
stim = visual.GratingStim(win, tex='sin', mask=None, size=(1, 1), units="deg", sf=1, ori=270, phase=0.5)
inducer1 = visual.GratingStim(win, tex='sin', mask=None, size=(7, 1), units="deg", pos=(-4, -4), sf=1, ori=270, contrast=inducer_contrast, phase=0)
inducer2 = visual.GratingStim(win, tex='sin', mask=None, size=(7, 1), units="deg", pos=(4,-4), sf=1, ori=270, contrast=inducer_contrast, phase=0)

# === Staircase setup ===
staircases = []
for phase in phases:
    stair = data.StairHandler(startVal=0.8,
                              stepType='lin',
                              stepSizes=[0.4],
                              minVal=-2,
                              maxVal=2,
                              nReversals=8,
                              nTrials=100)
    stair.extraInfo = {'phase': phase}
    staircases.append(stair)

# === Main trial loop ===
trial_clock = core.Clock()
t_start = trial_clock.getTime()

for stair in staircases:
    for increment_logcontrast in stair:
        stim.contrast = (10 ** increment_logcontrast) / 100
       # stim.phase = stair.extraInfo['phase']
        side = np.random.choice([1, 2])
        flip = np.random.choice([0, 1])
        #phaseshift = stair.extraInfo['phase']

        for frame in range(nframes):
            inducer1.phase += phaseStep
            inducer2.phase += phaseStep  
            stim.phase += phaseStep

            stim.pos = (-4 if side == 1 else 4, 0)
            stim.draw()
            inducer1.draw()
            inducer2.draw()
            fixation.draw()
            win.flip()

        # === Get response ===
        event.clearEvents()
        keys = event.waitKeys(keyList=['left', 'right', 'escape'])
        if 'escape' in keys:
            win.close()
            core.quit()

        response = 1 if ((keys[0] == 'left' and side == 1) or (keys[0] == 'right' and side == 2)) else 0
        stair.addResponse(response)

        if response == 1:
            correct_sound.play()
        else:
            incorrect_sound.play()

        core.wait(0.5)

# === Compute thresholds ===
thresholds = [np.mean(stair.intensities[-8:]) for stair in staircases]
t_end = trial_clock.getTime()

# === Save data ===
data_dict = {
    'participant': name,
    'inducer_logcontrast': inducer_logcontrast,
    'spatialfrequency': F,
    'temporalfrequency': TF,
    'noisesd': noisesd,
    'testsize': testsize * 2,
    'adaptorsize': adaptorsize * 2,
    'thresholds': thresholds,
    'timetaken_min': (t_end - t_start) / 60
}

#with open(outfile, 'w') as f:
#    json.dump(data_dict, f, indent=2)
#
# === Display summary ===
#print("\n****** Results summary ******")
#print(f"(Noise SD = {noisesd:.3f})")
#print(f"Inphase threshold: {thresholds[0]:.2f}")
#print(f"Antiphase threshold: {thresholds[1]:.2f}")

win.close()
core.quit()
