ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Whait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
print stuff

more_stuff = ["Day", "Night", "Song", "Freesbie", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "Threre we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
