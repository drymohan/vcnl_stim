#!/usr/bin/env python2

from __future__ import division

import math
import numpy as np

from psychopy import visual, event, core

frame_rate = 75 # s^-1
frame_time = 1/frame_rate # seconds

win = visual.Window(
    size=[1280, 1024],
    monitor='mbp',
    units = 'deg',
    fullscr=True, allowGUI=False, waitBlanking=True
    )

n_sweeps = 2

x_center, y_center = 0, 0


# total length of one sweep (through the center)
sweep_length = 1 # degs

# Degrees covered per second
sweep_speed = 1 # degs / s

# sweep_time = sweep_length / sweep_speed # seconds
# # stim_time = (n_sweeps*sweep_length) / sweep_speed # seconds
# n_sweep_frames = math.ceil(sweep_time / frame_time)

# frame_offsets = np.linspace(
#     -sweep_length/2, sweep_length/2, # sweep length is a "diameter"
#     n_sweep_frames+1, # +1 so that endpoint included but at accurate sweep_speed
#     endpoint=True # include endpoint, ie last frame will have gone sweep_length + sweep_per_frame
#     )

# if n_sweeps == 2:
#     tot_frame_offsets = np.hstack((
#         frame_offsets, 
#         np.flipud(frame_offsets[:-1]) # exclude last element and reverse
#         ))
# else:
#     tot_frame_offsets = frame_offsets


def make_xy_frame_pos(ori = 0, x_center=0, y_center=0, tot_frame_offsets=0):

    # Convert to radians for math functions
    ori = math.radians(ori+90) # movement is orthogonal to orientation by +90 degs

    x_frame_pos = [
        x_center + (offset * math.cos(ori))
        for offset
        in tot_frame_offsets
    ]

    y_frame_pos = [
        y_center + (offset * math.sin(ori))
        for offset
        in tot_frame_offsets
    ]

    return x_frame_pos, y_frame_pos
    
def psychopy_ori(ori):
    '''
        Converts from trigonometry orientation convention to PsychoPy convention
        For rotating stimuli using object.ori attributes in PsychoPy
        
        ori : degrees
        
        PsychoPy orientation is like a clock (0 at 12 o'clock, 90 at 3 o'clock etc
        We think like trigonometry (0 at 3 o'clock, 90 at 12 etc)
        
        Therefore, to transform to PsychoPy convention, reverse (this negative)
        and add 90 degrees to translate
    '''
    
    return -ori + 90
    
    
def animate_sweeping_bar(x_center, y_center, ori, sweep_length, sweep_speed, n_sweeps, bar, win):


    # total length of one sweep (through the center)
    sweep_length = 1 # degs

    # Degrees covered per second
    sweep_speed = 1 # degs / s

    sweep_time = sweep_length / sweep_speed # seconds
    # stim_time = (n_sweeps*sweep_length) / sweep_speed # seconds
    n_sweep_frames = math.ceil(sweep_time / frame_time)

    frame_offsets = np.linspace(
        -sweep_length/2, sweep_length/2, # sweep length is a "diameter"
        n_sweep_frames+1, # +1 so that endpoint included but at accurate sweep_speed
        endpoint=True # include endpoint, ie last frame will have gone sweep_length + sweep_per_frame
        )

    if n_sweeps == 2:
        tot_frame_offsets = np.hstack((
            frame_offsets, 
            np.flipud(frame_offsets[:-1]) # exclude last element and reverse
            ))
    else:
        tot_frame_offsets = frame_offsets

    x_frame_pos, y_frame_pos = make_xy_frame_pos(
       ori=ori, 
       x_center=x_center, y_center=y_center,
       tot_frame_offsets = tot_frame_offsets
       ) 

    for f_idx in range(len(x_frame_pos)):

        bar.pos = x_frame_pos[f_idx], y_frame_pos[f_idx]
        bar.draw()

        win.flip()

# n_frames = math.ceil(stim_time / frame_time) # int, rounded up one frame
# degs_per_frame = sweep_speed * frame_time # degs

oris = np.arange(0, 180, 20)

bar = visual.Rect(win, width = 0.1, height = 0.4, lineColor=None, fillColor=1 )

for ori in oris:
    if event.getKeys(keyList = ['q']):
        core.quit() 

    # x_frame_pos, y_frame_pos = make_xy_frame_pos(
    #     ori=ori, 
    #     x_center=x_center, y_center=y_center,
    #     tot_frame_offsets = tot_frame_offsets
    #     )

    bar.ori = psychopy_ori(ori)

    animate_sweeping_bar(
            x_center = x_center, y_center=y_center,
            sweep_length = sweep_length, sweep_speed=sweep_speed, n_sweeps = n_sweeps,
            ori=ori, bar = bar, win = win
        )

    # for f_idx in range(len(x_frame_pos)):
    #     bar.pos = x_frame_pos[f_idx], y_frame_pos[f_idx]
    #     bar.draw()

    #     win.flip()

win.close()