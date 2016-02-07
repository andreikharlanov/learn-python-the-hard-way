# Keywords
# from
from datetime import date

now = date.today()

print now.strftime("Today is %A.")

# and
variable_1 = 1
variable_2 = 2

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

# except, as, finally
def devide_by_zero(x):
    return x / 0

try:
    devide_by_zero(1)
except ZeroDivisionError as why:
    print "Oops. There was an error:", why
finally:
    print "But you are cool."

# for
for i in ["a", "b", "c"]:
    print i * 10

# global

nonsmoker = True

def smoker():
    global nonsmoker

    if nonsmoker == True:
        print "You're nonsmoker! Congratulations, you're smart!"
    else:
        print "You're smoker! Congratulations, you're dumb!"

smoker()

# in
for i in ["s", "b", "r"]:
    print i, "-->", i * 3

# lambda
make_power_function = lambda x, y: x ** y

print make_power_function(2, 2)

# not
apples_in_the_pocket = True

if not apples_in_the_pocket == False:
    print "You have apples!"
elif not apples_in_the_pocket == True:
    print "You don't have apples!"

# or
if apples_in_the_pocket == False or not apples_in_the_pocket == False:
    print "Tricky!"

# pass
def important_function(x, y, z):
    pass # remember to implement!

# raise, try
try:
    raise NameError
except NameError: pass

# return
def hi(name):
    return "Hi, " + name

print hi("Andrei")

# while
i = 20
while i > 10:
    print "'i' is still bigger than 10. I is:", i
    i -= 2

# with
with open("ex0.txt", "r") as file:
    print file.read()

# yield
my_list = [zz * zz * zz for zz in range(0,10)]
my_generator = (z * z for z in range(0, 10))

print "\nGenerator first time:"
for i in my_generator:
    print i

print "\nGenerator second time:"
for i in my_generator:
    print i

print "\nList first time:"
for i in my_list:
    print i

print "\nList second time:"
for i in my_list:
    print i

print "----"

def create_generator(power, r):
    list = range(r)
    for i in list:
        yield i ** power

my_generator_2 = create_generator(2, 11)

for i in my_generator_2:
    print i

# Data types
# True, False, None, string, number, float, list, dictionary

was_home = True
ate_apple = True
apples_in_bin = None
apples_name = "Gloria"
apples = 3
seeds_per_apple = 3.2
homework = ["Russian", "Mathematics", "History"]
grades = {"Russian": 2, "Mathematics": 2, "History": 5}

if was_home == True and ate_apple == False:
    print "You should have ate that apple."

if ate_apple == False:
    apples_in_bin =  0
else:
    apples_in_bin = 1
    apples -= 1
    print "Now you can grow %d apple trees." % seeds_per_apple * apples_in_bin

berated = False

print "What's your grade for the Russian class?"
print "Oh, i see, its", grades["Russian"]

if "History" in grades:
    print "At least they teach you history in school."

for i in homework:
    if berated == False:
        print "Now go study", i + "!"
        berated = True
    else:
        print "And", i + "!"

# String Escape Sequences
# \\, \', \", \a, \b, \f, \n, \r, \t, \v
print "This is a backslash symbol: \\"
print "This is a double quote symbol: \""
print 'This is a single quote symbol: \''
print "This 'bell' makes a sound: \a"
print "Backspace Word\bld"
print "Before formfeed.\fAfter formfeed."
print "Ha."
print "\nNew line here."
print "Rawwaw?\rR!"
print "Tab? \tYes!"
print "Vertical\vtab\vto\vfinish\vall\vthis."

# String formats
string_1 = "Aha."

print "We have %d apples." % 45
print "And %i pears." % 0
print "45 is %o in octal number system." % 45
print "45 is %x in hexadecimal number system (lowercase)." % 45
print "45 is %X in hexadecimal number system (uppercase)." % 45
print "We can write 45 as %e using exponential notation (lowercase)" % 45
print "We can write 45 as %E using exponential notation (uppercase)" % 45
print "As I said, we have %f apples." % 45
print "And %F pears." % 0
print "How many apple do we have? %g!" % 45
print "How many apple do we have? %G!" % 45
print "%%c accepts integer or single character string: %c and %c." % ("Y", 34)
print "You can throw anything at %%r: %r, %r, %r" % ("Yay", 45, -23.234)
print "And %%s accepts boring strings: %s." % string_1
print "100%%r!"

# Operators
print 5 + 1 - 3 * 2 / 4 ** 3 // 3

if 3 > 1 and 4 < 45 and 54 <= 54 and 55 >= 13 and 12 == 12 and 12 != 3:
    print "We are good."

print "A %s is not a %s." % ("Fool", "fool")

for i in [1, 2, 3]:
    print i ** (5 ** i)

yrad = {"xit": 5, "yh": 10}

xoma = 1
print xoma

xoma += 15
print xoma

xoma -= 3
print xoma

xoma /= 3
print xoma

xoma *= 23
print xoma

xoma //= 2
print xoma

xoma %= 13
print xoma

xoma **= 23
print xoma
