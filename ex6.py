# assign the value to the variable 'x' to the string "There are %d types of people.", insert '10' as an integer number to that string in place of %d
x = "There are %d types of people." % 10
# assign the value of the variable 'binary' to the string "binary"
binary = "binary"
# assign the value of the variable 'do_not' to the string "don't"
do_not = "don't"
# assign the value of the variable 'y' to the string "Those who know %s and those who %s.", insert the values of the variables 'binary' and 'do_not' to the places with %s in that string
y = "Those who know %s and those who %s." % (binary, do_not)

# print the value of the varialbe 'x' to the terminal
print x
# print the value of the varialbe 'y' to the terminal
print y

# print the string "I said: %r." and insert the value of the varible 'x' to the place with %r
print "I said: %r." % x
# print the string "I also said: '%s'." and insert the value of the varible 'y' as string to the place with %s
print "I also said: '%s'." % y

# assign the value of the variable 'hilarious' to False
hilarious = False
# assign the value of the variable 'joke_evaluation' to the string "Isn't that joke so funny?! %r", where %r is a place where we can insert any value later
joke_evaluation = "Isn't that joke so funny?! %r"

# print the value of the variable 'joke_evaluation' and insert the value of the variable 'hilarious' in a place with %r in 'joke_evaluation'
print joke_evaluation % hilarious

# assign the value of the variable 'w' to the string "This is the left side of..."
w = "This is the left side of..."
# assign the value of the variable 'e' to the string "a string with a right side."
e = "a string with a right side."

# pring the value of the variable 'w' and then print the value of the variable 'e'
print w + e
