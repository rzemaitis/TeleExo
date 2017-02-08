import subprocess
import os
import sys
from matplotlib import pyplot as plt
import numpy as np


#Paths
targetpath ="./Data/"
targetname="Target_star.txt"
fname=targetpath+targetname
lines=[]

stars=1
magid=1
magerrid=2

#Read lines without comments
with open(fname) as f:
	for line in f:
		if not line.startswith("#"):
			line=line.rstrip('\n')
			lines.append(line)
f.close()
data=[]
#Split lines into values, and put them into data array
for i in range (0,len(lines)):
	a=lines[i].split()
	data.append(a)
#Make lists for storing x, y and yerr
time=np.zeros(len(lines))
mag=[]
magerr=[]
for i in range(0,stars):
	mags=np.zeros(len(lines))
	magerrs=np.zeros(len(lines))
	for j in range(len(lines)):
		#print data[j][magid+(i+1)*2]
		mags[j]=float(data[j][magid+(i)*2])
		magerrs[j]=float(data[j][magerrid+(i)*2])
	mag.append(mags)
	magerr.append(magerrs)
for i in range(len(lines)):
	time[i]=float(data[i][0])
# Plot values
for i in range(0,stars):
	plt.errorbar((time[:]),(mag[i][:]),yerr=magerr[i][:],fmt='o')
# control the axis range
#plt.xlim(5.5, 18.5)
#plt.ylim(0, 8.0)
#plt.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.xlabel('Time (seconds)')
plt.ylabel('Magnitude')
plt.title('Light curve callibrated')
#plt.gca().set_color_cycle(["red", "green", "blue"])
plt.gca().invert_yaxis()
plt.show()
