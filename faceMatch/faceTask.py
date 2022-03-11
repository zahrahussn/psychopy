from __future__ import absolute_import, division, print_function
from psychopy import visual, event, core, gui, data, sound
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim
from random import shuffle, random #added this to track clicks
import random, copy, scipy, numpy
import os, shutil
import string, time

variable=''
params = {'ID number':'1', 'lang':'eng',
	 'frameRate':60,'duration':0.2,'maskduration':0.1,'blankduration':0.2,'response': 1.0, 'fp': 1.0,'task':'FaceMatch'}

dlg = gui.DlgFromDict(params, title='Face Match v1', fixed=['dateStr'])
if dlg.OK:
    1+1 #toFile('lastParams.pickle', params) #save params to file for next time
else:
    core.quit()#the user hit cancel so exit

fileName = 'data/FaceMatch'+params['ID number']+'_FaceMatchV1'     #Accessing data file to record data
dataFile = open(fileName+'.txt', 'a')
dataFile.write('nTrials, imagefileName, visfield,  Response, accuracy, RT\n')   #Data file listing #Is this enough to create a data file?
#if os.path.exists(fileName+'.txt')
#    ii=1
#    while True:
#    new_name = fileName + "_" + str(ii) + '.txt'
#    if not os.path.exists(new_name):
#       fileName = new_name
#       break 
#    ii += 1

win = visual.Window(fullscr=True, allowGUI= True, monitor = 'viewPixx', units = 'deg')
#Graphic User Interface True
win.mouseVisible=True #mouse is visible

fixation = visual.PatchStim(win, color=-1, tex=None, mask='cross',size=0.5 ,units='deg')
#win means in window, color is black, no text, mask is cross, size is 1.0, units in degrees,

#Feedback sounds 
corSnd = sound.Sound(1800, octave=14, secs=0.01) 
incorSnd = sound.Sound(700, octave=7, secs=0.01)

facePath='Stimuli/' #Retrieve faces stimuli from the Stimuli folder with their respective numbers, 5 male 5 female
imageM=[os.path.join(facePath+'M1'),os.path.join(facePath+'M2'),os.path.join(facePath+'M3'),os.path.join(facePath+'M4'),os.path.join(facePath+'M5')]
imageF=[os.path.join(facePath+'F1'),os.path.join(facePath+'F2'),os.path.join(facePath+'F3'),os.path.join(facePath+'F4'),os.path.join(facePath+'F5')]

faceWidth=4.2
faceHeight=4.2
faceSize=(faceWidth,faceHeight)
posLVF=((-2.5-faceWidth/2),0)      
posRVF=((2.5+faceWidth/2),0)

#Gaussian noise mask

noiseTexture = numpy.random.rand(128, 128) * 2.0 - 1
maskRight = visual.GratingStim(win, tex=noiseTexture, size=(6.5,6.5),pos=posRVF, units='deg', interpolate=False, autoLog=False)
maskLeft= visual.GratingStim(win, tex=noiseTexture,size=(6.5, 6.5), pos=posLVF, units='deg', interpolate=False, autoLog=False)


#Trial Handler randomizes and puts things in sequence the way you want them to be
stimList=[]
for image in range (0,len(imageM)):    #len is length. images picked from 0 to len(imageM) so basically up to 5 random images.
    for field in [0,1]: 
        for gender in [0,1]: 
            stimList.append({'gender':gender, 'field':field, 'image':image}) # setting trial sequence,gender for gender, field for visual field, images of course
trials = data.TrialHandler(stimList, 1) #Changed because she needs 100 trials. 5x20 is 100
trials.data.addDataType('RT')
trials.data.addDataType('response') #no need for repetition time if we already specified (ask)
trials.data.addDataType('accuracy')    #Do we add this here?
clockRT = core.Clock()  #Records reaction time

RTs=''
accuracy=''
response=''

nTrials=0

myMouse = event.Mouse() #adding mouse. Mouse coordinates are doubled for reasons we do not know. 
myMouse.clickReset() #resets at left click

for key in ['escape']: #press escape to quit the experiment whenever
    event.globalKeys.add(key, func=core.quit)

nTrials = 0
for thisTrial in trials: #Records the trials that are happening with this particular experiment. Put it after trial handler
    nTrials=nTrials+1 #Count which trial we're on
    # prepare face screen
    if trials.thisTrial.gender==1:  #face is male
        IM='M'
        imagefileName=imageM[trials.thisTrial.image]+'.jpg' #trials.thisTrial.image is 5 items spanning from 0 to 4 
        correctFace=trials.thisTrial.image #correct presented face from 0-1-2-3-4 for males
    else: # if female face
        IM='F'
        imagefileName=imageF[trials.thisTrial.image]+'.jpg'
        correctFace=trials.thisTrial.image+5 #+5 to consider females in the equation 5-6-7-8-9

    if trials.thisTrial.field==1: #  LVF trial 
        position=posLVF 
        visfield='L'
        IM_location='LVF' #IM is basically images all
        mask=maskLeft
    else: # RVF 
        position=posRVF
        visfield='R'
        IM_location='RVF'
        mask=maskRight

    faceStimulus= visual.ImageStim(win, image=imagefileName, pos=position,size=faceSize) #Inserts the picture into the window file, posLVF is the position, size is defined already
    
    # prepare face choice screen
    # randomize the positions
    # facestimulus 1 specify then add draw. 10 different images so 10 different lines. 
    xcords=[-10,-5,0,5,10,-10,-5,0,5,10] #adding coordinates for the face selection screen. 10 elements each list.
    ycords=[5,5,5,5,5,-5,-5,-5,-5,-5] 
    
    faceWidthChoice=3
    faceHeightChoice=3
    faceSizeChoice=(faceWidthChoice,faceHeightChoice) 
    
    faceStimuluslist=[]
    
    for i in range(10):
        if i<5:
            faceStimuluslist.append(visual.ImageStim(win, image=imageM[i]+'.jpg', pos=(xcords[i],ycords[i]),size=faceSizeChoice))
        else:
            faceStimuluslist.append(visual.ImageStim(win, image=imageF[i-5]+'.jpg', pos=(xcords[i],ycords[i]),size=faceSizeChoice))
    
    faceBuffer = visual.BufferImageStim(win, stim=faceStimuluslist, rect=(-1, 1, 1, -1))
    
    # present the stimuli. First fixation screen, then face presentation, then selection screen.
    
    for frameN in range(int(round(params['fp']*params['frameRate']))):  #drawing fixation screen for 0.2s
        fixation.draw()
        win.update()
    
    for frameN in range(int(round(params['duration']*params['frameRate']))): #drawing face presentation for 0.3s
        fixation.draw()
        faceStimulus.draw()
        win.update()
    
    for frameN in range(int(round(params['maskduration']*params['frameRate']))): #mask screen for 0.1s
        fixation.draw()
        mask.draw()
        win.update()
        
    for frameN in range(int(round(params['blankduration']*params['frameRate']))): #blank screen for 0.2 s blankdurationmL
        win.update()
        
    thisResponse = None
#    clockRT.reset()
    
    minimumdistance=10000
    myMouse.clickReset()

    while thisResponse == None:                
        faceBuffer.draw()
        fixation.draw()  
        win.update()
        buttons, RTs = myMouse.getPressed(getTime=True)
        if buttons[0]:  #left mouse click (0 is left click) (enters only if left mouse clicked)
            clickcoords=(myMouse.getPos()/2) #Again, we don't understand the reason behind coordinates doubling. Used this as a solution. This is specific for the version 2021.2.3.  
#            print("click at [%.2f,%.2f]"% (myMouse.getPos()[0],myMouse.getPos()[1]))
            thisResponse=1
            minimumdistance=10000 #Defining minimum distance variable for upcoming for loop 
            
            for i in range(10):
                distanceFaceClick=(((xcords[i]-clickcoords[0])**2)+((ycords[i]-clickcoords[1]))**2)
                
                if distanceFaceClick<minimumdistance:
                    clickedFace = i
                    response = clickedFace
                    minimumdistance=distanceFaceClick
            if clickedFace==correctFace:
                accuracy=1
                corSnd.play()
            else:
                accuracy=0
                incorSnd.play()
    dataFile.write('%d\t%s\t%s\t%s\t%s\t%s\n' %(nTrials, imagefileName, visfield, response, accuracy, RTs[0]))

event.clearEvents()

win.close()
core.quit()