import numpy as np
import os
import time
import subprocess
import sys
import math

#An initial target-defining function
def targetfind(stars,fname,cat,xcoord,ycoord):
	print("emacs "+fname+".cat&\n")
	emacscat = subprocess.Popen("emacs "+fname, shell=True)
	#CONTINUE HERE, FIX GAIA PLS
	#gaiacat = subprocess.Popen("gaia "+fname.rstrip(".cat")+".fits&", shell=True)
	#Gaia denies permission, solve the issue?
	print("For gaia, get a new terminal, and write\n")
	print("gaia "+os.getcwd()+"/"+fname.rstrip(".cat")+".fits&\n")
	#os.system("gaia ../Exoplanets1/check.fits&")
	print("Please find your object and write its number.\n")
	print("While you're at it, select " + str((len(stars)-1))+ " target stars from the list:\n")
	read = raw_input("Target star id?\n")
	
	stars[0][0]=int(read)
	stars[0][1]=cat[0][int(read)][xcoord]
	stars[0][2]=cat[0][int(read)][ycoord]
	for i in range(1,len(stars)-1):
		read = raw_input("Reference star %d?\n" %i)
		stars[i][0]=int(read)
		stars[i][1]=cat[0][int(read)][xcoord]
		stars[i][2]=cat[0][int(read)][ycoord]
	emacscat.kill()

#Finds stars of interest in the next frame
def nextfind(stars,cat,xcoord,ycoord,catid,limit):
	for i in range(0,len(stars)-1):
		min=limit
		dist=limit+1
		starid=0
		for j in range(0,len(cat[catid])-1):
			print cat[catid][j][xcoord]
			print stars[i][1]
			x=float(cat[catid][j][xcoord])-float(stars[i][1])
			y=float(cat[catid][j][ycoord])-float(stars[i][2])
			dist=math.sqrt(x**2+y**2)
			if(dist<min):
				min=dist
				starid=j
		if(min>limit):
			sys.exit("SCRIPT PANIC: UNEXPECTED JUMP DETECTED")
		else:
			stars[i][0]=cat[catid][starid][0]
			stars[i][1]=cat[catid][starid][xcoord]
			stars[i][2]=cat[catid][starid][ycoord]

#Deals with target finding after the jump
def afterjumper(stars,fname,cat,xcoord,ycoord,catid,limit):
	emacscat = subprocess.Popen("emacs "+fname, shell=True)
	#CONTINUE HERE, FIX GAIA PLS
	#gaiacat = subprocess.Popen("gaia "+fname.rstrip(".cat")+".fits&", shell=True)
	#Gaia denies permission, solve the issue?
	print("For gaia, get a new terminal, and write")
	print("gaia "+os.getcwd()+"/"+fname.rstrip(".cat")+".fits&\n")
	#os.system("gaia ../Exoplanets1/check.fits&")
	distlistx=[]
	distlisty=[]
	for i in range(1,len(stars)-1):
		distlistx.append(float(stars[0][1]-stars[i][1]))
		distlisty.append(float(stars[0][2]-stars[i][2]))
	print("Please find your object again and write its number.\n")
	read = raw_input("Target star id?\n")
	stars[0][0]=int(read)
	stars[0][1]=cat[catid][int(read)][xcoord]
	stars[0][2]=cat[catid][int(read)][ycoord]
	for i in range(0,len(stars)-1):
		distx=distlistx[i-1]
		disty=distlisty[i-1]
		min=limit+1
		starid=0
		for j in range(0,len(cat[catid])-1):
			x=float(stars[0][1])-float(cat[catid][j][xcoord])
			y=float(stars[0][2])-float(cat[catid][j][ycoord])
			diff=abs(distx-x)+abs(disty-y)
			print diff
			if(diff<min):
				min=diff
				starid=j
		print(min)
		if(min>limit):
			emacscat.kill()
			sys.exit("SCRIPT PANIC: REFERENCE STAR NOT FOUND")
		else:
			stars[i][0]=cat[catid][starid][0]
			stars[i][1]=cat[catid][starid][xcoord]
			stars[i][2]=cat[catid][starid][ycoord]
	emacscat.kill()

#Create files for output
targetpath ="./Data/"

targetfile = open(targetpath + "Target_star.txt", "w")
targetfixfile = open(targetpath + "Target_star_fixed","w")
referencefile = open(targetpath + "Reference_stars","w")


#Set all filenames
#Set path
#namepath="../Exoplanets1/"
namepath="../Exoplanets1/"
#Example"../Exoplanets1/qatar1b_r_10s_2_138.fits"
namebase="qatar1b_r_10s_"
nameroot=".cat"

#Hardwired numbers for listed stuff (start from 0)
xcoord=5
ycoord=6
mag=3
magerr=4
flux=1
fluxerr=2

#Create a list of catalogs
cat=[]

#Create jumpcount, filecount for that jump with global file counter
jump=1
filecount=1
globcount=1

#How many stars? (Including the target star)
staramount=5

#Create a numpy array for storing star id's, x's, y's and flux
stars=np.zeros((staramount,4))

#Choose an appropriate limit of star's coordinate drift and before it is considered an unexpected jump
limit=200
limit2=500

#Create an initial filename
fname=namepath+namebase+str(jump)+"_"+str(filecount).zfill(3)+nameroot

#Create a file for giving flux output
output = open("Output.txt", "w")

#Start the main loop
#Start with checking if file exists after a jump:
while os.path.isfile(fname):
	while os.path.isfile(fname):
		print("Will check %s\n" %fname)
		#Create a line array and a data array
		lines=[]
		data=[]

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
		#Put the whole data into a catalog
		cat.append(data)

		#Find a star
		if(globcount==1):
			targetfind(stars,fname,cat,xcoord,ycoord)
		elif(filecount==1):
			afterjumper(stars,fname,cat,xcoord,ycoord,globcount-1,limit2)
		else:
			nextfind(stars,cat,xcoord,ycoord,globcount-1,limit)
		
		#
		#
		#
		#
		#Do something with data for this star
		for i in range(0,len(stars)-1):
			stars[i][3]= cat[globcount-1][int(stars[i][0])][flux]
		#Create a string containting data
		info="%6d"%globcount
		for i in range(0,len(stars)-1):
			info += "%6d"%stars[i][3]
		info+='\n'
		targetfile.write(info)
		#Increment filecount and create a new name
		filecount += 1
		globcount += 1
		fname=namepath+namebase+str(jump)+"_"+str(filecount).zfill(3)+nameroot

	print("\nJump or end of files detected\n") 
	#Increment the jump and reset filecount
	jump += 1
	filecount=1
	#Create a new name
	fname=namepath+namebase+str(jump)+"_"+str(filecount).zfill(3)+nameroot
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
