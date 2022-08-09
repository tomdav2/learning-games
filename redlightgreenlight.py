#research area
#timers -
# https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html
#
#printing to the same line - 
# https://itnext.io/overwrite-previously-printed-lines-4218a9563527
#
#
#
#  every 5 to 10 seconds you have to type a randomly generated centance if you're unable to you get killed
# 

#Chantal_the_Doll

import random
import time
lightcolour = 1
LINE_CLEAR = '\x1b[2K' # <-- ANSI sequence

#declares lightcolour globally, plus 1 to make it change colour, timesleep makes it wait a random amount of time RLGL produces redlight or greenlight response
def lightprocess():
    global lightcolour
    lightcolour += 1
    time.sleep(random.randint(2,15))
    RLGL()

#if the lightcolour is even print red light, if not then print green
def RLGL():
    if (lightcolour % 2) == 0: 
        print(LINE_CLEAR, end='\r')
        print("red light", end='\r') 
        lightprocess()
    else:
        print(LINE_CLEAR, end='\r')
        print ("green light", end='\r')
        lightprocess()


RLGL()
