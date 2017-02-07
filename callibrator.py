import numpy as np
import os
import time
import subprocess
import sys
import math
import signal


#Create files for output
targetpath ="./Data/"

targetfixfile = open(targetpath + "Target_star_fixed","w")
referencefile = open(targetpath + "Reference_stars","w")


#Set all filenames
#Set path
#namepath="../Exoplanets1/"
namepath="../Data/"
#Example"../Exoplanets1/qatar1b_r_10s_2_138.fits"
namebase="Target_star"
nameroot=".txt"
timebase="Time"
timeroot=".txt"

#Hardwired numbers for listed stuff (start from 0)
magid=2
magerrid=3
mag=[]
magerr=[]
ref_stars=4

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
	magerrs=[]
	#Put lists into arrays
	for j in range(0,ref_stars):
		mags.append(a[magid+2*j])
		magerr.append(a[magerrid+2*j])
	mag.append(mags)
	magerr.append(magerrs)
#Find average magnitude and correct for it
avgmag=numpy.zeros(len(mags)-1)
oldavgmag=numpy.zeros(len(mags)-1)
propmag=[]
for i in range(0,len(mags)):
	for j in range(1,len(mags[i])):
		avgmag+=float(mags[i][j])
	avgmag/=ref_stars
	if not i==0:
		propmag-=(avgmag[i]-avgmag[i-1])
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
	info+=time[i]
	for j in range(0,len(avgmag))
		info+=str(avgmag[j])
	referencefile.write(info+'\n')
	

	
