#!/usr/bin/env python
terminal_output = open("Dec161056am_currently2DLfails.txt")
terminal_lines = terminal_output.readlines()
shell_script = open("Working_Brain_Submitted_Many_Directories.sh")
shell_lines = shell_script.readlines()
number_of_previous_downloads = 0
last_line = "placeholder"
for line in terminal_lines:
    if "Dload" in line:
        number_of_previous_downloads += 1
    if "GnuTLS recv error" in line:
        print line
        print last_line
        #print line
        print "failure at download number " + str(number_of_previous_downloads)
        print "this is the shell script line that the download failed at: "
        print(shell_lines[number_of_previous_downloads-1])
    last_line = line
terminal_output.close()
shell_script.close()
