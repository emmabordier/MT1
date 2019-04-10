#######CARACTÉRISATION CAMERA_DARK##############
import astropy
from astropy.io import fits
import scipy.ndimage.interpolation as sni
import numpy as np
import matplotlib.pyplot as plt

direc='/Users/bordieremma/Documents/Magistère_3/MT1'

#A T=5°C: médiane/moyenne en fonction du log(temps de pose)


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

mean1=[np.mean(d_5_001),np.mean(d_5_01),np.mean(d_5_1),np.mean(d_5_10),np.mean(d_5_60),np.mean(d_5_300)]
mean=mean1-np.mean(offset)
median1=[np.median(d_5_001),np.median(d_5_01),np.median(d_5_1),np.median(d_5_10),np.median(d_5_60),np.median(d_5_300)]
median=median1-np.median(offset)
error=[np.std(d_5_001),np.std(d_5_01),np.std(d_5_1),np.std(d_5_10),np.std(d_5_60),np.std(d_5_300)]
temps=[0.01,0.1,1,10,60,300]

plt.figure(0)
plt.plot(np.log(temps),mean)#,error)
#plt.plot(np.log(temps),median)#,label="mediane")
plt.title(r"Caractérisation dark à différents temps de pose à $T=5^\circ$C")
plt.xlabel("log(Temps de pose)")
plt.ylabel("ADU")
plt.legend()
plt.show()
plt.clf()

plt.figure(1)
plt.hist(d_5_300-offset,bins=40)#range=(np.mean(d_5_300-offset)*0.9 , np.mean(d_5_300-offset)*1.1))
plt.show()

