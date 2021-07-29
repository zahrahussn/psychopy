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

fileName = params['ID number']+'_WPTArb1'
dataFile = open('/home/zahrahussain/Documents/psychopy/data/wordPriming/'+fileName+'.txt', 'a')#a simple text file with 'comma-separated-values'
#dataFile = open(fileName+'.txt', 'a')
dataFile.write('word, cue, stimulus, condition,distractorType, subjectResp, accuracy, RT\n') 

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

stimSize=2.5 #size of the text 
textFont='Courier'
wordlistE=['shareef','7aneen','kaman','sa2el','kamal','3aneed']
wordlist1=[u'شريف',u'حنين',u'كمان',u'سائل',u'كمال',u'عنيد']#word list1
wordlist1Form=[u'عريف',u'حزين',u'زمان',u'سائم',u'رمال',u'عميد'] #similar form condition 
wordlist1Root=[u'أشرف',u'حنان',u'كمين',u'سؤال',u'كامل',u'عناد'] #same root condition
wordlist1Cont=[u'قالب',u'سراب',u'نصوص',u'معنى',u'قريب',u'مسرح'] #word control condition

#divided the word list into 2 lists (easier when I create the stimulus list, since I present 12 words compared to 6 pseudowords & 6 consonants) 
wordlist2E=['majrou7','mawjoud','salam','mar3oub','sadek','7okouk']   
wordlist2=[u'مجروح',u'موجود',u'سلام',u'مرعوب',u'صادق',u'حقوق'] #word list2
wordlist2Form=[u'مبروح',u'موعود',u'كلام',u'مركوب',u'صادر',u'حقول']
wordlist2Root=[u'جريحة',u'إيجاد',u'سلامة',u'مرعبة',u'صدقة',u'تحقيق']
wordlist2Cont=[u'إنشاء',u'أستاذ',u'جديد',u'حكاية',u'جملة',u'عادل']

pseudowordlistE=['laman','majkou7','2asraj','salad','kadel','momala']
pseudowordlist=[u'لمان',u'مجقوح',u'أصرج',u'سلاد',u'قادل',u'ممالة']   #pseudoword list 
pseudowordlistForm=[u'شمان',u'مجقول',u'أصرض',u'علاد',u'قودل',u'متالة']  #similar form condition 
pseudowordlistCont=[u'سقوق',u'اعتبى',u'شديف',u'أجغر',u'رموع',u'حوضوع']  #control condition

consonantslistE=['dthrm','htthm3','kghrsth','fbds','thtldm','mnthk']
consonantslist=[u'ضظرم',u'هتثمع',u'قغرصذ',u'فبدص',u'ثطلدم',u'منظك']   #consonantal string list
consonantslistForm=[u'ضعرم',u'متثمع',u'قغجصذ',u'فبدث',u'ثطجدم',u'لنظك']  #similar form condition
consonantslistCont=[u'ذثلق',u'رسلبق',u'شلبفر',u'نمتق',u'كنهقة',u'غبلت']  #control condition 

#distractor list
list_Dist=["أوعد","مسعود","محول","أسعد","أعرج","خارج","مسألة","أخرج","قائم","يقول","تراث","قائل","جريح","صارح","معرض","صريح","محالة","يقولون","عصافير","مقالة","ارتدى","عداوة","حقيبة","اعتدى","سلاح","سامح","قاتل","سماح","أبان","مدين","شعور","أدان","أركب","مرعب","ساعد","أرعب","أدبر","مجبر","راحل","أجبر","أعلم","سالم","راجع","أسلم","ركوع","أرجع","قارئ","رجوع","كميح","معلد","كماح","منيق","مرتى","منيد","ساقر","أقان","ساقل","ميهود","أرفب","موهود","مرزوب","تدراس","مربوب","فاخق","صدير","صاخق","كهتلس","ضذمرن","كملتس","طغهمق","ثغدهق","نغهمق","حلشخ","خجنق","ظلشخ","فقدم","رسته","بقدم","سرذق","مكزص","سرذم","خلقص","دهرف",
"خصقض",]
# setup trial handler
stimList=[]
for word in range(0,6): #This will yield 6 words NOT 7 
    for stimulus in ['words1','words2','pseudoword','consonants']:
        for cue in ['left', 'right']: # left right
            for cond in ['identity','control','relatedForm','relatedMorphology']:
                stimList.append({'cue': cue, 'stimulus': stimulus, 'cond': cond,'word': word})
trials = data.TrialHandler(stimList, 1)
trials.data.addDataType('accuracy')
trials.data.addDataType('RT')
clockRT = core.Clock() 

for thisTrial in trials: 
    D=numpy.random.random_integers(0,83) #to randomly select one word from list_Dist as distractor
    if D<47:
        distractor="word"  #To include in the data file a column that shows what was the type of the distractor, the list_Dist is arranged in such a way that the first 48 words in the list are words..etc
    elif D>65:
        distractor="consonants"
    else:
        distractor="pseudoword"
    stim2_D=visual.TextStim(win,font=textFont, text=list_Dist[int(D)], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic')
    
    if trials.thisTrial.cue=='right': #if right is target
        cue=lineRight
        stim2_D.pos=(-4,0) #To have the distractor on the opposite side
        if trials.thisTrial.stimulus=='words1': # if stimulus type is word from list 1
            corresp=1 # correct response = 1 since it is a word
            stim=wordlistE[trials.thisTrial.word] 
            if trials.thisTrial.cond=='identity': # word pair are identical
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
            
            # if word pair are completely different & no root word in common.
            elif trials.thisTrial.cond=='control': 
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist1Cont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
            
            #word pair are orthographically different by 1 letter, & no root word in common.
            elif trials.thisTrial.cond=='relatedForm': 
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist1Form[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
            
            else: #word pair has root in common (and some letters).
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist1Root[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))

        elif trials.thisTrial.stimulus=='words2':  # if stimulus type is word from list 2
            corresp=1 # correct response = 1 since it is a word
            stim=wordlist2E[trials.thisTrial.word] 
            if trials.thisTrial.cond=='identity': # word pair are identical
                word1= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
            
            # if word pair are completely different & no root word in common.
            elif trials.thisTrial.cond=='control': 
                word1= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist2Cont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
            
            #word pair are orthographically different by 1 letter, & no root word in common.
            elif trials.thisTrial.cond=='relatedForm': 
                word1= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist2Form[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
            
            else: #word pair has root in common (and some letters).
                word1= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist2Root[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
            
            
            
        elif trials.thisTrial.stimulus=='pseudoword':  # stimulus type is a psuedoword
            corresp=2 # correct response = 1 since it is not a word
            stim=pseudowordlistE[trials.thisTrial.word] 
            if trials.thisTrial.cond=='identity': # pseudoword pair are identical
                word1= visual.TextStim(win,font=textFont, text=pseudowordlist[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=pseudowordlist[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
            
            
            elif trials.thisTrial.cond=='control': #pseudoword pair are completely different & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=pseudowordlistCont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=pseudowordlistCont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
            
            elif trials.thisTrial.cond=='relatedForm': #pseudoword pair are orthographically different by 1 letter, & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=pseudowordlistForm[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=pseudowordlistForm[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
            
            else: #pseudoword pair has root in common (THIS IS NOT A CONDITION, so I want the code to skip it)
                continue
        
        elif trials.thisTrial.stimulus=='consonants':  # stimulus type is a psuedoword
            corresp=2 # correct response = 1 since it is not a word
            stim=consonantslistE[trials.thisTrial.word] 
            if trials.thisTrial.cond=='identity': # consonants pair are identical
                word1= visual.TextStim(win,font=textFont, text=consonantslist[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=consonantslist[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
            
            
            elif trials.thisTrial.cond=='control': #consonants pair are completely different & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=consonantslistCont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=consonantslistCont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
            
            elif trials.thisTrial.cond=='relatedForm': #consonants pair are orthographically different by 1 letter, & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=consonantslistForm[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
                word2= visual.TextStim(win,font=textFont, text=consonantslistForm[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(4,0))
            
            else: #consonants pair has root in common (THIS IS NOT A CONDITION, so I want the code to skip it).
                continue
    else: # left target
        cue=lineLeft
        stim2_D.pos=(4,0) #To have the distractor on the opposite side
        if trials.thisTrial.stimulus=='words1': # if stimulus type is word from list 1
            corresp=1 # correct response = 1 since it is a word
            stim=wordlistE[trials.thisTrial.word] 
            if trials.thisTrial.cond=='identity': # word pair are identical
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
            
            # if word pair are completely different & no root word in common.
            elif trials.thisTrial.cond=='control': 
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist1Cont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
            
            #word pair are orthographically different by 1 letter, & no root word in common.
            elif trials.thisTrial.cond=='relatedForm': 
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist1Form[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
            
            else: #word pair has root in common (and some letters).
                word1= visual.TextStim(win,font=textFont, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist1Root[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))

        elif trials.thisTrial.stimulus=='words2':  # if stimulus type is word from list 2
            corresp=1 # correct response = 1 since it is a word
            stim=wordlist2E[trials.thisTrial.word] 
            if trials.thisTrial.cond=='identity': # word pair are identical
                word1= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
            
            # if word pair are completely different & no root word in common.
            elif trials.thisTrial.cond=='control': 
                word1= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist2Cont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
            
            #word pair are orthographically different by 1 letter, & no root word in common.
            elif trials.thisTrial.cond=='relatedForm': 
                word1= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist2Form[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
            
            else: #word pair has root in common (and some letters).
                word1= visual.TextStim(win,font=textFont, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=wordlist2Root[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
            
            
            
        elif trials.thisTrial.stimulus=='pseudoword':  # stimulus type is a psuedoword
            corresp=2 # correct response = 1 since it is not a word
            stim=pseudowordlistE[trials.thisTrial.word] 
            if trials.thisTrial.cond=='identity': # pseudoword pair are identical
                word1= visual.TextStim(win,font=textFont, text=pseudowordlist[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=pseudowordlist[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
            
            
            elif trials.thisTrial.cond=='control': #pseudoword pair are completely different & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=pseudowordlistCont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=pseudowordlistCont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
            
            elif trials.thisTrial.cond=='relatedForm': #pseudoword pair are orthographically different by 1 letter, & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=pseudowordlistForm[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=pseudowordlistForm[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
            
            else: #pseudoword pair has root in common (THIS IS NOT A CONDITION, so I want the code to skip it)
                continue
        elif trials.thisTrial.stimulus=='consonants':  # stimulus type is a psuedoword
            corresp=2 # correct response = 1 since it is not a word
            stim=consonantslistE[trials.thisTrial.word] 
            if trials.thisTrial.cond=='identity': # consonants pair are identical
                word1= visual.TextStim(win,font=textFont, text=consonantslist[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=consonantslist[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
            
            
            elif trials.thisTrial.cond=='control': #consonants pair are completely different & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=consonantslistCont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=consonantslistCont[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
            
            elif trials.thisTrial.cond=='relatedForm': #consonants pair are orthographically different by 1 letter, & no root word in common.
                word1= visual.TextStim(win,font=textFont, text=consonantslistForm[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
                word2= visual.TextStim(win,font=textFont, text=consonantslistForm[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',languageStyle='Arabic',pos=(-4,0))
            
            else: #consonants pair has root in common (THIS IS NOT A CONDITION, so I want the code to skip it).
                continue

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
        maskLeft.draw() #add another mask for the distractor 
        fixation.draw()
        win.update()
    # show prime + fixation for 33 ms
    for frameN in range(int(round(params['primeduration']*params['frameRate']))):
        stim1.draw()
        fixation.draw()
        win.update()
    # show second word for 200 ms
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
