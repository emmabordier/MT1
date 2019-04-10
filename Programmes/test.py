import astropy
from astropy.io import fits
import scipy.ndimage.interpolation as sni
import numpy as np
import matplotlib.pyplot as plt


#OFFSET 


#5degres
offset5=np.zeros((2047,2047))
Tableau5=np.zeros((2047,20470)) #tableau qui contient les 10 offsets mesures a 5 degres

for i in range(10):
    Tableau5[:,i*2047:(i+1)*2047]=fits.open("../15_10/dark_0.001_00"+str(i)+".fit")[0].data
    offset5+=fits.open("../15_10/dark_0.001_00"+str(i)+".fit")[0].data

moyenne5=[]
sigma5=[]
mediane5=[]
mini5=[]
maxi5=[]

for i in range(10):
    a=Tableau5[:,i*2047:(i+1)*2047]
    moyenne5.append(np.mean(a))
    sigma5.append(np.std(a))
    mediane5.append(np.median(a))
    mini5.append(np.amin(a))
    maxi5.append(np.amax(a))

offset5=0.1*offset5 #offset=moyenne des 10 offset 
m5=offset5.mean()
s5=offset5.std()
med5=np.median(offset5)
mi5=np.amin(offset5)
ma5=np.amax(offset5)

print moyenne5, sigma5, mediane5, mini5, maxi5
print m5, s5, med5, mi5, ma5
"""
offset5=offset5.reshape(2047*2047,1)
plt.figure(0)
plt.hist(offset5, bins=40, range=(m5*0.9,m5*1.1))
plt.title(r"Histogramme offset($t_{pose}=0.001s$) a $5^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")
#plt.show()

"""

#15 degres

offset15=np.zeros((2047,2047))
Tableau15=np.zeros((2047,20470)) #tableau qui contient les 10 offsets mesures a 15 degres

for i in range(10):
    Tableau15[:,i*2047:(i+1)*2047]=fits.open("../22_10/d_15.8_0.001_00"+str(i)+".fit")[0].data
    offset15+=fits.open("../22_10/d_15.8_0.001_00"+str(i)+".fit")[0].data

moyenne15=[]
sigma15=[]
mediane15=[]
mini15=[]
maxi15=[]

for i in range(10):
    c=Tableau15[:,i*2047:(i+1)*2047]
    moyenne15.append(np.mean(c))
    sigma15.append(np.std(c))
    mediane15.append(np.median(c))
    mini15.append(np.amin(c))
    maxi15.append(np.amax(c))

offset15=0.1*offset15 #offset=moyenne des 10 offset 
m15=offset15.mean()
s15=offset15.std()
med15=np.median(offset15)
mi15=np.amin(offset15)
ma15=np.amax(offset15)

print moyenne15, sigma15, mediane15, mini15, maxi15
print m15, s15, med15, mi15, ma15


offset15=offset15.reshape(2047*2047,1)
plt.figure(0)
plt.hist(offset15, bins=40, range=(m15*0.9,m15*1.1))
plt.title(r"Histogramme offset($t_{pose}=0.001s$) a $15^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")
plt.show()

