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

fileName = params['ID number']+'_alignedArb'
dataFile = open('/home/zahrahussain/Documents/psychopy/data/wordComposite/Guards/'+fileName+'.txt', 'a') #data file is saved in the file called Guards 
#dataFile = open(fileName+'.txt', 'a')
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
wordlistE=['7okouk','Sa2el','Jamal','Dorous','Mi3taf','Sadek']
wordlist1=[u'حقوق',u'سائل', u'جمال',u'دروس', u'معطف',u'صادق']
wordlist2=[u'حقيبة',u'سارح',u'جميع',u'درجة',u'معبر',u'صابر']
wordlist3=[u'حقول',u'سائح',u'جماد',u'دروب',u'معرف',u'صادر']
wordlist4=[u'حقائق',u'سائلة',u'جميل',u'دراسة',u'معطوف',u'صادقة']

wordlist5=[u'وثوق',u'قبائل',u'سعال',u'مغروس',u'يخطف',u'خردق']
wordlist6=[u'شقوق',u'قائل',u'كمال',u'عروس',u'ملطف',u'فنادق']
wordlist7=[u'محقوق',u'مسائل',u'إجمال',u'مدروس',u'ألطف',u'صوادق']
wordlist8=[u'مرير',u'حكيم',u'ملعب',u'زميل',u'كبير',u'ربيع']

# setup trial handler
stimList=[]
for word in range(0,6): #This will yield 10 words NOT 11
    for cue in ['left', 'right']: # left right
        for resp in ['same', 'different']: # same different
           for cong in ['congruent', 'incongControl','incongForm','incongMorph']: # congruent incongruent
#                for cond in ['identity','control','form','morphological']:
                    stimList.append({'cue': cue, 'resp': resp, 'cong': cong,'word': word})
trials = data.TrialHandler(stimList, 2)
trials.data.addDataType('accuracy')
trials.data.addDataType('RT')
clockRT = core.Clock() 

for thisTrial in trials: 
    linew1=visual.Line(win, start=(0,2),end=(0,-3),pos=(0,0),lineColor=[-1,-1,-1]) #to draw a vertical line separating the word-halves
    linew2=visual.Line(win, start=(0,2),end=(0,-3),pos=(0,0),lineColor=[-1,-1,-1]) #to draw a vertical line separating the word-halves

    if trials.thisTrial.cue=='right': #if right is target
        cue=cueRight
        if trials.thisTrial.resp=='same': # if same trial, Target half same
            corresp=1 # correct response = 1
            if trials.thisTrial.cong=='congruent': # if congruent trial
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
                word2= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
    # if incongruent trial
            elif trials.thisTrial.cong=='incongControl': #Target half same, other half completely different & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
                word2= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
            elif trials.thisTrial.cong=='incongForm': #Target half same, other half is orthographically different by 1 letter, & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
                word2= visual.TextStim(win,font=textFont, text=wordlist3[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
#            else trials.thisTrial.cong=='incongMorph': #Target half same, other half has root in common (and some letters).
            else:
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
                word2= visual.TextStim(win,font=textFont, text=wordlist4[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')

        else: # if different trial
            corresp=2 
            if trials.thisTrial.cong=='congruent': # if congruent trial
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
                word2= visual.TextStim(win,font=textFont, text=wordlist8[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')

     # if incongruent trial
            elif trials.thisTrial.cong=='incongControl': #Target half different, other half same & no root word in common
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
                word2= visual.TextStim(win,font=textFont, text=wordlist5[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
            elif trials.thisTrial.cong=='incongForm': #Target half different, other half same, word orthographically different by 1 letter, & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
                word2= visual.TextStim(win,font=textFont, text=wordlist6[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
#            else trials.thisTrial.cong=='incongMorph': #Target half different,other half same, word has root in common (and some letters).
            else:
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
                word2= visual.TextStim(win,font=textFont, text=wordlist7[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')

    else: # left target
        cue=cueLeft
        if trials.thisTrial.resp =='same': # if same trial
            corresp=1 # correct response = 1
            if trials.thisTrial.cong=='congruent': # if congruent trial
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
                word2= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
      # if incongruent trial
            elif trials.thisTrial.cong=='incongControl': #Target half different, other half same & no root word in common
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
                word2= visual.TextStim(win,font=textFont, text=wordlist5[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
            elif trials.thisTrial.cong=='incongForm': #Target half different, other half same, word orthographically different by 1 letter, & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
                word2= visual.TextStim(win,font=textFont, text=wordlist6[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
#            else trials.thisTrial.cong=='incongMorph': #Target half different,other half same, word has root in common (and some letters).
            else:
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
                word2= visual.TextStim(win,font=textFont, text=wordlist7[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')

        else: # if different trial
            corresp=2 
            if trials.thisTrial.cong=='congruent': # if congruent trial
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
                word2= visual.TextStim(win,font=textFont, text=wordlist8[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
      # if incongruent trial
            elif trials.thisTrial.cong=='incongControl': #Target half same, other half completely different & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
                word2= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
            elif trials.thisTrial.cong=='incongForm': #Target half same, other half is orthographically different by 1 letter, & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
                word2= visual.TextStim(win,font=textFont, text=wordlist3[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
#            else trials.thisTrial.cong=='incongMorph': #Target half same, other half has root in common (and some letters).
            else:
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
                word2= visual.TextStim(win,font=textFont, text=wordlist4[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')

    stim=wordlistE[trials.thisTrial.word]        
    g=numpy.random.random_integers(0,1) #to choose which of the word pairs will be a target and which will be the study word. 

          #Setting the line position relative to what word it is (so that the line does not bisect a letter if the word is 5 letters) 
    #Setting the line to the right 
    #Words:دراسة،سائلة،معطوف،صادقة،حقائق
    if trials.thisTrial.cue=='right' and trials.thisTrial.resp=='same' and trials.thisTrial.cong=='incongMorph' and trials.thisTrial.word in [0,1,3,4,5]:
        linew2.pos=(0.5,0) #to draw a vertical line separating the word-halves
    #Word: حقيبة
    elif trials.thisTrial.cue=='right' and trials.thisTrial.resp=='same' and trials.thisTrial.cong=='incongControl' and trials.thisTrial.word in [0]:
        linew2.pos=(0.5,0) #to draw a vertical line separating the word-halves
   #Setting the line to the left
    #Word:محقوق،مسائل،إجمال
    elif trials.thisTrial.cue=='right' and trials.thisTrial.resp=='different' and trials.thisTrial.cong=='incongMorph' and trials.thisTrial.word in [0,1,2,3,5]:
        linew2.pos=(-0.5,0) #to draw a vertical line separating the word-halves
    #Word:فنادق
    elif trials.thisTrial.cue=='right' and trials.thisTrial.resp=='different' and trials.thisTrial.cong=='incongForm' and trials.thisTrial.word in [5]:
        linew2.pos=(-0.5,0) #to draw a vertical line separating the word-halvncongControl'
    #Word:قبائل
    elif trials.thisTrial.cue=='right' and trials.thisTrial.resp=='different' and trials.thisTrial.cong=='incongControl' and trials.thisTrial.word in [1,3]:
        linew2.pos=(-0.5,0) #to draw a vertical line separating the word-halvncongControl'
   #Now for the wordlists when the cue is to the left 
    #Setting the line to the right 
    #Word:محقوق،مسائل،إجمال
    elif trials.thisTrial.cue=='left' and trials.thisTrial.resp=='same' and trials.thisTrial.cong=='incongMorph' and trials.thisTrial.word in [0,1,2,3,5]:
        linew2.pos=(-0.5,0) #to draw a vertical line separating the word-halves
    #Word:قبائل
    elif trials.thisTrial.cue=='left' and trials.thisTrial.resp=='same' and trials.thisTrial.cong=='incongControl' and trials.thisTrial.word in [1,3]:
        linew2.pos=(-0.5,0) #to draw a vertical line separating the word-halves
    #Word:فنادق
    elif trials.thisTrial.cue=='left' and trials.thisTrial.resp=='same' and trials.thisTrial.cong=='incongForm' and trials.thisTrial.word in [5]:
        linew2.pos=(-0.5,0) #to draw a vertical line separating the word-halves
    #Setting the line to the right
    #Words:دراسة،سائلة،معطوق،صادقة،حقائق
    elif trials.thisTrial.cue=='left' and trials.thisTrial.resp=='different' and trials.thisTrial.cong=='incongMorph' and trials.thisTrial.word in [0,1,3,4,5]:
        linew2.pos=(0.5,0) #to draw a vertical line separating the word-halves
    #Word:حقيبة
    elif trials.thisTrial.cue=='left' and trials.thisTrial.resp=='different' and trials.thisTrial.cong=='incongControl' and trials.thisTrial.word in [0]:
        linew2.pos=(0.5,0) #to draw a vertical line separating the word-halves

    
    #Setting the line at the middle of the word for all 4 letter words.
    else:
        linew2.pos=(0,0) #to draw a vertical line separating the word-halves
    
#    print(trials.thisTrial.cue)
#    print(trials.thisTrial.resp)
#    print(trials.thisTrial.cong)
#    print(stim)
#    print(linew1.pos)
#    print(linew2.pos)
#    print(g)
        
    if g == 1: #word1 will be the study and word 2 will be the target
        stim1 = word1
        line1=linew1
        stim2 = word2
        line2=linew2
    else:      #word2 will be the study and word 1 will be the target 
        stim1 = word2
        line1=linew2
        stim2 = word1
        line2=linew1

    print("after g loop")
    print(line1.pos)
    print(line2.pos)
    
    
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
        line1.draw()
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
    line2.draw()
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
