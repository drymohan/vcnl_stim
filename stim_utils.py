#!/usr/bin/env python2

# This doesn't appear to affect division in another 
# script that this module is imported to 
from __future__ import division

import math

import serial
import numpy as np

from psychopy import visual, event, core


try:
    ard = serial.Serial('/dev/ACM0')
    flag = serial.Serial('/dev/USB0')
except:
    print('serial objects not available')

def setArd(n):
    ard.write(chr(n))
    
def mark():
    flag.write(1)


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


def make_xy_frame_pos(ori = 0, x_center=0, y_center=0, tot_frame_offsets=None):

    '''
    Generates x and y coordinates for every frame for a given ori and center

    Key input argument is tot_frame_offsets.
    This provides the translation, per frame, in degrees, that the bar must make.

    This function returns the actual position, in degrees, in both x and y coords
    that the bar must be for each frame.

    Parameters
    ----
    ori : float (degs)
        Orientation of the bar.  
        Direction of movement will be orthogonal to this orientation (+90)

    x_center, y_center : float (degs)
        Center of the movement of the bar.
        In psychopy, 0 represents the center of the screen

    tot_frame_offsets : iterable/array
        array of offsets from the center, each number representing a single frame

    Returns
    ----
    x_frame_pos, y_frame_pos : list
        two lists representing the x and y positions for each frame
    '''

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


def animate_sweeping_bar(x_center, y_center, ori, sweep_length, sweep_speed, n_sweeps, frame_rate, bar, win):

    '''
    Animates the provided bar, on the provided win, according to sweep and centre arguments

    Parameters
    ----
    x_center, y_center : float (degs)
        Center of the animated movement

    ori : float (degs)
        Orientation of the bar that is to be animated
        Passed to make_xy_frame_pos

    sweep_length : float (degs)
        Length of the sweep, in degs, as a diameter (ie, through the center, not to it)

    sweep_speed : float (degs / s)
        Speed at which the bar moves in degs per second

    n_sweeps : int
        Number of sweeps made through the center
        2 -> there and back again

    bar : psychopy.visual.Rect instance
        may be a list of bar instances that are to be animated together

    win : psychopy.visual.Window instance
    '''

    frame_time = 1/float(frame_rate)

    multi_bar = True if isinstance(bar, list) else False

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

        if multi_bar:
            for b in bar:
                b.pos = x_frame_pos[f_idx], y_frame_pos[f_idx]
                b.draw()
        else:
            bar.pos = x_frame_pos[f_idx], y_frame_pos[f_idx]
            bar.draw()

        win.flip()


def drift_grating(temp_freq, stim_time, frame_rate, grating, win):

    # python2 quirk ... integer division always results in integer
    # Here, avoiding this with both float conversion and above import of division
    frame_time = 1/float(frame_rate)

    n_frames = stim_time / frame_time

    # As PsychoPy phase is module 0-1 (rather than 0-2pi),
    # phase change per frame would be frame_time for temp_freq
    # of 1 (ie 1 sec -> 1 cycle)
    # Simply multiply by temp_freq to change phase chance for each
    # frame
    frame_phases = np.arange(n_frames) * frame_time * temp_freq

    for fp in frame_phases:
        grating.phase = fp
        grating.draw()

        win.flip()