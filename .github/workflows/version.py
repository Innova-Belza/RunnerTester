import os

type = ""
with open('versiontype.txt', 'r') as file:
    for line in file:
            type = line

open('versiontype.txt', 'w').close()

with open('version.txt', 'a+') as file:
    last_line = ""
    file.seek(0)
    for line in file:
        last_line = line

    if last_line == "":
            last_line = "version=1.0.0"
    else:
        last_line = last_line.replace("version=", "")
        last_line = last_line.split(".")

        type = type.lower();  
        
        if type == "version":
            last_line = str(int(last_line[0]) + 1) + ".0.0"
        elif type == "major":
            last_line = last_line[0] + "." + str(int(last_line[1]) + 1) + ".0"
        else:
            last_line = last_line[0] + "." + last_line[1] + "." + str(int(last_line[2]) + 1)

    file.write("\nversion=" + last_line) 

