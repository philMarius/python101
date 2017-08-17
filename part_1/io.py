'''Learning I/O in python'''

HANDLE = open("test.txt", "r")
DATA = HANDLE.readline()
print(DATA)
HANDLE.close()
