from astropy.io import fits
import os
import datetime
from dateutil.parser import parse

#Set all filenames
#Set path
namepath="../Exoplanets1/"
#Example"../Exoplanets1/qatar1b_r_10s_2_138.fits"
namebase="qatar1b_r_10s_"
nameroot=".fits"
jump=1
filecount=1

fname=namepath+namebase+str(jump)+"_"+str(filecount).zfill(3)+nameroot
time=[]

#Create files for output
targetpath ="./Data/"

targetfile = open(targetpath + "Time.txt", "w")

globcount=0
while os.path.isfile(fname):
	while os.path.isfile(fname):
		hdulist = fits.open(fname)
		date=hdulist[0].header['DATE-OBS']
		dt = parse(date)
		#d = datetime.datetime.strptime(s, "%Y-%b-%dT%H:%M:%S.%f")
		if (filecount==1 and jump==1):
			info=str(0)+'\n'
			h=dt.hour
			m=dt.minute
			s=dt.second
		else:
			ho=dt.hour-h
			mi=dt.minute-m
			se=dt.second-s
			info=str(ho*3600+mi*60+se)+'\n'
		targetfile.write(info)
		filecount+=1
		globcount+=1
		fname=namepath+namebase+str(jump)+"_"+str(filecount).zfill(3)+nameroot
		hdulist.close()
	filecount=1
	jump+=1
	print("And jump!")
	fname=namepath+namebase+str(jump)+"_"+str(filecount).zfill(3)+nameroot

targetfile.close()
#s = "19 Nov 2015  18:45:00.000"
#d = datetime.datetime.strptime(s, "%d %b %Y  %H:%M:%S.%f")
#d = datetime.datetime.strptime(s, "%Y-%b-%dT%H:%M:%S.%f")
#Actual: 2016-11-19T19:02:19.000

#		print dt.year
#				print dt.month
#			print dt.day
#			print dt.hour
#			print dt.minute
#			print dt.second
