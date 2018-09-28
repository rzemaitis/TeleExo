import numpy as np
import matplotlib.pylab as plt
from PyAstronomy.modelSuite import forTrans as ft

# Create MandelAgolLC object with circular orbit and quadratic limb darkening
ma = ft.MandelAgolLC(orbit="circular", ld="quad")

# Choose some time axis
time = np.linspace(0, 0.5, 1000)

################################################
# Set parameters
ma["per"] = 3.
#Inclination 90 86 80
ma["i"] = 90.
#Semimajor Axis
ma["a"] = 6.5
#Transit time
ma["T0"] = 0.25
#To-star ratio
ma["p"] = 0.16
#Linear Limb darkening
ma["linLimb"] = 0.47
ma["quadLimb"] = 0.24
#Keep it zero
ma["b"] = 0.

# ... and calculate model
y1 = ma.evaluate(time)
################################################

# Let's see what happened ...
plt.plot(time, y1, 'b.')

# Your new transits here...

ma["i"]=86.
y2= ma.evaluate(time)
plt.plot(time, y2, 'r.')


ma["i"]=80.
y3= ma.evaluate(time)
plt.plot(time, y3, 'g.')

plt.show()
