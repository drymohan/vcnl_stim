#!/usr/bin/env python2

from stim_utils import *

win = visual.Window(
    size=[1280, 1024],
    monitor='vcnl',
    units = 'deg',
    fullscr=True, allowGUI=False, waitBlanking=True
    )
frame_rate = 75 # s^-1
frame_time = 1/frame_rate # seconds

bar_width = 1

bar_length = 5

# How many sweeps through the center the bar makes (2 -> "there and back again")
n_sweeps = 2

# Center of bar sweep (center of screen is 0,0)
x_center, y_center = 0, 0 # degs

# total length of one sweep (through the center)
sweep_length = 5 # degs

# Degrees covered per second
sweep_speed = 4 # degs / s


oris = np.arange(0, 180, 20)

bar = visual.Rect(win, width = bar_width, height = bar_length, lineColor=None, fillColor=1 )

for ori in oris:
    if event.getKeys(keyList = ['q']):
        core.quit() 

    bar.ori = psychopy_ori(ori)

    animate_sweeping_bar(
            x_center = x_center, y_center=y_center,
            sweep_length = sweep_length, sweep_speed=sweep_speed, 
            n_sweeps = n_sweeps, frame_rate = frame_rate,
            ori=ori, bar = bar, win = win
        )

win.close()
