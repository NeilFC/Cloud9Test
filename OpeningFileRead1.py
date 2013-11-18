

# Open the specified text file in read mode, reading it line-by-line into a list
f = open("printedit.txt", 'r').readlines()

# Loop through the lines of the original input
for line in f:
    print line