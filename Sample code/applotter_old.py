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
plt.axhline(y=45, color='b', linestyle='-')
title_font = {'size':'40', 'color':'black','weight':'normal','verticalalignment':'bottom'} 
axis_font = {'size':'28'}
plt.xlabel('Aperture diameter (pixels)', **axis_font)
plt.ylabel('Flux', **axis_font)
plt.title('Aperture analysis', **title_font)
plt.xticks(fontsize=15)    # fontsize of the tick labels
plt.yticks(fontsize=15)    # fontsize of the tick labels
plt.show()

