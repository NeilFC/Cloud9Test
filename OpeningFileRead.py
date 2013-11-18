#Opening file for read and checking workflow

sourceFile = raw_input("\nWelcome to the mp3 tag slicer!\n\nEnter the name of the data file: ")

# Open the specified text file in read mode, reading it line-by-line into a list
f = open(sourceFile, 'r').readlines()

# Loop through the lines of the original input
for line in f:
    print line