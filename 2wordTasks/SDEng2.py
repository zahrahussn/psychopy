from __future__ import absolute_import, division, print_function
from psychopy import visual, event, core, gui, data
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim
from random import shuffle
import string, time
import random, copy, scipy
import numpy 
from psychopy import sound


params = {'ID number':'1',
	 'frameRate':120,'w1':0.2, 'ISI1': 0.3, 'w2': 0.2,'blank':0.3,'fp': 0.3,'task':'wordPrimingTask', 'computer':'raylan'}

dlg = gui.DlgFromDict(params, title='SameDiffTask', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', params) #save params to file for next time
else:
    core.quit()#the user hit cancel so exit

fileName = params['ID number']+'_SDTEng2'
dataFile = open('/home/zahrahussain/Documents/psychopy/data/wordSDT/'+fileName+'.txt', 'a')#a simple text file with 'comma-separated-values'
#dataFile = open(fileName+'.txt', 'a')
dataFile.write('word, cue, condition, distractorType, corresp, subjectResp, accuracy, RT\n') 

# Create a visual window:
#win = visual.Window(fullscr=True, allowGUI = True, monitor = 'testmonitor', units = 'deg')
win = visual.Window(fullscr=True, allowGUI = True, monitor = '2wordTasks', units = 'deg')
win.mouseVisible=False
fixation = visual.PatchStim(win, color=-1, tex=None, mask='circle',size=0.2, units='deg')
maskRight = visual.GratingStim(win=win,units="deg",size= 7,pos=(4,0),sf = 5.0 / 7)
maskLeft = visual.GratingStim(win=win,units="deg",size= 7,pos=(-4,0),sf = 5.0 / 7)
#mask.sf = 5.0 / 7

#Feedback
corSnd = sound.Sound(2200, octave=14, secs=0.01) # auditory feedback
incorSnd = sound.Sound(800, octave=7, secs=0.01) # auditory feedback

#Underline as Cue
lineLeft=visual.Line(win, start=(-1,-1.5),end=(-8,-1.5),lineColor=[-1,-1,-1],lineWidth=8.5)
lineRight=visual.Line(win, start=(1,-1.5),end=(8,-1.5),lineColor=[-1,-1,-1],lineWidth=8.5)

stimSize=2 #size of the text 
textFont='Courier'
wordlist1=['goose','horse','prize','angel','vocal','stage','brave','freak','giant','value','danger','cheap']#word list1
wordlist1Form=['moose','house','price','anger','local','stake','brace','creak','grant','valve','dagger','cheat'] #similar form condition 
wordlist1Cont=['panic','bunch','gloom','truck','green','broom','study','point','cover','north','troops','world'] #word control condition

#distractor lists
#distractor list
SDword1_Dist=["river","river","chest","chest","chair","chair","power","power","nation","nation","carrot","carrot","alone","alone","master","master","flower","flower","tutor","tutor","space","space","father","father","river","river","chest","chest","chair","chair","power","power","nation","nation","carrot","carrot","alone","alone","master","master","flower","flower","tutor","tutor","space","space","father","father","river","chest","chair","power","nation","carrot","alone","master","flower","tutor","space","father","river","chest","chair","power","nation","carrot","alone","master","flower","tutor","space","father","river","chest","chair","power","nation","carrot","alone","master","flower","tutor","space","father","river","chest","chair","power","nation","carrot","alone","master","flower","tutor","space","father"]
SDword2_Dist=["river","river","chest","chest","chair","chair","power","power","nation","nation","carrot","carrot","alone","alone","master","master","flower","flower","tutor","tutor","space","space","father","father","river","river","chest","chest","chair","chair","power","power","nation","nation","carrot","carrot","alone","alone","master","master","flower","flower","tutor","tutor","space","space","father","father","rider","crest","chain","tower","notion","parrot","clone","matter","blower","tumor","spice","rather","rider","crest","chain","tower","notion","parrot","clone","matter","blower","tumor","spice","rather","knock","moral","slope","habit","member","simple","brush","colony","banana","level","glory","spoons","knock","moral","slope","habit","member","simple","brush","colony","banana","level","glory","spoons"]


# setup trial handler
stimList=[]
for word in range(0,12): #This will yield 6 words NOT 7 
    for cue in ['left', 'right']: # left right
        for cond in ['identity1','identity2','control','relatedForm']:
            stimList.append({'cue': cue, 'cond': cond,'word': word})
trials = data.TrialHandler(stimList, 1)
trials.data.addDataType('accuracy')
trials.data.addDataType('RT')
clockRT = core.Clock() 

for thisTrial in trials: 
    D=numpy.random.random_integers(0,59) #to randomly select one word from list_Dist as distractor
    stim1_D=visual.TextStim(win,font=textFont, text=SDword1_Dist[int(D)], color =(-1,-1,-1),height=stimSize, units='deg')
    stim2_D=visual.TextStim(win,font=textFont, text=SDword2_Dist[int(D)], color =(-1,-1,-1),height=stimSize, units='deg')
    stim=wordlist1[trials.thisTrial.word]
    if D<47: #Fix these for the english list
        distractor="dist_identity"  #To include in the data file a column that shows what was the type of the distractor, the list_Dist is arranged in such a way that the first 48 words in the list are words..etc
    elif 47<=D<70:
        distractor="dist_control"
    elif 70<=D<93:
        distractor="dist_Form"
    else:
        distractor="dist_"
        
    if trials.thisTrial.cue=='right': #if right is target
        cue=lineRight
        stim1_D.pos=(-4,0) 
        stim2_D.pos=(-4,0)
        
        if trials.thisTrial.cond=='identity1': # word pair are identical
                corresp=1 #Reponse is same 
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
            
        elif trials.thisTrial.cond=='identity2': # word pair are identical
            corresp=1 
            word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
            word2= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
        
        # if word pair are completely different 
        elif trials.thisTrial.cond=='control': 
            corresp=2 #Response is different 
            word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
            word2= visual.TextStim(win,font=textFont, text=wordlist1Cont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
        
        #word pair are orthographically different by 1 letter
        else: 
            corresp=2
            word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
            word2= visual.TextStim(win,font=textFont, text=wordlist1Form[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))

    else: # left target
        cue=lineLeft
        stim1_D.pos=(4,0) 
        stim2_D.pos=(4,0)
        if trials.thisTrial.cond=='identity1': # word pair are identical
                corresp=1 
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
            
        elif trials.thisTrial.cond=='identity2': # word pair are identical
            corresp=1 
            word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
            word2= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
        
        # if word pair are completely different.
        elif trials.thisTrial.cond=='control': 
            corresp=2
            word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
            word2= visual.TextStim(win,font=textFont, text=wordlist1Cont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
        
        #word pair are orthographically different by 1 letter.
        else: 
            corresp=2
            word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
            word2= visual.TextStim(win,font=textFont, text=wordlist1Form[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
    
    g=numpy.random.random_integers(0,1) #to choose which of the word pairs will be a target and which will be the study word. 
    if g == 1: #word1 will be the study and word 2 will be the target
        stim1 = word1
        stim2 = word2
    else:      #word2 will be the study and word 1 will be the target 
        stim1 = word2
        stim2 = word1

    # show blank screen for 300 ms
    for frameN in range(int(round(params['blank']*params['frameRate']))):
        win.update()
    # show fixation point (alone) for 300 ms
    for frameN in range(int(round(params['fp']*params['frameRate']))):
        fixation.draw()
        win.update()
    # show word 1 + fixation for 200 ms
    for frameN in range(int(round(params['w1']*params['frameRate']))):
        stim1.draw()
        cue.draw()
        stim1_D.draw()
        fixation.draw()
        win.update()
    # show  mask + fixation for 300 ms
    for frameN in range(int(round(params['ISI1']*params['frameRate']))):
        maskRight.draw()
        maskLeft.draw() #add another mask for the distractor 
        fixation.draw()
        win.update()
    # show second word for 200 ms
    for frameN in range(int(round(params['w2']*params['frameRate']))):
        stim2.draw()
        stim2_D.draw()
        fixation.draw()
        cue.draw()
        win.update()
    
    # collect response
    thisResponse = None
    clockRT.reset()
    while thisResponse == None: 
        fixation.draw()
        win.update() 
        allKeys = event.getKeys(keyList=['escape','1','2'],timeStamped = clockRT)
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
    dataFile.write('%s %s %s %s %s %s %s %s\n' %(stim,trials.thisTrial.cue,trials.thisTrial.cond, distractor, corresp,thisKey[0], accuracy, round(thisRT,2)))
    
    
win.close()
core.quit()
