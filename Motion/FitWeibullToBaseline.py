 #This analysis script takes the psydat file output by BaselineTas.pyk (file name based on  params)
 #It then plots the staircases on top of each other on
 #the left and a combined psychometric function from the same data
 #on the right
 
from psychopy import data, gui, core
from psychopy.tools.filetools import fromFile
import pylab, platform, pandas
import numpy as np
 
#get the data from the psydat files
if platform.platform()[0:5] == 'Linux':
    params = {'Subject':'pilot1', 'Experimenter':'jb'}
    fileName = params['Experimenter']+'_'+params['Subject']+'_baseline'
    filePath = '../../psychopyData/Motion/'+fileName+'.psydat'
    
    allIntensities, allResponses = [],[]
    trials = fromFile(filePath)
    allIntensities.append(trials.data.coherence)
    allResponses.append(trials.data.accuracy)
    
else:
    # Open a dialog box to select files from  # this doesn't work in Link214 at the moment
    files = gui.fileOpenDlg('../../psychopyData/Motion/')
    if not files:
        core.quit()
    
    allIntensities, allResponses = [],[]
    for thisFileName in files:
        trials = fromFile(thisFileName)
        allIntensities.append(trials.data.coherence)
        allResponses.append(trials.data.accuracy)
    
#plot each staircase
if platform.platform()[0:5] != 'Linux':  # plotting doesn't work in Link214 at the moment
    pylab.subplot(121)
    colors = 'brgkcmbrgkcm'
    lines, names = [],[]
    for fileN, thisStair in enumerate(allIntensities):
        #lines.extend(pylab.plot(thisStair))
        #names = files[fileN]
        pylab.plot(thisStair, label=files[fileN])
    #pylab.legend()
    
#get combined data
combinedInten, combinedResp, combinedN = \
             data.functionFromStaircase(allIntensities, allResponses, 5)

#fit curve - in this case using a Weibull function
fit = data.FitWeibull(combinedInten, combinedResp, guess=[0.2, 0.5])
smoothInt = pylab.arange(min(combinedInten), max(combinedInten), 0.001)
smoothResp = fit.eval(smoothInt)
thresAccuracy = 0.99
thresh = fit.inverse(thresAccuracy)

if platform.platform()[0:5] != 'Linux':  # plotting doesn't work in Link214 at the moment
    #plot curve
    pylab.subplot(122)
    pylab.plot(smoothInt, smoothResp, '-')
    pylab.plot([thresh, thresh],[0,thresAccuracy],'--'); pylab.plot([0, thresh],\
    [thresAccuracy,thresAccuracy],'--')
    pylab.title('threshold = %0.3f' %(thresh))
    #plot points
    pylab.plot(combinedInten, combinedResp, 'o')
    pylab.ylim([0,1])
    
    pylab.show()

# print results
print("\n%s\n" % files)
print(pandas.DataFrame( np.transpose(np.vstack((combinedInten,combinedResp,fit.eval(combinedInten),combinedN))),range(0,len(combinedN)),["Coherence","Accuracy","Fitted","N trials"]))
print("\n99%% Threshold = %.3f\n" % thresh)

