numbers = []

def print_list_creation(stop_number):
    i = 0
    while i < stop_number:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

print_list_creation(6)


print "The numbers: "

for num in numbers:
    print num
