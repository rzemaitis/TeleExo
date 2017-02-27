import subprocess
import os
import sys
from matplotlib import pyplot as plt
import numpy as np


#Paths
targetpath ="./Data/"
targetname="Target_star_trim.txt"
timename="Time_trim.txt"
#targetname="Target_star.txt"
#timename="Time.txt"
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
		#print data[j][magid+(i+1)*2]
		mags[j]=float(data[j][magid+(i)*2])
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
		plt.plot((time[:]),(mag[i][:]),)
	else:
		plt.plot((time[:]),(mag[i][:]),'--')
# control the axis range
#plt.xlim(5.5, 18.5)
#plt.ylim(0, 8.0)
#Change the font
# Set the font dictionaries (for plot title and axis titles)
title_font = {'size':'40', 'color':'black','weight':'normal','verticalalignment':'bottom'} 
axis_font = {'size':'28'}
plt.xlabel('Time (seconds)', **axis_font)
plt.ylabel('Magnitude', **axis_font)
plt.title('Lightcurves (trimmed)', **title_font)
plt.xticks(fontsize=15)    # fontsize of the tick labels
plt.yticks(fontsize=15)    # fontsize of the tick labels
# Bottom vertical alignment for more space
#plt.gca().set_color_cycle(["red", "green", "blue"])
plt.gca().invert_yaxis()
plt.show()
