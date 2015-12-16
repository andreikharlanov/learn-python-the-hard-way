steps = 0

text_on_the_wall = "M... mmm.."

def first_text_room(room_number):
    print "    "
    print "----"
    print "    "
    print "You've made %d steps already." % steps
    print "You are in a room #%d" % room_number

def room_1():
    first_text_room(1)

    print "It has just two doors."
    print "1. The first one is behind you, you just untered through it."
    print "2. The second door is infront of you."

    print "Also there is a text on the wall. Do you want to read it?"
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
    first_text_room(2)

    print "It has two doors."
    print "1. The first one is behind you, you just untered through it."
    print "2. The second door is on the left."
    print "3. The third door is on the right."
    print "Which one do you take?"

    def room_2_choice():
        global steps

        choice = raw_input("> ")

        if choice == "first" or choice == "1" or choice == "behind":
            print "You chose door #1. OK!"
            steps += 1
            room_1()
        elif choice == "second" or choice == "2" or choice == "left":
            print "You chose door #2. OK! But it's closed."
            steps += 1
            room_2()
        elif choice == "third" or choice == "3" or choice == "right":
            print "You chose door #3. OK! But it's closed."
            steps += 1
            room_2()
        else:
            print "I don't understand you."
            room_2_choice()
    room_2_choice()

room_1()
