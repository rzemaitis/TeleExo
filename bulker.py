import subprocess
import os
import sys
from matplotlib import pyplot as plt
import numpy as np
import math

#Paths
targetpath ="./Data/"
targetname="Target_star_fixed.txt"
timename="Time_trim.txt"
fname=targetpath+targetname
tname=targetpath+timename

refstars=4
magid=1
timeid=0

#Read lines without comments
lines=[]
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

#Read lines without comments
tlines=[]
with open(tname) as f:
	for line in f:
		if not line.startswith("#"):
			line=line.rstrip('\n')
			tlines.append(line)
f.close()
tdata=[]
#Split lines into values, and put them into data array
for i in range (0,len(tlines)):
	a=tlines[i].split()
	tdata.append(a)

#Make means and stdevs
length=math.floor(len(data)/6)
if not len(data)%6==0:
	length+=1
means=np.zeros(length)
stdevs=np.zeros(length)
tmeans=np.zeros(length)
for i in range (0,int(length)):
	mean=np.zeros(6)
	stdev=np.zeros(6)
	tmean=np.zeros(6)
	if(i+6<len(lines)):
		if not i==0:
				print "Found"
				num=(i*6/6)-1
		else:
			num=i*6
		for j in range(i*6,i*6+6):
			print num
			mean[num]+=float(data[j][magid])
			stdev[num]+=float(data[j][magid])
			tmean[num]+=float(tdata[j][timeid])
			num+=1
		means[i]=np.mean(mean)
		stdevs[i]=np.std(stdev)
		tmeans[i]=np.mean(tmean)
	else:
		for j in range(i,i+i*6-len(data)):
			if not i==0:
				print "Found"
				num=(j/6)-1
			else:
				num=j
			mean[num]+=float(data[i][magid])
			stdev[num]+=float(data[i][magid])
			tmean[num]+=float(tdata[j][timeid])
		means[i]=np.mean(mean)
		stdevs[i]=np.std(stdev)
		tmeans[i]=np.mean(tmean)

outfile = open("Qatar1b.txt")
for i in range(len(means)):
	info+=str(tmeans[i])
	info+=str(means[i])
	info+=str(stdevs[i])

outfile.close()


			
