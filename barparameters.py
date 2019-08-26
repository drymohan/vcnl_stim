# Use this file to set the parameters for the moving bars. After assigning values to the parameter, run the corresponding script. 

from __future__ import division
import numpy as np


# Set this at the beginning of each run.
Unitnum=1
Runnum=1
Eye='right' #('right' for right eye; 'left' for left eye) 
numTrials= 2

#Stimulus parameters.

length=10 #np.arange(0, 15, 2**0.5) #Length of the bar.
width=1 # Width of the bar.
orientation=np.arange(0,180,20) # Orientation of the bar.
speed=5 # Speed of the bar in degrees per second
sweeplength=5 # Sweep length (works as in visage)
dl=-1 #dark bar= -1 or light bar =1.
contrast=1 # contrast value between 0 to 1 (0=0% contrast; 1=100% contrast)

#Uncomment aperture when running aperture tuning
#aperture=np.arange(0, length, 2**0.5)

# This section sets the x and y parameters for bar_rf.
start_disp=-3
end_disp=3
steps=0.5
displacement=np.arange(start_disp, end_disp, steps)


#import ori_tun



