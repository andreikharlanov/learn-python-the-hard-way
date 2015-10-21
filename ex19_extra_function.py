from sys import argv

script, arg_command_line1, arg_command_line2 = argv

arg_command_line_int = int(arg_command_line1)
arg_command_line_len = len(arg_command_line2)

def hummus_stars_smothie(amount_of_hummus, stars_count, amount_of_smothie):
    print "\n\n\n______________________________________________\n"
    print "You have %d jars of hummus?" % amount_of_hummus
    print "*" * stars_count
    print "And only %d jars of smothie..." % amount_of_smothie
    print "______________________________________________\n"

arg1 = 15
arg2 = 30
arg3 = 48
arg4 = 50
arg5 = 134

arg_user = int(raw_input("What's you secret numer? "))

hummus_stars_smothie(10, 10, 20)

hummus_stars_smothie(10 + 15, 20 - 2, 20 * 7)

hummus_stars_smothie(arg1, arg2, arg3)

hummus_stars_smothie(arg1 + 3, arg5 - 14, arg3 * 2)

hummus_stars_smothie(10 - 2, arg1, 4 * arg2)

hummus_stars_smothie(arg2 - arg1, arg1 * arg3, arg4 - 3)

hummus_stars_smothie(arg_user, arg_user + 10 , arg_user * arg1)

hummus_stars_smothie(10, 15, arg_command_line_int)

hummus_stars_smothie(arg_command_line_int * arg_user, 10 , arg_command_line_int - 4)

hummus_stars_smothie(arg_command_line_len, 19, arg5 * 10)
