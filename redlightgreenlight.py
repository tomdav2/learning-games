#research area
#timers - https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
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
countdown = random.randint(1,5)
lightcolour = 1
def lightprocess():
    lightcolour += 1
    time.sleep(countdown)


while (lightcolour % 2) == 0: 
    print("The number is even") 
    lightprocess

while (lightcolour % 2) != 0: 
    print ("The provided number is odd")
    lightprocess

