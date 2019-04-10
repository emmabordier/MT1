
#A T=5°C: médiane/moyenne en fonction du log(temps de pose)

import astropy
from astropy.io import fits
import scipy.ndimage.interpolation as sni
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
from scipy import stats  

direc='/Users/bordieremma/Documents/Magistere_3/MT1'

offset=np.zeros((2047,2047))
d_5_001=np.zeros((2047,2047))
d_5_01=np.zeros((2047,2047))
d_5_1=np.zeros((2047,2047))
d_5_10=np.zeros((2047,2047))
d_5_60=np.zeros((2047,2047))
d_5_300=np.zeros((2047,2047))
for i in range(10):
    offset+=fits.open(direc+"/15_10/dark_0.001_00"+str(i)+".fit")[0].data
    d_5_001+=fits.open(direc+"/15_10/dark_0.01_00"+str(i)+".fit")[0].data
    d_5_01+=fits.open(direc+"/15_10/dark_0.1_00"+str(i)+".fit")[0].data
    d_5_1+=fits.open(direc+"/15_10/dark_1_00"+str(i)+".fit")[0].data
    d_5_10+=fits.open(direc+"/15_10/dark_10_00"+str(i)+".fit")[0].data
    d_5_60+=fits.open(direc+"/15_10/dark_60_00"+str(i)+".fit")[0].data
    d_5_300+=fits.open(direc+"/15_10/dark_300_00"+str(i)+".fit")[0].data

offset=0.1*offset
d_5_001=0.1*d_5_001 #moyenne des dark a 5deg et tpose=0.01s
d_5_01=0.1*d_5_01
d_5_1=0.1*d_5_1
d_5_10=0.1*d_5_10
d_5_60=0.1*d_5_60
d_5_300=0.1*d_5_300

offset=offset.reshape(2047*2047,1)
d_5_001=d_5_001.reshape(2047*2047,1)
d_5_01=d_5_01.reshape(2047*2047,1)
d_5_1=d_5_1.reshape(2047*2047,1)
d_5_10=d_5_10.reshape(2047*2047,1)
d_5_60=d_5_60.reshape(2047*2047,1)
d_5_300=d_5_300.reshape(2047*2047,1)
#histo=d_5_300-262

mean1=[np.mean(d_5_001),np.mean(d_5_01),np.mean(d_5_1),np.mean(d_5_10),np.mean(d_5_60),np.mean(d_5_300)]
mean=mean1-np.mean(offset)
median1=[np.median(d_5_001),np.median(d_5_01),np.median(d_5_1),np.median(d_5_10),np.median(d_5_60),np.median(d_5_300)]
median=median1-np.median(offset)
#error=[np.std(d_5_001),np.std(d_5_01),np.std(d_5_1),np.std(d_5_10),np.std(d_5_60),np.std(d_5_300)]
temps=[0.01,0.1,1,10,60,300]


d_5_300_err=d_5_300[np.where(d_5_300<800)]
d_5_001_err=d_5_001[np.where(d_5_001<800)]
d_5_01_err=d_5_01[np.where(d_5_01<800)]
d_5_1_err=d_5_1[np.where(d_5_1<800)]
d_5_10_err=d_5_10[np.where(d_5_10<800)]
d_5_60_err=d_5_60[np.where(d_5_60<800)]
error=[np.std(d_5_001_err),np.std(d_5_01_err),np.std(d_5_1_err),np.std(d_5_10_err),np.std(d_5_60_err),np.std(d_5_300_err)]
print(error)

plt.figure(0)
plt.subplot(2,1,1)
plt.hist((d_5_300-offset), bins=80, range=(0,80)) #range=(np.mean(np.log(d_5_300))*0.9,np.mean(np.log(d_5_300)*1.1)))
plt.title(r"Histogramme dark($t_{pose}=300s$) a $5^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")
plt.subplot(2,1,2)
plt.scatter(np.log(temps),median)
plt.errorbar(np.log(temps),median,error,ls='none', ecolor = 'red')#,error)
#plt.plot(np.log(temps),median)#,label="mediane")
plt.title(r"Caractérisation dark à différents temps de pose à $T=5^\circ$C")
plt.xlabel("log(Temps de pose)")
plt.ylabel("ADU")
#plt.legend()

plt.tight_layout()
plt.show()



