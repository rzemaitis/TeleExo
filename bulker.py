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
	if(i*6+6<len(data)):
		if not i==0:
				print "Found in next %d"%i+" length %d"%length
				num=0
		else:
			num=0
		for j in range(i*6,i*6+6):
			print num
			print "Current line %d"%(j+1)+" length of all data %d"%len(data)
			mean[num]+=float(data[j][magid])
			stdev[num]+=float(data[j][magid])
			tmean[num]+=float(tdata[j][timeid])
			num+=1
	else:
		print "Found last one"
		#for j in range(i,i+i*6-len(data)):
		num=0
		mean=np.zeros(len(data)-i*6)
		stdev=np.zeros(len(data)-i*6)
		tmean=np.zeros(len(data)-i*6)
		for j in range(i*6,len(data)):
			print "Current line %d"%(j+1)+" length of all data %d"%len(data)
			mean[num]+=float(data[i][magid])
			stdev[num]+=float(data[i][magid])
			print str(stdev[num])
			tmean[num]+=float(tdata[j][timeid])
			num+=1
	means[i]=np.mean(mean)
	stdevs[i]=np.std(stdev)/math.sqrt(num)
	tmeans[i]=np.mean(tmean)

outfile = open("Qatar1b.txt")
outfile.write("#The columns are: Time, Mag, Magerr.")
for i in range(len(means)):
	info+=str(tmeans[i])
	info+=str(means[i])
	info+=str(stdevs[i])
	outfile.write(info+'\n')
outfile.close()


			
