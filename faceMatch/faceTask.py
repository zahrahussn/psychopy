from __future__ import absolute_import, division, print_function
from psychopy import visual, event, core, gui, data, sound
from psychopy.tools.filetools import fromFile, toFile
from random import shuffle, random #added this to track clicks
import random, copy, scipy, numpy
import os, shutil
import string, time
import platform

#variable=''
params = {'ID number':'1','Number of distractors':0,'Number of trials per condition':8}

dlg = gui.DlgFromDict(params, title='Face Match', fixed=['dateStr'])
if dlg.OK == False:
    core.quit()#the user hit cancel so exit

if platform.platform()[0:5] == 'Linux': # if we're on Linux, then we're probably using the viewpixx monitor
    monitor = 'viewPixx'
    params['frameRate']=120
    print('hello')
else:
    monitor = 'testMonitor'
    params['frameRate']=60
params['fpduration']=1.0
params['stimulusduration']=0.150

params['maskduration']=0.1
params['blankduration']=0.2

#stimulusduration='0.1'

if params['Number of distractors'] == 0:
    dataFileName = 'data/FaceMatch'+params['ID number']+'_NoDistractor' #Accessing data file to record data
else:
    dataFileName = 'data/FaceMatch'+params['ID number']+'_WithDistractor'
if os.path.exists(dataFileName+'.csv'): # if datafile already exist, append a number
    ii=2
    while True:
        new_name = dataFileName + "_" + str(ii)
        if not os.path.exists(new_name+'.csv'):
            dataFileName = new_name
            break 
        ii += 1
with open(dataFileName+'.csv', 'a') as dataFile:
    if params['Number of distractors'] == 0:
        dataFile.write('nTrials\t faceID\t visfield\t response\t accuracy\t RT\t stimDuration\n')#Data file without distractor
    else:
        dataFile.write('nTrials\t faceID\t visfield\t distractorID\t response\t accuracy\t RT\t stimDuration\n')   #Data file with distractor

win = visual.Window(fullscr=True, allowGUI= True, monitor = monitor, units = 'deg')

# fixation cross
fixation = visual.PatchStim(win, color=-1, tex=None, mask='cross',size=0.5 ,units='deg')
#win means in window, color is black, no text, mask is cross, size is 1.0, units in degrees,

#Feedback sounds 
corSnd = sound.Sound(1800, octave=14, secs=0.01) 
incorSnd = sound.Sound(700, octave=7, secs=0.01)

facePath='Stimuli/' #Retrieve faces stimuli from the Stimuli folder with their respective numbers, 5 male 5 female
imageM=['M1','M2','M3','M4','M5']
imageF=['F1','F2','F3','F4','F5']

# Make face stimulus
faceWidth=4.2
faceHeight=4.2
faceSize=(faceWidth,faceHeight)
posLVF=((-2.5-faceWidth/2),0)
posRVF=((2.5+faceWidth/2),0)
faceStimulus= visual.ImageStim(win,size=faceSize) # create face stimulus without specifying the image or position

if params['Number of distractors'] > 0:
    distPath='Distractor/' #Retrieving distractors from Distractor folder with their respective numbers
    imageDist=['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10']
    distStimulus = visual.ImageStim(win, size=faceSize)
    
    #Draws a rectangular cue for face presentation
    cueVertices = [(-faceWidth/2,-faceHeight/2),(-faceWidth/2,faceHeight/2),(faceWidth/2,faceHeight/2),(faceWidth/2,-faceHeight/2)]
    cue = visual.ShapeStim(win, vertices=cueVertices, units='deg',lineColor='red', fillColor=None, lineWidth=3)
    
#Gaussian noise mask
noiseTexture = numpy.random.rand(128, 128) * 2.0 - 1
maskRight = visual.GratingStim(win, tex=noiseTexture, size=faceSize, pos=posRVF, units='deg', interpolate=False, autoLog=False)
maskLeft= visual.GratingStim(win, tex=noiseTexture, size=faceSize, pos=posLVF, units='deg', interpolate=False, autoLog=False)

# prepare face choice screen
faceWidthChoice=3
faceHeightChoice=3
faceSizeChoice=(faceWidthChoice,faceHeightChoice) 
xcoords=[-10,-5,0,5,10,-10,-5,0,5,10] #adding coordinates for the face selection screen. 10 elements each list.
ycoords=[5,5,5,5,5,-5,-5,-5,-5,-5] 

faceStimuluslist=[]
for i in range(10):
    if i<5:
        faceStimuluslist.append(visual.ImageStim(win, image=facePath+imageM[i]+'.jpg', pos=(xcoords[i],ycoords[i]),size=faceSizeChoice))
    else:
        faceStimuluslist.append(visual.ImageStim(win, image=facePath+imageF[i-5]+'.jpg', pos=(xcoords[i],ycoords[i]),size=faceSizeChoice))

faceBuffer = visual.BufferImageStim(win, stim=faceStimuluslist, rect=(-1, 1, 1, -1))


#Trial Handler randomizes and puts things in sequence the way you want them to be
stimList=[]
for image in range (0,len(imageM)):    #len is length. images picked from 0 to len(imageM) so basically up to 5 random images.
    for field in [0,1]: 
        for gender in [0,1]: 
            stimList.append({'gender':gender, 'field':field, 'image':image}) # setting trial sequence,gender for gender, field for visual field, images of course
trials = data.TrialHandler(stimList, params['Number of trials per condition']) 

myMouse = event.Mouse() #adding mouse
myMouse.setVisible(False) # hide cursor for now

for key in ['escape']: #press escape to quit the experiment whenever
    event.globalKeys.add(key, func=core.quit)\

# show face choice screen until space bar is pressed
msg = visual.TextStim(win, text='Press the space bar to begin')
keyPress = ['']
while keyPress[0] not in ['space']:
    faceBuffer.draw()
    msg.draw()
    win.flip()
    keyPress = event.waitKeys()

nTrials = 0
for thisTrial in trials: #Records the trials that are happening with this particular experiment. Put it after trial handler
    nTrials=nTrials+1 #Count which trial we're on
    
    # prepare face screen
    if trials.thisTrial.gender==1:  #face is male
        image=imageM[trials.thisTrial.image] #trials.thisTrial.image is 5 items spanning from 0 to 4 
        correctFace=trials.thisTrial.image #correct presented face from 0-1-2-3-4 for males
    else: # if female face
        image=imageF[trials.thisTrial.image]
        correctFace=trials.thisTrial.image+5 #+5 to consider females in the equation 5-6-7-8-9
    # set the image(s)
    faceStimulus.image = facePath+image+'.jpg'
    if params['Number of distractors'] > 0:
        distractor = numpy.random.random_integers(0,len(imageDist)-1) #to randomly select one one distractor face
        distStimulus.image = distPath+imageDist[distractor]+'.jpg'
    # set the locations
    if trials.thisTrial.field==1: #  LVF trial 
        faceStimulus.pos=posLVF 
        visfield='L'
        mask=maskLeft
        if params['Number of distractors'] > 0:
            cue.pos = posLVF
            distStimulus.pos = posRVF
            distMask = maskRight
    else: # RVF 
        faceStimulus.pos=posRVF
        visfield='R'
        mask=maskRight
        if params['Number of distractors'] > 0:
            cue.pos = posRVF
            distStimulus.pos = posLVF
            distMask = maskLeft
    
    # present the stimuli. First fixation screen, then face presentation, then selection screen.
    
    for frameN in range(int(round(params['fpduration']*params['frameRate']))): #drawing fixation screen for 0.2s
        fixation.draw()
        win.update()
    
    for frameN in range(int(round(params['stimulusduration']*params['frameRate']))): #drawing face presentation for 0.3s
        fixation.draw()
        faceStimulus.draw()
        if params['Number of distractors'] > 0:
            distStimulus.draw()
            cue.draw()
        win.update()
    
    for frameN in range(int(round(params['maskduration']*params['frameRate']))): #mask screen for 0.1s
        fixation.draw()
        mask.draw()
        if params['Number of distractors'] > 0:
            distMask.draw()
        win.update()
        
    for frameN in range(int(round(params['blankduration']*params['frameRate']))): #blank screen for 0.2 s blankdurationmL
        win.update()
        
    clickedFace = None
    myMouse.setVisible(True) # show mouse cursor
    myMouse.setPos(newPos=(0,0)) # recenter mouse cursor
    myMouse.clickReset() # reset mouse button, including timer (RT will be calculated from now)
    while clickedFace == None:
        faceBuffer.draw()
        fixation.draw()
        win.update()
        buttons, RTs = myMouse.getPressed(getTime=True)
        if buttons[0]:  #left mouse click (0 is left click) (enters only if left mouse clicked)
            clickcoords=myMouse.getPos()
            if platform.platform()[0:6] == 'Darwin': # On some versions on Mac (e.g. 2021.2.3), click coordinates in deg of visual angle are twice larger than they should.  
                clickcoords = clickcoords/2
#            print("click at [%.2f,%.2f]"% (clickcoords[0],clickcoords[1]))
            
            for i in range(10): # for each thumbnail face
                
                if ( # if the click is within this particular face
                    clickcoords[0]>(xcoords[i]-faceWidthChoice/2) and clickcoords[0]<(xcoords[i]+faceWidthChoice/2) and
                    clickcoords[1]>(ycoords[i]-faceHeightChoice/2) and clickcoords[1]<(ycoords[i]+faceHeightChoice/2) 
                   ):
                    clickedFace = i
                    
                    if clickedFace==correctFace:
                        accuracy=1
                        corSnd.play()
                    else:
                        accuracy=0
                        incorSnd.play()
                    
                    if clickedFace<5:  #face is male
                        clickedImage = imageM[clickedFace]
                    else:
                        clickedImage = imageF[clickedFace - 5]
                    with open(dataFileName+'.csv', 'a') as dataFile:
                        if params['Number of distractors'] == 0:
                            dataFile.write('%d\t%s\t%s\t%s\t%d\t%f\t0.15 s\n' %(nTrials, image, visfield, clickedImage, accuracy, RTs[0]))
                        else:
                            dataFile.write('%d\t%s\t%s\t%s\t%s\t%d\t%f\t0.15 s\n' %(nTrials, image, visfield, imageDist[distractor], clickedImage, accuracy, RTs[0],))
                    
                    myMouse.setVisible(False) # hide cursor

win.close()
core.quit()
