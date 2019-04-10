import astropy
from astropy.io import fits
import matplotlib.pyplot as plt


direc='/Users/bordieremma/Documents/Magistere_3/MT1/15_10/'
direc1="/Users/bordieremma/Documents/Magistere_3/MT1/"

image1=fits.open(direc+"mercure_001.fit")[0].data
image2=fits.open(direc1+"calib_054.fit")[0].data

mercure1=image1
mercure2=image2

plt.figure()
mercure=plt.imshow(mercure1, cmap='PRGn')
#mercure.set_cmap('nipy_spectral')
#plt.colorbar()

plt. figure()
plt.imshow(mercure2)# cmap='Blues')#,cmap='seismic')
#plt.colorbar()

plt.show()