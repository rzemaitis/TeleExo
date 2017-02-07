import subprocess
import os
import sys
from matplotlib import pyplot as plt
import numpy as np


#Paths
targetpath ="./Data/"
targetname="Apcheck.txt"
fname=targetpath+targetname

lines=[]
#Read lines without comments
with open(fname) as f:
	for line in f:
		if not line.startswith("#"):
			line=line.rstrip('\n')
			lines.append(line)
	f.close()

#Lists for plotting
apsizelist=np.zeros(len(lines))
fluxlist=np.zeros(len(lines))

#Split lines into values, and put them into data array
for i in range (0,len(lines)):
	a=lines[i].split()
	apsizelist[i]=int(a[0])
	fluxlist[i]=float(a[1])

# Plot values
plot = plt.plot(apsizelist,fluxlist,'ro')
# control the axis range and labels
#plt.xlim(5.5, 18.5)
#plt.ylim(0, 8.0)
plt.xlabel('Aperture size')
plt.ylabel('Flux')
plt.show()
