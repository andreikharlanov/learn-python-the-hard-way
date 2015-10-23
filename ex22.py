from sys import argv
from os.path import exists

script_name, command_line_argument_1, command_line_argument_2 = argv

"This is a string."

variable_str = "This is the value of the variable 'variable_str'."

variable_short_str = "One! "

variable_int = 2

variable_float = 2.45

variable_boolen = True

print "Print this string."

print variable_str

print variable_int

print variable_float

print variable_boolen

print command_line_argument_1

print "Insert a string here: %s" % variable_str

print "Insert an integer here: %d" % variable_int

print "Insert a floating number: %f" % variable_float

print "Insert a boolen value: %s" % variable_boolen

print "Insert a raw content of the varibale here for debugging: %r" % variable_int

print "Insert three strings: %s, %s, %s." % ("la", "la", "la")

print "Insert an integer and a string: %d, %s" % (variable_int, variable_str)

print "Insert a string three times: %s" % (variable_short_str * 3)

print "Left part plus " + "right part."

print "Left part,", "right part."

print "_" * 40

print "\nOne\nOne\tTwo\nOne\tTwo\tThree\n"

print "\"\t\'\n"

text_file_from = open(command_line_argument_1)
text_file_from_content = text_file_from.read()

print "This is the content of the %s now: %s" % (command_line_argument_1, text_file_from_content)

text_file_to_write = open(command_line_argument_2, 'w')
text_file_to_write.close()

text_file_to_read = open(command_line_argument_2, 'r')
text_file_to_content = text_file_to_read.read()
print "This is the content of the %s BEFORE COPY: %s" % (command_line_argument_2, text_file_to_content)
text_file_to_read.close()

text_file_to_write = open(command_line_argument_2, 'w')
text_file_to_write.write(text_file_from_content)
text_file_to_write.close()
text_file_from.close()

text_file_to_read = open(command_line_argument_2, 'r')
text_file_to_content = text_file_to_read.read()
print "This is the content of the %s AFTER COPY: %s" % (command_line_argument_2, text_file_to_content)
text_file_to_read.close()
