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
	 'frameRate':60,'duration':0.3, 'ISI1': 0.2, 'ISI2': 0.5,'fp': 0.5,'task':'wordComposite', 'computer':'raylan'}

dlg = gui.DlgFromDict(params, title='wordComposite', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', params) #save params to file for next time
else:
    core.quit()#the user hit cancel so exit

fileName = params['ID number']+'_alignedEng'+'_'+params['_computer']
dataFile = open('/home/zahrahussain/Documents/psychopy/data/wordComposite/'+fileName+'.txt', 'a')#a simple text file with 'comma-separated-values'
dataFile.write('word, same, congruent, response, accuracy, RT\n') 

# Create a visual window:
#win = visual.Window(fullscr=True, allowGUI = True, monitor = 'testMonitor', units = 'deg')
win = visual.Window(fullscr=True, allowGUI = True, monitor = 'attentionExperimentsMonitor', units = 'deg')
win.mouseVisible=False
fixation = visual.PatchStim(win, color=-1, tex=None, mask='circle',size=0.2, units='deg')
mask=visual.RadialStim(win, tex='sqrXsqr',color=1, size=4,
    visibleWedge=[0, 360], radialCycles=4, angularCycles=8, interpolate=False,
    autoLog=False) 
corSnd = sound.Sound(2200, octave=14, secs=0.01) # auditory feedback
incorSnd = sound.Sound(800, octave=7, secs=0.01) # auditory feedback

stimSize=2 #size of the text 
textFont='Courier'
wordlist1=['basket', 'reward', 'coffin', 'active', 'bonbon', 'couple', 'legend', 'revive', 'middle', 'divide']
wordlist2=['basics','rewind','coffee','actors','bonnet', 'coupon', 'legion', 'revoke', 'midget', 'divine']
wordlist3=['marble','cowboy','muffle','nature','career', 'temper', 'attack', 'motion', 'cancer', 'resume']
wordlist4=['market','coward','muffin','native','carbon', 'temple', 'attend', 'motive', 'candle', 'reside']

line=visual.Line(win, start=(0,2),end=(0,-3),lineColor=[-1,-1,-1]) #to draw a vertical line separating the word-halves

# setup trial handler
stimList=[]
for word in range(0,10): #This will yield 10 words NOT 11.
    for top in [1,0]: # same different
        for cong in [1,0]: # congruent incongruent
            stimList.append({'top': top, 'cong':cong, 'word':word}) # setting trial sequence
trials = data.TrialHandler(stimList, 5)
trials.data.addDataType('accuracy')
trials.data.addDataType('RT')
clockRT = core.Clock() 


for thisTrial in trials:
    if trials.thisTrial.top==1: # if 'same' top/aligned trial
        corresp=1 # correct response = 1
        if trials.thisTrial.cong==1: # if same-congruent/aligned trial
                stim_wordleft= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
                stim_wordright= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
        else: # if same-incongruent/aligned trial
                stim_wordleft= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
                stim_wordright= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
    else: # if 'different' top/aligned trial
        corresp=2 
        if trials.thisTrial.cong==1: # if different-congruent/aligned trial
            stim_wordleft= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
            stim_wordright= visual.TextStim(win,font=textFont, text=wordlist3[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
        else: # if different-incongruent/aligned trial
            stim_wordleft= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
            stim_wordright= visual.TextStim(win,font=textFont, text=wordlist4[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg') 

    # show blank screen for 500 ms
    for frameN in range(int(round(params['ISI2']*params['frameRate']))):
        win.update()
    # show fixation point for one second
    for frameN in range(int(round(params['fp']*params['frameRate']))):
        fixation.draw()
        win.update()
    # show first word for 200 ms
    for frameN in range(int(round(params['duration']*params['frameRate']))):
        stim_wordleft.draw()
        line.draw()
        win.update()
    # show mask for 500 ms
    for frameN in range(int(round(params['ISI1']*params['frameRate']))):
        mask.draw()
        win.update()
    # show second word for 200 ms
    thisResponse = None
    while thisResponse == None:
        clockRT.reset()
        stim_wordright.draw()
        line.draw()
        win.update()

# collect response
        allKeys = event.waitKeys(keyList=['escape','1','2'],timeStamped = clockRT)
        for keyTuple in allKeys:
            [thisKey, thisRT] = keyTuple
        for thisKey in allKeys:
            if thisKey[0] in ['escape']:core.quit()
            elif thisKey[0] in ['1','2']:
                if int(thisKey[0]) == corresp:
                    thisResponse=1
                    accuracy = 1
                    corSnd.play()
                else: 
                    thisResponse=1
                    accuracy = 0
                    incorSnd.play()
    trials.addData('RT', thisRT)
    event.clearEvents()
    dataFile.write('%s %s %s %s %s %s\n' %(wordlist1[trials.thisTrial.word],trials.thisTrial.top,trials.thisTrial.cong,thisKey[0], accuracy, round(thisRT,2)))

win.close()
core.quit()