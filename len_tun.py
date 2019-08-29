#!/usr/bin/env python2

from stim_utils import *
import barparameters as par
import random
import csv

#set trial parameters here
Unitnum=1
Runnum=1
Eye='right' #('right' for right eye; 'left' for left eye) 
numTrials= 1
blanktime=1

#Set stimulus Parameters here

contrast=1# contrast value between 0 to 1 (0=0% contrast; 1=100% contrast)
width=0.5 # Width of the bar.par
speed=10 # Speed of the bar in degrees per second
sweeplength=5 # Sweep length (works as in visage)
dl=1 #dark bar= -1 or light bar =1.
ori=0 # orientation of the bar
disp='NA'
aperture='NA'

#Orientation Parameters

st_len=0
end_len=10
steps=2**0.5

# DO NOT CHANGE THE CODE BELOW THIS POINT
lengths= np.arange(st_len, end_len, steps)

win = visual.Window(
    size=[1280, 1024],
    monitor='vcnl',
    units = 'deg',
    fullscr=True, allowGUI=False, waitBlanking=True
    )
frame_rate = 75 # s^-1
frame_time = 1/frame_rate # seconds

# define the marker values. Markers will start at 1.
markers=np.arange(np.size(lengths))+1
marker_count = 0

bar_width = width


# How many sweeps through the center the bar makes (2 -> "there and back again")
n_sweeps = 2

# Center of bar sweep (center of screen is 0,0)
x_center, y_center = 0, 0 # degs

# total length of one sweep (through the center)
sweep_length = sweeplength # degs

# Degrees covered per second
sweep_speed = speed # degs / s


bar = visual.Rect(win, width = bar_width, ori = psychopy_ori(ori), lineColor=None, fillColor=dl )
core.wait(4)

l_rand= range(np.size(lengths))
random.shuffle(l_rand)
blank=visual.Rect(win, fillColor=0, lineColor=None)
sq_blank=visual.Rect(win, width=1.5, height=1.5, lineColor=None, fillColor=-1)
sq_blank.pos=[-7.8,6]
for numTrials in range(numTrials):
    for l_idx in l_rand:
        if event.getKeys(keyList = ['q']):
            core.quit() 
        
        bar.height = lengths[l_idx]
        setMarker(markers[l_idx])
        
        blank.draw()
        sq_blank.draw()
        win.flip()
        core.wait(blanktime)
        
        marker_count+=1

        animate_sweeping_bar(
                x_center = x_center, y_center=y_center,
                sweep_length = sweep_length, sweep_speed=sweep_speed, 
                n_sweeps = n_sweeps, frame_rate = frame_rate,
                ori=ori, bar = bar, win = win
            )

win.close()

params=[Unitnum, Runnum, Eye, numTrials, blanktime, lengths, width, speed, sweeplength, dl, contrast, ori, disp, aperture]
filename='Unit%s_parameters.csv'%(Unitnum)
with open(filename, 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(params)
csvFile.close()
