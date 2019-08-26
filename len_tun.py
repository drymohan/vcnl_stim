#!/usr/bin/env python2

from stim_utils import *
import barparameters as par
import random

win = visual.Window(
    size=[1280, 1024],
    monitor='vcnl',
    units = 'deg',
    fullscr=True, allowGUI=False, waitBlanking=True
    )
frame_rate = 75 # s^-1
frame_time = 1/frame_rate # seconds

# define the marker values. Markers will start at 1.
markers=np.arange(np.size(par.length))+1
marker_count = 0

bar_width = par.width

ori = par.orientation

# How many sweeps through the center the bar makes (2 -> "there and back again")
n_sweeps = 2

# Center of bar sweep (center of screen is 0,0)
x_center, y_center = 0, 0 # degs

# total length of one sweep (through the center)
sweep_length = par.sweeplength # degs

# Degrees covered per second
sweep_speed = par.speed # degs / s


lengths = par.length

bar = visual.Rect(win, width = bar_width, ori = psychopy_ori(ori), lineColor=None, fillColor=par.dl )
core.wait(4)

l_rand= range(np.size(lengths))
random.shuffle(l_rand)

for numTrials in range(par.numTrials):
    for l_idx in l_rand:
        if event.getKeys(keyList = ['q']):
            core.quit() 

        bar.height = lengths[l_idx]
        setMarker(markers[l_idx])
        
        marker_count+=1

        animate_sweeping_bar(
                x_center = x_center, y_center=y_center,
                sweep_length = sweep_length, sweep_speed=sweep_speed, 
                n_sweeps = n_sweeps, frame_rate = frame_rate,
                ori=ori, bar = bar, win = win
            )

win.close()
