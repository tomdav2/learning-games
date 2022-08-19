import keyboard # <- pip install keyboard
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
# better way of detecting which key to press https://www.pythonforbeginners.com/basics/how-to-detect-keypress-in-python#:~:text=To%20detect%20keypress%2C%20we%20will,is%20pressed%20on%20the%20keyboard.
#
#Chantal_the_Doll

letters = string.ascii_letters
LINE_FLUSH = '\r\033[K' # flushes previous print
LINE_CLEAR = '\x1b[2K' # <-- ANSI sequence to clear that line
PREVLINE = '\033[F' # this should go to the start of the previous line


steps = 0
redLight = "red light"
greenLight = "green light"


while steps <20:
    lightChangeInt = (random.randint(1,6))
#timing
    time.sleep(lightChangeInt)
#RedLight - if you type during this you die
    if (lightChangeInt % 2) == 0:
        print(redLight)
        if keyboard._KeyboardListener(string.ascii_letters):
            print("KILLED")
            print(steps)
            break
    else:
#GreenLight - enable typing and random typing sequence
        print(greenLight)
        run = ''.join(random.choice(string.ascii_letters) for i in range (random.randint(1,6)))
        print(run)
        char = input()
        if run == char:
            steps += 1
            print(steps)
        else:
            #change this to fall over press escape to stand up
            print("KILLED")
            print(steps)
            break