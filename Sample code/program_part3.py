# Import some required modules
import numpy as np
import matplotlib.pylab as plt
# ... and now the funcFit package
from PyAstronomy import funcFit as fuf

# Starting from with Voigt profile
vp = fuf.Voigt1d()
# Set some values to create a model
vp["A"] = -0.4
vp["al"] = 0.7
vp["mu"] = 5500.
vp["ad"] = 0.3
vp["off"] = 1.0

x = np.linspace(5490., 5510., 200)
# Create our data with some noise
yerr = np.ones(len(x))*0.01
y = vp.evaluate(x) + np.random.normal(0.0, 0.01, len(x))

# Say, we have a guess of the parameters, which is, however,
# not entirely correct
vp["A"] = -0.376
vp["al"] = 0.9
vp["mu"] = 5499.7
vp["ad"] = 0.4
vp["off"] = 1.0

# Plot the data and our guess
plt.errorbar(x, y, yerr=yerr, fmt='b.-')
plt.plot(x, vp.evaluate(x), 'r--')
plt.show()

# Thaw the parameters, which we wish to vary
# during the sampling
vp.thaw(["A", "al", "mu", "ad"])

# Use current parameters as starting point for the sampling
X0 = vp.freeParameters()
print "Starting point for sampling: ", X0


##############################################################
### Using pymc for sampling, for emcee see below
##############################################################

# Now we specify the limits within which the individual parameters
# can be varied. Actually, you specify the limits of uniform priors
# here.
lims = {"A":[-1.0,0.0], "al":[0.0,3.], "ad":[0.0,3.0], "mu":[5495., 5505.]}

# Provide a guess for the proposal step widths.
# Try to guess the scale of the problem in the individual
# parameters.
steps = {"A":0.02, "al":0.01, "ad":0.01, "mu":0.05}

# Start the sampling. The resulting Marchov-Chain will be written
# to the file 'mcmcTA.tmp'. In default configuration, pickle
# is used to write that file.
# To save the chain to a compressed 'hdf5'
# file, you have to specify the dbArgs keyword; e.g., use:
#   dbArgs = {"db":"hdf5", "dbname":"mcmcExample.hdf5"}
vp.fitMCMC(x, y, X0, lims, steps, yerr=yerr, \
           iter=2500, burn=0, thin=1, \
           dbfile="mcmcTA.tmp")

ta = fuf.TraceAnalysis("mcmcTA.tmp")
# Use the burn-in from the previous example

# Comment and uncomment. What's the difference?
#ta.setBurn(500)

means = ta.parameterSet(prescription="mean")
print "Set of mean values: ", means
vp.assignValues(means)
plt.errorbar(x, y, yerr=yerr, fmt='b.-')
plt.plot(x, vp.evaluate(x), 'r.-')
plt.show()

ta.plotTraceHist("mu")
ta.show()
