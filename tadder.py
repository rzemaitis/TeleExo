#Set all filenames
#Set path
#namepath="../Exoplanets1/"
namepath="./Data/"
#Example"../Exoplanets1/qatar1b_r_10s_2_138.fits"
namebase="XMag"
nameroot=".txt"
timebase="Time"


#Add time!
lines = mainfile.readlines()
fname=namepath+namebase+nameroot
with open(fname) as f:
	for line in f:
		if not line.startswith("#"):
			line=line.rstrip('\n')
			lines.append(line)
f.close()
data=[]
for i in range (0,len(lines)):
	a=lines[i].split()
	data.append(a)
timefile = open(namepath+timebase+nameroot,"r")
tlines = timefile.readlines()
timefile.close()
mainfile = open(namepath+namebase+nameroot,"w")
for i in range(len(lines)):
		print "Writing %d"%i
		mainfile.write(lines[i].replace(str(i+1), tlines[i].rstrip('\n')))
mainfile.close()
