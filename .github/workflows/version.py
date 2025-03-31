import os

with open('version.txt', 'a+') as file:
    try:  # catch OSError in case of a one line file 
        file.seek(-2, os.SEEK_END)
        while file.read(1) != b'\n':
            file.seek(-2, os.SEEK_CUR)
    except OSError:
        file.seek(0)
    last_line = file.readline()

    file.write("\n" + last_line)

