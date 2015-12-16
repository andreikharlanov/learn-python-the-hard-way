from sys import exit

def interpret_string(s):
    if not isinstance(s, basestring):
        return False
    if s.isdigit():
        return int(s)
    else:
        try:
            return float(s)
        except ValueError:
            return False

def get_number():
    choice = raw_input("> ")

    number = interpret_string(choice)

    if number == False:
        print "Type a number, idiot!"
        return get_number()
    else:
        return number

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


def dead(why):
    print why, "Good job!"
    exit(0)

gold_room()
