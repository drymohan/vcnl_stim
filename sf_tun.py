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

stim_time = 4 # seconds
diameter = 4 # degs
contrast = 1 # 0-1 (ie 0 to 100%)

temp_freq = 2 # cycles / sec

ori = 0

# Center of bar sweep (center of screen is 0,0)
x_center, y_center = 0, 0 # degs

sfs = np.arange(0, 10, 1)

grating = visual.grating.GratingStim(win, mask='circle',
        pos = (x_center, y_center), contrast = contrast, 
        ori = psychopy_ori(ori), size = diameter
    )

for sf in sfs:
    if event.getKeys(keyList = ['q']):
        core.quit() 

    grating.sf = sf

    drift_grating(
        temp_freq = temp_freq, stim_time = stim_time,
        frame_rate = frame_rate, grating = grating, win = win
        )

win.close()
