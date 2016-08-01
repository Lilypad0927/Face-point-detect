f = open("bbox.txt", "r")  
o = open("bbox2.txt", "w")

toRemove = 'image\1'

while True:  
    line = f.readline()  
    if line:  
		s = line
		line = s[(len(toRemove)+2):]
		print line;
		print >> o, line,
    else:  
        break
f.close()  