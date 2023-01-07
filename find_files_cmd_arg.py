import os
import sys

file_to_find = sys.argv[1]
path = sys.argv[2]

print(sys.argv)

print("Found files:")
for dirpath, folders, files in os.walk(path):
    for file in files:
        if file == file_to_find:
            print(os.path.join(dirpath, file))