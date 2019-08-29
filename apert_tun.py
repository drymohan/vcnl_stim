#!/usr/bin/env python2

from stim_utils import *
import barparameters as par
import random
import csv

#set trial parameters here
Unitnum=1
Runnum=1
Eye='right' #('right' for right eye; 'left' for left eye) 
numTrials= 2
blanktime=1

#Set stimulus Parameters here

length=5 #Length of the bar.
width=0.5 # Width of the bar.par
speed=10 # Speed of the bar in degrees per second
sweeplength=5 # Sweep length (works as in visage)
dl=1 #dark bar= -1 or light bar =1.
contrast=1 # contrast value between 0 to 1 (0=0% contrast; 1=100% contrast)
disp='NA'
ori=0
#aperture Parameters

st_aper=0
steps=2**0.5

# DO NOT CHANGE THE CODE BEYOND THIS POINT
aperture=np.arange(st_aper, length, steps)


win = visual.Window(
    size=[1280, 1024],
    monitor='vcnl',
    units = 'deg',
    fullscr=True, allowGUI=False, waitBlanking=True
    )
frame_rate = 75 # s^-1
frame_time = 1/frame_rate # seconds

markers=np.arange(np.size(aperture))+1
marker_count = 0

bar_width = width

# Initial length of bar without aperture 
bar_length = length


# How many sweeps through the center the bar makes (2 -> "there and back again")
n_sweeps = 2

# Center of bar sweep (center of screen is 0,0)
x_center, y_center = 0, 0 # degs

# total length of one sweep (through the center)
sweep_length = sweeplength # degs

# Degrees covered per second
sweep_speed = speed # degs / s


ap_lengths = aperture

bar = visual.Rect(win, width = bar_width, height = bar_length,
	ori = psychopy_ori(ori), lineColor=None, fillColor=dl)
apert = visual.Rect(win, width=bar_width, 
	ori = psychopy_ori(ori), lineColor=None, fillColor=0)
core.wait(4)

ap_rand= range(np.size(ap_lengths))
random.shuffle(ap_rand)

for numTrials in range(numTrials):
    for ap_idx in ap_rand:
        if event.getKeys(keyList = ['q']):
            core.quit() 

        apert.height = ap_lengths[ap_idx]
        setMarker(markers[ap_idx])
                
        animate_sweeping_bar(
                x_center = x_center, y_center=y_center,
                sweep_length = sweep_length, sweep_speed=sweep_speed, 
                n_sweeps = n_sweeps, frame_rate = frame_rate,
                ori=ori, bar = [bar, apert], win = win
            )

win.close()

params=[Unitnum, Runnum, Eye, numTrials, blanktime, length, width, speed, sweeplength, dl, contrast, ori, disp, aperture]
filename='Unit%s_parameters.csv'%(Unitnum)
with open(filename, 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(params)
csvFile.close()