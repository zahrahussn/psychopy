 #This analysis script takes one or more datafiles from BaselineTask as input
 #from a GUI. It then plots the staircases on top of each other on
 #the left and a combined psychometric function from the same data
 #on the right
 
from psychopy import data, gui, core
from psychopy.tools.filetools import fromFile
import pylab
 
#Open a dialog box to select files from
files = gui.fileOpenDlg('.')
if not files:
    core.quit()

#get the data from all the files
allIntensities, allResponses = [],[]
for thisFileName in files:
    thisDat = fromFile(thisFileName)
    allIntensities.append( thisDat.data.coherence)
    allResponses.append( thisDat.data.accuracy)

#plot each staircase
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
print(thresh)

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