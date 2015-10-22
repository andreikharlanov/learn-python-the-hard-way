# import argv from 'sys' module
from sys import argv

# get the values of the variables 'script' and 'input_file' from the command line arguments
script, input_file = argv

# define the 'print_all' function
def print_all(f):
    print f.read()

# define the 'print_all' function
def rewind(f):
    f.seek(0)
# define the 'print_a_line' function
def print_a_line(line_count, f):
    # print the value of the variable 'line_count' and the result of calling the 'readline' function on the 'f' argument
    print line_count, f.readline()

# assign the value of the variable current_file to 'input_file' file object
current_file = open(input_file)

# print a string
print "First let's print the whole file:\n"

# run the function 'print_all' with the 'current_file' as an argument
print_all(current_file)

# print a string
print "Now let's rewind, kind of like a tape."

# run the function 'rewind' with the 'current_file' as an argument
rewind(current_file)

# print a string
print "Let's print three lines:"

# assign the value of 1 to the 'current_line' variable
current_line = 1
# run the function 'print_a_line' with 'current_line' and 'current_file' as arguments
print_a_line(current_line, current_file)

# increase the value of the 'current_line' variable by 1
current_line += 1
# run the function 'print_a_line' with 'current_line' and 'current_file' as arguments
print_a_line(current_line, current_file)

# increase the value of the 'current_line' variable by 1
current_line += 1
# run the function 'print_a_line' with 'current_line' and 'current_file' as arguments
print_a_line(current_line, current_file)
