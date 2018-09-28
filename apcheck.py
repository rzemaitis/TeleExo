import subprocess
import os
import sys
import math
from colorama import init
from colorama import Fore, Back, Style
from matplotlib import pyplot as plt

#Init colorama
init(autoreset=True)


def inplace_change(filename, old_string, new_string):
	# Safely read the input filename using 'with'
	with open(filename) as f:
		s = f.read()
		if old_string not in s:
			print (Fore.RED +'"{old_string}" not found in {filename}.'.format(**locals()))
			return
	# Safely write the changed content, if found in the file
	with open(filename, 'w') as f:
		print Fore.GREEN +'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals())
		s = s.replace(old_string, new_string)
		f.write(s)
	


#Gets the star's flux
def fluxfind(data,fname,xcoord,ycoord,fluxid,limit):

	min=limit+1
	starid=0
	for i in range(0,len(data)):
		x=xcoord-float(data[i][5])
		y=ycoord-float(data[i][6])
		dist=math.sqrt(x**2+y**2)
		if(dist<min):
			min=dist
			starid=i
	if(min>limit or starid==0):
		sys.exit("SCRIPT PANIC: STAR NOT FOUND")
	else:
		return starid



#Set all strings for file paths
#Set path
namepath="../Test/"
#Set catalog name
namecat="test.cat"
#Example"../Exoplanets1/qatar1b_r_10s_2_138.fits"
namebase="qatar1b_r_10s_"
nameroot=".fits"
catname=".cat"
defaultcat="test.cat"
proppath=namepath+"config/"
#Create files for output
targetpath ="./Data/"
targetfile = open(targetpath + "Apcheck.txt", "w")

#Create jumpcount and filecount
jump=1
filecount=1

#Create an initial filename
fname=namepath+namebase+str(jump)+"_"+str(filecount).zfill(3)+nameroot
cname=fname.replace(nameroot,catname)
pname=proppath+"default.sex"
#Aperture in file
oldap=5
#Mark flux id in catalogue
fluxid=1
fluxerrid=2
#Hardwired X and Y coordinates
xcoord=2667
ycoord=1774
limit=5
#How large and small the apertures?
minap=5
maxap=80
#Lists for plotting
apsizelist=[]
fluxlist=[]

for i in range(minap,maxap):
	ap=i
	#Change param
	#Read lines without comments
	with open(pname) as f:
		for line in f:
			if not line.startswith("#"):
				if line.startswith("PHOT_APERTURES   "):
					old_string=line
	f.close()
	new_string="PHOT_APERTURES   "+str(ap)+"              # MAG_APER aperture diameter(s) in pixels\n"
	inplace_change(pname,old_string, new_string)
	#Execute sextractor
	#print("sextractor "+ fname+" -c "+namepath+"config/default.sex")
	process = subprocess.Popen("sextractor "+ fname+" -c "+namepath+"config/default.sex", shell=True)
	process.wait()
	#Change name of test.cat to name of fits file, but with .cat extension
	rename = subprocess.Popen("mv "+defaultcat+" "+namepath+fname.replace(nameroot,catname), shell=True)
	rename.wait()
	#Create a line array and a data array
	lines=[]
	data=[]
	#Read lines without comments
	with open(cname) as f:
		for line in f:
			if not line.startswith("#"):
				line=line.rstrip('\n')
				#print line.rstrip()
				lines.append(line)
	f.close()
	#Split lines into values, and put them into data array
	for j in range (0,len(lines)):
		a=lines[j].split()
		data.append(a)
	#Find flux
	id=fluxfind(data,cname,xcoord,ycoord,fluxid,limit)
	flux=float(data[id][fluxid])
	fluxerr=float(data[id][fluxerrid])
	#Write flux into file
	info="%5d"%i
	info+="%10.2f %10.2f"%(flux,fluxerr)
	targetfile.write(info+'\n')
	apsizelist.append(str(i))
	fluxlist.append(str(flux))
	oldap=ap


#Make ap 5 again
ap=5
#Change param
old_string="PHOT_APERTURES   "+str(oldap)+"              # MAG_APER aperture diameter(s) in pixels"
new_string="PHOT_APERTURES   "+str(ap)+"              # MAG_APER aperture diameter(s) in pixels"
inplace_change(pname,old_string, new_string)


targetfile.close()
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
