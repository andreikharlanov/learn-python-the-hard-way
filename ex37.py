variable_1 = 1
variable_2 = 2

# and
if variable_1 == 1 and variable_2 == 2:
    print "Everything is OK!\n"

# assert
a = "a"

assert a == "a", "Oops, 'a' is not an 'a'"

# break
for n in range(2, 7):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        # loop fell through without finding a factor
        print n, 'is a prime number'

# continue
for i in range(1,5):
    # if i + 1 > 2 start a new iteration of the for-loop
    # i will be printed only if i == 1 or i == 2
    if i + 1 > 3:
        continue
    print i

# def
def print_yo(name):
    print "Yo,", name

print_yo("Andrei")

print "\n-----\n"

# del
list_1 = ['a', 'b', 'c']

del list_1[0]

print list_1

# if, elif, else
print "\n-----\n"
for i in range(0,10):
    if (i % 2) == 0 and i != 0:
        print i
        print "'i' is an equal number!"
    elif (i % 2) == 0:
        print i
        print "'i' is 0!"
    else:
        print i
        print "'i' is an odd number!"

# except, as
def devide_by_zero(x):
    return x / 0

try:
    devide_by_zero(1)
except ZeroDivisionError as why:
    print "Oops. There was an error:", why

# for
for i in ["a", "b", "c"]:
    print i * 10
