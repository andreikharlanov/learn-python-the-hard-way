numbers = []

def print_list_creation(stop_number, step):
    for i in range(0, stop_number, step):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

print_list_creation(122,13)

print "The numbers: "

for num in numbers:
    print num
