import os
import sys
import fnmatch

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
        try:
            recursive = sys.argv[3]
        except IndexError as e:
            pass               
    except IndexError as e:
        print("Path is missing!")
        path = input("Path where to search the file: ")
        recursive = input("Recursive searching (type 'R' if yes): ").upper()
    

def find_file_recursive(filename, folder_path):
    if os.path.exists(folder_path): 
        print("Matched files in specified folder and subfolders:")
        for dirpath, folders, files in os.walk(folder_path):
            founded_files = fnmatch.filter(files, file_to_find)
            for file in founded_files:
                print(os.path.join(dirpath, file))
    else:
        print(f"Wrong path! {e}")
                
def find_file(filename, folder_path):
    try:
        print("Matched files in specified folder:")
        files = [item for item in os.listdir(folder_path) if os.path.isfile(f"{folder_path}\{item}")]
        founded_files = fnmatch.filter(files, file_to_find)
        for f in founded_files:
            print(f"{folder_path}\{f}")
    except OSError as e:
        print(f"Wrong path! {e}")
        
if __name__ == "__main__":
    if recursive == "R":
        find_file_recursive(file_to_find, path)
    else:
        find_file(file_to_find, path)