import os
import time
import subprocess



#Set all filenames
#Set path
#namepath="../Exoplanets1/"
namepath="../4ff/"
#Example"../Exoplanets1/qatar1b_r_10s_2_138.fits"
namebase="qatar1b_r_10s_"
nameroot=".fits"
jump=1
filecount=1

fname=namepath+str(jump)+"_"+str(filecount).zfill(3)+nameroot
newfname=namepath+namebase+str(jump)+"_"+str(filecount).zfill(3)+nameroot
while os.path.isfile(fname):
	while os.path.isfile(fname):
		emacscat = subprocess.Popen("mv "+fname+" "+newfname, shell=True)
		emacscat.wait()
		filecount+=1
		fname=namepath+str(jump)+"_"+str(filecount).zfill(3)+nameroot
		newfname=namepath+namebase+str(jump)+"_"+str(filecount).zfill(3)+nameroot
	filecount=1
	jump+=1
	newfname=namepath+namebase+str(jump)+"_"+str(filecount).zfill(3)+nameroot
	fname=namepath+str(jump)+"_"+str(filecount).zfill(3)+nameroot
