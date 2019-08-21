#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
The most accurate way to time your stimulus presentation is to
present for a certain number of frames. For that to work you need
your window flips to synchronize to the monitor and not to drop
any frames. This script examines the precision of your frame flips.

Shut down as many applications as possible, especially those that
might try to update
"""

from __future__ import division

from psychopy import visual, logging, core, event
visual.useFBO = True  # if available (try without for comparison)

import matplotlib
#matplotlib.use('Qt4Agg')  # change this to control the plotting 'back end'
import pylab

import serial

ser = serial.Serial('/dev/ttyACM0')

nIntervals = 6000
win = visual.Window([1280, 1024], fullscr=True, allowGUI=False, waitBlanking=True, units='norm')
#progBar = visual.GratingStim(win, tex=None, mask=None,
#    size=[0, 0.05], color='red', pos=[0, -0.9], autoLog=False)
myStim = visual.GratingStim(win, tex='sin', mask='gauss',
    size=300, sf=0.05, units='pix', autoLog=False)
    
rect_fill_color = 1
errol_stim = visual.Rect(win, width=2, height=2, fillColor = rect_fill_color, lineColor=None)
# logging.console.setLevel(logging.INFO)# uncomment to log every frame


markers = [1, 2]

marker_count = 0

def setMarker(m):
    ser.write(chr(m))
    

def sendMarker(flag):
    if flag:
        ser.write(chr(0))
    else:
        pass

win.recordFrameIntervals = True

core.wait(2)
for frameN in range(nIntervals + 1):
#    progBar.setSize([2.0 * frameN/nIntervals, 0.05])
#    progBar.draw()
#    myStim.setPhase(0.1, '+')
#    myStim.draw()

    if frameN%10 == 0:

        
        setMarker(markers[marker_count%2])
        marker_count+=1

        errol_stim.fillColor *= -1
        
        
        win.callOnFlip(sendMarker, True)
    else:
        win.callOnFlip(sendMarker, False)
    
    errol_stim.draw()
    if event.getKeys():
        print 'stopped early'
        break
    win.logOnFlip(msg='frame=%i' %frameN, level=logging.EXP)
    win.flip()
    
win.fullscr = False
win.close()

# calculate some values
intervalsMS = pylab.array(win.frameIntervals) * 1000
m = pylab.mean(intervalsMS)
sd = pylab.std(intervalsMS)
# se=sd/pylab.sqrt(len(intervalsMS)) # for CI of the mean

msg = "Mean=%.1fms, s.d.=%.2f, 99%%CI(frame)=%.2f-%.2f"
distString = msg % (m, sd, m - 2.58 * sd, m + 2.58 * sd)
nTotal = len(intervalsMS)
nDropped = sum(intervalsMS > (1.5 * m))
msg = "Dropped/Frames = %i/%i = %.3f%%"
droppedString = msg % (nDropped, nTotal, 100 * nDropped / float(nTotal))

# plot the frameintervals
pylab.figure(figsize=[12, 8])
pylab.subplot(1, 2, 1)
pylab.plot(intervalsMS, '-')
pylab.ylabel('t (ms)')
pylab.xlabel('frame N')
pylab.title(droppedString)

pylab.subplot(1, 2, 2)
pylab.hist(intervalsMS, 50, normed=0, histtype='stepfilled')
pylab.xlabel('t (ms)')
pylab.ylabel('n frames')
pylab.title(distString)
pylab.show()

win.close()
core.quit()

# The contents of this file are in the public domain.
