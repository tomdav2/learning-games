#start at the start
#red light/green light
#generate random letter
#print letter

#says red light (0)
#waits for random time
#moves to green light (1)

#research#
#https://stackoverflow.com/questions/18773474/simple-way-to-run-two-while-loops-at-the-same-time-using-threading

import threading
import time
import random
import string
import keyboard

global steps

def lightChange():
    global lightStatus
    global kill
    kill = ('')
    while kill != True:
        print("green light")
        lightStatus = True
        time.sleep(random.randint(1,6))
        print("red light")
        keyboard.start_recording()
        lightStatus = False
        time.sleep(random.randint(1,6))
        kill = keyboard.stop_recording()
    else:
        dead()

def squidGame():
    global run
    global char
    global steps
    steps = 0
    while steps <20:
        run = ''.join(random.choice(string.ascii_letters) for i in range (random.randint(1,6)))
        print(run)
        char = input()
        if run == char:
            steps += 1
            print(steps)
        else:
            dead() #fall

def dead():
    thread1.join(thread2)
    print("KILLED")
    print(steps)


thread1 = threading.Thread(target=lightChange)
thread1.start()

thread2 = threading.Thread(target=squidGame)
thread2.start()

if kill is True:
    dead()