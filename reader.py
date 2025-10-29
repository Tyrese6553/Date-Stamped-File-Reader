import os
import sys

def main():
    file = sys.argv[1]

    path = r"C:\testing"
    files = os.listdir(path)

    new_files = [os.path.splitext(file)[0] for file in files]
    
    print(new_files)
    
    if file in new_files:
        print(file)
    else:
        print("File not found")






if __name__ == "__main__":
    main()