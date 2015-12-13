def room_3():
    print "Do you want to go though the exit? Yes or no?"

    exit = raw_input("Choose wisely! > ")

    if exit == "yes":
        print "Your are a smart person. You survived."
    elif exit == "no":
        print "You're a fool. A bear comes to the room you are standing in and eats you. What a bad move that was."
    else:
        print "Are you blind? You're supposed to say yes or no, idiot!"
        room_3()

print "You enter a dark room with three doors. Do you go through door #1, door #2 or door #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a chees cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The beat eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print "You found an exit from this horrible world."
    print "Do you want to go though the exit? Yes or no?"

    exit = raw_input("Choose wisely! > ")

    if exit == "yes":
        print "Your are a smart person. You survived."
    elif exit == "no":
        print "You're a fool. A bear comes to the room you are standing in and eats you. What a bad move that was."
    else:
        print "Are you blind? You're supposed to say yes or no, idiot!"
        room_3()

else:
    print "You stumble around and fall on a knife and die. Good job!"
