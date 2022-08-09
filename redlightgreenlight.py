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

import string
import random
import time
lightcolour = 1
LINE_CLEAR = '\x1b[2K' # <-- ANSI sequence to clear that line
PREVLINE = '\033[F' # this should go to the start of the previous line



#declares lightcolour globally, plus 1 to make it change colour, timesleep makes it wait a random amount of time RLGL produces redlight or greenlight response
def lightprocess():
    global lightcolour
    lightcolour += 1
    time.sleep(random.randint(1,5))
    RLGL()

#if the lightcolour is even print red light, if not then print green
def RLGL():
    if (lightcolour % 2) == 0: 
        print(PREVLINE, LINE_CLEAR + "red light", end='\n')
        lightprocess()
    else:
        print(PREVLINE, LINE_CLEAR + "green light", end='\n')
        lightprocess()


RLGL()