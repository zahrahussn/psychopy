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
    toFile('lastParams.pickle', params)#save params to file for next time
else:
    core.quit()#the user hit cancel so exit

fileName = params['ID number']+'_alignedArb'+'_'+params['computer']
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
wordlistE=['Arif','Sa2el','Jamal','7okouk','Rojou3','Kafif','Sarir','Jawab','Mourouj','Zamil']
wordlist1=[u'عريف',u'سائل', u'جمال', u'حقوق',u'رجوع',u'كفيف', u'سرير', u'جواب', u'مروج',u'زميل']
wordlist2=[u'عريض',u'سارح',u'جميع',u'حقول',u'رجال',u'كفوء',u'سريع',u'جواد',u'مريب',u'زمان']
wordlist3=[u'شريك',u'قاصر',u'مقاس',u'شفاف',u'شمال',u'سخاء',u'كباش',u'صوار',u'خراب',u'عميق']
wordlist4=[u'شريف',u'قائل',u'مقال',u'شفوق',u'شموع',u'سخيف',u'كبير',u'صواب',u'خروج',u'عميل']

#line=visual.Line(win, start=(0.15,2),end=(0.15,-3),lineColor=[-1,-1,-1]) #to draw a vertical line separating the word-halves

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
#w=numpy.random.random_integers(0,3) # select a random number between 0 and 3
    if trials.thisTrial.top==1: # if 'same' top/aligned trial
        corresp=1 # correct response = 1
        if trials.thisTrial.cong==1: # if same-congruent/aligned trial
                stim_wordleft= visual.TextStim(win, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1), height=stimSize, units='deg', font=textFont, languageStyle='Arabic')
                stim_wordright= visual.TextStim(win, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',font=textFont,languageStyle='Arabic')
        else: # if same-incongruent/aligned trial
                stim_wordleft= visual.TextStim(win, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',font=textFont,languageStyle='Arabic')
                stim_wordright= visual.TextStim(win, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',font=textFont,languageStyle='Arabic')
    else: # if 'different' top/aligned trial
        corresp=2 
        if trials.thisTrial.cong==1: # if different-congruent/aligned trial
            stim_wordleft= visual.TextStim(win, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',font=textFont,languageStyle='Arabic')
            stim_wordright= visual.TextStim(win, text=wordlist3[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',font=textFont,languageStyle='Arabic')
        else: # if different-incongruent/aligned trial
            stim_wordleft= visual.TextStim(win, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',font=textFont,languageStyle='Arabic')
            stim_wordright= visual.TextStim(win, text=wordlist4[trials.thisTrial.word], color =(-1,-1,-1),height=stimSize, units='deg',font=textFont,languageStyle='Arabic') 
#show blank screen for 500 ms
    for frameN in range(int(round(params['ISI2']*params['frameRate']))):
        win.update()
    # show fixation point for one second
    for frameN in range(int(round(params['fp']*params['frameRate']))):
        fixation.draw()
        win.update()
    # show first word for 200 ms
    for frameN in range(int(round(params['duration']*params['frameRate']))):
        stim_wordleft.draw()
        #line.draw()
        win.update()
    # show frame for 500 ms
    for frameN in range(int(round(params['ISI1']*params['frameRate']))):
        mask.draw()
        win.update()
    # show second word for 200 ms
    
    thisResponse = None
    while thisResponse == None:
        clockRT.reset()
        stim_wordright.draw()
        #line.draw()
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
    dataFile.write('%s %s %s %s %s %s \n' %(wordlistE[trials.thisTrial.word], trials.thisTrial.top, trials.thisTrial.cong, thisKey[0], accuracy, round(thisRT,2)))

win.close()
core.quit()