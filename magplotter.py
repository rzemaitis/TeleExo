import subprocess
import os
import sys
from matplotlib import pyplot as plt
import numpy as np


#Paths
targetpath ="./Data/"
targetname="Target_star_fixed.txt"
fname=targetpath+targetname
lines=[]

stars=2
magid=1
#magerrid=2

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
#print data
time=np.zeros(len(lines))
mag=[]
#magerr=[]
for i in range(0,stars):
	mags=np.zeros(len(lines))
	#magerrs=np.zeros(len(lines))
	for j in range(len(lines)):
		#print data[j][magid+(i+1)*2]
		mags[j]=float(data[j][magid+(i)])
	#	magerrs[j]=float(data[j][magerrid+(i)*2])
	mag.append(mags)
	#magerr.append(magerrs)
for i in range(len(lines)):
	time[i]=float(data[i][0])
# Plot values
#for i in range(0,stars):
	#plt.errorbar((time[:]),(mag[i][:]),yerr=magerr[i][:],fmt='o')
for i in range(0,stars):
	if i==0:
		plt.plot((time[:]),(mag[i][:]))
	else:
		plt.plot((time[:]),(mag[i][:]),'--')
# control the axis range
#plt.xlim(5.5, 18.5)
#plt.ylim(0, 8.0)
title_font = {'size':'40', 'color':'black','weight':'normal','verticalalignment':'bottom'} 
axis_font = {'size':'28'}
plt.xlabel('Time (seconds)', **axis_font)
plt.ylabel('Magnitude', **axis_font)
plt.title('Lightcurve (calibrated)', **title_font)
plt.xticks(fontsize=15)    # fontsize of the tick labels
plt.yticks(fontsize=15)    # fontsize of the tick labels
#plt.gca().set_color_cycle(["red", "green", "blue"])
plt.gca().invert_yaxis()
plt.show()
