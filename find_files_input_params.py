import os
import sys

file_to_find = ""
path = ""
recursive = ""

try:
    file_to_find = sys.argv[1]
except IndexError as e:
    file_to_find = input("Name of file to search: ")
    path = input("Path where to search the file: ")
    recursive = input("Recursive searching (type 'R' if yes): ").upper()
    
if path == "":    
    try: 
        path = sys.argv[2]
    except IndexError as e:
        print("Path is missing!")
        path = input("Path where to search the file: ")
        recursive = input("Recursive searching (type 'R' if yes): ").upper()
    

def find_file_recursive(filename, path):
    print("Found files:")
    for dirpath, folders, files in os.walk(path):
        for file in files:
            if file == file_to_find:
                print(os.path.join(dirpath, file))
                
def find_file(filename, path):
    print("Found files:")
    files = [item for item in os.listdir(path) if os.path.isfile(f"{path}\{item}")]
    for f in files:
        if f == file_to_find:
            print(f"{path}\{f}")
        
if __name__ == "__main__":
    if recursive == "R":
        find_file_recursive(file_to_find, path)
    else:
        find_file(file_to_find, path)