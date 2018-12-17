#!/usr/bin/env python

file = open("RadialGliaStudyName files as submitted and put into subdirectories.sh")
lines = file.readlines()
new_file = open("Working_Glia_Submitted_Many_Directories.sh", "a")

for line in lines:
    # get rid of new line character
    # testing to get the line right
    # print line.rstrip() + " --insecure"
    # new line character required cause for loop was taking care of that
    entry = line.rstrip() + " --insecure \n"
    new_file.write(entry)
file.close()
new_file.close()
