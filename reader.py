import os
import sys
import re

def main():
    y_input = int(input())
    m_input = int(input())
    d_input = int(input())

    path = r"C:\testing"
    files = os.scandir(path)
    new_files = []
    pattern = r"^Y([0-9]{4})M(0[0-9]|1[0-2])D(0[1-9]|1[0-9]|2[0-9]|3[0-1])\.[0-9]{4}$"
    for file in files:
        if file.is_file() and re.match(pattern, file.name):
            new_files.append(file.name)

    date_list = []
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

    for i, file in enumerate(date_list):
        if file[0] == y_input and file[1] == m_input and file[2] == d_input:
            print(new_files[i])



if __name__ == "__main__":
    main()