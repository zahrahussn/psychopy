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

fileName = params['ID number']+'_alignedEng'+'_'+params['computer']
dataFile = open('/home/zahrahussain/Documents/psychopy/data/wordComposite/'+fileName+'.txt', 'a')#a simple text file with 'comma-separated-values'
dataFile.write('word, cue, resp, congruent, subjectResp, accuracy, RT\n') 

# Create a visual window:
win = visual.Window(fullscr=True, allowGUI = True, monitor = 'testMonitor', units = 'deg')
#win = visual.Window(fullscr=True, allowGUI = True, monitor = 'attentionExperimentsMonitor', units = 'deg')
win.mouseVisible=False
fixation = visual.PatchStim(win, color=-1, tex=None, mask='circle',size=0.2, units='deg')
#mask=visual.RadialStim(win, tex='sqrXsqr',color=1, size=8,
#    visibleWedge=[0, 360], radialCycles=4, angularCycles=8, interpolate=False,
#    autoLog=False) 
mask = visual.GratingStim(win=win,units="deg",size= 7)
mask.sf = 5.0 / 7

corSnd = sound.Sound(2200, octave=14, secs=0.01) # auditory feedback
incorSnd = sound.Sound(800, octave=7, secs=0.01) # auditory feedback

#cue for which side is the target  
cueLeftVert=[(-2,3),(-3,3),(-3,-3),(-2,-3)]
cueLeft= visual.ShapeStim(win,vertices=cueLeftVert,closeShape=False,lineWidth=5,pos=(-3,0),lineColor='black')
cueRightVert=[(2,3),(3,3),(3,-3),(2,-3)]
cueRight= visual.ShapeStim(win,vertices=cueRightVert,closeShape=False,lineWidth=5,pos=(3,0),lineColor='black')


stimSize=2 #size of the text 
textFont='Courier'
wordlist1=['basket', 'reward', 'coffin', 'active', 'bonbon', 'couple', 'legend', 'revive', 'middle', 'divide']
wordlist2=['basics','rewind','coffee','actors','bonnet', 'coupon', 'legion', 'revoke', 'midget', 'divine']
wordlist3=['marble','cowboy','muffle','nature','career', 'temper', 'attack', 'motion', 'cancer', 'resume']
wordlist4=['market','coward','muffin','native','carbon', 'temple', 'attend', 'motive', 'candle', 'reside']

line=visual.Line(win, start=(0,2),end=(0,-3),lineColor=[-1,-1,-1]) #to draw a vertical line separating the word-halves

# setup trial handler
stimList=[]
for word in range(0,10): #This will yield 10 words NOT 11
    for cue in ['left', 'right']: # left right
        for resp in ['same', 'different']: # same different
           for cong in ['congruent', 'incongruent']: # congruent incongruent
            stimList.append({'cue': cue, 'resp': resp, 'cong': cong, 'word': word})
trials = data.TrialHandler(stimList, 1)
trials.data.addDataType('accuracy')
trials.data.addDataType('RT')
clockRT = core.Clock() 

for thisTrial in trials: 
    if trials.thisTrial.cue=='left': #if left is target
        cue=cueLeft
        if trials.thisTrial.resp=='same': # if same trial
            corresp=1 # correct response = 1
            if trials.thisTrial.cong=='congruent': # if congruent trial
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
                word2= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
            else: # if incongruent trial
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
                word2= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
        else: # if different trial
            corresp=2 
            if trials.thisTrial.cong=='congruent': # if congruent trial
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
                word2= visual.TextStim(win,font=textFont, text=wordlist3[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
            else: # if incongruent trial
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
                word2= visual.TextStim(win,font=textFont, text=wordlist4[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')

    else: # right target
        cue=cueRight
        if trials.thisTrial.resp =='same': # if same trial
            corresp=1 # correct response = 1
            if trials.thisTrial.cong=='congruent': # if congruent trial
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
                word2= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
            else: # if incongruent trial
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
                word2= visual.TextStim(win,font=textFont, text=wordlist4[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
        else: # if different trial
            corresp=2 
            if trials.thisTrial.cong=='congruent': # if congruent trial
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
                word2= visual.TextStim(win,font=textFont, text=wordlist3[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
            else: # if incongruent trial
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
                word2= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg')
                
    stim=wordlist1[trials.thisTrial.word]        
    g=numpy.random.random_integers(0,1) #to choose which of the word pairs will be a target and which will be the study word. 
    
    if g == 1: #word1 will be the study and word 2 will be the target
        stim1 = word1
        stim2 = word2
    else:      #word2 will be the study and word 1 will be the target 
        stim1 = word2
        stim2 = word1
        
    # show blank screen for 500 ms
    for frameN in range(int(round(params['ISI2']*params['frameRate']))):
        win.update()
    # show fixation point for 500 ms
    for frameN in range(int(round(params['fp']*params['frameRate']))):
        fixation.draw()
        win.update()
    # show first word for 300 ms
    for frameN in range(int(round(params['duration']*params['frameRate']))):
        stim1.draw()
        line.draw()
        win.update()
    # show mask for 200 ms
    for frameN in range(int(round(params['ISI1']*params['frameRate']))):
        mask.draw()
        win.update()
    # show mask + cue for 200 ms
    for frameN in range(int(round(params['ISI1']*params['frameRate']))):
        mask.draw()
        cue.draw()
        win.update()
    # show second word 
    thisResponse = None
    clockRT.reset()
    cue.draw()
    stim2.draw()
    line.draw()
    win.update()
    while thisResponse == None: #could be put after
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
    dataFile.write('%s %s %s %s %s %s %s\n' %(stim,trials.thisTrial.cue,trials.thisTrial.resp,trials.thisTrial.cong,thisKey[0], accuracy, round(thisRT,2)))
    
    
win.close()
core.quit()
