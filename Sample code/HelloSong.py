import pyfits as pf
import numpy as np
import matplotlib.pylab as plt
#from PyAstronomy import pyasl

f = open('data.lst', 'r')
datanum=int(f.readline())
name=open('data.lst').read().split('\n')
#name=f.readlines()
#name=f.read()
#print(name)
dat=[]
hdr=[]
for i in range(1,len(name)-1):
	#print(name[i])
	dat.append(pf.getdata(name[i]))# Get the data
	hdr.append(pf.getheader(name[i])) # Get the full header
	#print(np.shape(data)) # produces: (5, 51, 2048) = (layer, order, npix)
	#print(hdr.get('slit')) # returns the slit number
# Plot order 30 (counting stats at 0) with the wavelength solution before the science exposure
#plt.plot( data[4,29,:], data[0,29,:]/data[2,29,:] )
#Start from 6140 to 6166 Angstroms
lowangs = 6140
highangs = 6166
slit = 40
prange = 2048#len(dat[4,0,:])
wrange= 51#len(data[4,:,0])
#print (prange)
'''edibles = ["ham", "spam","eggs","nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        break
    print("Great, delicious " + food)
else:
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")
'''
first=0
#print(slits)
for j in range(0,datanum-1):
	data=dat[j]
	bvc=hdr[j].get("BVC")
	#print(bvc)
	slits=[]
	#print(len(data[4,:,0]))
	#and data[4,i,len(data[4,i,:])-1]<highangs
	flag=0
	for i in range(0,wrange):
		#print("checking %d" % i)
		if data[4,i,0]>lowangs and flag==0:
			#print("For %d order, from min at %f with max at %f" % (i,data[4,i,0],data[4,i,len(data[4,i,:])-1]))
			slits.append(i-1)
			slits.append(i)
			flag=1
		if data[4,i,len(data[4,i,:])-1]<highangs and flag==1:
			slits.append(i)
		#	print("For %d order, from min at %f with max at %f" % (i,data[4,i,0],data[4,i,len(data[4,i,:])-1]))
		else:
			if data[4,i,0]<highangs and flag==1:
				slits.append(i)
			#	print("For %d order, from min at %f with max at %f" % (i,data[4,i,0],data[4,i,len(data[4,i,:])-1]))
	#print(slits)
	#CHECK WHY NOT PRANGE
	plt.xlim(data[4,slits[0],0],data[4,slits[len(slits)-1],prange-1])
	#plt.ylim(0,1.2)
	for i in range(0,len(slits)-1):
		#data[4,slits[i],:]+=bvc*/3e5
		#print(i)
		#print("Before: %f" % data[0,slits[i],0])
		data[0,slits[i],:]/=data[2,slits[i],:]
		#print("After: %f" % data[0,slits[i],0])
		wmean=np.mean(data[0,slits[i],:])
		#print(data[0,slit,:])
		#print(wmean)
		data[0,slits[i],:]/=wmean
		for k in range(data[4,slits[i],0],data[4,slits[i],prange-1])
			max=0.
			for m in range(k,k+0.5)
				if(data[0,slits[i],m]	
				max=max(
	#Fit every 0.5 Angstroms
	for i in range(0,
	
	fdata=[]
	fdata.append(data)
	slitnum=len(slits)-1
	for i in range(0,len(slits)-1):
		if first==0:
			plt.plot(data[4,slits[i],:], data[0,slits[i],:] )
	first+=1
plt.show()
f.close()
#print('From %d to %d Angstroms /n' % (data[4,i,0],data[4,i,np.len(data[5,i,:]-1))
#Start from 6140 to 6166'''
