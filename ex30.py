# assign value "30" to the variable "people"
people = 30
# assign value "40" to the variable "cars"
cars = 40
# assign value "15" to the variable "trucks"
trucks = 15

# check if the value of "cars" is bigger than the value of "people"; if True, print the line
if cars > people:
    print "We should take the cars."
# if the last comparison returnsFalse, check if the value of "cars" is smaller than the value of "people"; if True, print the line
elif cars < people:
    print "We should not take the cars."
# if the last comparison returnsFalse, print the line
else:
    print "We can't decide."

# check if the value of "trucks" is bigger than the value of "cars"; if True, print the line
if trucks > cars:
    print "That's too many trucks."
# if the last comparison returns False, check if the value of "trucks" is smaller than the value of "cars"; if True, print the line
elif trucks < cars:
    print "Maybe we could take the trucks."
# if the last comparison returns False, print the line
else:
    print "We still can't decide."

# check if the value of "people" is bigger than the value of "trucks"; if True, print the line
if people > trucks:
    print "Alright, let's just take the trucks."
# if the last comparison returns False, print the line
else:
    print "Fine, let's stay home then."
