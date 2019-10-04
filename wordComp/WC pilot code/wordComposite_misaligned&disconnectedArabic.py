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
	 'frameRate':60,'duration':0.3, 'ISI1': 0.2, 'ISI2': 0.5,'fp': 0.5,'task':'wordComposite','computer':'raylan'}

dlg = gui.DlgFromDict(params, title='wordComposite', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', params)#save params to file for next time
else:
    core.quit()#the user hit cancel so exit

fileName = params['ID number']+'_misaligned&DisconnectedArb'+'_'+params['computer']
dataFile = open('/home/zahrahussain/Documents/psychopy/data/wordComposite/'+fileName+'.txt', 'a')#a simple text file with 'comma-separated-values'
dataFile.write('word, same, congruent, response, accuracy, RT\n') 

# Create a visual window:
#

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
# fonts: Arial, Al Tarikh, Tahoma

wordlistE=['Arif','Sa2el','Jamal','7okouk','Rojou3','Kafif','Sarir','Jawab','Mourouj','Zamil']
toplist1=[u'عر',u'سا',u'جم',u'حق',u'رج',u'كف',u'سر',u'جو',u'مر',u'زم']
bottomlist1=[u'يف',u'ئل',u'ال',u'وق',u'وع',u'يف',u'ير',u'اب',u'وج',u'يل']

bottomlist2=[u'يض',u'رح',u'يع',u'ول',u'ال',u'وء',u'يع',u'اد',u'يب',u'ان']

bottomlist3=[u'يك',u'صر',u'اس',u'اف',u'ال',u'اء',u'اش',u'ار',u'اب',u'يق']

wordlist1=[u'عريف',u'سائل', u'جمال', u'حقوق',u'رجوع',u'كفيف', u'سرير', u'جواب', u'مروج',u'زميل']
wordlist2=[u'عريض',u'سارح',u'جميع',u'حقول',u'رجال',u'كفوء',u'سريع',u'جواد',u'مريب',u'زمان']
wordlist3=[u'شريك',u'قاصر',u'مقاس',u'شفاف',u'شمال',u'سخاء',u'كباش',u'صوار',u'خراب',u'عميق']
wordlist4=[u'شريف',u'قائل',u'مقال',u'شفوق',u'شموع',u'سخيف',u'كبير',u'صواب',u'خروج',u'عميل']

toplist4=[u'شر',u'قا',u'مق',u'شف',u'شم',u'سخ',u'كب',u'صو',u'خر',u'عم']


#line=visual.Line(win, start=(0,2),end=(0,-3),lineColor=[-1,-1,-1]) #to draw a vertical line separating the word-halves

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
    
    x1=+1.5
    y1=0
    x2=-1.5
    y2=-1
    if trials.thisTrial.top==1: # if 'same' top/misaligned trial
        corresp=1 # correct response = 1
        if trials.thisTrial.cong==1: # if same-congruent/misaligned trial
            stim_left1= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font= textFont, height=stimSize, units='deg', languageStyle='Arabic')
            stim_right1= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            stim_left2=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            stim_right2=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
        else: # if same-incongruent/misaligned trial
            stim_left1= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            stim_right1= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            stim_left2=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            stim_right2=visual.TextStim(win, text=bottomlist2[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
    else: # if 'different' top/misaligned trial
        corresp=2 # incorrect response =2
        if trials.thisTrial.cong==1: # if different-congruent trial
            stim_left1= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            stim_right1= visual.TextStim(win, text=toplist4[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            stim_left2=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            stim_right2=visual.TextStim(win, text=bottomlist3[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
        else: # if different-incongruent/misaligned trial
            stim_left1= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            stim_right1= visual.TextStim(win, text=toplist4[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            stim_left2=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            stim_right2=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
 
# show blank screen for 500 ms
    for frameN in range(int(round(params['ISI2']*params['frameRate']))):
        win.update()

    # show fixation point for one second
    for frameN in range(int(round(params['fp']*params['frameRate']))):
        fixation.draw()
        win.update()
    # show first word for 200 ms
    for frameN in range(int(round(params['duration']*params['frameRate']))):
        stim_left1.draw()
        stim_left2.draw()
        #line.draw()
        win.update()
    # show mask for 500 ms
    for frameN in range(int(round(params['ISI1']*params['frameRate']))):
        mask.draw()
        win.update()
    # show second word for 200 ms
    thisResponse = None
    while thisResponse == None:
        clockRT.reset()

        stim_right1.draw()
        stim_right2.draw()
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
    dataFile.write('%s %s %s %s %s %s\n' %(wordlistE[trials.thisTrial.word], trials.thisTrial.top, trials.thisTrial.cong, thisKey[0], accuracy, round(thisRT,2)))
win.close()
core.quit()