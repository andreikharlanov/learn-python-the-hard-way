import random

steps = 0

previous_room = 1

text_on_the_wall = "\nM... mmm..\n"

howdy = ["Hey, boy!", "La-la-la, whom I see...", "Are you back, baby boy?"]

print howdy[random.randrange(0,3)]

def welcome_text_room(room_number):
    print "\n----\n"
    print "You've made %d steps already.\n" % steps
    print "You are in a room #%d.\n" % room_number

def go_to_room(room_number):
    if room_number == 1:
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

def unfinished_room():
    print "This room is unfinished. We'll transfer you to room you entred this one from."
    print "Now you'll go back to %d room." % previous_room
    go_to_room(previous_room)

def room_1():
    welcome_text_room(1)

    global previous_room
    previous_room = 1

    print "It has just two doors:"
    print "1. Green door."
    print "2. Red door.\n"

    print "Also there is a text on the wall. Do you want to read it?\n"
    print "Say 'text', if you want to read the text on the wall."
    print "Say 'red', if you want to enter the red door."
    print "Say 'green', if you want to enter the red door."

    def room_1_choice():
        global steps

        choice = raw_input("> ")

        if choice == "text":
            print "Here is the text on the wall:"
            print text_on_the_wall
            steps += 1
            room_1()
        elif choice == "1" or choice == "red":
            print "You open the red door infront of you."
            steps += 1
            room_2()
        elif choice == "2" or choice == "green" or choice == "back":
            print "You try to open the green door. Tough luck, it's closed."
            steps += 1
            room_1()
        else:
            print "I don't understand you."
            room_1_choice()
    room_1_choice()

def room_2():
    welcome_text_room(2)

    print "It has five doors:"
    print "1. Red."
    print "2. Yellow."
    print "3. The small orange door. It seems unusual."
    print "4. Green."
    print "5. Blue.\n"
    print "Which one do you take?"

    def room_2_choice():
        global steps
        global previous_room

        choice = raw_input("> ")

        if choice == "1" or choice == "red":
            print "You chose door #1. OK!"
            steps += 1
            previous_room = 2
            room_1()
        elif choice == "2" or choice == "yellow":
            print "You chose door #2. OK!"
            steps += 1
            previous_room = 2
            room_3()
        elif choice == "3" or choice == "orange":
            print "You chose door #3. OK!"
            steps += 1
            previous_room = 2
            room_4()
        elif choice == "4" or choice == "green":
            print "You chose door #4. OK!"
            steps += 1
            previous_room = 2
            room_5()
        elif choice == "5" or choice == "blue":
            print "You chose door #5. You will go to the room #6."
            steps += 1
            previous_room = 2
            room_6()
        elif choice == "go back":
            go_to_room(previous_room)
        else:
            print "I don't understand you."
            room_2_choice()
    room_2_choice()

def room_3():
    welcome_text_room(3)

    unfinished_room()

def room_4():
    welcome_text_room(4)

    unfinished_room()

def room_5():
    welcome_text_room(5)

    unfinished_room()

def room_6():
    welcome_text_room(6)

    unfinished_room()

def room_7():
    welcome_text_room(7)

    unfinished_room()
def room_7():
    welcome_text_room(8)

    unfinished_room()

def room_9():
    welcome_text_room(9)

    unfinished_room()

def room_10():
    welcome_text_room(10)

    unfinished_room()

def room_11():
    welcome_text_room(11)

    unfinished_room()

def room_12():
    welcome_text_room(12)

    unfinished_room()

# Start the game
room_1()
