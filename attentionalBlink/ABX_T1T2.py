from psychopy import *
#from psychopy import sound
import numpy, scipy, pygame
import time, copy, string, strop

params = {'ID number':'1',
	 'frameRate':60,'duration':0.015, 'ISI': 0.075, 'fp': 1,'task':'T1_T2'}


dlg = gui.DlgFromDict(params, title='T1_T2', fixed=['dateStr'])
if dlg.OK:
    misc.toFile('lastParams.pickle', params)#save params to file for next time
else:
    core.quit()#the user hit cancel so exit
    
fileName = params['ID number']+'_'+params['task'] 
dataFile = open(fileName+'.txt', 'a')#a simple text fil e with 'comma-separated-values'
dataFile.write('T1, T2, lag, T1resp, correct1, T2resp, correct2\n') 
    

letters=['A','B','R','D','E','N','G','H','K','P', 'X']
distractors=['1','2','3','4','5','6','7','8','9']
win = visual.Window([1024,768],allowGUI=False, monitor='boyd', units='deg', fullscr=True)
#win= visual.Window([700,700],allowGUI=False, monitor='testMonitor', units='deg', fullscr=False)
#win.setGamma([2.25,2.25,2.25])  
target = visual.TextStim(win, pos=[0,0], height=1.5,color=[-1,-1,-1], font='Arial', units='deg')
fixation = visual.PatchStim(win, color=-1, tex=None, mask='circle',size=0.2, units='deg')

# create the list of stimulus conditions: 3 T1 positions, and 8 T2 positions (or 8 lags), i.e., 24 stimulus conditions 
stimList = []
for T1pos in [5,7]:
    for T2pres in [0,1]:
        for T2pos in [1,3,5,7,9]:
            stimList.append({'T1pos': T1pos, 'T2pres': T2pres, 'T2pos': T2pos})
trials = data.TrialHandler(stimList, 10)

for thisTrial in trials:
    
    T1position = trials.thisTrial['T1pos']
    T1=letters[numpy.random.random_integers(0,9)]
    
    T2position = trials.thisTrial['T1pos'] + trials.thisTrial['T2pos']
    if trials.thisTrial['T2pres']==1:
        T2=letters[10]
    else:
        T2=distractors[numpy.random.random_integers(0,8)]
    
     #fixation screen
    for frameN in range(int(round(params['fp']*params['frameRate']))):
        fixation.draw()
        win.update()
        
    for pos in range(1,20):
        
        D=distractors[numpy.random.random_integers(0,8)]
          
        if pos == T1position:
           stim=T1
           col=1
           
        elif pos == T2position:
            stim=T2
            col=-1
            
        else:
            stim=D
            col=-1
            
        stim=visual.TextStim(win, text=stim, pos=[0,0], height=1.5, color=[col,col,col], units='deg')
        for frameN in range(int(round(params['duration']*params['frameRate']))):
                stim.draw()
                win.update()
                
        #blank screen
        for frameN in range(int(round(params['ISI']*params['frameRate']))):
                win.update()
                
    thisResp1=None
    while thisResp1==None:
        allKeys=event.waitKeys()
        for T1resp in allKeys:
            if T1resp in ['escape']:core.quit()#abort experiment
            T1resp=string.upper(T1resp)
            if T1resp==T1: 
                thisResp1 = 1 
            else: thisResp1 = 0 
            trials.data.add('correct1', thisResp1)  # add the data to our set
            
    thisResp2=None
    while thisResp2==None:
        allKeys=event.waitKeys()
        for T2resp in allKeys:
            if T2resp in ['escape']:core.quit()#abort experiment
            #T2resp=T2resp
            if int(T2resp)==int(trials.thisTrial['T2pres']): 
                thisResp2 = 1 
            else: thisResp2 = 0 
            trials.data.add('correct2', thisResp2)  # add the data to our set
    
    event.clearEvents() #must clear other (eg mouse) events - they clog the buffer
    dataFile.write('%s %s %s %s %i %s %i\n' %(T1,trials.thisTrial['T2pres'], trials.thisTrial['T2pos'], T1resp, thisResp1, T2resp, thisResp2))
     
dataFile.close()
win.close()
core.quit()
   
   