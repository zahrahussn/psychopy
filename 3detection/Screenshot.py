from psychopy import core, visual, event
import numpy as np
from scipy.ndimage import rotate
from scipy.io import loadmat
from psychopy.hardware import keyboard

# set up the window
win = visual.Window([1000, 800], allowGUI=True, monitor='testMonitor', units='deg', checkTiming=False)

# parameters
frameRate = 120
stimDuration = 0.2
noiseSd = np.sqrt(0.1)
noiseMean = 0

# grating
array = np.linspace(0, 1, 256)
grating = np.sin(1 * np.pi * 4 * array)  # sine wave
clearGrating = np.tile(grating, (256, 1)) * 0.5

# texture
textures = loadmat('/home/zahra/Documents/psychopy/3detection/theTextures.mat')
clearTexture = textures['theStimulus4']['stim2'][0][0] * 0.5

# noise
random_state = np.random.default_rng(12345)  # fixed seed for reproducibility
noiseMatrix = random_state.normal(noiseMean, noiseSd, (256, 256))
noiseMatrix = np.clip(noiseMatrix, -1, 1)

# grating embedded in noise
gratingInNoise = noiseMatrix + clearGrating
gratingInNoise = np.clip(gratingInNoise, -1, 1) * 0.3

# texture embedded in noise
textureInNoise = noiseMatrix + clearTexture
textureInNoise = np.clip(textureInNoise, -1, 1) * 0.3

stimuli = [
    visual.ImageStim(win, image=clearGrating, size=4, interpolate=False),
    visual.ImageStim(win, image=clearTexture, size=4, interpolate=False),
    visual.ImageStim(win, image=noiseMatrix, size=4, interpolate=False),
    visual.ImageStim(win, image=gratingInNoise, size=4, interpolate=False),
    visual.ImageStim(win, image=textureInNoise, size=4, interpolate=False),
]

instructions = visual.TextStim(win, text="press space to view the next stimulus, esc to exit.",
                               pos=(0, -5), wrapWidth=20)

kb = keyboard.Keyboard()

for stim in stimuli:
    stim.draw()
    instructions.draw()
    win.flip()
    keys = kb.waitKeys(keyList=['space', 'escape'])
    if 'escape' in keys:
        break

win.close()
core.quit()
