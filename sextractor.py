import numpy as np

def targetfind():
	var = raw_input("Please find your object and write its number:")
	print var

#Set filename
filename="../Exoplanets1/test.cat"
#Create a line array
lines=[]
#Read lines without comments
with open(filename) as f:
	for line in f:
		if not line.startswith("#"):
			line=line.rstrip('\n')
			#print line.rstrip()
			lines.append(line)
#Create array for storing data
data=[]

#Split lines into values, and put them into
for i in range (0,len(lines)-1):
	a=lines[i].split()
	data.append(a)
print data[0][1]


targetfind()
#for i in range (0,len(lines)-1):
#	data[i][]=chars[i]
