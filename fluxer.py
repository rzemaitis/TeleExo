import numpy as np
import os
import time
import subprocess


#An initial target-defining function
def targetfind():
	os.system("emacs ../Exoplanets1/test.cat&")

	#Gaia denies permission, solve the issue?
	#os.system("gaia ../Exoplanets1/check.fits&")
	var = raw_input("Please find your object and write its number:")
	return var

#Deals with target finding after the jump
#def afterjumper():

targetpath ="./Data/"

targetfile = open(targetpath + "Target_star.txt", "w")
targetfixfile = open(targetpath + "Target_star_fixed","w")
referencefile = open(targetpath + "Reference_stars","w")


#Set all filenames
#Set path
#namepath="../Exoplanets1/"
namepath="./"
#Set catalog name
namecat="test.cat"
#Example"../Exoplanets1/qatar1b_r_10s_2_138.fits"
namebase="qatar1b_r_10s_"
nameroot=".fits"


#Create a catalog
cat=[]

#Create jumpcount and filecount
jump=1
filecount=1


#Create an initial filename
fname=namepath+namebase+str(jump)+"_"+str(filecount).zfill(3)+nameroot

print("Will check %s\n" %fname)

#Initialise the target and reference stars
#targetfind()

#Start the main loop
#Start with checking if file exists after a jump:
while os.path.isfile(fname):
	while os.path.isfile(fname):
		#Create a line array and a data array
		lines=[]
		data=[]
		#Execute sextractor
		process = subprocess.Popen("sextractor "+ fname+" -c "+namepath+"config/default.sex", shell=True)
		process.wait()
		#Read lines without comments
		with open(fname) as f:
			for line in f:
				if not line.startswith("#"):
					line=line.rstrip('\n')
					#print line.rstrip()
					lines.append(line)
		f.close()

		#Split lines into values, and put them into data array
		for i in range (0,len(lines)-1):
			a=lines[i].split()
			data.append(a)

		#Increment filecount and create a new name
		filecount += 1
		fname=namepath+namebase+str(jump)+"_"+str(filecount).zfill(3)+nameroot

		#Put the whole data into a catalog
		cat.append(data)

	print("\nJump or end of files detected\n") 
	#Increment the jump and reset filecount
	jump += 1
	print(jump)
	filecount=1
	#Create a new name
	fname=namepath+namebase+str(jump)+str(filecount).zfill(3)+nameroot
#
#
#
#Close all output files
targetfile.close()
targetfixfile.close()
referencefile.close()


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
