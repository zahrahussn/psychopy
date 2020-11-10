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

fileName = params['ID number']+'_misalignedArb'
dataFile = open('/home/zahrahussain/Documents/psychopy/data/wordComposite/Guards/'+fileName+'.txt', 'a') #data file is saved in the file called Guards
#dataFile = open(fileName+'.txt', 'a')#a simple text file with 'comma-separated-values'
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
#In this code the word will be displayed twice above each other and grey rectangles will hide half the words to make the misalignement smoother and the spacing between the misaligned letters smaller.
wordlistE=['7okouk','Sa2el','Jamal','Dorous','Mi3taf','Sadek']
toplist1=[u'حقوق',u'سائل', u'جمال',u'دروس', u'معطف',u'صادق']
toplist2=[u'وثوق',u'قبائل',u'سعال',u'مغروس',u'يخطف',u'خردق']
toplist3=[u'شقوق',u'قائل',u'كمال',u'عروس',u'ملطف',u'فنادق']
toplist4=[u'محقوق',u'مسائل',u'إجمال',u'مدروس',u'ألطف',u'صوادق']
toplist5=[u'مرير',u'حكيم',u'ملعب',u'زميل',u'كبير',u'ربيع']

bottomlist1=[u'حقوق',u'سائل', u'جمال',u'دروس', u'معطف',u'صادق']
bottomlist2=[u'حقيبة',u'سارح',u'جميع',u'درجة',u'معبر',u'صابر']
bottomlist3=[u'حقول',u'سائح',u'جماد',u'دروب',u'معرف',u'صادر']
bottomlist4=[u'حقائق',u'سائلة',u'جميل',u'دراسة',u'معطوف',u'صادقة']

bottomlist5=[u'مرير',u'حكيم',u'ملعب',u'زميل',u'كبير',u'ربيع']

line=visual.Line(win, start=(0,2),end=(0,-3),lineColor=[-1,-1,-1]) #to draw a vertical line separating the word-halves

# setup trial handler
stimList=[]
for word in range(0,6): #This will yield 6 words
    for cue in ['left', 'right']: # left right
        for resp in ['same', 'different']: # same different
           for cong in ['congruent', 'incongControl','incongForm','incongMorph']: # congruent incongruent
            stimList.append({'cue': cue, 'resp': resp, 'cong': cong, 'word': word})
trials = data.TrialHandler(stimList, 2)
trials.data.addDataType('accuracy')
trials.data.addDataType('RT')
clockRT = core.Clock() 

for thisTrial in trials:

    x1=0
    y1=0.5
    x2=0
    y2=-1.1
    if trials.thisTrial.cue=='right': #if right is target
        cue=cueRight
        if trials.thisTrial.resp=='same': # if same trial
            corresp=1 # correct response = 1
            if trials.thisTrial.cong=='congruent': # if congruent trial
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font= textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            elif trials.thisTrial.cong=='incongControl': #Target half same, other half completely different & no root word in common.
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font= textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist2[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            elif trials.thisTrial.cong=='incongForm': #Target half same, other half is orthographically different by 1 letter, & no root word in common.
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font= textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist3[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            else: #Target half same, other half has root in common (and some letters).
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font= textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist4[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')

        else: # if 'different' top/misaligned trial
            corresp=2 # correct response =2
            if trials.thisTrial.cong=='congruent': # if congruent trial
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font= textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist5[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist5[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            elif trials.thisTrial.cong=='incongControl': #Target half different, other half same & no root word in common
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist2[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            elif trials.thisTrial.cong=='incongForm': #Target half different, other half same, word orthographically different by 1 letter, & no root word in common.
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist3[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            else: #Incongmorph 
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist4[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')

    else: # left target
        cue=cueLeft
        if trials.thisTrial.resp=='same': # if same trial
            corresp=1 # correct response = 1
            if trials.thisTrial.cong=='congruent': # if congruent trial
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font= textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            elif trials.thisTrial.cong=='incongControl': #Target half different, other half same & no root word in common
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist2[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            elif trials.thisTrial.cong=='incongForm': #Target half different, other half same, word orthographically different by 1 letter, & no root word in common.
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist3[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            else:
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist4[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')

        else: # if 'different' top/misaligned trial
            corresp=2 # incorrect response =2
            if trials.thisTrial.cong=='congruent': # if congruent trial
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist5[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist5[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            elif trials.thisTrial.cong=='incongControl': #Target half different, other half same & no root word in common
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist2[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            elif trials.thisTrial.cong=='incongForm': #Target half different, other half same, word orthographically different by 1 letter, & no root word in common.
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist3[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
            else:
                word1_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_right= visual.TextStim(win, text=toplist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x1,y1],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word1_left=visual.TextStim(win, text=bottomlist1[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')
                word2_left=visual.TextStim(win, text=bottomlist4[trials.thisTrial.word], color =(-1,-1,-1), pos=[x2,y2],font=textFont, height=stimSize, units='deg', languageStyle='Arabic')

    stim=wordlistE[trials.thisTrial.word]        
    g=numpy.random.randint(0,1) #to choose which of the word pairs will be a target and which will be the study word. 
    

    #The 4 letter words that are disconnected between the 2nd and 3rd letters are very far apart when x=1.75; identifying these words using the bounding box so that I decrease their x position.     
    width1=word1_left.boundingBox
    width2=word2_left.boundingBox
    width3=word1_right.boundingBox
    width4=word2_right.boundingBox
#    print(width1)
#    print(width2)
#    print(width3)
#    print(width4)
    square1Vert= [(-5,-0.9),(-5,1.5),(0,1.5),(0,-0.9)]
    square1= ShapeStim(win, vertices=square1Vert, fillColor=[0,0,0], lineWidth=0, size=.7)
    square2Vert= [(0,-0.82),(5,-0.82),(5,-3.5),(0,-3.5)]
    square2= ShapeStim(win, vertices=square2Vert, fillColor=[0,0,0], lineWidth=0, size=.7)

# #These loops help set the 2 halves of the 4 letter disconnected words closer to the midline as they normally would appear if they were aligned. 
#    if width1[0]<171:
#        word1_left.pos=[-1.2,-1]
#        print(word1_left.pos)
#    else :
#        x1=x1
#    if width2[0]<171:
#        word2_left.pos=[-1.2,-1]
# #       print(word2_left.pos)
#    else:
#        x1=x1
#    if width3[0]<171:
#        word1_right.pos=[1,0]
# #       print(word1_right.pos)
#    else:
#        x1=x1
#    if width4[0]<171:
#        word2_right.pos=[1,0]
#  #      print(word2_right.pos)
#    else:
#        x1=x1
    #changing the coordinates of the problematic words such that they are aligned better and closer to the line bisecting the word.
#bottomlist4 words
    if trials.thisTrial.cue=='right' and trials.thisTrial.resp=='same' and trials.thisTrial.cong=='incongMorph' and trials.thisTrial.word in [0,1,3,5]:
        word2_left.pos=[-0.5,-1.1]
    elif trials.thisTrial.cue=='left' and trials.thisTrial.resp=='different' and trials.thisTrial.cong=='incongMorph' and trials.thisTrial.word in [0,1,3,5]:
        word2_left.pos=[-0.5,-1.1]
# ma3touf
    if trials.thisTrial.cue=='right' and trials.thisTrial.resp=='same' and trials.thisTrial.cong=='incongMorph' and trials.thisTrial.word in [4]:
        word2_left.pos=[-0.6,-1.1]
    elif trials.thisTrial.cue=='left' and trials.thisTrial.resp=='different' and trials.thisTrial.cong=='incongMorph' and trials.thisTrial.word in [4]:
        word2_left.pos=[-0.6,-1.1]
   #Sa2ela
    if trials.thisTrial.cue=='right' and trials.thisTrial.resp=='same' and trials.thisTrial.cong=='incongMorph' and trials.thisTrial.word in [1]:
        word2_left.pos=[-0.6,-1.1]
    elif trials.thisTrial.cue=='left' and trials.thisTrial.resp=='different' and trials.thisTrial.cong=='incongMorph' and trials.thisTrial.word in [1]:
        word2_left.pos=[-0.6,-1.1]
#Masa2el
    if trials.thisTrial.cue=='right' and trials.thisTrial.resp=='different' and trials.thisTrial.cong=='incongMorph' and trials.thisTrial.word in [1,2,3,5]:
        word2_right.pos=[0.5,0.5]
    elif trials.thisTrial.cue=='left' and trials.thisTrial.resp=='same' and trials.thisTrial.cong=='incongMorph' and trials.thisTrial.word in [1,2,3,5]:
        word2_right.pos=[0.5,0.5]

#fanadek
    if trials.thisTrial.cue=='right' and trials.thisTrial.resp=='different' and trials.thisTrial.cong=='incongForm' and trials.thisTrial.word in [5]:
        word2_right.pos=[0.5,0.5]
    elif trials.thisTrial.cue=='left' and trials.thisTrial.resp=='same' and trials.thisTrial.cong=='incongForm' and trials.thisTrial.word in [5]:
        word2_right.pos=[0.5,0.5]
    #حقيبة
    if trials.thisTrial.cue=='right' and trials.thisTrial.resp=='same' and trials.thisTrial.cong=='incongControl' and trials.thisTrial.word in [0]:
        word2_left.pos=[-0.5,-1.1]
    elif trials.thisTrial.cue=='left' and trials.thisTrial.resp=='different' and trials.thisTrial.cong=='incongControl' and trials.thisTrial.word in [0]:
        word2_left.pos=[-0.5,-1.1]

    #قبائل
    if trials.thisTrial.cue=='right' and trials.thisTrial.resp=='different' and trials.thisTrial.cong=='incongControl' and trials.thisTrial.word in [1,3]:
        word2_right.pos=[0.5,0.5]
    elif trials.thisTrial.cue=='left' and trials.thisTrial.resp=='same' and trials.thisTrial.cong=='incongControl' and trials.thisTrial.word in [1,3]:
        word2_right.pos=[0.5,0.5]
  #Rabi3
    if trials.thisTrial.cue=='right' and trials.thisTrial.resp=='different' and trials.thisTrial.cong=='congruent' and trials.thisTrial.word in [1,5]:
        word2_left.pos=[0.2,-1.1]
        word2_right.pos=[0,0.6]
    elif trials.thisTrial.cue=='left' and trials.thisTrial.resp=='different' and trials.thisTrial.cong=='congruent' and trials.thisTrial.word in [1,5]:
        word2_left.pos=[0.2,-1.1]
        word2_right.pos=[0.,0.6]

#7okoul
    if trials.thisTrial.cue=='right' and trials.thisTrial.resp=='same' and trials.thisTrial.cong=='incongForm' and trials.thisTrial.word in [0]:
        word2_left.pos=[0.2,-1.1]
    elif trials.thisTrial.cue=='left' and trials.thisTrial.resp=='different' and trials.thisTrial.cong=='incongForm' and trials.thisTrial.word in [0]:
        word2_left.pos=[0.2,-1.1]


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
        square1.draw()
        square2.draw()
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
    square1.draw()
    square2.draw()
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
