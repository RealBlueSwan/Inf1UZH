#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):                                    # If the input file does not exist, the function should return `False` and not write any output file.
        return False
    
    with open(path_reading, 'r') as f:                                      # read mode 'r'
        content = f.read()                                                  # read the entire file
        with open(path_writing, 'w') as r:                          
            
            if not content:                                                 # If the input file does exist, but is empty, an empty output file should be written.
                r.write(content)
            
            else:
                for line in content.splitlines():                           # split on newlines
                    if line == 'Name':                                      # if its the first line and only 'name' is there
                        r.write('Firstname,Lastname')                       # An input file that only contains the header (`Name`) should result in a file that contains only the headers `Firstname,Lastname`.
                        continue

                    elif line == '':                                        # If the line is empty
                        r.write('\n,')
                        continue 
                    
                    if ';' in line:
                        row = line.strip().replace(';', '').split(' ')      # split on commas
                        lastname, name = row[0], row[1]                     # convert the numbers from strings where necessary
                    else:
                        row = line.strip().split(' ')                       # split on commas
                        name, lastname = row[0], row[1]                     # convert the numbers from strings where necessary

                    r.write(f'\n{name},{lastname}')  


# The following line calls your solution function with the provided input file
# and then attempts to read and print the contents of the resulting output file.
# You do not need to modify these lines.
INPUT_PATH = "task/my_data.txt"
OUTPUT_PATH = "task/my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")

