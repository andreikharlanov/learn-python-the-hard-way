from sys import argv

script, filename_to_read = argv

txt = open(filename_to_read)

print txt.read()
txt.close()
