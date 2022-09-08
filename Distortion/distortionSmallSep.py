from psychopy import *
import pygame
from pygame.locals import *
from numpy import sin, pi, cos, tan, arctan, arctanh, arctan2, sqrt
import time
pygame.init()

params = {'A:Observer':'', 'Distance':'114', 'FilterRE':'Red', 'Condition':'', 'Judgement':''}

dlg = gui.DlgFromDict(params, title='distortion', fixed=['dateStr'])
if dlg.OK:
    misc.toFile('lastParams.pickle', params)#save params to file for next time
else:
    core.quit()#the user hit cancel so exit
params['date'] = time.strftime("%b_%d_%H%M", time.localtime())#add the current time
fileName = params['A:Observer'] + '_' + params['Distance']+'_'+params['FilterRE']+'_'+params['Condition']+'_'+params['Judgement'] +'_'+params['date'] 
dataFile = open('/home/zahrahussain/Documents/psychopy/data/distortion/'+fileName+'.txt', 'a')#a simple text file with 'comma-separated-values'
dataFile.write('targetX, targetY,  targetX-512, targetY-384, responseX, responseY, responseX-512, responseY-384, targetOrientationDeg, targetRadiusPixels\n') 

# CHANGED STIMLIST TO X AND Y TO TEST AT SMALL SEPARATIONS; FLIP X AND Y FOR VERTICAL./HORIZONTAL,
# SMALL/LARGE SEPARATIONS; ZH OCT 2014

# Change X and Y round here for separation; yx: hor small, vert large
stimList = []
#for y in [ 59.13, 190.37, 319.02, 447.30, -59.13, -190.37, -319.02, -447.30]: # nottingham
#    for x in [ 24.96, -24.96, 59.2, -59.2 ]: # nottingham
for y in [ -510, -364, -217, -67, 67, 217, 364, 510]: # aub viewpixx
    for x in [ -67, -29, 29, 67 ]: # aub viewpixx
        stimList.append(
        {'xpos':x, 'ypos':y}
        )
bgcolor = 236,233,0
linecolor1 =  0,245,0
linecolor2 = 245, 0, 0

dotradius=9
fixptx=12
fpcolor=0,0,0
fpwidth=3 # default 3
white=255,255,255
black=0,0,0
x = y = 0
resx=1920
resy=1080
cx= (resx/2) #+55
cy= (resy/2) #-10
trials = data.TrialHandler(stimList,7, method='random')
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
#pygame.display.set_gamma(2.117,2.236,2.16)
font = pygame.font.SysFont("Helvetica",30)
#s = font.render("Use the mouse to position the green cursor on top of the red spot.",True,(0,0,0))
#u = font.render("Keep your gaze fixed on the central cross at all times.",True,(0,0,0))
#t = font.render("Hit a key when ready.",True,(0,0,0))
#pygame.mouse.set_visible(0)
#screen.fill(bgcolor)
#screen.blit(s, (resx/4,200))
#screen.blit(u, (resx/3.5,350))
#screen.blit(t, (resx/3,500))
#pygame.display.update()
#event.waitKeys()
pygame.event.clear()
for thisTrial in trials:
    pygame.mouse.set_visible(0)
    screen.fill(bgcolor)
    pygame.display.update()
    pygame.time.wait(1000)
    pygame.mouse.set_pos([resx/2,resy/2])
    running = 1
    trialClock = core.Clock();t=0
    while running:
        t=trialClock.getTime()
        event = pygame.event.poll()
        mouseevent=pygame.mouse.get_pos()
        
       # if (t%1)<0.5:
        
       # pygame.display.update()
        #elif(t%1)>0.5:
#            pygame.draw.line(screen, white, (500, 384),(524,384),3)
#            pygame.draw.line(screen, white, (512, 372),(512,396),3)
#            pygame.display.update()
        
        
        #if event.type == pygame.MOUSEMOTION:
        x = mouseevent[0]
        y=mouseevent[1]
        screen.fill(bgcolor)
#        y1=trials.thisTrial['mag']*sin(trials.thisTrial['ori']*pi/180)
#        x1=trials.thisTrial['mag']*cos(trials.thisTrial['ori']*pi/180)
        x1=trials.thisTrial['xpos']
        y1=trials.thisTrial['ypos']
        y1=round(y1+(resy/2))
        x1=round(x1+(resx/2))
        pygame.mouse.set_visible(0)
        if (t%.125)<.0625:
       # if (t%.133)<.0666:
#         pygame.draw.circle(screen,linecolor1,(x1,y1),9) #tSarget
            screen.fill(bgcolor)
            pygame.draw.circle(screen,linecolor1,(x1,y1),dotradius) #target
#            pygame.draw.line(screen, black, (((cx)-12.0), ((cy))),((cx) +12.0,cy),3.0)
#            pygame.draw.line(screen, black, (cx,((cy)-12.0)),(cx,((cy)+12.0)), 3.0)
            pygame.draw.line(screen, fpcolor, ((((resx/2))-fixptx), ((resy/2))),((resx/2)+fixptx,resy/2),fpwidth)
            pygame.draw.line(screen, fpcolor, (resx/2,((resy/2)-fixptx)),(resx/2,((resy/2)+fixptx)),fpwidth)
#            pygame.draw.line(screen, linecolor1, (((resx/2)-fixptx), ((resy/2))),((resx/2),resy/2),3)
#            pygame.draw.line(screen, linecolor1, (resx/2,((resy/2)-fixptx)),(resx/2,((resy/2))),3)
#            pygame.draw.line(screen, linecolor2, (((resx/2)), ((resy/2))),((resx/2)+fixptx,resy/2),3)
#            pygame.draw.line(screen, linecolor2, (resx/2,((resy/2))),(resx/2,((resy/2)+fixptx)),3)
            
            pygame.display.update()
        elif(t%.125)>.0625:
#            pygame.draw.circle(screen,linecolor1,(x1,y1),dotradius) #target
            pygame.draw.circle(screen, linecolor2, (x,y), dotradius) #cursor (response)
#            pygame.draw.line(screen, black, (((cx)-12), ((cy))),((cx) +12,cy),3)
#            pygame.draw.line(screen, black, (cx,((cy)-12)),(cx,((cy)+12)), 3)
            pygame.draw.line(screen,fpcolor, (((resx/2)-fixptx), ((resy/2))),((resx/2)+fixptx,resy/2),fpwidth) 
            pygame.draw.line(screen, fpcolor, (resx/2,((resy/2)-fixptx)),(resx/2,((resy/2)+fixptx)),fpwidth)
#            pygame.draw.line(screen, linecolor1, (((resx/2)-fixptx), ((resy/2))),((resx/2),resy/2),3)
#            pygame.draw.line(screen, linecolor1, (resx/2,((resy/2)-fixptx)),(resx/2,((resy/2))),3)
#            pygame.draw.line(screen, linecolor2, (((resx/2)), ((resy/2))),((resx/2)+fixptx,resy/2),3)
#            pygame.draw.line(screen, linecolor2, (resx/2,((resy/2))),(resx/2,((resy/2)+fixptx)),3)
            pygame.display.update()
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                pygame.display.quit()
                core.quit()
            elif event.key==pygame.K_SPACE:
                running=0
                pygame.time.wait(200)
                #ButtonPress = event.button
                MousePos = x,y
            
            x2=x1-(resx/2)
            y2=y1-(resy/2)
            m02=MousePos[0]-resx/2
            m12=MousePos[1]-resy/2
            stimOriRad=arctan2(y2,x2)
            rOriRad=arctan2((y-(resy/2)),(x-(resx/2)))
            rOriDeg=rOriRad*(180/pi)
            rMag=sqrt(((x-(resx/2))*(x-(resx/2)))+((y-(resy/2))*(y-(resy/2))))
            dataFile.write('%i,%i,%i,%i,%i,%i,%i,%i,%i,%i\n' %(x1,y1,x2,y2,MousePos[0], MousePos[1], m02,m12,thisTrial.xpos,thisTrial.ypos))
            pygame.event.clear()
            #dataFile.write('%i,%i,%i,%i,%i,%i,%i,%i,%,i\n' %(x1,y1,x2, y2, MousePos[0], MousePos[1], m02, m12, thisTrial.ori))
            #pygame.event.clear()
                
#         print x1,y1,x2,y2
#            print MousePos
#            print m02,m12
#            print thisTrial.ori, stimOriRad, thisTrial.mag
#            print rOriDeg,rOriRad, rMag
                #core.wait(.2)
dataFile.close()
#event.clearEvents()   
pygame.display.quit()
core.quit()
     
