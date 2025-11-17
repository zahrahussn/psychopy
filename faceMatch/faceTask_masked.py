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
trialsPerCondition = 10

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
 
fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.2)
frameFeedback = visual.ShapeStim(win, color='green',lineWidth=1.5, vertices=((0, 0), (0, 0), (0, 0)))

#Feedback sounds 
corSnd = sound.Sound(1800, octave=14, stereo=True, secs=0.05)
incorSnd = sound.Sound(700, octave=7, stereo=True, secs=0.05)

facePath='Stimuli/' #Retrieve faces stimuli from the Stimuli folder with their respective numbers, 5 male 5 female
imageNames=['face1', 'face2', 'face3', 'face4', 'face5', 'face6', 'face7', 'face8', 'face9', 'face10'] 

# Make face stimulus
faceWidth=4.2
faceHeight=4.2
faceSize=(faceWidth,faceHeight)
facePos=(0,0)
faceStimulus= visual.ImageStim(win,size=faceSize) # create face stimulus without specifying the image or position
   
#Gaussian noise mask
noiseTexture = numpy.random.rand(128, 128) * 2.0 - 1
# Dimensions for partial masks
half_height = faceHeight / 2.0
upper_center_y = facePos[1] + (faceHeight / 4.0)
lower_center_y = facePos[1] - (faceHeight / 4.0)

maskUpper = visual.GratingStim(win, tex=noiseTexture, size=(faceWidth, half_height), pos=(facePos[0], upper_center_y), units='deg', interpolate=False, autoLog=False)
maskLower = visual.GratingStim(win, tex=noiseTexture, size=(faceWidth, half_height), pos=(facePos[0], lower_center_y), units='deg', interpolate=False, autoLog=False)
zeroMask = None

# prepare face choice screen
faceWidthChoice=3
faceHeightChoice=3
faceSizeChoice=(faceWidthChoice,faceHeightChoice) 
xcoords=[-10,-5,0,5,10,-10,-5,0,5,10] # coordinates for the face selection screen
ycoords=[5,5,5,5,5,-5,-5,-5,-5,-5] 

faceStimuluslist=[]
for i in range(10):
    faceStimuluslist.append(visual.ImageStim(win, image=facePath+imageNames[i]+'.jpg', pos=(xcoords[i],ycoords[i]),size=faceSizeChoice))

faceBuffer = visual.BufferImageStim(win, stim=faceStimuluslist, rect=(-1, 1, 1, -1))

# Trial Handler 
stimList=[]
for image in range (0,len(imageNames)):    
    for mask in ['upper','lower', 'none']:
        stimList.append({'mask':mask, 'image':image}) 
trials = data.TrialHandler(stimList, trialsPerCondition) 

myMouse = event.Mouse() 
myMouse.setVisible(False) # hide cursor for now

# show face choice screen until space bar is pressed
msg = visual.TextStim(win, text='Press the space bar to begin')
keyPress = ['']
while 'space' not in keyPress:
    faceBuffer.draw()
    msg.draw()
    win.flip()
    keyPress = event.waitKeys()

trial = 0
for thisTrial in trials: 
    trial=trial+1 
    
    myMouse.setPos((0,0)) # recenter mouse cursor
    myMouse.buttons = [0, 0, 0]  # manually clear pressed state
    thisFace=imageNames[trials.thisTrial.image]
    correctFace=trials.thisTrial.image
    faceStimulus.image = facePath+thisFace+'.jpg'

    # set the mask
    if trials.thisTrial.mask=='upper': #  eyes masked
        mask=maskUpper
    elif trials.thisTrial.mask=='lower': # mouth masked
        mask=maskLower
    else:
        mask=zeroMask
        
    # present the stimuli. First fixation screen, then face presentation, then selection screen.  
    for frameN in range(int(round(fpduration*frameRate))): #drawing fixation screen for 1s
        fixation.draw()
        win.update()
    
    for frameN in range(int(round(stimulusduration*frameRate))): #drawing face presentation for 0.3s
        faceStimulus.draw()
        if mask is not None:
            mask.draw()
        win.update()
    
    for frameN in range(int(round(blankduration*frameRate))): #blank screen for 0.2 s blankdurationmL
        win.update()
    
    keys = event.getKeys(keyList=['escape', 'left', 'right'])
    if 'escape' in keys:
        core.quit()
    
    myMouse.setVisible(True)  # show mouse cursor
    myMouse.clickReset() # reset mouse button, including timer (RT will be calculated from now)
    clickedFace = None
    while clickedFace is None:
        faceBuffer.draw()
        fixation.draw()
        win.flip()
    
        buttons, RTs = myMouse.getPressed(getTime=True)
        if buttons[0]:  #left mouse click (0 is left click) (enters only if left mouse clicked)
            clickcoords=myMouse.getPos()
            myMouse.setVisible(False)  # hide mouse cursor
    
            # check which face was clicked
            for i in range(10):
                if (xcoords[i] - faceWidthChoice/2 < clickcoords[0] < xcoords[i] + faceWidthChoice/2 and
                    ycoords[i] - faceHeightChoice/2 < clickcoords[1] < ycoords[i] + faceHeightChoice/2):
                    
                    # clickedFace is the index of the face the participant clicked
                    faceX = clickcoords[0]
                    faceY = clickcoords[1]
                    
                    halfWidth = faceWidthChoice / 2
                    halfHeight = faceHeightChoice / 2
                    
                    # vertices: bottom-left, bottom-right, top-right, top-left
                    vertices = (
                        (faceX - halfWidth, faceY - halfHeight),
                        (faceX + halfWidth, faceY - halfHeight),
                        (faceX + halfWidth, faceY + halfHeight),
                        (faceX - halfWidth, faceY + halfHeight)
                    )                   
                        
                    clickedFace = i
                    # accuracy & feedback
                    if clickedFace == correctFace:
                        accuracy = 1
                        frameColor = 'green' if accuracy == 1 else 'red'
                        frameFeedback = visual.ShapeStim(win, vertices=vertices, lineColor=frameColor, lineWidth=2.0, fillColor=None) 
                        corSnd.play()
                        for frameN in range(int(round(feedback * frameRate))):
                            frameFeedback.draw()
                            win.flip()
                    else:
                        accuracy = 0
                        frameColor = 'green' if accuracy == 1 else 'red'
                        frameFeedback = visual.ShapeStim(win, vertices=vertices, lineColor=frameColor, lineWidth=2.0, fillColor=None) 
                        incorSnd.play()
                        for frameN in range(int(round(feedback * frameRate))):
                            frameFeedback.draw()
                            win.flip()
    
                    clickedImage = imageNames[clickedFace] 
                    with open(dataFileName + '.csv', 'a', newline='') as dataFile:
                        writer = csv.writer(dataFile)
                        writer.writerow([
                            trial,
                            trials.thisTrial['image']+1,
                            trials.thisTrial['mask'],
                            clickedImage,
                            accuracy,
                            round(RTs[0],2),
                            f"{stimulusduration} s"
                        ])
    
                    myMouse.setVisible(False)
                    break  # stop checking other faces after a click
win.close()
core.quit()
