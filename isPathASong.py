#Finding if full_path is a song or a directory


full_path = "C:\Users\nfrau\Music\Esperanza Spalding - Radio music society 2012"

a = len(full_path) - 3

print a

if full_path[a] != ".":
    print "Analyzing directory:", full_path