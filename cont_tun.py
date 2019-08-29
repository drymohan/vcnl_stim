#!/usr/bin/env python2

from stim_utils import *
import barparameters as par
import serial
import csv

#set trial parameters here
Unitnum=1
Runnum=1
Eye='right' #('right' for right eye; 'left' for left eye) 
numTrials= 2
blanktime=1

#Set stimulus Parameters here

length=1 #Length of the bar.
width=0.5 # Width of the bar.par
speed=10 # Speed of the bar in degrees per second
sweeplength=5 # Sweep length (works as in visage)
dl=1 #dark bar= -1 or light bar =1.
ori=0 # contrast value between 0 to 1 (0=0% contrast; 1=100% contrast)
disp=0
#Orientation Parameters

st_cont=0.1
end_cont=1
steps=0.1

# DO NOT CHANGE THE CODE BELOW THIS POINT

contrast=np.arange(st_cont, end_cont, steps)


# define the marker values. Markers will start at 1.
markers=np.arange(np.size(par.contrast))+1


win = visual.Window(
    size=[1280, 1024],
    monitor='vcnl',
    units = 'deg',
    fullscr=True, allowGUI=False, waitBlanking=True
    )
frame_rate = 75 # s^-1
frame_time = 1/frame_rate # seconds

bar_width = par.width

bar_length = par.length

# How many sweeps through the center the bar makes (2 -> "there and back again")
n_sweeps = 2

# Center of bar sweep (center of screen is 0,0)
x_center, y_center = 0, 0 # degs

# total length of one sweep (through the center)
sweep_length = par.sweeplength # degs

# Degrees covered per second
sweep_speed = par.speed # degs / s


ori = par.orientation
contrasts= par.contrast


bar = visual.Rect(win, width = bar_width, height = bar_length, lineColor=None, fillColor=par.dl, ori = psychopy_ori(ori))
bar.useShaders=True
blank=visual.Rect(win, fillColor= 0, lineColor=None)
sq_blank=visual.Rect(win, width=1.5, height=1.5, lineColor=None, fillColor= -1)
sq_blank.pos=[-7.8,6]
#sq.pos=[1-0.1, 1-0.1]
core.wait(4)
for numTrials in range(par.numTrials):
    for cidx in range(len(contrasts)):
        if event.getKeys(keyList = ['q']):
            core.quit() 

        bar.contrast = contrasts[cidx]
        setMarker(markers[cidx])
        
        
        blank.draw()
        sq_blank.draw()
        win.flip()
        core.wait(1)
        
        animate_sweeping_bar(
                x_center = x_center, y_center=y_center,
                sweep_length = sweep_length, sweep_speed=sweep_speed, 
                n_sweeps = n_sweeps, frame_rate = frame_rate,
                ori=ori, bar = bar, win = win
            )
        

win.close()

params=[Unitnum, Runnum, Eye, numTrials, blanktime, length, width, speed, sweeplength, dl, contrast, oris, disp]
filename='Unit%s_parameters.csv'%(Unitnum)
with open(filename, 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(params)
csvFile.close()
