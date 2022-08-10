
#research area
#timers -
# https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html
#
#printing to the same line - 
# https://itnext.io/overwrite-previously-printed-lines-4218a9563527
#
# keyboard press - https://www.delftstack.com/howto/python/python-detect-keypress/
#
#
# every 5 to 10 seconds you have to type a randomly generated centance if you're unable to you get killed
#Chantal_the_Doll

import time
import random
import string

#research area
#timers -
# https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html
#
#printing to the same line - 
# https://itnext.io/overwrite-previously-printed-lines-4218a9563527
#
# keyboard press - https://www.delftstack.com/howto/python/python-detect-keypress/
#
#
# every 5 to 10 seconds you have to type a randomly generated centance if you're unable to you get killed
#Chantal_the_Doll

import time
import random
import string


LINE_FLUSH = '\r\033[K' # flushes previous print
LINE_CLEAR = '\x1b[2K' # <-- ANSI sequence to clear that line
PREVLINE = '\033[F' # this should go to the start of the previous line
STEPS = 0
REDLIGHT = "red light"
GREENLIGHT = "green light"


while STEPS <20:
    LIGHTCHANGEINT = (random.randint(1,6))
    time.sleep(LIGHTCHANGEINT)
    if (LIGHTCHANGEINT % 2) == 0:
        print(LINE_FLUSH, REDLIGHT, end='\n')
    else:
        print(LINE_FLUSH, GREENLIGHT, end='\n')