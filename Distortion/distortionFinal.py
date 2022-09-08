from psychopy import *
import pygame
from pygame.locals import *
from numpy import sin, pi, cos, tan, arctan, arctanh, arctan2, sqrt
import time
pygame.init()

params = {'A:Observer':'', 'Distance':'114', 'FilterRE':'Red', 'Monoc or Dichoptic':'Dichoptic','Prism':'ZeroDiop'}

dlg = gui.DlgFromDict(params, title='distortion', fixed=['dateStr'])
if dlg.OK:
    misc.toFile('lastParams.pickle', params)#save params to file for next time
else:
    core.quit()#the user hit cancel so exit
params['date'] = time.strftime("%b_%d_%H%M", time.localtime())#add the current time
fileName = params['A:Observer'] + '_' + params['Distance']+'_'+params['FilterRE']+'_'+params['Monoc or Dichoptic']+'_'+params['Prism']+'_'+params['date'] 
dataFile = open('/home/zahrahussain/Documents/psychopy/data/distortion/'+fileName+'.txt', 'a')#a simple text file with 'comma-separated-values'
dataFile.write('targetX, targetY,  targetX-resx, targetY-resy, responseX, responseY, responseX-resx, responseY-resy, targetOrientationDeg, targetRadiusPixels\n') 

stimList = []
for theta in [ 22.5, 67.5000 , 112.5000 , 157.5000 , 202.5000,  247.5000 , 292.5000 , 337.5000]:
#for theta in [ 22.5, 157.5000 , 202.5000,  337.5000]:
#for theta in [3.19, 7.59]:
#for theta in [67.5000 , 112.5000 , 247.5000 , 292.5000]:
    # for radius in [ 64.0, 192.0, 320.0, 448.0 ]: # nottingham
    for radius in [ 73, 73*3, 73*5, 73*7 ]: # aub viewpixx
#    for radius in [448]:
        stimList.append(
        {'ori':theta, 'mag':radius}
        )
bgcolor = 236,233,0
linecolor1 =  0,245,0
#linecolor2 =  0.0, 245.0, 0.0
#linecolor = 245.0, 0.0, 0.0 # changed for Jamie Oct 30 2014

linecolor2 = 245, 0, 0
dotradius=9
#dotradius=5.0
fixptx=12
#fixptx=6.0
fpcolor=0,0,0
#fpcolor=linecolor1
fpwidth=3 # default 3
#fpwidth=2.0 # default 3
#fpcolor=linecolor1


white=255.0,255.0,255.0
black=0,0,0
#black=0.0, 245.0, 0.0
x = y = 0.0
#resx=1280.0;
#resy=1024.0;
resx=1920;
resy=1080;
cx= (resx/2) #+55
cy= (resy/2) #-10
trials = data.TrialHandler(stimList,7, method='random')
#screen = pygame.display.set_mode((1024,780), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
#screen = pygame.display.set_mode((800, 400))
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
        y = mouseevent[1]
        screen.fill(bgcolor)
        y1=trials.thisTrial['mag']*sin(trials.thisTrial['ori']*pi/180)
        x1=trials.thisTrial['mag']*cos(trials.thisTrial['ori']*pi/180)
        y1=y1+(resy/2)
        x1=x1+(resx/2)
        pygame.mouse.set_visible(0)
        if (t%.125)<.0625:
       # if (t%.133)<.0666:
#         pygame.draw.circle(screen,linecolor1,(x1,y1),9) #tSarget
            screen.fill(bgcolor)
            pygame.draw.circle(screen,linecolor1,(int(x1),int(y1)),(dotradius)) #target
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
               #pygame.quit()
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
            dataFile.write('%i,%i,%i,%i,%i,%i,%i,%i,%i,%i\n' %(x1,y1,x2,y2,MousePos[0], MousePos[1], m02,m12,thisTrial.ori,thisTrial.mag))
            pygame.event.clear()
            #dataFile.write('%i,%i,%i,%i,%i,%i,%i,%i,%,i\n' %(x1,y1,x2, y2, MousePos[0], MousePos[1], m02, m12, thisTrial.ori))
            #pygame.event.clear()
                
#            print x1,y1,x2,y2
#            print MousePos
#            print m02,m12
#            print thisTrial.ori, stimOriRad, thisTrial.mag
#            print rOriDeg,rOriRad, rMag
                #core.wait(.2)
dataFile.close()
#event.clearEvents()   
pygame.display.quit()
core.quit()
     
