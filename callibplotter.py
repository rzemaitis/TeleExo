import subprocess
import os
import sys
from matplotlib import pyplot as plt
import numpy as np

#Paths
targetpath ="./Data/"
targetname="Reference_stars.txt"
timename="Time_trim.txt"
fname=targetpath+targetname
tname=targetpath+timename
lines=[]

refstars=4
magid=1

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
mag=[]
for i in range(0,refstars):
	mags=np.zeros(len(lines))
	for j in range(len(lines)):
		#print str(len(data))+" "+str(len(data[j]))+" "+str(i)
		#print data[j][magid+(i)]
		mags[j]=float(data[j][magid+(i)])
	mag.append(mags)
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

	


# Plot values
for i in range(0,refstars):
	if i==0:
		print str(len(time))+" "+str(len(mag[i][:]))
		plt.scatter((time[:]),(mag[i][:]),s=40,c='r',marker='o',zorder=1)
	else:
		plt.plot((time[:]),(mag[i][:]),zorder=0)
# control the axis range
plt.xlim(-50, 10000)
#plt.ylim(0, 8.0)
title_font = {'size':'40', 'color':'black','weight':'normal','verticalalignment':'bottom'} 
axis_font = {'size':'28'}
plt.xlabel('Time (seconds)', **axis_font)
plt.ylabel('$mag_{ref} - mag_{true}$', **axis_font)
plt.title('Calibration curves', **title_font)
plt.xticks(fontsize=15)    # fontsize of the tick labels
plt.yticks(fontsize=15)    # fontsize of the tick labels
#plt.gca().set_color_cycle(["red", "green", "blue"])
plt.gca().invert_yaxis()
plt.show()
