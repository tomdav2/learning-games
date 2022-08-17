import keyboard # pip install keyboard
import random
import string


run = ''.join(random.choice(string.ascii_letters) for i in range (1)) #letter generator
steps = 0 # current steps character is on


#steps below 20?
#generate letter
#show letter
#ask for input
#matches letter?
#move to next step / kill

while steps <20:
    run = ''.join(random.choice(string.ascii_letters) for i in range (random.randint(1,6)))
    print(run)
    char = input()
    if run == char:
        steps += 1
        print(steps)
    else:
        print("KILLED")
        steps = 0
        print(steps)