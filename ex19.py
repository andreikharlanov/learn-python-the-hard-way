# define the 'cheese_and_crackers' function, it takes two arguments: 'cheese_count' and 'boxes_of_crackers'
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print a string, insert the value of the argument 'cheese_count' instead of %d
    print "You have %d cheeses!" % cheese_count
    # print a string, insert the value of the argument 'boxes_of_crackers' instead of %d
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # print a string
    print "Man that's enough for a party!"
    # print a string, put new line in the end
    print "Get a blanket.\n"

# print a string
print "We can just give the function numbers directly:"
# call the 'cheese_and_crackers' function this arguments: 20 and 30
cheese_and_crackers(20, 30)

# print a string
print "OR, we can use variables from our script:"
# set the value of the variable 'amount_of_cheese' to 10
amount_of_cheese = 10
# set the value of the variable 'amount_of_crackers' to 50
amount_of_crackers = 50

# call the 'cheese_and_crackers' function this arguments: the value of the variable 'amount_of_cheese' and the value of the variable 'amount_of_crackers'
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print a string
print "We can even do math inside too:"
# call the 'cheese_and_crackers' function this arguments: 10 + 20 and 5 + 6
cheese_and_crackers(10 + 20, 5 + 6)

# print a string
print "And we can combine the two, variables and math:"
# call the 'cheese_and_crackers' function this arguments: the value of the variable 'amount_of_cheese' + 100 and the value of the variable 'amount_of_crackers' + 1000
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
