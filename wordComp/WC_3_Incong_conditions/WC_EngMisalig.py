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
	 'frameRate':120,'duration':0.3, 'ISI1': 0.2, 'ISI2': 0.5,'fp': 0.5,'task':'wordComposite', 'computer':'raylan'} #FrameRate is 120 on the ViewPixx

dlg = gui.DlgFromDict(params, title='wordComposite', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', params) #save params to file for next time
else:
    core.quit()#the user hit cancel so exit

fileName = params['ID number']+'_misalignedEng'
dataFile = open('/home/zahrahussain/Documents/psychopy/data/wordComposite/Guards/'+fileName+'.txt', 'a') #data file is saved in the file called Guards
dataFile.write('word, cue, resp, congruent, subjectResp, accuracy, RT\n') 

# Create a visual window:
#win = visual.Window(fullscr=True, allowGUI = True, monitor = 'testMonitor', units = 'deg')
win = visual.Window(fullscr=True, allowGUI = True, monitor = 'WordComposite', units = 'deg') #Using WordComposite monitor set at 57cm viewing distance 
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


stimSize=1.8 #size of the text 
textFont='Courier'

wordlist1=['basket','reward','active','couple','legend','divide']

toplist1=['bas','rew','act','cou','leg','div']
bottomlist1=['ket','ard','ive','ple','end','ide']
bottomlist2=['ics','ind','ors','pon','ion','ine']
toplist2=['mar','cow','nat','tem','att','res']
bottomlist3=['ble','boy','ure','per','ack','ume']


line=visual.Line(win, start=(0,2),end=(0,-3),lineColor=[-1,-1,-1]) #to draw a vertical line separating the word-halves

# setup trial handler
stimList=[]
for word in range(0,6): #This will yield 10 words NOT 11
    for cue in ['left', 'right']: # left right
        for resp in ['same', 'different']: # same different
           for cong in ['congruent', 'incongruent']: # congruent incongruent
            stimList.append({'cue': cue, 'resp': resp, 'cong': cong, 'word': word})
trials = data.TrialHandler(stimList, 2)
trials.data.addDataType('accuracy')
trials.data.addDataType('RT')
clockRT = core.Clock() 

for thisTrial in trials:

    x1=-1.75
    y1=0
    x2=1.75
    y2=-1
    if trials.thisTrial.cue=='left': #if left is target
        cue=cueLeft
        if trials.thisTrial.resp=='same': # if same trial
            corresp=1 # correct response = 1
            if trials.thisTrial.cong=='congruent': # if congruent trial
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font= textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            else: # if same-incongruent/misaligned trial
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist2[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
        else: # if 'different' top/misaligned trial
            corresp=2 # correct response =2
            if trials.thisTrial.cong==1: # if different-congruent trial
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist2[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist3[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            else: # if different-incongruent/misaligned trial
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist2[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
    else: # right target
        cue=cueRight
        if trials.thisTrial.resp=='same': # if same trial
            corresp=1 # correct response = 1
            if trials.thisTrial.cong=='congruent': # if congruent trial
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font= textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            else: # if same-incongruent/misaligned trial
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist2[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
        else: # if 'different' top/misaligned trial
            corresp=2 # incorrect response =2
            if trials.thisTrial.cong==1: # if different-congruent trial
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist2[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist3[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            else: # if different-incongruent/misaligned trial
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist2[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')

    stim=wordlist1[trials.thisTrial.word]        
    #g=numpy.random.random_integers(0,1) #to choose which of the word pairs will be a target and which will be the study word. 
    g=numpy.random.randint(0,1+1) #to choose which of the word pairs will be a target and which will be the study word. 
    
    if g == 1: #word1 will be the study and word 2 will be the target
        stim1_right = word1_right
        stim1_left = word1_left
        stim2_right = word2_right
        stim2_left = word2_left
    else:      #word2 will be the study and word 1 will be the target 
        stim1_right = word2_right
        stim1_left = word2_left
        stim2_right = word1_right
        stim2_left = word1_left
        
    # show blank screen for 500 ms
    for frameN in range(int(round(params['ISI2']*params['frameRate']))):
        win.update()
    # show fixation point for 500 ms
    for frameN in range(int(round(params['fp']*params['frameRate']))):
        fixation.draw()
        win.update()
    # show first word for 300 ms
    for frameN in range(int(round(params['duration']*params['frameRate']))):
        stim1_right.draw()
        stim1_left.draw()
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
    stim2_right.draw()
    stim2_left.draw()
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
