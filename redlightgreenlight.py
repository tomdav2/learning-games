#research area
#timers -
# https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html
#
#
# 
#  
# 
# 
# 
# every 5 to 10 seconds you have to type a randomly generated centance if you're unable to you get killed
# 

#Chantal_the_Doll

import random
import time
#countdown = random.randint(1,5)
lightcolour = 1

def lightprocess():
    global lightcolour
    lightcolour += 1
    time.sleep(random.randint(1,5))
    RLGL()

def RLGL():
    if (lightcolour % 2) == 0: 
        print("red light") 
        lightprocess()
    else:
        print ("green light")
        lightprocess()


RLGL()
