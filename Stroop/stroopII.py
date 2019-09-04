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
	 'frameRate':60,'duration':0.2, 'ISI': 0.02, 'fp': 1,'task':'Stroop_II', 'computer':'raylan'}

dlg = gui.DlgFromDict(params, title='Stroop_II', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', params)#save params to file for next time
else:
    core.quit()#the user hit cancel so exit
    
fileName = params['ID number']+'_s2'+'_'+params['computer']
dataFile = open('/home/zahrahussain/Documents/psychopy/data/stroop/Joint EEG data/'+fileName+'.txt', 'a')#a simple text file with 'comma-separated-values'
dataFile.write('colors, response, accuracy, RT\n') 

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
colourList=['red','green','blue','yellow']
stimList=[]
for color in [1,2,3,4]:
    stimList.append({'color': color})
trials = data.TrialHandler(stimList, 25)

trials.data.addDataType('accuracy')
trials.data.addDataType('RT')
clockRT = core.Clock() 

for thisTrial in trials:
    c = int(trials.thisTrial['color'])-1
    colour=colourList[c]
    square = ShapeStim(win, vertices=SquareVert, fillColor=colour, lineWidth=0, size=5, pos=(0,0))

    # show fixation point for one second
    for frameN in range(int(round(params['fp']*params['frameRate']))):
        fixation.draw()
        win.update()

    # show arrow for 200 ms
    for frameN in range(int(round(params['duration']*params['frameRate']))):
        square.draw() 
        win.update()
    
    # show blank screen for 500 ms
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
            if thisKey[0] in ['escape']:core.quit()
            elif thisKey[0] in ['1','2','3','4']:
                if int(thisKey[0]) == int(trials.thisTrial['color']):
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
    dataFile.write('%s %s %s %s \n' %(trials.thisTrial['color'], thisKey[0], accuracy, round(thisRT,2)))
    


win.close()
core.quit()
