from psychopy import visual, event
from psychopy.tools.filetools import fromFile, toFile
import time, numpy as np
from scipy.io import loadmat
import os
#myPath = '/Users/zhussain1/Dropbox/Research/Ongoing/leftObjectBias/psychoPyCode/nov2024'
#os.chdir(myPath)

win = visual.Window([1600, 900], allowGUI=True, monitor='detectingMonitor', units='deg', checkTiming=False, color=[0,0,0])
#contrasts=[0.0005, 0.0009, 0.0016, 0.0028, 0.0050] # variance
contrasts=[0.0003 ,   0.0004 ,   0.0008  ,  0.0014 ,   0.0025]
seed = int(time.time() * 1000) 
random_state = np.random.default_rng(seed)
noiseMatrix = random_state.normal(0, np.sqrt(0.01), (256, 256))
textures=loadmat('stimuli/texturesA.mat')
images = textures['images']
texture_list = []
for i in range(10):
    image = images[f'nz{i+1}'][0][0]
    image = image*np.sqrt(1/np.var(image))
    texture_list.append(image) 
    
faces=loadmat('stimuli/facesA.mat')    
images = faces['images']
face_list = []
keys = images.dtype.names
sorted_keys = sorted(keys, key=lambda x: int(x[4:]))  # Extract the numeric part of "stimX" and sort
for key in sorted_keys:
    image = images[key][0][0]
    image = image*np.sqrt(1/np.var(image))
    face_list.append(image)

# Display 5 pairs of images (texture and face) at 5 contrasts
x_start = -8  # Starting x-coordinate for placement
x_spacing = 4  # Spacing between images

while not event.getKeys():  # Continue until a keypress
    for i in range(5):  # Display only 5 images
        xloc = x_start + i * x_spacing

        # Create and scale texture stimulus
        thisTexture = texture_list[1]
        thisTexture = np.sqrt(contrasts[i]) * thisTexture
        noisyTexture=np.clip(noiseMatrix+thisTexture, -1, 1)
        thisTextureStim = visual.ImageStim(
            win, image=noisyTexture, size=3, pos=(xloc, 2), mask=None, interpolate=True,ori=180
        )

        # Create and scale face stimulus
        thisFace = face_list[1]
        thisFace = np.sqrt(contrasts[i]) * thisFace
        noisyFace=np.clip(noiseMatrix+thisFace, -1, 1)
        thisFaceStim = visual.ImageStim(
            win, image=noisyFace, size=3, pos=(xloc, -2), mask=None, interpolate=True, ori=180
        )

        # Draw stimuli
        thisTextureStim.draw()
        thisFaceStim.draw()

    # Flip the window to display everything
    win.flip()

# Close the window after exiting the loop
win.close()