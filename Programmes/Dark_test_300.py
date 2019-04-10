
#A T=5°C: médiane/moyenne en fonction du log(temps de pose)

import astropy
from astropy.io import fits
import scipy.ndimage.interpolation as sni
import numpy as np
import matplotlib.pyplot as plt

direc='/Users/bordieremma/Documents/Magistere_3/MT1'

offset=np.zeros((2047,2047))
d_5_300=np.zeros((2047,2047))
for i in range(10):
    offset+=fits.open(direc+"/15_10/dark_0.001_00"+str(i)+".fit")[0].data
    d_5_300+=fits.open(direc+"/15_10/dark_300_00"+str(i)+".fit")[0].data

offset=0.1*offset
d_5_300=0.1*d_5_300

offset=offset.reshape(2047*2047,1)
d_5_300=d_5_300.reshape(2047*2047,1)
#histo=d_5_300-262

temps=[0.01,0.1,1,10,60,300]

plt.figure(0)
plt.subplot(2,2,1)
plt.hist((d_5_300-265), bins=40, range=(0,70)) #range=(np.mean(np.log(d_5_300))*0.9,np.mean(np.log(d_5_300)*1.1)))
plt.title(r"Histogramme dark($t_{pose}=300s$) a $5^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")


plt.tight_layout()
plt.show()
