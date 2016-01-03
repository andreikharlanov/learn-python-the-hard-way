import time

print "Hom many seconds do you wish to wait?"

seconds = int(raw_input("> "))

while seconds != 0:
    if seconds == 1:
        print "You need to wait for 1 second."
    elif seconds != 1:
        print "You need to wait for %d seconds." % seconds
    seconds -= 1
    time.sleep(1)
