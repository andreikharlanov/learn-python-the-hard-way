import time

seconds = 0

while seconds < 15:
    print seconds
    if seconds < 14:
        print "You need to wait for %d seconds." % (15 - seconds)
    elif seconds == 14:
        print "You need to wait for 1 second."
    seconds += 1
    time.sleep(1)
