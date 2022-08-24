#research#
#https://stackoverflow.com/questions/18773474/simple-way-to-run-two-while-loops-at-the-same-time-using-threading
# threading info https://www.pythontutorial.net/python-concurrency/python-threading/ 


import threading
import time
import random
import string
import keyboard
import sys


steps = int()
kill = (False)
lightNum = (False)


def dead():
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
    print("green light")
    lightNum = False


def redLight():
    global lightNum
    print("red light")
    lightNum = True


def squidGame():
    global steps
    global lightNum
    while steps <20:
        run = ''.join(random.choice(string.ascii_letters) for i in range (random.randint(1,2)))
        print(run)
        char = input()
        if run == char:
            steps += 1
            print(steps)
        else:
            dead() #fall


# starts both the light change and word game
thread1 = threading.Thread(target=squidGame)
thread1.start()

thread2 = threading.Thread(target=lightChange)
thread2.start()
