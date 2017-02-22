import numpy as np
import os
import time
import subprocess
import sys
import math
import signal
from colorama import init
from colorama import Fore, Back, Style
#Init colorama
init(autoreset=True)

#Set all filenames
#Set path
#namepath="../Exoplanets1/"
namepath="./Data/"
#Example"../Exoplanets1/qatar1b_r_10s_2_138.fits"
namebase="Target_star"
nameroot=".txt"
timebase="Time"
xmagbase="XMag"
magid=1
#Stars, including target star
stars=4
#Exclude these images at specific times
excl=[5052,5064]
#Threshold
thresh=0.12
#excl=[]
#Create a filename
fname=namepath+namebase+nameroot
#Read lines without comments
lines=[]
with open(fname) as f:
	for line in f:
		if not line.startswith("#"):
			line=line.rstrip('\n')
			lines.append(line)
f.close()
#Read time for exclusion
timefile = open(namepath+timebase+nameroot,"r")
tlines = timefile.readlines()
timefile.close()
time=[]
for i in range (0,len(tlines)):
	a=tlines[i].split()
	time.append(a)
#Split lines into values, and put them into data array
data=[]
for i in range (0,len(lines)):
	a=lines[i].split()
	data.append(a)

#Boolean list for masking bad lines
mask=[]
#Index stopper to get rid of more than one bad dip
stuck=0

for i in range(len(lines)):
	dropcheck=False
	for j in range(0,stars):
		if i==0:
			mask.append(True)
			dropcheck=True
			break
		#print str(magid+j*2)
		if stuck==0:
			newmag=float(data[i][magid+j*2])
			oldmag=float(data[i-1][magid+j*2])
		else:
			newmag=float(data[i][magid+j*2])
			oldmag=float(data[stuck][magid+j*2])
		#print "Excl time "+str(excl).strip('[]')+" Our time "+str(time[i][0])
		if int(time[i][0]) in excl:
			print Fore.BLUE+"Found excl!"
			mask.append(False)
			dropcheck=True
			break
		if(abs(newmag-oldmag)>thresh and newmag>oldmag):
			#print("Image= %d false"%i)
			mask.append(False)
			#print "Newmag "+str(newmag)+" Oldmag "+str(oldmag)
			if stuck==0:				
				stuck=i-1
			#print ("i is at "+str(i)+" j is at "+str(j))
			dropcheck=True
			break
	if not dropcheck:
		stuck=0
	#	print("Image= %d true"%i)
		mask.append(True)
	#print "Mask is now "+str(len(mask))+" long while we're at i %d"%(i+1)

#Write new file
starfile = open(namepath+namebase+"_trim"+nameroot,"w")
for i in range(len(lines)):
	if(mask[i]):
		#print data[i][magid]
		starfile.write(lines[i]+'\n')
'''	else:
		print "No"
		print str(mask[i])+" "+str(i)
		print data[i][magid]'''
#Cut time file
timefile = open(namepath+timebase+"_trim"+nameroot,"w")
for i in range(len(lines)):
	if(mask[i]):
		timefile.write(tlines[i])

#Cut xmag file
xmagfile = open(namepath+xmagbase+nameroot,"r")
lines = xmagfile.readlines()
xmagfile.close()
xmagfile = open(namepath+xmagbase+"_trim"+nameroot,"w")
for i in range(len(lines)):
	if(mask[i]):
		xmagfile.write(lines[i])
timefile.close()
starfile.close()
xmagfile.close()
