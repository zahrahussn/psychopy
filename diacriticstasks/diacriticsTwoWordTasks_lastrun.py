#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.0),
    on Wed Jul 28 16:38:31 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.0'
expName = 'diacriticsTwoWordTasks'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/macbook/Desktop/Documents/ZH/diacriticsTask/diacriticsTwoWordTasks/diacriticsTwoWordTasks_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "commoneInstructions"
commoneInstructionsClock = core.Clock()
CommonInst = visual.ImageStim(
    win=win,
    name='CommonInst', 
    image='InstructionsCommon.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.5, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "innitialCode"
innitialCodeClock = core.Clock()
randint = function(min, maxplusone) {
  return Math.floor((Math.random() * (maxplusone - min) )) + min;
}

/* The randint() function on python includes the lower limit and excludes the upper limit,
i.e.: (0,3) would yiled three numbers: 0, 1, 2. 
When it is converting it to Javascript, it includes the upper limit,
i.e.: (0,3) would yield 4 numbers: 0, 1, 2, 3. 
This code component changes the conversion to Javascript, in order for it to match python.*/
list_Dist=["أوعد","مسعود","محول","أسعد","أعرج","خارج","مسألة","أخرج","قائم","يقول","تراث","قائل","جريح","صارح","معرض","صريح","محالة","يقولون","عصافير","مقالة","ارتدى","عداوة","حقيبة","اعتدى","سلاح","سامح","قاتل","سماح","أبان","مدين","شعور","أدان","أركب","مرعب","ساعد","أرعب","أدبر","مجبر","راحل","أجبر","أعلم","سالم","راجع","أسلم","ركوع","أرجع","قارئ","رجوع","كميح","معلد","كماح","منيق","مرتى","منيد","ساقر","أقان","ساقل","ميهود","أرفب","موهود","مرزوب","تدراس","مربوب","فاخق","صدير","صاخق","كهتلس","ضذمرن","كملتس","طغهمق","ثغدهق","نغهمق","حلشخ","خجنق","ظلشخ","فقدم","رسته","بقدم","سرذق","مكزص","سرذم","خلقص","دهرف","خصقض",]
fontsize=0.2


# Initialize components for Routine "LDInst1"
LDInst1Clock = core.Clock()
LDInst_1 = visual.ImageStim(
    win=win,
    name='LDInst_1', 
    image='Lex-InstArb1.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.5, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "LDInst2"
LDInst2Clock = core.Clock()
LDInst_2 = visual.ImageStim(
    win=win,
    name='LDInst_2', 
    image='Lex-InstArb2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.5, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "LDInst3"
LDInst3Clock = core.Clock()
LDInst_4 = visual.ImageStim(
    win=win,
    name='LDInst_4', 
    image='Lex-InstArb4.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.5, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "LDInst4"
LDInst4Clock = core.Clock()
LDInst = visual.ImageStim(
    win=win,
    name='LDInst', 
    image='Lex-InstArb3.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.5, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "LDPracticeInst"
LDPracticeInstClock = core.Clock()
practiceInst = visual.ImageStim(
    win=win,
    name='practiceInst', 
    image='Lex-InstPractice.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.5, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "fixationInst"
fixationInstClock = core.Clock()
fixationInst_1 = visual.ImageStim(
    win=win,
    name='fixationInst_1', 
    image='Reminder.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.5, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "practiceWord"
practiceWordClock = core.Clock()
xstim1_D=""
ystim1_D=""
stim1_D=""

fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',
    size=(0.04,0.04),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
noiseImage = visual.ImageStim(
    win=win,
    name='noiseImage', 
    image='noiseRect.png', mask=None,
    ori=0.0, pos=[0,0], size=(0.5, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
noiseImage_D = visual.ImageStim(
    win=win,
    name='noiseImage_D', 
    image='noiseRect.png', mask=None,
    ori=0.0, pos=[0,0], size=(0.5, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
wordPractice = visual.TextStim(win=win, name='wordPractice',
    text='',
    font='Courier',
    pos=[0,0], height=fontsize, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
distWord = visual.TextStim(win=win, name='distWord',
    text='',
    font='Courier',
    pos=[0,0], height=fontsize, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
cue = visual.Line(
    win=win, name='cue',
    start=(-(0.65, 0.65)[0]/2.0, 0), end=(+(0.65, 0.65)[0]/2.0, 0),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-6.0, interpolate=True)
PracticeResponse = keyboard.Keyboard()

# Initialize components for Routine "feedbackResponse"
feedbackResponseClock = core.Clock()
soundfile=['Correct.wav','Incorrect.wav']

feedback = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='feedback')
feedback.setVolume(1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "commoneInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
commoneInstructionsComponents = [CommonInst, key_resp]
for thisComponent in commoneInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
commoneInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "commoneInstructions"-------
while continueRoutine:
    # get current time
    t = commoneInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=commoneInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CommonInst* updates
    if CommonInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        CommonInst.frameNStart = frameN  # exact frame index
        CommonInst.tStart = t  # local t and not account for scr refresh
        CommonInst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(CommonInst, 'tStartRefresh')  # time at next scr refresh
        CommonInst.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in commoneInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "commoneInstructions"-------
for thisComponent in commoneInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('CommonInst.started', CommonInst.tStartRefresh)
thisExp.addData('CommonInst.stopped', CommonInst.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "commoneInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "innitialCode"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
innitialCodeComponents = []
for thisComponent in innitialCodeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
innitialCodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "innitialCode"-------
while continueRoutine:
    # get current time
    t = innitialCodeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=innitialCodeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in innitialCodeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "innitialCode"-------
for thisComponent in innitialCodeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "innitialCode" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "LDInst1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
LDInst1Components = [LDInst_1, key_resp_2]
for thisComponent in LDInst1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LDInst1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "LDInst1"-------
while continueRoutine:
    # get current time
    t = LDInst1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LDInst1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *LDInst_1* updates
    if LDInst_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        LDInst_1.frameNStart = frameN  # exact frame index
        LDInst_1.tStart = t  # local t and not account for scr refresh
        LDInst_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(LDInst_1, 'tStartRefresh')  # time at next scr refresh
        LDInst_1.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LDInst1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "LDInst1"-------
for thisComponent in LDInst1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('LDInst_1.started', LDInst_1.tStartRefresh)
thisExp.addData('LDInst_1.stopped', LDInst_1.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "LDInst1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "LDInst2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
LDInst2Components = [LDInst_2, key_resp_3]
for thisComponent in LDInst2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LDInst2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "LDInst2"-------
while continueRoutine:
    # get current time
    t = LDInst2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LDInst2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *LDInst_2* updates
    if LDInst_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        LDInst_2.frameNStart = frameN  # exact frame index
        LDInst_2.tStart = t  # local t and not account for scr refresh
        LDInst_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(LDInst_2, 'tStartRefresh')  # time at next scr refresh
        LDInst_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LDInst2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "LDInst2"-------
for thisComponent in LDInst2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('LDInst_2.started', LDInst_2.tStartRefresh)
thisExp.addData('LDInst_2.stopped', LDInst_2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "LDInst2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "LDInst3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
LDInst3Components = [LDInst_4, key_resp_4]
for thisComponent in LDInst3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LDInst3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "LDInst3"-------
while continueRoutine:
    # get current time
    t = LDInst3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LDInst3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *LDInst_4* updates
    if LDInst_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        LDInst_4.frameNStart = frameN  # exact frame index
        LDInst_4.tStart = t  # local t and not account for scr refresh
        LDInst_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(LDInst_4, 'tStartRefresh')  # time at next scr refresh
        LDInst_4.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LDInst3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "LDInst3"-------
for thisComponent in LDInst3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('LDInst_4.started', LDInst_4.tStartRefresh)
thisExp.addData('LDInst_4.stopped', LDInst_4.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "LDInst3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "LDInst4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
LDInst4Components = [LDInst, key_resp_5]
for thisComponent in LDInst4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LDInst4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "LDInst4"-------
while continueRoutine:
    # get current time
    t = LDInst4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LDInst4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *LDInst* updates
    if LDInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        LDInst.frameNStart = frameN  # exact frame index
        LDInst.tStart = t  # local t and not account for scr refresh
        LDInst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(LDInst, 'tStartRefresh')  # time at next scr refresh
        LDInst.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LDInst4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "LDInst4"-------
for thisComponent in LDInst4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('LDInst.started', LDInst.tStartRefresh)
thisExp.addData('LDInst.stopped', LDInst.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "LDInst4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "LDPracticeInst"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
LDPracticeInstComponents = [practiceInst, key_resp_6]
for thisComponent in LDPracticeInstComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LDPracticeInstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "LDPracticeInst"-------
while continueRoutine:
    # get current time
    t = LDPracticeInstClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LDPracticeInstClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceInst* updates
    if practiceInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceInst.frameNStart = frameN  # exact frame index
        practiceInst.tStart = t  # local t and not account for scr refresh
        practiceInst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceInst, 'tStartRefresh')  # time at next scr refresh
        practiceInst.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LDPracticeInstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "LDPracticeInst"-------
for thisComponent in LDPracticeInstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practiceInst.started', practiceInst.tStartRefresh)
thisExp.addData('practiceInst.stopped', practiceInst.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "LDPracticeInst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixationInst"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
fixationInstComponents = [fixationInst_1, key_resp_7]
for thisComponent in fixationInstComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixationInstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixationInst"-------
while continueRoutine:
    # get current time
    t = fixationInstClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixationInstClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixationInst_1* updates
    if fixationInst_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixationInst_1.frameNStart = frameN  # exact frame index
        fixationInst_1.tStart = t  # local t and not account for scr refresh
        fixationInst_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixationInst_1, 'tStartRefresh')  # time at next scr refresh
        fixationInst_1.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationInstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixationInst"-------
for thisComponent in fixationInstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixationInst_1.started', fixationInst_1.tStartRefresh)
thisExp.addData('fixationInst_1.stopped', fixationInst_1.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
# the Routine "fixationInst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practiceTrial = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PracticeArb.xlsx'),
    seed=None, name='practiceTrial')
thisExp.addLoop(practiceTrial)  # add the loop to the experiment
thisPracticeTrial = practiceTrial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
if thisPracticeTrial != None:
    for paramName in thisPracticeTrial:
        exec('{} = thisPracticeTrial[paramName]'.format(paramName))

for thisPracticeTrial in practiceTrial:
    currentLoop = practiceTrial
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial:
            exec('{} = thisPracticeTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practiceWord"-------
    continueRoutine = True
    # update component parameters for each repeat
    D_int=randint(0,84)
    
    xstim1_D=-xword1
    ystim1_D=-yword1
    stim1_D=list_Dist[int(D_int)]
    
    if D_int<48:
        distractor="word"
    elif D_int>66:
        distractor="consonants"
    else:
        distractor="word" 
    noiseImage.setPos((xword1,yword1))
    noiseImage_D.setPos((xstim1_D,ystim1_D))
    wordPractice.setPos((xword1, yword1))
    wordPractice.setText(word1)
    distWord.setPos((xstim1_D, ystim1_D))
    distWord.setText(stim1_D
)
    cue.setPos((xword1, -0.11))
    PracticeResponse.keys = []
    PracticeResponse.rt = []
    _PracticeResponse_allKeys = []
    # keep track of which components have finished
    practiceWordComponents = [fixation, noiseImage, noiseImage_D, wordPractice, distWord, cue, PracticeResponse]
    for thisComponent in practiceWordComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceWordClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceWord"-------
    while continueRoutine:
        # get current time
        t = practiceWordClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceWordClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        
        # *noiseImage* updates
        if noiseImage.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
            # keep track of start time/frame for later
            noiseImage.frameNStart = frameN  # exact frame index
            noiseImage.tStart = t  # local t and not account for scr refresh
            noiseImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noiseImage, 'tStartRefresh')  # time at next scr refresh
            noiseImage.setAutoDraw(True)
        if noiseImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noiseImage.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                noiseImage.tStop = t  # not accounting for scr refresh
                noiseImage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(noiseImage, 'tStopRefresh')  # time at next scr refresh
                noiseImage.setAutoDraw(False)
        
        # *noiseImage_D* updates
        if noiseImage_D.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
            # keep track of start time/frame for later
            noiseImage_D.frameNStart = frameN  # exact frame index
            noiseImage_D.tStart = t  # local t and not account for scr refresh
            noiseImage_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noiseImage_D, 'tStartRefresh')  # time at next scr refresh
            noiseImage_D.setAutoDraw(True)
        if noiseImage_D.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noiseImage_D.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                noiseImage_D.tStop = t  # not accounting for scr refresh
                noiseImage_D.frameNStop = frameN  # exact frame index
                win.timeOnFlip(noiseImage_D, 'tStopRefresh')  # time at next scr refresh
                noiseImage_D.setAutoDraw(False)
        
        # *wordPractice* updates
        if wordPractice.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
            # keep track of start time/frame for later
            wordPractice.frameNStart = frameN  # exact frame index
            wordPractice.tStart = t  # local t and not account for scr refresh
            wordPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wordPractice, 'tStartRefresh')  # time at next scr refresh
            wordPractice.setAutoDraw(True)
        if wordPractice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wordPractice.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                wordPractice.tStop = t  # not accounting for scr refresh
                wordPractice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wordPractice, 'tStopRefresh')  # time at next scr refresh
                wordPractice.setAutoDraw(False)
        
        # *distWord* updates
        if distWord.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
            # keep track of start time/frame for later
            distWord.frameNStart = frameN  # exact frame index
            distWord.tStart = t  # local t and not account for scr refresh
            distWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distWord, 'tStartRefresh')  # time at next scr refresh
            distWord.setAutoDraw(True)
        if distWord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > distWord.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                distWord.tStop = t  # not accounting for scr refresh
                distWord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(distWord, 'tStopRefresh')  # time at next scr refresh
                distWord.setAutoDraw(False)
        
        # *cue* updates
        if cue.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
            # keep track of start time/frame for later
            cue.frameNStart = frameN  # exact frame index
            cue.tStart = t  # local t and not account for scr refresh
            cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue, 'tStartRefresh')  # time at next scr refresh
            cue.setAutoDraw(True)
        if cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                cue.tStop = t  # not accounting for scr refresh
                cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue, 'tStopRefresh')  # time at next scr refresh
                cue.setAutoDraw(False)
        
        # *PracticeResponse* updates
        waitOnFlip = False
        if PracticeResponse.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
            # keep track of start time/frame for later
            PracticeResponse.frameNStart = frameN  # exact frame index
            PracticeResponse.tStart = t  # local t and not account for scr refresh
            PracticeResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PracticeResponse, 'tStartRefresh')  # time at next scr refresh
            PracticeResponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(PracticeResponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(PracticeResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if PracticeResponse.status == STARTED and not waitOnFlip:
            theseKeys = PracticeResponse.getKeys(keyList=['1', '2', 'esc'], waitRelease=False)
            _PracticeResponse_allKeys.extend(theseKeys)
            if len(_PracticeResponse_allKeys):
                PracticeResponse.keys = _PracticeResponse_allKeys[-1].name  # just the last key pressed
                PracticeResponse.rt = _PracticeResponse_allKeys[-1].rt
                # was this correct?
                if (PracticeResponse.keys == str(corrAns)) or (PracticeResponse.keys == corrAns):
                    PracticeResponse.corr = 1
                else:
                    PracticeResponse.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceWordComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceWord"-------
    for thisComponent in practiceWordComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceTrial.addData('distractor',distractor)
    practiceTrial.addData('fixation.started', fixation.tStartRefresh)
    practiceTrial.addData('fixation.stopped', fixation.tStopRefresh)
    practiceTrial.addData('noiseImage.started', noiseImage.tStartRefresh)
    practiceTrial.addData('noiseImage.stopped', noiseImage.tStopRefresh)
    practiceTrial.addData('noiseImage_D.started', noiseImage_D.tStartRefresh)
    practiceTrial.addData('noiseImage_D.stopped', noiseImage_D.tStopRefresh)
    practiceTrial.addData('wordPractice.started', wordPractice.tStartRefresh)
    practiceTrial.addData('wordPractice.stopped', wordPractice.tStopRefresh)
    practiceTrial.addData('distWord.started', distWord.tStartRefresh)
    practiceTrial.addData('distWord.stopped', distWord.tStopRefresh)
    practiceTrial.addData('cue.started', cue.tStartRefresh)
    practiceTrial.addData('cue.stopped', cue.tStopRefresh)
    # check responses
    if PracticeResponse.keys in ['', [], None]:  # No response was made
        PracticeResponse.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           PracticeResponse.corr = 1;  # correct non-response
        else:
           PracticeResponse.corr = 0;  # failed to respond (incorrectly)
    # store data for practiceTrial (TrialHandler)
    practiceTrial.addData('PracticeResponse.keys',PracticeResponse.keys)
    practiceTrial.addData('PracticeResponse.corr', PracticeResponse.corr)
    if PracticeResponse.keys != None:  # we had a response
        practiceTrial.addData('PracticeResponse.rt', PracticeResponse.rt)
    practiceTrial.addData('PracticeResponse.started', PracticeResponse.tStartRefresh)
    practiceTrial.addData('PracticeResponse.stopped', PracticeResponse.tStopRefresh)
    # the Routine "practiceWord" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackResponse"-------
    continueRoutine = True
    # update component parameters for each repeat
    if PracticeResponse.corr:
        feedback1=soundfile[0]
    else:
        feedback1=soundfile[1]
    feedback.setSound('feedback1', hamming=True)
    feedback.setVolume(1.0, log=False)
    # keep track of which components have finished
    feedbackResponseComponents = [feedback]
    for thisComponent in feedbackResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackResponse"-------
    while continueRoutine:
        # get current time
        t = feedbackResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop feedback
        if feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback.frameNStart = frameN  # exact frame index
            feedback.tStart = t  # local t and not account for scr refresh
            feedback.tStartRefresh = tThisFlipGlobal  # on global time
            feedback.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackResponse"-------
    for thisComponent in feedbackResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    feedback.stop()  # ensure sound has stopped at end of routine
    practiceTrial.addData('feedback.started', feedback.tStartRefresh)
    practiceTrial.addData('feedback.stopped', feedback.tStopRefresh)
    # the Routine "feedbackResponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practiceTrial'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
