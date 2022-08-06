bouncer = 0
name = input("hello, what's your name? \n")

while bouncer < 3:
    item = input("what are you bringing in? \n")
    if name [0] == item [0]:
        bouncer += 1
        print("Yeah come in!")
    if name [0] != item [0]:
        print("nope")
else:
    print("you've won!")