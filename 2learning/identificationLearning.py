from psychopy import core, visual, gui, data, event, sound
from psychopy.tools.filetools import fromFile, toFile
import time, numpy as np
from scipy.io import loadmat
import os
import platform
from psychopy.hardware import keyboard
#myPath = '/Users/zhussain1/Dropbox/Research/Ongoing/leftObjectBias/psychoPyCode/nov2024'
#os.chdir(myPath)
subject = 'cn25' # alphanumeric subject code - experimenter intials followed by two digits (00, 01, etc)
stimSet='A' # A or B, case-sensitive
day=1
stimulus= 'texture' # 'face' or 'texture', case-sensitive
if day ==1:
    nBlocks=4 # 4 blocks day 1, 1 block day 2
else:
    nBlocks=2
#dlg = gui.Dlg(title="Object identification")
#dlg.addField('Subject', 'zh') # 0
#dlg.addField('Stimulus', choices=['Face', 'Texture']) # 1       
#dlg.addField('Set', choices=['A', 'B']) # 2       
#user_input = dlg.show()
#if dlg.OK:
#   print("all good") 
#else:
#    core.quit()  # the user hit cancel so exit
#subject = user_input[0]  
#stimulus = user_input[1]  
#stimSet = user_input[2]
#nBlocks=4
# frameRate = 60

computer='sinistra'
trialsPerCondition=2 # 10 faces x 5 contrasts x 2 reps = 100 trials/block x 4 blocks = 400 trials
stimDuration = 0.3
stimSize=6
isi= 1
fixate1 = 1.5
fixate2 = 0.5
blank = 1
thumbsize = 4
#contrasts=[0.0003, 0.0005, 0.00086, 0.00147, 0.0025] #0.0003, 0.0009, 0.0016, 0.0028, 0.0050  variance
contrasts=[0.0003, 0.0005, 0.00086, 0.00147, 0.0025] #0.0003, 0.0009, 0.0016, 0.0028, 0.0050  variance
nvar=0.01 # noise variance
noiseMean = 0 # noise mean
xcoords=[-12,-6,0,6,12,-12,-6,0,6,12] # coordinates for the face selection screen
ycoords=[6,6,6,6,6,-6,-6,-6,-6,-6]
correctSound = sound.Sound(1800, octave=14, stereo=True, secs=0.05)
incorrectSound = sound.Sound(400, octave=7, stereo=True, secs=0.05)
kb = keyboard.Keyboard()

# make a text file to save data
fileName = subject+'_'+stimulus+'_'+stimSet+'_day'+str(day)
dataFile = open('../../psychopyData/learning2024/'+fileName+'.csv', 'a') 
dataFile.write('computer, block, trial,stimulus,stimID,contrast,stimChosen,correct, rt\n')

# create window and stimuli
if platform.platform()[0:5] == 'Linux': # if we're on Linux, then we're probably using the viewpixx monitor
    monitor = 'viewPixx'
    frameRate=120
    import ctypes
    xlib = ctypes.cdll.LoadLibrary("libX11.so")
    xlib.XInitThreads()
else:
    monitor = 'testMonitor'
    frameRate=60

#win = visual.Window([1600, 900], allowGUI=True, monitor=monitor, units='deg', checkTiming=False, color=[0,0,0])
win = visual.Window(fullscr=True,allowGUI=True, monitor=monitor, units='deg', checkTiming=False, color=[0,0,0])

if stimulus=="texture":
    if stimSet=="A":
        textures=loadmat('stimuli/NoiseStruct1.mat')
    else:
        textures=loadmat('stimuli/NoiseStruct2.mat')
    images = textures['images']
    image_list = []
    for i in range(10):
        image = images[f'nz{i+1}'][0][0]
        image_list.append(image)  
else:
    if stimSet=="A":
        faces=loadmat('stimuli/facesA.mat')
    else:
        faces=loadmat('stimuli/facesB.mat')
    images = faces['images']
    image_list = []
    keys = images.dtype.names
    sorted_keys = sorted(keys, key=lambda x: int(x[4:]))  # Extract the numeric part of "stimX" and sort
    for key in sorted_keys:
        image = images[key][0][0]  # Access the image data
        image_list.append(image)
fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.3, interpolate=True)
fixationCorrect = visual.GratingStim(win, color='green', tex=None, mask='circle', size=0.3, interpolate=True)
fixationIncorrect = visual.GratingStim(win, color='red', tex=None, mask='circle', size=0.3, interpolate=True)
seed = int(time.time() * 1000) 
random_state = np.random.default_rng(seed)
noiseMatrix = random_state.normal(noiseMean, np.sqrt(nvar), (256, 256))
#noiseMatrix = np.clip(noiseMatrix, -1, 1)

thumbnails = []
for i in range(10):
    image_list[i]=image_list[i]*np.sqrt(1/np.var(image_list[i]))
    image_list[i]=image_list[i]-np.mean(image_list[i])
    image_list[i]=image_list[i]-np.mean(image_list[i])
    min_val = image_list[i].min()
    max_val = image_list[i].max()
    # Normalize to -1 to +1
    image_list[i] = 2 * ((image_list[i] - min_val) / (max_val - min_val)) - 1
    thumbnails.append(visual.ImageStim(win, image=image_list[i], pos=(xcoords[i],ycoords[i]),size=thumbsize, ori=180,contrast=1, opacity=1.0, interpolate=True))
faceBuffer = visual.BufferImageStim(win, stim=thumbnails, rect=(-1, 1, 1, -1))

message1 = visual.TextStim(win, pos=[0, +3], text='Hit a key when ready.')
message2 = visual.TextStim(win, pos=[0, -3],wrapWidth=200,
                            text="Click on the item that was presented")
breakMessage = visual.TextStim(win, pos=[0, 0],wrapWidth=200,
                            text="End of block. Press spacebar to continue.")      
endMessage = visual.TextStim(win, pos=[0, 0],wrapWidth=200,
                            text="Done!")      

keys = kb.getKeys()
while not keys:
    message1.draw()
    message2.draw()
    fixation.draw()
    win.flip()
    keys = kb.getKeys()
#event.waitKeys()

blockNumber=0
for blocks in range(nBlocks):
    blockNumber=blockNumber+1
    # setup trial handler
    stimList=[]
    for image in range(10):
        for contrast in contrasts: # variance
            stimList.append({'image': image, 'contrast': contrast})
    trials = data.TrialHandler(stimList, trialsPerCondition)
    trials.data.addDataType('accuracy')
    trials.data.addDataType('RT')
    clockRT = core.Clock() 
    
    # display instructions and wait
    myMouse = event.Mouse() #adding mouse
    #myMouse.setVisible(False) # hide cursor for now
    win.mouseVisible = False
    trialNumber=0
    for thisTrial in trials:
        trialNumber=trialNumber+1
        correctFace=trials.thisTrial.image
        #print(correctFace)
        thisImage=image_list[trials.thisTrial.image]
        thisImage=thisImage*np.sqrt(1/np.var(thisImage))
        thisImage=np.sqrt(trials.thisTrial.contrast) * thisImage
        noisyImage=np.clip(noiseMatrix+thisImage, -1, 1)
    #    print(trials.thisTrial.contrast)
    #    print(np.var(thisImage))
    #    print(np.min(noisyImage))
    #    print(np.max(noisyImage))
        thisStim = visual.ImageStim(win, image=noisyImage, size=stimSize, pos=(0, 0), mask=None, interpolate=True, ori=180)
    
        # fixate 1
        for frameN in range(int(round(fixate1 * frameRate))):
            win.mouseVisible=False
            fixation.draw()
            win.flip()    
            
        # stimulus
        for frameN in range(int(round(stimDuration * frameRate))):
            win.mouseVisible=False
            thisStim.draw()
            win.flip()
    
        # fixate 2
        for frameN in range(int(round(fixate2 * frameRate))):
            win.mouseVisible=False
            fixation.draw()
            win.flip()
        
        # get response
        clickedFace = None
        myMouse.setVisible(True) 
        myMouse.setPos(newPos=(0,0)) 
        myMouse.clickReset() # reset mouse button, including timer (RT will be calculated from now)
        while clickedFace == None:
            keys = kb.getKeys(keyList=['escape','1','0'])
            for thisKey in keys:
                if thisKey.name in ['escape']:core.quit()
            
            faceBuffer.draw()
            fixation.draw()
            win.update()
            buttons, RTs = myMouse.getPressed(getTime=True)
            if buttons[0]:  #left mouse click (0 is left click) (enters only if left mouse clicked)
                clickcoords=myMouse.getPos()
    #            if platform.platform()[0:6] == 'Darwin': # On some versions on Mac (e.g. 2021.2.3), click coordinates in deg of visual angle are twice larger than they should.  
    #                clickcoords = clickcoords/2
    #            print("click at [%.2f,%.2f]"% (clickcoords[0],clickcoords[1]))
                
                for i in range(10): # for each thumbnail face
                    
                    if ( # if the click is within this particular face
                        clickcoords[0]>(xcoords[i]-thumbsize/2) and clickcoords[0]<(xcoords[i]+thumbsize/2) and
                        clickcoords[1]>(ycoords[i]-thumbsize/2) and clickcoords[1]<(ycoords[i]+thumbsize/2) 
                       ):
                        clickedFace = i
                        
                        if clickedFace==correctFace:
                            accuracy=1
                            win.mouseVisible = False
                            correctSound.play()  
                           # blank
                            for frameN in range(int(round(blank * frameRate))):
                                win.mouseVisible=False
                                fixationCorrect.draw()
                                win.flip()
                        else:
                            accuracy=0
                            win.mouseVisible = False
                            incorrectSound.play()
                            for frameN in range(int(round(blank * frameRate))):
                                win.mouseVisible=False
                                fixationIncorrect.draw()
                                win.flip()
        dataFile.write(f"{computer},{blockNumber},{trialNumber},{stimSet},{trials.thisTrial.image+1},{trials.thisTrial.contrast},{clickedFace+1},{accuracy}, {round(RTs[0],2)}\n")
        #dataFile.write('%i\t%s\t%i\t%.6f\t%i\n' % (trialNumber, stimulus, trials.thisTrial.image+1, trials.thisTrial.contrast, accuracy))
     
    if blockNumber<4:
        for frameN in range(int(round(blank * frameRate))):
            breakMessage.draw()
            win.flip()
        
        # check for a keypress
        #event.waitKeys()
        keys = kb.getKeys()
        while not keys:
            keys = kb.getKeys()
                                
# staircase has ended
dataFile.close()
savedFile = fileName + '.txt'

for frameN in range(int(round(5 * frameRate))):
    endMessage.draw()
    win.flip()
