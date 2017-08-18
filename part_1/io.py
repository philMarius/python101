'''Learning I/O in python'''

import os

os.chdir('/Users/phil/dev/python/python101/part_1/')  # For some reason this was needed?

# Reading one line

HANDLE = open('test.txt')
DATA = HANDLE.readline()
print(DATA)
HANDLE.close()

# Reading all the lines

HANDLE = open('test.txt')
for line in HANDLE:
    print(line)
HANDLE.close()

# Different type of loop

HANDLE = open('test.txt')
while True:
    DATA = HANDLE.read(1024)
    print(DATA)
    if not DATA:
        break

# Writing to file

HANDLE = open('another_test.txt', 'w')
HANDLE.write("This is a test!")
HANDLE.close()

# With operator

with open('test.txt') as file_handler:
    for line in file_handler:
        print(line)
