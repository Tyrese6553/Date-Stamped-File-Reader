import os
import sys
import re

def main():
    #file = "Y2000M01D01"

    path = r"C:\testing"
    files = os.scandir(path)
    new_files = []
    for file in files:
        if file.is_file():
            new_files.append(file.name)


    date_list = []
    pattern = r"^Y([0-9]{4})M(0[0-9]|1[0-2])D(0[1-9]|1[0-9]|2[0-9]|3[0-1])\.[0-9]{4}$"
    for file in new_files:
        date = []
        matches = re.match(pattern, file)
        if matches:
            y = int(matches.group(1))
            m = int(matches.group(2))
            d = int(matches.group(3))
        date.append(y)
        date.append(m)
        date.append(d)
        date_list.append(date)
    print(date_list)






if __name__ == "__main__":
    main()