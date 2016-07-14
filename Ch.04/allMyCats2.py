#!/usr/local/bin/python3


catNames = []

def noCatsMsg ():
    print ("You have no cats. ", end="")
    print ("Good Bye.")
    print ()

print ("Do you have any cats? (yes/no)")

while True:
    reply = input ()
    if reply == "no":
        noCatsMsg ()
        break
    elif reply == "yes":
        while True:
            print ("Enter the name of cat " + str (len (catNames) + 1) +
                     " (Or enter nothing to stop.):")
            name = input ()

            if name == "":
                break
            catNames = catNames + [name]    # list concatenation:
        if len (catNames) < 1:
            noCatsMsg ()
            break
        elif len (catNames) == 1:
            print ("You have " + str (len(catNames)) + " cat. ", end="")
            print ("It's name is:")
        else:
            print ("You have " + str (len (catNames)) + " cats. ", end="")
            print ("Their names are:")

        for name in catNames:
            print ("    " + name)
        break
    else:
        print ("You must reply with either 'yes' or 'no'.")

