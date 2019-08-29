#!/usr/bin/env python2

from stim_utils import *
import serial
import random
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
contrast=1 # contrast value between 0 to 1 (0=0% contrast; 1=100% contrast)
disp='NA'
aperture='NA'
#Orientation Parameters

st_ori=0
end_ori=180
steps=20

# DO NOT CHANGE THE CODE BELOW THIS POINT

oris=np.arange(st_ori, end_ori, steps)

# define the marker values. Markers will start at 1.
markers=np.arange(np.size(oris))+1
#marker_count = 0

win = visual.Window(
    size=[1280, 1024],
    monitor='vcnl',
    units = 'deg',
    fullscr=True, allowGUI=False, waitBlanking=True
    )
frame_rate = 75 # s^-1
frame_time = 1/frame_rate # seconds

bar_width = width

bar_length = length

# How many sweeps through the center the bar makes (2 -> "there and back again")
n_sweeps = 2

# Center of bar sweep (center of screen is 0,0)
x_center, y_center = 0, 0 # degs

# total length of one sweep (through the center)
sweep_length = sweeplength # degs

# Degrees covered per second
sweep_speed = speed # degs / s


bar = visual.Rect(win, width = bar_width, height = bar_length, lineColor=None, fillColor=dl, contrast=contrast )
core.wait(4)

ori_rand= range(np.size(oris))
random.shuffle(ori_rand)
blank=visual.Rect(win, fillColor=0, lineColor=None)
sq_blank=visual.Rect(win, width=1.5, height=1.5, lineColor=None, fillColor=-1)
sq_blank.pos=[-7.8,6]

for numTrials in range(numTrials):
    for ori_idx in ori_rand:
        if event.getKeys(keyList = ['q']):
            core.quit() 

        bar.ori = psychopy_ori(oris[ori_idx])
        setMarker(markers[ori_idx])
        blank.draw()
        sq_blank.draw()
        win.flip()
        core.wait(blanktime)
        #marker_count+=1
        animate_sweeping_bar(
                x_center = x_center, y_center=y_center,
                sweep_length = sweep_length, sweep_speed=sweep_speed, 
                n_sweeps = n_sweeps, frame_rate = frame_rate,
                ori=oris[ori_idx], bar = bar, win = win
            )
        
            #show_blank(1)
win.close()

#writing parameters to a csv file
params=[Unitnum, Runnum, Eye, numTrials, blanktime, length, width, speed, sweeplength, dl, contrast, oris, disp, aperture]
filename='Unit%s_parameters.csv'%(Unitnum)
with open(filename, 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(params)
csvFile.close()

