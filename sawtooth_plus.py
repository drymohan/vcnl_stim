from __future__ import division
from psychopy import visual, core, event
#from psychopy.tools.monitorunittools import *
from run_sawtooth_plus import *
import numpy as np
import stim_utils 
import random
random.seed(0)
if __name__ == "__main__":
    raise('please run this program from "run_sawtooth_plus.py"')
########################################################################################
#%% create a window
winRectPix = [1280, 1024]
ifi = 1/75  # inter-frame interval. 0.05 is the default but i don't know how to set it 
if is_On:
    background = -1
else:
    background = 1
mywin = visual.Window(size=winRectPix, 
                    monitor="vcnl", 
                    units="deg", 
                    fullscr=True, 
                    color = background,
                    allowGUI=False)
core.wait(wait_before_start)

#diagonalPix = np.sqrt(winRectPix[0]**2+winRectPix[1]**2) 
# increase this number if the stimulus is not large enough to cover the entire screen
diagonalDeg = 30 

########################################################################################
# don't touch this part
#%% create stimuli
res = 100
num_saw2 = num_saw+1
saw_inc = np.arange(0,1,1/res)
inc_phase_saw = np.roll(np.tile(saw_inc, num_saw2+1), 1)[:num_saw2*res-res+2]
dec_overall = np.arange(0,-p*num_saw2,-p*num_saw2/(res*num_saw2))[:num_saw2*res-res+2]
stim_phase = inc_phase_saw + dec_overall
seq_max = stim_phase.max()
seq_min = stim_phase.min()
map_max = 1; map_min = -1
stim_phase = (map_max-map_min)/(seq_max-seq_min)*(stim_phase-seq_max)+map_max

tooth_span_deg = (num_saw)/spatialFreq
blank_span_deg = diagonalDeg
blank_len = int(inc_phase_saw.shape[0]*(blank_span_deg/tooth_span_deg))
blackscreen = np.zeros(blank_len)-1
whitescreen = np.zeros(blank_len)+1

pattern = np.concatenate([whitescreen, stim_phase, blackscreen])[None,:]
blankRatio = (whitescreen.shape[0])/(pattern.shape[1])
stimRatio = 1-(2*blankRatio)

## program_tf is not the temporal frequency of the grating, but it is not an error 
program_tf = stimRatio*temporalFreq/(num_saw)
phase_step = program_tf*ifi



#############################################################################
# make ori a np.array
if type(ori)==list:
    ori = np.array(ori)
elif type(ori)==int:
    ori = np.array([ori])

# change ori
ori = -ori
if not is_On: 
    is_On = -1
    ori = ori+180
else:
    is_On = 1

# match ori with markers   
ori2marker = dict(zip(ori, range(1,len(ori)+1)))

# randomise 
if randomise:
    random.shuffle(ori)

# a trial list
if RepeatLoop_outside_OriLoop:
    final_ori_list = np.tile(ori, num_repeat)
else:
    final_ori_list = np.repeat(ori, num_repeat)


################################################################################
#import matplotlib.pyplot as plt
#plt.plot(pattern.transpose()); plt.show()
#%% prepare the grating
## note that sf here is not the spatial frequency of the grating, but it is not an error
grating = visual.GratingStim(win=mywin, 
                mask=None, 
                size=diagonalDeg, pos=[0,0], sf=blankRatio/diagonalDeg,
                ori=0,
                tex = pattern)

recycle =  visual.GratingStim(win=mywin, 
                mask=None, 
                size=diagonalDeg, pos=[0,0], sf=blankRatio/diagonalDeg,
                tex = None)
                
              
              
#%% present stimuli
# note that the ori here is not the ori you set in run_sawtooth_plus.py

initial_phase = -(blankRatio/2+stimRatio/2)*is_On
phase = initial_phase

for i_ori in final_ori_list: 
    grating.setOri(i_ori)
    stim_utils.setMarker(ori2marker[i_ori])
    mywin.callOnFlip(stim_utils.sendMarker, True)
    
    while True:
        # present the grating
        grating.setPhase(phase) 
        grating.draw()
        mywin.flip()
        phase += phase_step*is_On

        # reset the phase when a cycle ends
        if abs(phase-initial_phase)>blankRatio+stimRatio:
            phase = initial_phase # initial phase
            
            # recycle the luminance
            for i in np.arange(is_On, -is_On , -is_On*ifi/recycle_sec):
                recycle.setColor(i)
                recycle.draw()
                mywin.flip()
            break
    
        if event.getKeys(keyList = ['q']):
            mywin.close()
            core.quit() 


#cleanup
mywin.close()
core.quit()

# a copy of the entire script in case someone accidental makes some changes 
"""
from __future__ import division
from psychopy import visual, core, event
#from psychopy.tools.monitorunittools import *
from run_sawtooth_plus import *
import numpy as np
import stim_utils 
import random
random.seed(0)
if __name__ == "__main__":
    raise('please run this program from "run_sawtooth_plus.py"')
########################################################################################
#%% create a window
winRectPix = [1280, 1024]
ifi = 1/75  # inter-frame interval. 0.05 is the default but i don't know how to set it 
if is_On:
    background = -1
else:
    background = 1
mywin = visual.Window(size=winRectPix, 
                    monitor="vcnl", 
                    units="deg", 
                    fullscr=True, 
                    color = background,
                    allowGUI=False)
core.wait(wait_before_start)

#diagonalPix = np.sqrt(winRectPix[0]**2+winRectPix[1]**2) 
# increase this number if the stimulus is not large enough to cover the entire screen
diagonalDeg = 30 

########################################################################################
# don't touch this part
#%% create stimuli
res = 100
num_saw2 = num_saw+1
saw_inc = np.arange(0,1,1/res)
inc_phase_saw = np.roll(np.tile(saw_inc, num_saw2+1), 1)[:num_saw2*res-res+2]
dec_overall = np.arange(0,-p*num_saw2,-p*num_saw2/(res*num_saw2))[:num_saw2*res-res+2]
stim_phase = inc_phase_saw + dec_overall
seq_max = stim_phase.max()
seq_min = stim_phase.min()
map_max = 1; map_min = -1
stim_phase = (map_max-map_min)/(seq_max-seq_min)*(stim_phase-seq_max)+map_max

tooth_span_deg = (num_saw)/spatialFreq
blank_span_deg = diagonalDeg
blank_len = int(inc_phase_saw.shape[0]*(blank_span_deg/tooth_span_deg))
blackscreen = np.zeros(blank_len)-1
whitescreen = np.zeros(blank_len)+1

pattern = np.concatenate([whitescreen, stim_phase, blackscreen])[None,:]
blankRatio = (whitescreen.shape[0])/(pattern.shape[1])
stimRatio = 1-(2*blankRatio)

## program_tf is not the temporal frequency of the grating, but it is not an error 
program_tf = stimRatio*temporalFreq/(num_saw)
phase_step = program_tf*ifi



#############################################################################
# make ori a np.array
if type(ori)==list:
    ori = np.array(ori)
elif type(ori)==int:
    ori = np.array([ori])

# change ori
ori = -ori
if not is_On: 
    is_On = -1
    ori = ori+180
else:
    is_On = 1

# match ori with markers   
ori2marker = dict(zip(ori, range(1,len(ori)+1)))

# randomise 
if randomise:
    random.shuffle(ori)

# a trial list
if RepeatLoop_outside_OriLoop:
    final_ori_list = np.tile(ori, num_repeat)
else:
    final_ori_list = np.repeat(ori, num_repeat)


################################################################################
#import matplotlib.pyplot as plt
#plt.plot(pattern.transpose()); plt.show()
#%% prepare the grating
## note that sf here is not the spatial frequency of the grating, but it is not an error
grating = visual.GratingStim(win=mywin, 
                mask=None, 
                size=diagonalDeg, pos=[0,0], sf=blankRatio/diagonalDeg,
                ori=0,
                tex = pattern)

recycle =  visual.GratingStim(win=mywin, 
                mask=None, 
                size=diagonalDeg, pos=[0,0], sf=blankRatio/diagonalDeg,
                tex = None)
                
              
              
#%% present stimuli
# note that the ori here is not the ori you set in run_sawtooth_plus.py

initial_phase = -(blankRatio/2+stimRatio/2)*is_On
phase = initial_phase

for i_ori in final_ori_list: 
    grating.setOri(i_ori)
    stim_utils.setMarker(ori2marker[i_ori])
    mywin.callOnFlip(stim_utils.sendMarker, True)
    
    while True:
        # present the grating
        grating.setPhase(phase) 
        grating.draw()
        mywin.flip()
        phase += phase_step*is_On

        # reset the phase when a cycle ends
        if abs(phase-initial_phase)>blankRatio+stimRatio:
            phase = initial_phase # initial phase
            
            # recycle the luminance
            for i in np.arange(is_On, -is_On , -is_On*ifi/recycle_sec):
                recycle.setColor(i)
                recycle.draw()
                mywin.flip()
            break
    
        if event.getKeys(keyList = ['q']):
            mywin.close()
            core.quit() 


#cleanup
mywin.close()
core.quit()

"""