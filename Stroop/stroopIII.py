from __future__ import absolute_import, division, print_function
from psychopy import visual, event, core, gui, data
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim
from random import shuffle
import string, time
import random, copy, scipy, pygame
import numpy 
from psychopy import prefs
from psychopy import sound

params = {'ID number':'1',
	 'frameRate':60,'duration':0.2, 'ISI': 0.02, 'fp': 1,'task':'Stroop_III', 'computer':'raylan'}

dlg = gui.DlgFromDict(params, title='Stroop_Task', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', params)#save params to file for next time
else:
    core.quit()#the user hit cancel so exit
    
fileName = params['ID number']+'_s3'+'_'+params['_computer']
dataFile = open('/home/zahrahussain/Documents/psychopy/data/stroop/Joint EEG data/'+fileName+'.txt', 'a')#a simple text fil e with 'comma-separated-values'
dataFile.write('congruency, colour, word, accuracy, RT\n') 

# Create a visual window:
# win = visual.Window(fullscr=True, allowGUI = True, monitor = 'testMonitor', units = 'deg')
win = visual.Window(fullscr=True, allowGUI = True, monitor = 'attentionExperimentsMonitor', units = 'deg')
win.mouseVisible=False
fixation = visual.PatchStim(win, color=1, tex=None, mask='circle',size=0.2, units='deg')
corSnd = sound.Sound(2200, octave=14, secs=0.01) # auditory feedback
incorSnd = sound.Sound(800, octave=7, secs=0.01) # auditory feedback
colours=['red','green','blue','yellow']

# setup trial handler
stimList=[]
for color in [1,2,3,4]:
        for con in [1,0]:
            stimList.append({'color': color, 'con': con})
trials = data.TrialHandler(stimList, 25)
trials.data.addDataType('accuracy')
trials.data.addDataType('RT')
clockRT = core.Clock() 

for thisTrial in trials:
    wordList=['red','green','blue','yellow'] # define the word list 
    colourRGB=[(1,-0.25,-0.25), (-0.25,1,-0.25), (-0.5,-0.5,1),(0.75,0.75,0) ] # set the colour values: RGBY 
    col=int(trials.thisTrial['color'])-1 # set the trial type to an integer between 0-3 to correctly index the above lists (else 1-4)
    
    if trials.thisTrial['con']==1: # if congruent trial
        word=wordList[col] # choose matching colour word from word list
    elif trials.thisTrial['con']==0: # if incongruent trial
        del(wordList[col]) # delete the congruent color word from the word list
        word=wordList[numpy.random.random_integers(0,2)] # randomly select another word from the new list
        
    stim = visual.TextStim(win, text=word, color =colourRGB[col]) # create the word stimulus in the given colour 

    # show fixation point for one second
    for frameN in range(int(round(params['fp']*params['frameRate']))):
        fixation.draw()
        win.update()

    # show word for 200 ms
    for frameN in range(int(round(params['duration']*params['frameRate']))):
        stim.draw() 
        win.update()
    
    # show blank screen for 200 ms
    for frameN in range(int(round(params['ISI']*params['frameRate']))):
        win.update()
            
    clockRT.reset()
    # collect response
    thisResponse = None
    while thisResponse == None:
        allKeys = event.waitKeys(timeStamped = clockRT)
        for keyTuple in allKeys:
            [thisKey, thisRT] = keyTuple
        for thisKey in allKeys:
            if thisKey in ['escape']:core.quit()
            elif int(thisKey[0]) == int(trials.thisTrial['color']):
                thisResponse=1
                accuracy = 1
                corSnd.play()
            else: 
                thisResponse=1
                accuracy = 0
                incorSnd.play()

    trials.addData('accuracy', accuracy)        
    trials.addData('RT', thisRT)
    event.clearEvents()
    dataFile.write('%s %s %s %s %s\n' %(trials.thisTrial['con'], colours[col], word, accuracy, round(thisRT,2)))

win.close()
core.quit()


