import random
import time
from sys import exit

steps = 0

previous_room_now = 0

set_previous_room = 0

coins = 0

coins_room_3 = False

# If a user has ever tooken coins in the room #5 behind the monster
coins_room_5 = False

monster_woken_up_room_5 = False

coins_choice_too_much = False

treasure_knowledge = False

treasure = False

tunnel_door = False

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
            if previous_room_now != 0:
                set_previous_room = 1
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
            steps += 1
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

    print "It has two doors and a pile of coins. So you have some options what to do:"
    print "1. Open yellow door."
    print "2. Open red door."
    print "3. Take some coins."

    print "\nWhat do you want to do?"

    def room_3_choice():
        global steps
        global previous_room_now
        global set_previous_room
        global coins
        global coins_room_3
        global coins_choice_too_much

        choice = raw_input("> ")

        if choice == "1" or choice == "yellow" or choice == "open yellow door" or choice == "yellow door":
            print "You chose door #1. OK!"
            steps += 1
            set_previous_room = 3
            room_2()
        elif choice == "2" or choice == "red":
            print "You chose door #2. OK!"
            steps += 1
            set_previous_room = 3
            room_4()
        elif coins_room_3 == False and choice == "3" or choice == "coins" or choice == "take coins" or choice == "take some coins":
            steps += 1
            print "OK, how many coins do you want to take?"
            coins_choice = raw_input("> ")
            coins_amount = int(coins_choice)
            if coins_amount == 0:
                steps += 1
                coins_room_3 = True
                print "Why did this? Don't waste my time."
                print "You have 0 coins but less time then before. Stupid."
                print "Now choose what door to open next."
                room_3_choice()
            elif coins_amount > 0 and coins_amount <= 3:
                steps += 1
                coins_room_3 = True
                coins += coins_amount
                print "Cool, now you have %d coins in your pocket." % coins
                print "Now choose what door to open next."
                room_3_choice()
            elif coins_amount > 3:
                steps += 1
                coins_room_3 = True
                coins_choice_too_much = True

                print "Oh, you are greedy. We don't alow to take so much coins here."
                print "You're trapped in a cage for your greediness."
                print "You'll be trapped for %d seconds as you tried to take %d coins." % (coins_amount, coins_amount)

                seconds = coins_amount

                while seconds > -1:
                    if seconds > 1:
                        print "You need to wait for %d seconds." % seconds
                        seconds -= 1
                        time.sleep(1)
                    elif seconds == 1:
                        print "You need to wait for 1 second."
                        seconds -= 1
                        time.sleep(1)
                    elif seconds == 0:
                        seconds -= 1
                        print "You are free now."
                        print "Choose what door to open next."

                room_3_choice()
        elif (coins_room_3 == True and choice == "3" and coins > 0 or
            coins_room_3 == True and choice == "coins" and coins > 0 or
            coins_room_3 == True and choice == "take coins" and coins > 0 or
            coins_room_3 == True and choice == "take some coins" and coins > 0):
            steps += 1
            print "Don't be greedy, you've already took some coins before."
            print "Now choose what door to open next."
            room_3_choice()
        elif (coins_room_3 == True and choice == "3" and coins == 0 and coins_choice_too_much == False or
            coins_room_3 == True and choice == "coins" and coins == 0 and coins_choice_too_much == False or
            coins_room_3 == True and choice == "take coins" and coins == 0 and coins_choice_too_much == False or
            coins_room_3 == True and choice == "take some coins" and coins == 0 and coins_choice_too_much == False):
            steps += 1
            print "You are not allowed to touch coins again, because last time you wasted everyone's time."
            print "Stupid."
            print "Now choose what door to open next."
            room_3_choice()
        elif (coins_room_3 == True and choice == "3" and coins_choice_too_much == True or
            coins_room_3 == True and choice == "coins" and coins_choice_too_much == True or
            coins_room_3 == True and choice == "take coins" and coins_choice_too_much == True or
            coins_room_3 == True and choice == "take some coins" and coins_choice_too_much == True):
            steps += 1
            print "You are not allowed to touch coins again, you are too greedy."
            print "Try taking less coins next time."
            print "Stupid."
            print "Now choose what door to open next."
            room_3_choice()
        elif choice == "go back":
            steps += 1
            set_previous_room = 3
            go_to_room(previous_room_now)
        else:
            print "I don't understand you."
            room_3_choice()
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
        global treasure_knowledge
        global treasure
        global tunnel_door

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
            if tunnel_door == True:
                steps += 1
                set_previous_room = 4
                if treasure_knowledge == True:
                    print "Oh, you found a treasure in the tunnel!"
                    treasure = True
                room_6()
            else:
                print "You chose door #3. But there are a lot of stones in front of it."
                print "You can't open it."
                room_4_choice()
        elif choice == "4" or choice == "orange":
            print "You chose door #4. OK!"
            steps += 1
            set_previous_room = 4
            room_2()
        elif choice == "go back":
            steps += 1
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

    print "\nAnd you see a pile of coins in the corner. But there is a monster in front of the coins."
    print "The monster may be sleeping. But you are not sure."

    print "\nDo you want to open green door?"
    print "Or do you want to kick the monster's ass?"
    print "Or you want to try to coins?"

    def room_5_choice():
        global steps
        global previous_room_now
        global set_previous_room
        global coins
        global coins_room_5
        global monster_woken_up_room_5

        choice = raw_input("> ")

        if choice == "1" or choice == "door" or choice == "open" or choice == "green":
            print "You chose door #1. OK!"
            steps += 1
            set_previous_room = 5
            room_2()
        elif choice == "coins":
            if coins_room_5 == False and monster_woken_up_room_5 == False:
                steps += 1
                coins += 5
                coins_room_5 = True
                print "Good choice! Took 5 coins from the pile! Now you have %d coins." % coins
                room_5()
            elif coins_room_5 == True and monster_woken_up_room_5 == False:
                steps += 1
                coins -= 5
                monster_woken_up_room_5 = True
                print "You are too greedy! You have already took coins from this room."
                print "This time you woke up the monster and he took 5 coins from you."
                print "Now you have %d coins." % coins
            else:
                steps += 1
                print "The moster is in the way and she is not sleeping. You'd beter go away."
                room_5()
        elif choice == "monster" or choice == "kick ass" or choice == "kick":
            steps += 1
            print "You're stupid. Now the monster is awake. She is blocking the way to the coins."
            monster_woken_up_room_5 = True
            room_5()
        elif choice == "go back":
            steps += 1
            set_previous_room = 5
            go_to_room(previous_room_now)
        else:
            print "I don't understand you."
            room_5_choice()
    room_5_choice()

def room_6():
    welcome_text_room(6)

    global previous_room_now
    global set_previous_room

    previous_room_now = set_previous_room

    print "It has four doors:"
    print "1. Blue."
    print "2. Purpe."
    print "3. Yellow."
    print "4. Red."
    print "\nWhich one do you take?"

    def room_6_choice():
        global steps
        global previous_room_now
        global set_previous_room
        global treasure
        global tunnel_door

        choice = raw_input("> ")

        if choice == "1" or choice == "blue":
            print "You chose door #1. OK!"
            steps += 1
            set_previous_room = 6
            room_2()
        elif choice == "2" or choice == "purple":
            print "You chose door #2. OK!"
            if treasure_knowledge == True:
                print "Oh, you found a treasure in the tunnel!"
                treasure = True
            steps += 1
            set_previous_room = 6
            tunnel_door = True
            room_4()
        elif choice == "3" or choice == "yellow":
            print "You chose door #3. OK!"
            steps += 1
            set_previous_room = 6
            room_7()
        elif choice == "4" or choice == "red":
            print "You chose door #4. OK!"
            steps += 1
            set_previous_room = 6
            room_9()
        elif choice == "go back":
            steps += 1
            set_previous_room = 6
            go_to_room(previous_room_now)
        else:
            print "I don't understand you."
            room_6_choice()
    room_6_choice()

def room_7():
    welcome_text_room(7)

    global previous_room_now
    global set_previous_room

    previous_room_now = set_previous_room

    print "It has two doors:"
    print "1. Yellow."
    print "2. Green."
    print "And you see a wayfarer in the dark corner."
    print "\nDo you want to open a door? If yes, what door?"
    print "Or do you want to talk with the wayfarer?"

    def room_7_choice():
        global treasure_knowledge
        global steps
        global previous_room_now
        global set_previous_room

        choice = raw_input("> ")

        if choice == "1" or choice == "yellow":
            print "You chose door #1. OK!"
            steps += 1
            set_previous_room = 7
            room_6()
        elif choice == "2" or choice == "green":
            print "You chose door #2. OK!"
            steps += 1
            set_previous_room = 7
            room_8()
        elif choice == "talk" or choie == "wayfarer":
            steps += 1
            print "You talk to the wayfarer."
            print "He told you that in the tunnel behind the purple door in the room #6 you can find a treasure."
            print "Go there if you want."
            treasure_knowledge = True
            room_7()
        elif choice == "go back":
            steps += 1
            set_previous_room = 7
            go_to_room(previous_room_now)
        else:
            print "I don't understand you."
            room_7_choice()
    room_7_choice()

def room_8():
    welcome_text_room(8)

    global previous_room_now
    global set_previous_room

    previous_room_now = set_previous_room

    print "It has two doors:"
    print "1. Green."
    print "2. Blue."
    print "\nWhich one do you take?"

    def room_8_choice():
        global steps
        global previous_room_now
        global set_previous_room

        choice = raw_input("> ")

        if choice == "1" or choice == "green":
            print "You chose door #1. OK!"
            steps += 1
            set_previous_room = 8
            room_7()
        elif choice == "2" or choice == "blue":
            print "You chose door #2. OK!"
            steps += 1
            set_previous_room = 8
            room_9()
        elif choice == "go back":
            steps += 1
            set_previous_room = 8
            go_to_room(previous_room_now)
        else:
            print "I don't understand you."
            room_8_choice()
    room_8_choice()

def room_9():
    welcome_text_room(9)

    global previous_room_now
    global set_previous_room

    previous_room_now = set_previous_room

    print "It has four doors:"
    print "1. Red."
    print "2. Blue."
    print "3. Green."
    print "4. Yellow."
    print "\nWhich one do you take?"

    def room_9_choice():
        global steps
        global previous_room_now
        global set_previous_room

        choice = raw_input("> ")

        if choice == "1" or choice == "red":
            print "You chose door #1. OK!"
            steps += 1
            set_previous_room = 9
            room_6()
        elif choice == "2" or choice == "blue":
            print "You chose door #2. OK!"
            steps += 1
            set_previous_room = 9
            room_8()
        elif choice == "3" or choice == "green":
            print "You chose door #3. OK!"
            steps += 1
            set_previous_room = 9
            room_11()
        elif choice == "4" or choice == "yellow":
            print "You chose door #4. OK!"
            steps += 1
            set_previous_room = 9
            room_10()
        elif choice == "go back":
            steps += 1
            set_previous_room = 9
            go_to_room(previous_room_now)
        else:
            print "I don't understand you."
            room_9_choice()
    room_9_choice()

def room_10():
    welcome_text_room(10)

    global previous_room_now
    global set_previous_room

    previous_room_now = set_previous_room

    print "It has just one door:"
    print "1. Yellow door."

    print "\nDo you want to open that door?\n"

    def room_10_choice():
        global steps
        global previous_room_now
        global set_previous_room

        choice = raw_input("> ")

        if choice == "1" or choice == "yes" or choice == "open" or choice == "yellow":
            print "You chose door #1. OK!"
            steps += 1
            set_previous_room = 10
            room_9()
        elif choice == "no":
            print "Be brave, open that door!"
            room_10_choice()
        elif choice == "go back":
            steps += 1
            set_previous_room = 10
            go_to_room(previous_room_now)
        else:
            print "I don't understand you."
            room_10_choice()
    room_10_choice()

def room_11():
    welcome_text_room(11)

    global previous_room_now
    global set_previous_room

    previous_room_now = set_previous_room

    print "It has three doors:"
    print "1. Green."
    print "2. Red."
    print "3. Black."
    print "\nWhich one do you take?"

    def room_11_choice():
        global steps
        global previous_room_now
        global set_previous_room
        global coins

        choice = raw_input("> ")

        if choice == "1" or choice == "green":
            print "You chose door #1. OK!"
            steps += 1
            set_previous_room = 11
            room_9()
        elif choice == "2" or choice == "red":
            print "You chose door #2. OK!"
            print "You found the exit. Nice. Now chill."
            steps += 1
            print "You completed the game in %d steps." % steps
            print "You have %d coins in you pocket." % coins
            if coins_room_3 == True and coins == 0:
                print "You can blame only yourself for your financial situation."
                print "You had your chance to take some coins. But you blew it."
                print "Stupid."
            if treasure == True:
                print "And you found a treasure in the tunnel!"
            exit(0)
        elif choice == "3" or choice == "black":
            print "You chose door #3. OK!"
            steps += 1
            set_previous_room = 11
            room_13()
        elif choice == "go back":
            steps += 1
            set_previous_room = 11
            go_to_room(previous_room_now)
        else:
            print "I don't understand you."
            room_11_choice()
    room_11_choice()

def room_12():
    global steps
    global previous_room_now
    global set_previous_room

    previous_room_now = set_previous_room

    welcome_text_room(12)

    print "There is a monster! You ran away."
    steps += 1
    set_previous_room = 12
    go_to_room(previous_room_now)

def room_13():
    global steps
    global previous_room_now
    global set_previous_room

    previous_room_now = set_previous_room

    welcome_text_room(13)

    print "There is a monster! You ran away."
    steps += 1
    set_previous_room = 13
    go_to_room(previous_room_now)

# Start the game
room_1()
