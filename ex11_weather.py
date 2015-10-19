live_in = raw_input('Where do you live now? ')
weather = raw_input("Is it hot or cold in " + live_in + " now? ")

print "So, you live in", live_in, "and the weater there is", weather, "now. It's nice to know!"
print "So, you live in %s and the weater there is %s now. It's nice to know!" % (live_in, weather)
