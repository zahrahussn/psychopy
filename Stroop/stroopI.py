from __future__ import absolute_import, division, print_function
from psychopy import visual, event, core, gui, data
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim
from random import shuffle
import string, time
import random, copy, scipy, pygame
import numpy 
from psychopy import sound

params = {'ID number':'1',
	 'frameRate':60,'duration':0.2, 'ISI': 0.02, 'fp': 1, 'task':'stroop_I','computer':'raylan'}

dlg = gui.DlgFromDict(params, title='Stroop_I', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', params)#save params to file for next time
else:
    core.quit()#the user hit cancel so exit
    
fileName = params['ID number']+'_s1'
dataFile = open('/home/zahrahussain/Documents/psychopy/data/stroop/Joint EEG data/'+fileName+'.txt', 'a')#a simple text file with 'comma-separated-values'
dataFile.write('word, response, accuracy, RT\n') 

# Create a visual window:
# win = visual.Window(fullscr=True, allowGUI = True, monitor = 'testMonitor', units = 'deg')
win = visual.Window(fullscr=True, allowGUI = True, monitor = 'attentionExperimentsMonitor', units = 'deg')
win.mouseVisible=False
fixation = visual.PatchStim(win, color=-1, tex=None, mask='circle',size=0.2, units='deg')
corSnd = sound.Sound(2200, octave=14, secs=0.01) # auditory feedback
incorSnd = sound.Sound(800, octave=7, secs=0.01) # auditory feedback

# Create (but not yet display) a square:
SquareVert = [(-.2,-.2),(-.2,.2),(.2,.2),(.2,-.2)]

# setup trial handler

stimList=[]
for word in [1,2,3,4]:
    stimList.append({'word': word})
trials = data.TrialHandler(stimList, 25)

trials.data.addDataType('accuracy')
trials.data.addDataType('RT')
clockRT = core.Clock() 

for thisTrial in trials:
    c = int(trials.thisTrial['word'])-1
    wordList=['red','green','blue','yellow']
    stim = visual.TextStim(win, text=wordList[c], color =(-1,-1,-1)) # create the word stimulus in the given colour 

    # show fixation point for one second
    for frameN in range(int(round(params['fp']*params['frameRate']))):
        fixation.draw()
        win.update()
    
    #show stimulus 
    thisResponse = None
    while thisResponse == None:
        clockRT.reset()
        stim.draw() 
        win.update()

    # collect response

        allKeys = event.waitKeys(keyList=['escape','1','2','3','4'],timeStamped = clockRT)
        for keyTuple in allKeys:
            [thisKey, thisRT] = keyTuple
        for thisKey in allKeys:
            if thisKey[0] in ['escape']:core.quit()
            elif thisKey[0] in ['1','2','3','4']:
                if int(thisKey[0]) == int(trials.thisTrial['word']):
                    thisResponse=1
                    accuracy = 1
                    corSnd.play()
                else: 
                    thisResponse=1
                    accuracy = 0
                    incorSnd.play()
            trials.data.add('accuracy', accuracy)
    

    trials.addData('RT', thisRT)
    event.clearEvents()
    dataFile.write('%s %s %s %s \n' %(wordList[c], thisKey[0],  accuracy, round(thisRT,2)))
    


win.close()
core.quit()
