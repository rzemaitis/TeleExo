import subprocess
import os
import sys
from matplotlib import pyplot as plt
import numpy as np


#Paths
targetpath ="./Data/"
targetname="Target_star.txt"
timename="Time.txt"
fname=targetpath+targetname
tname=targetpath+timename
lines=[]
#Read lines without comments
with open(fname) as f:
	for line in f:
		if not line.startswith("#"):
			line=line.rstrip('\n')
			lines.append(line)
	f.close()

lines=[]
with open(tname) as f:
	for line in f:
		if not line.startswith("#"):
			line=line.rstrip('\n')
			lines.append(line)
	f.close()
time=np.zeros(len(lines))
for i in range(0,len(lines)):
	time[i]=float(lines[i])

#Lists for plotting
mag1=np.zeros(len(time))
mag2=np.zeros(len(time))
mag3=np.zeros(len(time))
mag4=np.zeros(len(time))
refstars=4
magid=3

#Split lines into values, and put them into data array
for j in range (0,len(lines)):
	a=lines[i].split()
	magsappend(magid+2*j)
	


# Plot values
plot = plt.plot(float(time[:]),float(mag1[:]),float(time[:]),float(mag2[:]),float(time[:]),float(mags3[:]),float(time[:]),float(mag4[:]))
# control the axis range and labels
#plt.xlim(5.5, 18.5)
#plt.ylim(0, 8.0)
plt.xlabel('Time')
plt.ylabel('Magnitude')
plt.show()
