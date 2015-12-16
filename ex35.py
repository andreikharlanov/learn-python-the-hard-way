from sys import exit

def interpret_string(s):

    """This function checks if the passed variable is a integer or float number.
    If yes, it returns an integer or a float.
    If the passed variable is not an integer or a float, it returns False.
    """

    # Check if the passed variable is a string, if not return False
    if not isinstance(s, basestring):
        return False
    # Check if the passed varialbe contains only digits.
    # If yes, it's possible to return it as an integer. And we do just that.
    if s.isdigit():
        return int(s)
    # If the passed variable is not an integer,
    # we check if we can return it as a float.
    # If we can, the function returns a float.
    # If it's impossible to make a float out of the passed varible,
    # we catch the ValueError and the function returns False.
    try:
        return float(s)
    except ValueError:
        return False

def get_number():
    choice = raw_input("> ")

    possibly_number = interpret_string(choice)

    if possibly_number == False:
        print "Type a number, idiot!"
        return get_number()
    else:
        return possibly_number

def gold_room():
    print "This room is full of gold. How much do you take?"

    how_much = get_number()

    if how_much < 50:
        print "You took %r money." % how_much
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        print "You took %r money." % how_much
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."

            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
