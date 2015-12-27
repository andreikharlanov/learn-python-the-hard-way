import random

steps = 0

previous_room_now = 0

set_previous_room = 0

text_on_the_wall = "\nM... mmm..\n"

howdy = ["Hey, boy!", "La-la-la, whom I see...", "Are you back, baby boy?"]

print howdy[random.randrange(0,3)]

def welcome_text_room(room_number):
    print "\n----\n"
    # print "You've made %d steps already.\n" % steps
    print "You are in a room #%d.\n" % room_number

def go_to_room(room_number):
    if room_number == 0:
        room_0()
    elif room_number == 1:
        room_1()
    elif room_number == 2:
        room_2()
    elif room_number == 3:
        room_3()
    elif room_number == 4:
        room_4()
    elif room_number == 5:
        room_5()
    elif room_number == 6:
        room_6()
    elif room_number == 7:
        room_7()
    elif room_number == 8:
        room_8()
    elif room_number == 9:
        room_9()
    elif room_number == 10:
        room_10()
    elif room_number == 11:
        room_11()
    elif room_number == 12:
        room_12()

def unfinished_room(room_number):
    global steps
    global previous_room_now
    global set_previous_room

    previous_room_now = set_previous_room

    print "This room is unfinished. We'll transfer you to room you entred this one from."
    print "Now you'll go back to the room #%d." % previous_room_now
    steps += 1
    set_previous_room = room_number
    go_to_room(previous_room_now)

def room_0():
    print "There is no way to go back to room #0."
    go_to_room(1)

def room_1():
    welcome_text_room(1)

    global previous_room_now
    global set_previous_room

    previous_room_now = set_previous_room

    print "It has just two doors:"
    print "1. Green door."
    print "2. Red door."

    print "\nAlso there is a text on the wall. Do you want to read it?\n"
    print "Type 'text', if you want to read the text on the wall."
    print "Otherwise type the color of the door you want to enter."

    def room_1_choice():
        global steps
        global previous_room_now
        global set_previous_room

        choice = raw_input("> ")

        if choice == "text":
            print "Here is the text on the wall:"
            print text_on_the_wall
            steps += 1
            room_1()
        elif choice == "1" or choice == "green":
            print "You try to open the green door. Tough luck, it's closed."
            steps += 1
            room_1()
        elif choice == "2" or choice == "red":
            print "You open the red door infront of you."
            steps += 1
            set_previous_room = 1
            room_2()
        elif choice == "go back":
            steps += 1
            go_to_room(previous_room_now)
        else:
            print "I don't understand you."
            room_1_choice()
    room_1_choice()

def room_2():
    welcome_text_room(2)

    global previous_room_now
    global set_previous_room

    previous_room_now = set_previous_room

    print "It has five doors:"
    print "1. Red."
    print "2. Yellow."
    print "3. The small orange door. It seems unusual."
    print "4. Green."
    print "5. Blue."
    print "\nWhich one do you take?"

    def room_2_choice():
        global steps
        global previous_room_now
        global set_previous_room

        choice = raw_input("> ")

        if choice == "1" or choice == "red":
            print "You chose door #1. OK!"
            steps += 1
            set_previous_room = 2
            room_1()
        elif choice == "2" or choice == "yellow":
            print "You chose door #2. OK!"
            steps += 1
            set_previous_room = 2
            room_3()
        elif choice == "3" or choice == "orange":
            print "You chose door #3. OK!"
            steps += 1
            set_previous_room = 2
            room_4()
        elif choice == "4" or choice == "green":
            print "You chose door #4. OK!"
            steps += 1
            set_previous_room = 2
            room_5()
        elif choice == "5" or choice == "blue":
            print "You chose door #5. You will go to the room #6."
            steps += 1
            set_previous_room = 2
            room_6()
        elif choice == "go back":
            set_previous_room = 2
            go_to_room(previous_room_now)
        else:
            print "I don't understand you."
            room_2_choice()
    room_2_choice()

def room_3():
    welcome_text_room(3)

    global previous_room_now
    global set_previous_room

    previous_room_now = set_previous_room

    print "It has two doors:"
    print "1. Yellow."
    print "2. Red."
    print "\nWhich one do you take?"

    def room_3_choice():
        global steps
        global previous_room_now
        global set_previous_room

        choice = raw_input("> ")

        if choice == "1" or choice == "yellow":
            print "You chose door #1. OK!"
            steps += 1
            set_previous_room = 3
            room_2()
        elif choice == "2" or choice == "red":
            print "You chose door #2. OK!"
            steps += 1
            set_previous_room = 3
            room_4()
        elif choice == "go back":
            set_previous_room = 3
            go_to_room(previous_room_now)
        else:
            print "I don't understand you."
            room_2_choice()
    room_3_choice()

def room_4():
    welcome_text_room(4)

    global previous_room_now
    global set_previous_room

    previous_room_now = set_previous_room

    print "It has four doors:"
    print "1. Red."
    print "2. Green."
    print "3. Purple"
    print "4. Orange."
    print "\nWhich one do you take?"

    def room_4_choice():
        global steps
        global previous_room_now
        global set_previous_room

        choice = raw_input("> ")

        if choice == "1" or choice == "red":
            print "You chose door #1. OK!"
            steps += 1
            set_previous_room = 4
            room_3()
        elif choice == "2" or choice == "green":
            print "You chose door #2. OK!"
            steps += 1
            set_previous_room = 4
            room_12()
        elif choice == "3" or choice == "purple":
            print "You chose door #3. But there are a lot of stones in front of it."
            print "You can't open it."
            steps += 1
            room_4_choice()
        elif choice == "4" or choice == "orange":
            print "You chose door #4. OK!"
            steps += 1
            set_previous_room = 4
            room_2()
        elif choice == "go back":
            set_previous_room = 4
            go_to_room(previous_room_now)
        else:
            print "I don't understand you."
            room_4_choice()
    room_4_choice()

def room_5():
    welcome_text_room(5)

    global previous_room_now
    global set_previous_room

    previous_room_now = set_previous_room

    print "It has just one door:"
    print "1. Green door."

    print "\nDo you want to open that door?\n"

    def room_5_choice():
        global steps
        global previous_room_now
        global set_previous_room

        choice = raw_input("> ")

        if choice == "1" or choice == "yes" or choice == "open" or choice == "green":
            print "You chose door #1. OK!"
            steps += 1
            set_previous_room = 5
            room_2()
        elif choice == "no":
            print "Be brave, open that door!"
            room_5_choice()
        elif choice == "go back":
            steps += 1
            go_to_room(previous_room_now)
        else:
            print "I don't understand you."
            room_5_choice()
    room_5_choice()

def room_6():
    welcome_text_room(6)

    unfinished_room(6)

def room_7():
    welcome_text_room(7)

    unfinished_room(7)

def room_7():
    welcome_text_room(8)

    unfinished_room(8)

def room_9():
    welcome_text_room(9)

    unfinished_room(9)

def room_10():
    welcome_text_room(10)

    unfinished_room(10)

def room_11():
    welcome_text_room(11)

    unfinished_room(11)

def room_12():
    global steps
    global previous_room_now
    global set_previous_room

    previous_room_now = set_previous_room

    welcome_text_room(4)

    print "There is a monster! You ran away."
    steps += 1
    set_previous_room = 12
    go_to_room(previous_room_now)

# Start the game
room_1()
