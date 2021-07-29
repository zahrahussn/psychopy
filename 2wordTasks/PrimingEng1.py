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
	 'frameRate':120,'primeduration':0.033, 'ISI1': 0.5, 'probeduration': 0.2,'fp': 0.2,'task':'wordPrimingTask', 'computer':'raylan'}

dlg = gui.DlgFromDict(params, title='wordPrimingTask', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', params) #save params to file for next time
else:
    core.quit()#the user hit cancel so exit

fileName = params['ID number']+'_WPTArb'
dataFile = open('/home/zahrahussain/Documents/psychopy/data/wordPriming/'+fileName+'.txt', 'a')#a simple text file with 'comma-separated-values'
#dataFile = open(fileName+'.txt', 'a')
dataFile.write('word, cue, stimulus, condition, distractorType subjectResp, accuracy, RT\n') 

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
wordlist1=['river','chest','chair','power','nation','carrot']#word list1
wordlist1Form=['rider','crest','chain','tower','notion','parrot'] #similar form condition 
wordlist1Cont=['knock','moral','slope','habit','member','simple'] #word control condition

#divided the word list into 2 lists (easier when I create the stimulus list, since I present 12 words compared to 6 pseudowords & 6 consonants) 
wordlist2=['alone','master','flower','tutor','space','father'] #word list2
wordlist2Form=['clone','matter','blower','tumor','spice','rather']
wordlist2Cont=['brush','colony','banana','level','glory','spoons']

pseudowordlist=['chost','chail','sation','flomer','trame','fither']   #pseudoword list 
pseudowordlistForm=['chont','crail','wation','blomer','trape','pither']  #similar form condition 
pseudowordlistCont=['prige','stume','rekume','thucks','clush','cloans']  #control condition

consonantslist=['ctsnr','blsvcl','ntswm','lnfrk','fwrbc','kbplm']   #consonantal string list
consonantslistForm=['ctmnr','klsvl','ptswm','lngrk','fsrbc','kbplj']  #similar form condition
consonantslistCont=['kwhvp','jhdwrf','qlcfk','mtsld','pknlv','cjthd']  #control condition 

#distractor list
list_Dist=["judge","crown","nudge","bribe","clock","tribe","model","crack","motel","truce","skunk","trace","chase","group","phase","kettle","paving","settle","clear","sword","clean","jelly","watch","belly","regent","whisky","recent","miser","glass","mixer","cake","word","bake","honey","tools","money","lanent","donger","racent","tatom","hettle","tator","phime","nabble","phise","spime","plush","spame","povet","vacal","pover","misten","liant","masten","jtrpc","kjrdb","ftrpc","crhlt","wtcfn","crhlg","pbtrk","ndchj","pvtrk","tsrkn","pjhbc","tsrbn","crdrz","lnkmf","crdsz","msrnlt","bvdzt","mstnlt"]

# setup trial handler
stimList=[]
for word in range(0,6): #This will yield 6 words NOT 7 
    for stimulus in ['words1','words2','pseudoword','consonants']:
        for cue in ['left', 'right']: # left right
            for cond in ['identity','control','relatedForm']:
                stimList.append({'cue': cue, 'stimulus': stimulus, 'cond': cond,'word': word})
trials = data.TrialHandler(stimList, 1)
trials.data.addDataType('accuracy')
trials.data.addDataType('RT')
clockRT = core.Clock() 

for thisTrial in trials: 
    D=numpy.random.random_integers(0,71) #randomly generating a number to randomly select one word from list_Dist as distractor
    if D<35:   
        distractor="word"  #To include in the data file a column that shows what was the type of the distractor, the list_Dist is arranged in such a way that the first 36 words in the list are words..etc
    elif D>53:
        distractor="consonants"
    else:
        distractor="pseudoword"
    stim2_D=visual.TextStim(win,font=textFont, text=list_Dist[int(D)], color =(-1,-1,-1),height=stimSize, units='deg')#stim2_D will be the distractor, with text indexed from list_Dist using the value of D
    
    if trials.thisTrial.cue=='right': #if right is target
        cue=lineRight
        stim2_D.pos=(-4,0) #To have the distractor on the opposite side
        if trials.thisTrial.stimulus=='words1': # if stimulus type is word from list 1
            corresp=1 # correct response = 1 since it is a word
            stim=wordlist1[trials.thisTrial.word] 
            if trials.thisTrial.cond=='identity': # word pair are identical
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
            
            # if word pair are completely different & no root word in common.
            elif trials.thisTrial.cond=='control': 
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist1Cont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
            
            #word pair are orthographically different by 1 letter, & no root word in common.
            else: 
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist1Form[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
            

        elif trials.thisTrial.stimulus=='words2':  # if stimulus type is word from list 2
            corresp=1 # correct response = 1 since it is a word
            stim=wordlist2[trials.thisTrial.word] 
            if trials.thisTrial.cond=='identity': # word pair are identical
                word1= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
            
            # if word pair are completely different & no root word in common.
            elif trials.thisTrial.cond=='control': 
                word1= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist2Cont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
            
            #word pair are orthographically different by 1 letter, & no root word in common.
            else: 
                word1= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist2Form[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
            
            
            
            
        elif trials.thisTrial.stimulus=='pseudoword':  # stimulus type is a psuedoword
            corresp=2 # correct response = 1 since it is not a word
            stim=pseudowordlist[trials.thisTrial.word] 
            if trials.thisTrial.cond=='identity': # pseudoword pair are identical
                word1= visual.TextStim(win,font=textFont, text=pseudowordlist[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=pseudowordlist[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
            
            
            elif trials.thisTrial.cond=='control': #pseudoword pair are completely different & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=pseudowordlistCont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=pseudowordlistCont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
            
            else: #pseudoword pair are orthographically different by 1 letter, & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=pseudowordlistForm[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=pseudowordlistForm[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
            
        elif trials.thisTrial.stimulus=='consonants':  # stimulus type is a psuedoword
            corresp=2 # correct response = 1 since it is not a word
            stim=consonantslist[trials.thisTrial.word] 
            if trials.thisTrial.cond=='identity': # consonants pair are identical
                word1= visual.TextStim(win,font=textFont, text=consonantslist[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=consonantslist[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
            
            
            elif trials.thisTrial.cond=='control': #consonants pair are completely different & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=consonantslistCont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=consonantslistCont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
            
            else: #consonants pair are orthographically different by 1 letter, & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=consonantslistForm[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=consonantslistForm[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(4,0))
            
    else: # left target
        cue=lineLeft
        stim2_D.pos=(4,0) #To have the distractor on the opposite side
        if trials.thisTrial.stimulus=='words1': # if stimulus type is word from list 1
            corresp=1 # correct response = 1 since it is a word
            stim=wordlistE[trials.thisTrial.word] 
            if trials.thisTrial.cond=='identity': # word pair are identical
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
            
            # if word pair are completely different & no root word in common.
            elif trials.thisTrial.cond=='control': 
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist1Cont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
            
            #word pair are orthographically different by 1 letter, & no root word in common.
            else: 
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist1Form[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
            

        elif trials.thisTrial.stimulus=='words2':  # if stimulus type is word from list 2
            corresp=1 # correct response = 1 since it is a word
            stim=wordlist2E[trials.thisTrial.word] 
            if trials.thisTrial.cond=='identity': # word pair are identical
                word1= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
            
            # if word pair are completely different & no root word in common.
            elif trials.thisTrial.cond=='control': 
                word1= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist2Cont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
            
            #word pair are orthographically different by 1 letter, & no root word in common.
            else: 
                word1= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist2Form[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
            

            
        elif trials.thisTrial.stimulus=='pseudoword':  # stimulus type is a psuedoword
            corresp=2 # correct response = 1 since it is not a word
            stim=pseudowordlistE[trials.thisTrial.word] 
            if trials.thisTrial.cond=='identity': # pseudoword pair are identical
                word1= visual.TextStim(win,font=textFont, text=pseudowordlist[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=pseudowordlist[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
            
            
            elif trials.thisTrial.cond=='control': #pseudoword pair are completely different & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=pseudowordlistCont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=pseudowordlistCont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
            
            else: #pseudoword pair are orthographically different by 1 letter, & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=pseudowordlistForm[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=pseudowordlistForm[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
            
        elif trials.thisTrial.stimulus=='consonants':  # stimulus type is a psuedoword
            corresp=2 # correct response = 1 since it is not a word
            stim=consonantslistE[trials.thisTrial.word] 
            if trials.thisTrial.cond=='identity': # consonants pair are identical
                word1= visual.TextStim(win,font=textFont, text=consonantslist[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=consonantslist[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
            
            
            elif trials.thisTrial.cond=='control': #consonants pair are completely different & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=consonantslistCont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=consonantslistCont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
            
            else: #consonants pair are orthographically different by 1 letter, & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=consonantslistForm[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=consonantslistForm[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',pos=(-4,0))
            
    g=numpy.random.random_integers(0,1) #to choose which of the word pairs will be a target and which will be the study word. 
    if g == 1: #word1 will be the study and word 2 will be the target
        stim1 = word1
        #line1=lineLeft
        stim2 = word2
        #line2=lineRight
    else:      #word2 will be the study and word 1 will be the target 
        stim1 = word2
        #line1=lineRight
        stim2 = word1
        #line2=lineLeft

    # show blank screen for 200 ms
    for frameN in range(int(round(params['fp']*params['frameRate']))):
        win.update()
    # show fixation point (alone) for 200 ms
    for frameN in range(int(round(params['fp']*params['frameRate']))):
        fixation.draw()
        win.update()
    # show mask + fixation for 500 ms
    for frameN in range(int(round(params['ISI1']*params['frameRate']))):
        maskRight.draw()
        maskLeft.draw()
        fixation.draw()
        win.update()
    # show prime + fixation for 33 ms
    for frameN in range(int(round(params['primeduration']*params['frameRate']))):
        stim1.draw()
        fixation.draw()
        win.update()
    # show second word for 200 ms

    thisResponse = None
    #clockRT.reset()
    for frameN in range(int(round(params['probeduration']*params['frameRate']))):
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
    dataFile.write('%s %s %s %s %s %s %s %s\n' %(stim,trials.thisTrial.cue,trials.thisTrial.stimulus,trials.thisTrial.cond,distractor,thisKey[0], accuracy, round(thisRT,2)))
    
    
win.close()
core.quit()
