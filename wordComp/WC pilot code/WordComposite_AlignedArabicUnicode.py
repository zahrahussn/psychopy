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
	 'frameRate':60,'duration':0.3, 'ISI1': 0.2, 'ISI2': 0.5,'fp': 0.5,'task':'wordComposite'}

dlg = gui.DlgFromDict(params, title='wordComposite', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', params)#save params to file for next time
else:
    core.quit()#the user hit cancel so exit

fileName = params['ID number']+'_s1'
dataFile = open(fileName+'.txt', 'a')#a simple text file with 'comma-separated-values'
dataFile.write('word, sameTop, congruent, response, accuracy, RT\n') 

# Create a visual window:
win = visual.Window(fullscr=True, allowGUI = True, monitor = 'testMonitor', units = 'deg')
win.mouseVisible=False
fixation = visual.PatchStim(win, color=-1, tex=None, mask='circle',size=0.2, units='deg')
mask=visual.RadialStim(win, tex='sqrXsqr',color=1, size=4,
    visibleWedge=[0, 360], radialCycles=4, angularCycles=8, interpolate=False,
    autoLog=False) 
corSnd = sound.Sound(2200, octave=14, secs=0.01) # auditory feedback
incorSnd = sound.Sound(800, octave=7, secs=0.01) # auditory feedback
wordlistE=['Arif','Sa2el','Jamal','Sadek','Sila7','Kilab','Sarir','Jawab','Mourouj','Zamil']
wordlist1=[u'\u0639\u0631\u064a\u0641',u'\u0633\u0627\u0626\u0644',u'\u062c\u0645\u0627\u0644',u'\u0635\u0627\u062f\u0642',u'\u0633\u0644\u0627\u062d',u'\u0643\u0644\u0627\u0628',u'\u0633\u0631\u064a\u0631',u'\u062c\u0648\u0627\u0628',u'\u0645\u0631\u0648\u062c',u'\u0632\u0645\u064a\u0644']
wordlist2=[u'\u0639\u0631\u064a\u0636',u'\u0633\u0627\u0631\u062d',u'\u062c\u0645\u064a\u0639',u'\u0635\u0627\u0626\u0628',u'\u0633\u0644\u064a\u0645',u'\u0643\u0644\u0627\u0645',u'\u0633\u0631\u064a\u0639',u'\u062c\u0648\u0627\u062f',u'\u0645\u0631\u064a\u0628',u'\u0632\u0645\u0627\u0646']

wordlist3=[u'\u0642\u0627\u0631\u0628',u'\u0635\u0627\u0628\u0631',u'\u062e\u0637\u064a\u0631',u'\u0643\u0628\u064a\u0631',u'\u0645\u0644\u0639\u0628',u'\u062d\u0642\u0648\u0644',u'\u062d\u0632\u064a\u0646',u'\u0645\u0642\u0627\u0645',u'\u0631\u0641\u064a\u0642',u'\u0645\u0643\u0627\u0646']
wordlist4=[u'\u0634\u0631\u064a\u0641',u'\u0642\u0627\u0626\u0644',u'\u0645\u0642\u0627\u0644',u'\u0628\u0646\u062f\u0642',u'\u0633\u0645\u0627\u062d',u'\u0639\u062a\u0627\u0628',u'\u0623\u0645\u064a\u0631',u'\u0643\u062a\u0627\u0628',u'\u062e\u0631\u0648\u062c',u'\u0639\u0645\u064a\u0644']

# setup trial handler
stimList=[]
for word in range(0,9):
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
                stim_wordleft= visual.TextStim(win, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),font='Arial', languageStyle='Arabic')
                stim_wordright= visual.TextStim(win, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),font='Arial',languageStyle='Arabic')
        else: # if same-incongruent/aligned trial
                stim_wordleft= visual.TextStim(win, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),font='Arial',languageStyle='Arabic')
                stim_wordright= visual.TextStim(win, text=wordlist2[trials.thisTrial.word], color =(-1,-1,-1),font='Arial',languageStyle='Arabic')
    else: # if 'different' top/aligned trial
        corresp=2 
        if trials.thisTrial.cong==1: # if different-congruent/aligned trial
            stim_wordleft= visual.TextStim(win, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),font='Arial',languageStyle='Arabic')
            stim_wordright= visual.TextStim(win, text=wordlist3[trials.thisTrial.word], color =(-1,-1,-1),font='Arial',languageStyle='Arabic')
        else: # if different-incongruent/aligned trial
            stim_wordleft= visual.TextStim(win, text=wordlist1[trials.thisTrial.word], color =(-1,-1,-1),font='Arial',languageStyle='Arabic')
            stim_wordright= visual.TextStim(win, text=wordlist4[trials.thisTrial.word], color =(-1,-1,-1),font='Arial',languageStyle='Arabic') 
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
        win.update()
    # show frame for 500 ms
    for frameN in range(int(round(params['ISI1']*params['frameRate']))):
        mask.draw()
        win.update()
    # show second word for 200 ms
    
    thisResponse = None
    while thisResponse == None:
        clockRT.reset()

#for frameN in range(int(round(params['duration']*params['frameRate']))):
        stim_wordright.draw()
        win.update()

# collect response
        allKeys = event.waitKeys(timeStamped = clockRT)
        for keyTuple in allKeys:
            [thisKey, thisRT] = keyTuple
        for thisKey in allKeys:
            if thisKey[0] in ['escape']:core.quit()
            elif int(thisKey[0]) == corresp:
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