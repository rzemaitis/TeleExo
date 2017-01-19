import numpy as np
import os
import time
import subprocess

#Set all strings for file paths
#Set path
namepath="../Exoplanets1/"
#Set catalog name
namecat="test.cat"
#Example"../Exoplanets1/qatar1b_r_10s_2_138.fits"
namebase="qatar1b_r_10s_"
nameroot=".fits"
catname=".cat"
defaultcat="test.cat"


#Create jumpcount and filecount
jump=1
filecount=1


#Create an initial filename
fname=namepath+namebase+str(jump)+"_"+str(filecount).zfill(3)+nameroot


#Start the main loop
#The loop goes until a consecutive file exists:
while os.path.isfile(fname):
	while os.path.isfile(fname):
		#Execute sextractor
		process = subprocess.Popen("sextractor "+ fname+" -c "+namepath+"config/default.sex", shell=True)
		process.wait()
		#Increment filecount and create a new name
		filecount += 1
		fname=namepath+namebase+str(jump)+"_"+str(filecount).zfill(3)+nameroot
		#Change name of test.cat to name of fits file, but with .cat extension
		rename = subprocess.Popen("mv "+defaultcat+" "+namepath+fname.replace(nameroot,catname), shell=True)		
		print("mv "+defaultcat+" "+namepath+fname.replace(nameroot,catname))
		rename.wait()
	print("\nJump or end of files detected\n") 
	#Increment the jump and reset filecount
	jump += 1
	filecount=1
	#Create a new name
	fname=namepath+namebase+str(jump)+"_"+str(filecount).zfill(3)+nameroot
	print("Will check %s\n" %fname)







# CODE DUMP
#
#
#
#
#
#os.system("sextractor " + name + " -c "+namepath+"/config/default.sex")
#time.sleep(3)
#print data[0][1]
#for i in range (0,len(lines)-1):
#	data[i][]=chars[i]

#text_file = open("Output.txt", "w")
#text_file.write("Purchase Amount: %s" % TotalAmount)
#text_file.close()
