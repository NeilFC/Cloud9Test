#Sectioning full_path into tags


#first a work example
full_path = "C:/Users/nfrau/Music/Aditya Verma -- sarod traditional music from India/Raga Puriya Dhanashri.mp3"

charcut_list = []
a = len(full_path) 
for n in range(a):
    if full_path[n] == "/":
        charcut_list.append(n)
       
print charcut_list

#assigning lenght of list to variable
lenlist = len(charcut_list)
#test
print lenlist


#assigning variables to cut points

last_value = charcut_list[lenlist-1]
before_last = charcut_list[lenlist-2]
one_before = charcut_list[lenlist-3]
two_before = charcut_list[lenlist-4]
#test
print last_value, before_last, one_before, two_before


#assigning slices to variable tags

song = full_path[(last_value+1):(a-4)]
print "Song:", song
album = full_path[(before_last+1):(last_value)]
print "Album:", album
artist = full_path[(one_before+1):before_last]
print "Artist:", artist


#problem: in the example artist is enbedded on level 2. 
#check if this is common. This code will split level 'album' after and before '--'

d = len(album)
for n in range(d):
    if album[n] == "-" and album[n+1] == "-":
        artist = album[0:n-1]
        split_album = album [n+2:]
        print "Correction: the artist is", artist
        print "and the album is", split_album
        break
album = split_album

