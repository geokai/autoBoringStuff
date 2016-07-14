while True:
    print ("Who are you?")
    name = input ()

    if name != "Joe":
        print ("You are not authorized.")
        continue
    print ("Hello Joe. What is the password? (Is it a fish.)")
    password = input ()

    if password == "swordfish":
        print ("Welcome Joe.")
        break
print ("Access granted.")
