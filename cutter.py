import numpy as np
import os
import time
import subprocess
import sys
import math
import signal
from colorama import init
from colorama import Fore, Back, Style


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
#Split lines into values, and put them into data array
data=[]
for i in range (0,len(lines)):
	a=lines[i].split()
	data.append(a)

#Boolean list for masking bad lines
mask=[]
#Index stopper to get rid of more than one bad dip
stuck=0

for i in range(len(data)):
	if not i==0:
		newmag=float(data[i][magid])
		oldmag=float(data[i-1][magid])
		if not stuck==0:
			oldmag=float(data[stuck][magid])
		if(abs(newmag-oldmag)>1 and newmag>oldmag):
			print("Image= %d "%i)
			mask.append(False)
			if stuck==0:				
				stuck=i-1
		else:
			mask.append(True)
			stuck=0
	else:
		mask.append(True)
#Write new file
starfile = open(namepath+namebase+"_trim"+nameroot,"w")
for i in range(len(lines)):
	if(mask[i]):
		starfile.write(lines[i]+'\n')
#Cut time file
timefile = open(namepath+timebase+nameroot,"r")
lines = timefile.readlines()
timefile.close()
timefile = open(namepath+timebase+"_trim"+nameroot,"w")
for i in range(len(lines)):
	if(mask[i]):
		timefile.write(lines[i])

#Cut xmag file
xmagfile = open(namepath+xmagbase+nameroot,"r")
lines = xmagfile.readlines()
xmagfile.close()
xmagfile = open(namepath+xmagebase+"_trim"+nameroot,"w")
for i in range(len(lines)):
	if(mask[i]):
		xmagfile.write(lines[i])

timefile.close()
starfile.close()
xmagfile.close()
