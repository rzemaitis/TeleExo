import numpy as np
import os
import time
import subprocess
import sys
import math
import signal


#Create files for output
targetpath ="./Data/"

targetfixfile = open(targetpath + "Target_star_fixed.txt","w")
referencefile = open(targetpath + "Reference_stars.txt","w")


#Set all filenames
#Set path
#namepath="../Exoplanets1/"
namepath="./Data/"
#Example"../Exoplanets1/qatar1b_r_10s_2_138.fits"
namebase="Target_star_trim"
nameroot=".txt"
timebase="Time_trim"
timeroot=".txt"

#Hardwired numbers for listed stuff (start from 0)
magid=1
#magerrid=2
mag=[]
#magerr=[]
#Stars, including target star
refstars=4

fname=namepath+namebase+nameroot
lines=[]
#Read lines without comments
with open(fname) as f:
	for line in f:
		if not line.startswith("#"):
			line=line.rstrip('\n')
			#print line.rstrip()
			lines.append(line)
f.close()
#Split lines into values, and put them into data array
for i in range (0,len(lines)):
	a=lines[i].split()
	#Temporary lists for putting in info from lines into one list
	mags=[]
	#magerrs=[]
	#Put lists into arrays
	#REMEMBER:mag[line][star]
	for j in range(0,refstars):
		mags.append(a[magid+2*j])
		#magerrs.append(a[magerrid+2*j])
		#print magerr
	mag.append(mags)
	#magerr.append(magerrs)
#Find average magnitude and correct for it
avgmag=np.zeros(len(mag))
#avgmagerr=np.zeros(len(mag))
#propmagerr=np.zeros(len(mag))
propmag=np.zeros(len(mag))

#Calculate true magnitude from 10 first frames for reference stars
tmag=np.zeros(len(mag))
for i in range(1,refstars):
	for j in range(0,10):
		tmag[i]+=float(mag[j][i])
	#print "Tmag for %d star "%i+"is: %f"%tmag[i]
	tmag[i]/=10


#Calculate callibration factor for reference stars
#REMEMBER:callibs[star][line]
callibs=[]
for i in range(1,refstars):
	callib=np.zeros(len(mag))
	for j in range(0,len(mag)):
		#print str(float(mag[j][i]))
		#print callib[i]
		callib[j]=float(mag[j][i])-tmag[i]
	#if i==0:
		#print "Callib for %d star "%i+str(callib[:])
	callibs.append(callib)

#Average callibration factor
callibavg=np.zeros(len(mag))
for i in range(0,len(mag)):
	for j in range(0,refstars-1):
		#print "%f "%len(callibs[j])+"%f "%len(callibavg)
		callibavg[i]+=callibs[j][i]
	callibavg[i]/=refstars-1

#Corect for our star of interest
for i in range(0,len(mag)):
	propmag[i]=float(mag[i][0])-callibavg[i]

#Add time
tname=namepath+timebase+timeroot
time=[]
with open(tname) as f:
	for line in f:
		if not line.startswith("#"):
			line=line.rstrip('\n')
			#print line.rstrip()
			time.append(line)

for i in range(0,len(time)):
	ref=time[i]
	prop=time[i]
	ref+=" "+"%15f"%callibavg[i]
	for j in range(0,refstars-1):
		ref+=" "+"%15f"%float(callibs[j][i])
	referencefile.write(ref+'\n')
	prop+=" "+"%15f"%propmag[i]+ " "+"%15f"%float(mag[i][0])
	#prop+=" "+str(propmagerr[i])
	targetfixfile.write(prop+'\n')
referencefile.close()
targetfixfile.close()

	
