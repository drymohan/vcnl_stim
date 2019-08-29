#%% parameters setting
import csv

# set trial parameters here
Unitnum=1
Runnum=1
Eye='right' #('right' for right eye; 'left' for left eye) 

# the number of sawtooths, which is the number of edges + 1
num_saw = 10;      

# p is the (-slope of the overall luminance change/slope of the sawtooth) 
# when p = 1: staircase; 
# when p -> 0: normal sawtooth grating (but it cannot take zero) 
p = 1              

# the time it takes the blank screen to change the luminance
recycle_sec = 2;   

# [True, False] = [On, Off]
is_On = False          

# cycles per degree
# cycles per second
spatialFreq = 1
temporalFreq = 10; 
    
# anti-clockwise: [0,90,180,270] = [right,up,left,down]
ori = [0, 45, 90, 180]            
# can take int, np.array or list
# markers will be the index of the array+1

# if true, ABCD ABCD ABCD. if false, AAA BBB CCC DDD
RepeatLoop_outside_OriLoop = True
num_repeat = 2
randomise = True

# wait for a few second at the begining of the program (for ttl)
wait_before_start = 3
# don't touch this
if __name__ == "__main__":
    import sawtooth_plus
    
# a copy of the entire script in case someone accidental makes some changes 
""" 
#%% parameters setting
# the number of sawtooths, which is the number of edges + 1
num_saw = 10;      

# p is the (-slope of the overall luminance change/slope of the sawtooth) 
# when p = 1: staircase; 
# when p -> 0: normal sawtooth grating (but it cannot take zero) 
p = 1              

# the time it takes the blank screen to change the luminance
recycle_sec = 0.2;   

# [True, False] = [On, Off]
is_On = False          

# cycles per degree
# cycles per second
spatialFreq = 1
temporalFreq = 10; 
    
# anti-clockwise: [0,90,180,270] = [right,up,left,down]
ori = [0, 45, 90, 180]            
# can take int, np.array or list
# markers will be the index of the array+1

# if true, ABCD ABCD ABCD. if false, AAA BBB CCC DDD
RepeatLoop_outside_OriLoop = True
num_repeat = 2
randomise = True

# wait for a few second at the begining of the program (for ttl)
wait_before_start = 3
# don't touch this
if __name__ == "__main__":
    import sawtooth_plus
"""
params=[Unitnum, Runnum, Eye, num_saw, p, recycle_sec, is_On, ori, spatialFreq, temporalFreq, RepeatLoop_outside_OriLoop , num_repeat, randomise, wait_before_start]
filename='Unit%s_sawtooth.csv'%(Unitnum)
with open(filename, 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(params)
csvFile.close()