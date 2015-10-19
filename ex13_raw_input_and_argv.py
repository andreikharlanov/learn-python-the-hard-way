from sys import argv

script, argument = argv

name = raw_input("What's your name, by the way? ")

print "So, you called", script, "script"
print "And gave it this argument:", argument
print "Thank you, %s!" % name
