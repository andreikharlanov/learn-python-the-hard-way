# import argv variables from the "sys" module
from sys import argv

# get the value for the 'script' and the 'filename' variables from the script arguments
script, filename = argv

# open a file with the name stored in the 'filename' variable and assign that file to the 'txt' variable
txt = open(filename)

# print a string with the name of the opened file
print "Here's your file %r:" % filename
# print the content of the file assigned to 'txt' variable
print txt.read()

# pring the string
print "Type the filename again:"
# get a name of the new file from the user
file_again = raw_input("> ")

# open the file with the name stored in 'file_again' variable and assign that file to the 'txt_again' variable
txt_again = open(file_again)

#print the content of the file assigned to the 'txt_again' variable
print txt_again.read()
