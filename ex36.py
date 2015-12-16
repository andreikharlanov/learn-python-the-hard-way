steps = 0

def room():
    print "    "
    print "----"
    print "You've made %d steps already." % steps
    print "You are in a room #"
    print "It has two doors."
    print "1. The first one is behind you, you just untered through it."
    print "2. The second door is on the left."
    print "3. The third door is on the right."
    print "Which one do you take?"

    def room_1_choice():
        global steps

        door_choice = raw_input("> ")

        if door_choice == "first" or door_choice == "1" or door_choice == "behind":
            print "You chose door #1. OK!"
            steps += 1
            room()
        elif door_choice == "second" or door_choice == "2" or door_choice == "left":
            print "You chose door #2. OK!"
            steps += 1
            room()
        elif door_choice == "third" or door_choice == "3" or door_choice == "right":
            print "You chose door #3. OK!"
            steps += 1
            room()
        else:
            print "I don't understand you."
            room_1_choice()
    room_1_choice()

room()
