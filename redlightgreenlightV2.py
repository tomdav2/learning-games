#research#
#https://stackoverflow.com/questions/18773474/simple-way-to-run-two-while-loops-at-the-same-time-using-threading
# threading info https://www.pythontutorial.net/python-concurrency/python-threading/ 

# when light change happens it needs to flush the char input
#while loop so that when a user guesses a step right on a greenlight it desont wait for a red light


import threading
import time
import random
import string
import keyboard
import sys


def dead():
   # thread1.join
   # thread2.join
    print("KILLED")
    sys.exit()


def lightChange():
    global redInput
    while kill != True and steps <20:
        greenLight()
        time.sleep(random.randint(1,6))
        redLight()
        keyboard.start_recording
        time.sleep(random.randint(1,6))
        redInput = keyboard.stop_recording
    if lightNum(True) and redInput(True):
        dead()
    if steps >20:
        print("win")
    else:
        dead()



def greenLight():
    global lightNum
    global steps
    lightNum = False
    print("green light")
    global run
    run = ''.join(random.choice(string.ascii_letters) for i in range (random.randint(1,2)))
    print(run)
    char = input()
    if run == char:
        steps += 1
    else:
        dead() #fall


def redLight():
    global lightNum
    lightNum = True
    print("red light  ")


       


#thread1 = threading.Thread(target=squidGame)
#thread2 = threading.Thread(target=lightChange)
steps = int()
kill = (False)
lightNum = (False)


#curser control
lineFlush = '\r\033[K' # flushes previous print
lineClear = '\x1b[2K' # <-- ANSI sequence to clear that line
linePrev = '\033[F' # this should go to the start of the previous line
lineUp = '\033[1A' # up a line


#thread1.start()
#time.sleep(1)
#thread2.start()

lightChange()