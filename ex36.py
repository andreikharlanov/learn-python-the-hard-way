steps = 0

previous_room = 1

text_on_the_wall = "\nM... mmm..\n"

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
    print "This room is unfinished. We transfer you to room you entred this one from."
    print "Now you'll go back to %d room." % previous_room
    go_to_room(previous_room)

def room_1():
    welcome_text_room(1)

    global previous_room
    previous_room = 1

    print "It has just two doors:"
    print "1. The first one is behind you, you just entered through it."
    print "2. The second door is infront of you.\n"

    print "Also there is a text on the wall. Do you want to read it?\n"
    print "Say 'yes', if you want to read the text."
    print "Say 'no', if you don't want to read the text and enter the door infront of you."
    print "Say 'back', if you want to go back."

    def room_1_choice():
        global steps

        choice = raw_input("> ")

        if choice == "yes":
            print "Here is the text on the wall:"
            print text_on_the_wall
            steps += 1
            room_1()
        elif choice == "no":
            print "You open the door infront of you "
            steps += 1
            room_2()
        elif choice == "back":
            print "You try to open the door behind you. Tough luck, it's closed."
            steps += 1
            room_1()
        else:
            print "I don't understand you."
            room_1_choice()
    room_1_choice()

def room_2():
    welcome_text_room(2)

    print "It has five doors:"
    print "1. The first one is behind you, you just untered through it."
    print "2. The door on your left."
    print "3. The small door infront of you. It seems unusual."
    print "4. The big door infront of you."
    print "5. The door on the right.\n"
    print "Which one do you take?"

    def room_2_choice():
        global steps
        global previous_room

        choice = raw_input("> ")

        if choice == "first" or choice == "1" or choice == "behind":
            print "You chose door #1. OK!"
            steps += 1
            previous_room = 2
            room_1()
        elif choice == "second" or choice == "2" or choice == "left":
            print "You chose door #2. OK!"
            steps += 1
            previous_room = 2
            room_3()
        elif choice == "third" or choice == "3" or choice == "small":
            print "You chose door #3. OK!"
            steps += 1
            previous_room = 2
            room_4()
        elif choice == "fourth" or choice == "4" or choice == "infront":
            print "You chose door #4. OK!"
            steps += 1
            previous_room = 2
            room_5()
        elif choice == "fifth" or choice == "5" or choice == "right":
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

room_1()
