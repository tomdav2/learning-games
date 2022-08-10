
import keyboard # pip install keyboard
import random
import string


run = ''.join(random.choice(string.ascii_letters) for i in range (1))
char = ""
steps = 0

def died():
    run = ''.join(random.choice(string.ascii_letters) for i in range (1))
    char = ""
    steps = 0

print(run)
char = input()


while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed(run):
            print("one step closer")
    except:
        print("you died")
        died()
        break  # if user pressed a key other than the given key the loop will break

