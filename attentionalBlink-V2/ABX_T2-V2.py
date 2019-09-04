from psychopy import *
#from psychopy import sound
import numpy, scipy, pygame
import time, copy, string, strop

params = {'ID number':'1',
	 'frameRate':60,'duration':0.08, 'ISI': 0.03, 'fp': 1,'task':'T2-V2'}


dlg = gui.DlgFromDict(params, title='T2-V2', fixed=['dateStr'])
if dlg.OK:
    misc.toFile('lastParams.pickle', params)#save params to file for next time
else:
    core.quit()#the user hit cancel so exit
    
fileName = params['ID number']+'_'+params['task'] 
dataFile = open(fileName+'.txt', 'a')#a simple text fil e with 'comma-separated-values'
dataFile.write('T1, lag, T2, T2resp, correct2\n') 
    

letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['2','3','4','5','6','7','8','9']
win = visual.Window([1024,768],allowGUI=False, monitor='raylan', units='deg', fullscr=True)
#win= visual.Window([2880,1800],allowGUI=False, monitor='testMonitor2', units='deg', fullscr=True)
#win= visual.Window([700,700],allowGUI=False, monitor='testMonitor', units='deg', fullscr=False)
#win.setGamma([2.25,2.25,2.25])  
target = visual.TextStim(win, pos=[0,0], height=1.5,color=[-1,-1,-1], font='Arial', units='deg')
fixation = visual.PatchStim(win, color=-1, tex=None, mask='circle',size=0.2, units='deg')

# create the list of stimulus conditions: 3 T1 positions, and 8 T2 positions (or 8 lags), i.e., 24 stimulus conditions 
stimList = []
for T1pos in [5,6,7]:
    for T2pres in [1]:
        for T2pos in [1,3,5,7,9]:
            stimList.append({'T1pos': T1pos, 'T2pres': T2pres, 'T2pos': T2pos})
trials = data.TrialHandler(stimList, 15)

for thisTrial in trials:
    
    T1position = trials.thisTrial['T1pos']
    T1=numbers[numpy.random.random_integers(0,7)]
    
    T2position = trials.thisTrial['T1pos'] + trials.thisTrial['T2pos']
    if trials.thisTrial['T2pres']==1:
        T2=numbers[numpy.random.random_integers(0,7)]
    else:
        T2=letters[numpy.random.random_integers(0,25)]
    
     #fixation screen
    for frameN in range(int(round(params['fp']*params['frameRate']))):
        fixation.draw()
        win.update()
        
    for pos in range(1,20):
        
        D=letters[numpy.random.random_integers(0,25)]
          
        if pos == T1position:
           stim=T1
           col=-1
           
        elif pos == T2position:
            stim=T2
            col=-1
            
        else:
            stim=D
            col=-1
            
        stim=visual.TextStim(win, text=stim, pos=[0,0], height=1.5,color=[col,col,col], units='deg')
        for frameN in range(int(round(params['duration']*params['frameRate']))):
                stim.draw()
                win.update()
                
        #blank screen
        for frameN in range(int(round(params['ISI']*params['frameRate']))):
                win.update()

    thisResp2=None
    while thisResp2==None:
        allKeys=event.waitKeys(keyList=['2','3','4','5','6','7','8','9', 'escape'])
        for T2resp in allKeys:
            if T2resp in ['escape']:core.quit()#abort experiment
            #T2resp=T2resp
            if int(T2resp)==int(T2): 
                thisResp2 = 1 
            else: thisResp2 = 0 
            trials.data.add('correct2', thisResp2)  # add the data to our set
    
    event.clearEvents() #must clear other (eg mouse) events - they clog the buffer
    dataFile.write('%s %s %s %s %i\n' %(T1, trials.thisTrial['T2pos'], T2, T2resp, thisResp2))
     
dataFile.close()
win.close()
core.quit()
   
   