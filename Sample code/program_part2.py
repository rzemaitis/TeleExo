import numpy as np
import matplotlib.pylab as mpl
from numpy import *
import scipy 
import scipy.ndimage
import scipy.integrate
import pyfits
import operator
from PyAstronomy import funcFit as fuf
from PyAstronomy import pyasl
from PyAstronomy.pyaC import pyaErrors as PE
from itertools import combinations
import pymc
from PyAstronomy.modelSuite import forTrans as ft
from scipy.interpolate import UnivariateSpline
import random
from PyAstronomy.modelSuite.XTran import _ZList
from scipy import stats

##############################################################################
##############################################################################

class QuadraticLD(fuf.OneDFit):
  def __init__(self):
    fuf.OneDFit.__init__(self, ["u1", "u2"])
  def evaluate(self, x):
    y = 1. - self["u1"]*(1. - x) - self["u2"]*(1. - x)**2
    return y

##############################################################################
##############################################################################

# Read input filter, wavelength and transmission.
wave_filter = np.loadtxt('JCR.dat')[::,0]*10.
tran_filter = np.loadtxt('JCR.dat')[::,1]
tran_filter = tran_filter/max(tran_filter)

mpl.plot(wave_filter, tran_filter)
mpl.show()

# Angle-resolved spectra.
data, hdr = pyfits.getdata("lte04900-4.50-0.0.PHOENIX-ACES-AGSS-COND-SPECINT-2011.fits", header=True)
wave_data = np.arange(hdr["CRVAL1"], hdr["CRVAL1"]+hdr["NAXIS1"]*hdr["CDELT1"], hdr["CDELT1"])

# Get the mu values at which the spectra are calculated.
mu = pyfits.getdata("lte04900-4.50-0.0.PHOENIX-ACES-AGSS-COND-SPECINT-2011.fits", "MU")

# Creating a "common" wavelength vector:
dp_nr = 50000
waveLD = np.linspace(wave_data[0], wave_data[-1], dp_nr)

data_int = np.zeros(dp_nr*len(mu)).reshape(dp_nr,len(mu))
for jj in range(len(mu)):
    data_int[:,jj] = np.interp(waveLD, wave_data, data[jj])

tran_filter_interpolate = np.interp(waveLD, wave_filter, tran_filter)
mpl.plot(wave_filter, tran_filter)
mpl.plot(waveLD, tran_filter_interpolate)
mpl.show()

# Define the class that will do the fitting, and prepare for the fit.
LD_values = QuadraticLD()
LD_values.assignValue({"u1":0.7, "u2":0.7})
LD_values.thaw(["u1", "u2"])

# Now do two loops. One external going through the different wave_bins, and one internal
# doing the I(mu)/I(0) quadratic fit to get the limb darkening coefficients.

intensity = np.zeros(len(mu))
for jj in range(len(mu)):
    intensity[jj] = np.sum(data_int[:,jj]*tran_filter_interpolate)
    
intensity_max = max(intensity)
intensity = intensity/intensity_max

mpl.plot(mu, intensity)
mpl.show()

mu_int = np.linspace(0,1,1000)
intensity_int = np.interp(mu_int, mu, intensity)

# Get rid of the lowest mu's to do 2nd order fitting.
ind = np.where( mu_int >= 0.15 )
mu_trunc = mu_int[ind]
intensity_trunc = intensity_int[ind]
    
LD_values.fit(mu_trunc, intensity_trunc, xtol = 1.e-7, ftol = 1.e-7, disp = 0)
model_trunc = LD_values.evaluate(mu_trunc)
   
mpl.plot(mu, intensity)
mpl.plot(mu_trunc, model_trunc+0.05)
mpl.show()
 
LD_u1 = LD_values["u1"]
LD_u2 = LD_values["u2"]

print LD_u1, LD_u2
