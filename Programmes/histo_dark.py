import astropy
from astropy.io import fits
import scipy.ndimage.interpolation as sni
import numpy as np
import matplotlib.pyplot as plt

direc='/Users/bordieremma/Documents/Magistere_3/MT1'

"""
dark_5_001=np.zeros((2047,20470))
dark_5_01=np.zeros((2047,20470))
dark_5_1=np.zeros((2047,20470))
dark_5_10=np.zeros((2047,20470))
dark_5_60=np.zeros((2047,20470))
dark_5_300=np.zeros((2047,20470))

dark_15_001=np.zeros((2047,20470))
dark_15_01=np.zeros((2047,20470))
dark_15_1=np.zeros((2047,20470))
dark_15_10=np.zeros((2047,20470))

d_5_001=np.zeros((2047,2047))
d_5_01=np.zeros((2047,2047))
d_5_1=np.zeros((2047,2047))
d_5_10=np.zeros((2047,2047))
d_5_60=np.zeros((2047,2047))
d_5_300=np.zeros((2047,2047))

d_15_001=np.zeros((2047,2047))
d_15_01=np.zeros((2047,2047))
d_15_1=np.zeros((2047,2047))
d_15_10=np.zeros((2047,2047))

for i in range(10):
        dark_5_001[:,i*2047:(i+1)*2047]=fits.open("../15_10/dark_0.01_00"+str(i)+".fit")[0].data
        d_5_001+=fits.open("../15_10/dark_0.01_00"+str(i)+".fit")[0].data
        dark_5_01[:,i*2047:(i+1)*2047]=fits.open("../15_10/dark_0.1_00"+str(i)+".fit")[0].data
        d_5_01+=fits.open("../15_10/dark_0.1_00"+str(i)+".fit")[0].data
        dark_5_1[:,i*2047:(i+1)*2047]=fits.open("../15_10/dark_1_00"+str(i)+".fit")[0].data
        d_5_1+=fits.open("../15_10/dark_1_00"+str(i)+".fit")[0].data
        dark_5_10[:,i*2047:(i+1)*2047]=fits.open("../15_10/dark_10_00"+str(i)+".fit")[0].data
        d_5_10+=fits.open("../15_10/dark_10_00"+str(i)+".fit")[0].data
        dark_5_60[:,i*2047:(i+1)*2047]=fits.open("../15_10/dark_60_00"+str(i)+".fit")[0].data
        d_5_60+=fits.open("../15_10/dark_60_00"+str(i)+".fit")[0].data
        dark_5_300[:,i*2047:(i+1)*2047]=fits.open("../15_10/dark_300_00"+str(i)+".fit")[0].data
        d_5_300+=fits.open("../15_10/dark_300_00"+str(i)+".fit")[0].data
        dark_15_001[:,i*2047:(i+1)*2047]=fits.open("../22_10/d_15.8_0.01_00"+str(i)+".fit")[0].data
        d_15_001+=fits.open("../22_10/d_15.8_0.01_00"+str(i)+".fit")[0].data
        dark_15_01[:,i*2047:(i+1)*2047]=fits.open("../22_10/d_15.8_0.1_00"+str(i)+".fit")[0].data
        d_15_01+=fits.open("../22_10/d_15.8_0.1_00"+str(i)+".fit")[0].data
        dark_15_1[:,i*2047:(i+1)*2047]=fits.open("../22_10/d_15.8_1_00"+str(i)+".fit")[0].data
        d_15_1+=fits.open("../22_10/d_15.8_1_00"+str(i)+".fit")[0].data
        dark_15_10[:,i*2047:(i+1)*2047]=fits.open("../22_10/d_15.8_10_00"+str(i)+".fit")[0].data
        d_15_10+=fits.open("../22_10/d_15.8_10_00"+str(i)+".fit")[0].data


#Etude statistique


S_5=np.zeros((6,5,10))

for i in range(10):
    S_5[0,0,i]=np.mean(dark_5_001[:,i*2047:(i+1)*2047])
    S_5[0,1,i]=np.std(dark_5_001[:,i*2047:(i+1)*2047])
    S_5[0,2,i]=np.median(dark_5_001[:,i*2047:(i+1)*2047])
    S_5[0,3,i]=np.amin(dark_5_001[:,i*2047:(i+1)*2047])
    S_5[0,4,i]=np.amax(dark_5_001[:,i*2047:(i+1)*2047])
    S_5[1,0,i]=np.mean(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[1,1,i]=np.std(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[1,2,i]=np.median(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[1,3,i]=np.amin(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[1,4,i]=np.amax(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[2,0,i]=np.mean(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[2,1,i]=np.std(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[2,2,i]=np.median(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[2,3,i]=np.amin(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[2,4,i]=np.amax(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[3,0,i]=np.mean(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[3,1,i]=np.std(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[3,2,i]=np.median(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[3,3,i]=np.amin(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[3,4,i]=np.amax(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[4,0,i]=np.mean(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[4,1,i]=np.std(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[4,2,i]=np.median(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[4,3,i]=np.amin(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[4,4,i]=np.amax(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[5,0,i]=np.mean(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[5,1,i]=np.std(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[5,2,i]=np.median(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[5,3,i]=np.amin(dark_5_01[:,i*2047:(i+1)*2047])
    S_5[5,4,i]=np.amax(dark_5_01[:,i*2047:(i+1)*2047])

S_15=np.zeros((4,5,10)) #tableau contenant pour chaque temps de pose (6 differents),les stat(5:mean,std,median,max,min) pour chaque fichier(10)

for i in range(10):
    S_15[0,0,i]=np.mean(dark_15_001[:,i*2047:(i+1)*2047])
    S_15[0,1,i]=np.std(dark_15_001[:,i*2047:(i+1)*2047])
    S_15[0,2,i]=np.median(dark_15_001[:,i*2047:(i+1)*2047])
    S_15[0,3,i]=np.amin(dark_15_001[:,i*2047:(i+1)*2047])
    S_15[0,4,i]=np.amax(dark_15_001[:,i*2047:(i+1)*2047])
    S_15[1,0,i]=np.mean(dark_15_01[:,i*2047:(i+1)*2047])
    S_15[1,1,i]=np.std(dark_15_01[:,i*2047:(i+1)*2047])
    S_15[1,2,i]=np.median(dark_15_01[:,i*2047:(i+1)*2047])
    S_15[1,3,i]=np.amin(dark_15_01[:,i*2047:(i+1)*2047])
    S_15[1,4,i]=np.amax(dark_15_01[:,i*2047:(i+1)*2047])
    S_15[2,0,i]=np.mean(dark_15_01[:,i*2047:(i+1)*2047])
    S_15[2,1,i]=np.std(dark_15_01[:,i*2047:(i+1)*2047])
    S_15[2,2,i]=np.median(dark_15_01[:,i*2047:(i+1)*2047])
    S_15[2,3,i]=np.amin(dark_15_01[:,i*2047:(i+1)*2047])
    S_15[2,4,i]=np.amax(dark_15_01[:,i*2047:(i+1)*2047])
    S_15[3,0,i]=np.mean(dark_15_01[:,i*2047:(i+1)*2047])
    S_15[3,1,i]=np.std(dark_15_01[:,i*2047:(i+1)*2047])
    S_15[3,2,i]=np.median(dark_15_01[:,i*2047:(i+1)*2047])
    S_15[3,3,i]=np.amin(dark_15_01[:,i*2047:(i+1)*2047])
    S_15[3,4,i]=np.amax(dark_15_01[:,i*2047:(i+1)*2047])

M_5=np.zeros((6,5))  #tableau donnant a 5deg pour chaque temps de pose (6, moyenne des 10) les stat

d_5_001=0.1*d_5_001 #moyenne des dark a 5deg et tpose=0.01s
d_5_01=0.1*d_5_01
d_5_1=0.1*d_5_1
d_5_10=0.1*d_5_10
d_5_60=0.1*d_5_60
d_5_300=0.1*d_5_300
M_5[0,0]=d_5_001.mean()
M_5[0,1]=d_5_001.std()
M_5[0,2]=np.median(d_5_001)
M_5[0,3]=np.amin(d_5_001)
M_5[0,4]=np.amax(d_5_001)
M_5[1,0]=d_5_01.mean()
M_5[1,1]=d_5_01.std()
M_5[1,2]=np.median(d_5_01)
M_5[1,3]=np.amin(d_5_01)
M_5[1,4]=np.amax(d_5_01)
M_5[2,0]=d_5_1.mean()
M_5[2,1]=d_5_1.std()
M_5[2,2]=np.median(d_5_1)
M_5[2,3]=np.amin(d_5_1)
M_5[2,4]=np.amax(d_5_1)
M_5[3,0]=d_5_10.mean()
M_5[3,1]=d_5_10.std()
M_5[3,2]=np.median(d_5_10)
M_5[3,3]=np.amin(d_5_10)
M_5[3,4]=np.amax(d_5_10)
M_5[4,0]=d_5_60.mean()
M_5[4,1]=d_5_60.std()
M_5[4,2]=np.median(d_5_60)
M_5[4,3]=np.amin(d_5_60)
M_5[4,4]=np.amax(d_5_60)
M_5[4,0]=d_5_300.mean()
M_5[4,1]=d_5_300.std()
M_5[4,2]=np.median(d_5_300)
M_5[4,3]=np.amin(d_5_300)
M_5[4,4]=np.amax(d_5_300)

M_15=np.zeros((4,5)) # a 15 degres seulement 4 temps de pose differents

d_15_001=0.1*d_15_001 #moyenne des dark a 5deg et tpose=0.01s
d_15_01=0.1*d_15_01
d_15_1=0.1*d_15_1
d_15_10=0.1*d_15_10
M_15[0,0]=d_15_001.mean()
M_15[0,1]=d_15_001.std()
M_15[0,2]=np.median(d_15_001)
M_15[0,3]=np.amin(d_15_001)
M_15[0,4]=np.amax(d_15_001)
M_15[1,0]=d_15_01.mean()
M_15[1,1]=d_15_01.std()
M_15[1,2]=np.median(d_15_01)
M_15[1,3]=np.amin(d_15_01)
M_15[1,4]=np.amax(d_15_01)
M_15[2,0]=d_15_1.mean()
M_15[2,1]=d_15_1.std()
M_15[2,2]=np.median(d_15_1)
M_15[2,3]=np.amin(d_15_1)
M_15[2,4]=np.amax(d_15_1)
M_15[3,0]=d_15_10.mean()
M_15[3,1]=d_15_10.std()
M_15[3,2]=np.median(d_15_10)
M_15[3,3]=np.amin(d_15_10)
M_15[3,4]=np.amax(d_15_10)
    

print S_5[0,:], M_5[0]
print S_5[1,:], M_5[1]
print S_5[2,:], M_5[2]
print S_5[3,:], M_5[3]
print S_5[4,:], M_5[4]
print S_5[5,:], M_5[5]

print S_15[0,:], M_15[0]
print S_15[1,:], M_15[1]
print S_15[2,:], M_15[2]
print S_15[3,:], M_15[3]

"""


#Comparaison histogrammes dark a differents temps de pose pour 5degres

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

offset=np.mean(offset)

#offset=offset.reshape(2047*2047,1)
d_5_001=d_5_001.reshape(2047*2047,1)-offset
d_5_01=d_5_01.reshape(2047*2047,1)-offset
d_5_1=d_5_1.reshape(2047*2047,1)-offset
d_5_10=d_5_10.reshape(2047*2047,1)-offset
d_5_60=d_5_60.reshape(2047*2047,1)-offset
d_5_300=d_5_300.reshape(2047*2047,1)-offset
#histo=d_5_300-262


plt.figure(0)
plt.subplot(3,2,1)
plt.hist(d_5_001, bins=40, range=(np.mean(d_5_001)*0.9,np.mean(d_5_001)*1.1))
plt.title(r"Histogramme dark($t_{pose}=0.01s$) a $5^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")
plt.subplot(3,2,2)
plt.hist(d_5_01, bins=40, range=(np.mean(d_5_01)*0.9,np.mean(d_5_01)*1.1))
plt.title(r"Histogramme dark($t_{pose}=0.1s$) a $5^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")
plt.subplot(3,2,3)
plt.hist(d_5_1, bins=40, range=(np.mean(d_5_1)*0.9,np.mean(d_5_1)*1.1))
plt.title(r"Histogramme dark($t_{pose}=1s$) a $5^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")
plt.subplot(3,2,4)
plt.hist(d_5_10, bins=40, range=(np.mean(d_5_10)*0.9,np.mean(d_5_10)*1.1))
plt.title(r"Histogramme dark($t_{pose}=10s$) a $5^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")
plt.subplot(3,2,5)
plt.hist(d_5_60, bins=40, range=(np.mean(d_5_60)*0.9,np.mean(d_5_60)*1.1))
plt.title(r"Histogramme dark($t_{pose}=60s$) a $5^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")
plt.subplot(3,2,6)
plt.hist((d_5_300-265), bins=40, range=(0,70)) #range=(np.mean(np.log(d_5_300))*0.9,np.mean(np.log(d_5_300)*1.1)))
plt.title(r"Histogramme dark($t_{pose}=300s$) a $5^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")
plt.tight_layout()
plt.show()


'''

#Comparaison histogrammes dark a differents temps de pose pour 15degres

d_15_001=np.zeros((2047,2047))
d_15_01=np.zeros((2047,2047))
d_15_1=np.zeros((2047,2047))
d_15_10=np.zeros((2047,2047))

for i in range(10):
        d_15_001+=fits.open(direc+"/22_10/d_15.8_0.01_00"+str(i)+".fit")[0].data
        d_15_01+=fits.open(direc+"/22_10/d_15.8_0.1_00"+str(i)+".fit")[0].data
        d_15_1+=fits.open(direc+"/22_10/d_15.8_1_00"+str(i)+".fit")[0].data
        d_15_10+=fits.open(direc+"/22_10/d_15.8_10_00"+str(i)+".fit")[0].data


d_15_001=0.1*d_15_001 #moyenne des dark a 15deg et tpose=0.01s
d_15_01=0.1*d_15_01
d_15_1=0.1*d_15_1
d_15_10=0.1*d_15_10



d_15_001=d_15_001.reshape(2047*2047,1)
d_15_01=d_15_01.reshape(2047*2047,1)
d_15_1=d_15_1.reshape(2047*2047,1)
d_15_10=d_15_10.reshape(2047*2047,1)

plt.figure(0)
plt.subplot(2,2,1)
plt.hist(d_15_001, bins=40, range=(np.mean(d_15_001)*0.9,np.mean(d_15_001)*1.1))
plt.title(r"Histogramme dark($t_{pose}=0.01s$) a $15^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")
plt.subplot(2,2,2)
plt.hist(d_15_01, bins=40, range=(np.mean(d_15_01)*0.9,np.mean(d_15_01)*1.1))
plt.title(r"Histogramme dark($t_{pose}=0.1s$) a $15^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")
plt.subplot(2,2,3)
plt.hist(d_15_1, bins=40, range=(np.mean(d_15_1)*0.9,np.mean(d_15_1)*1.1))
plt.title(r"Histogramme dark($t_{pose}=1s$) a $15^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")
plt.subplot(2,2,4)
plt.hist(d_15_10, bins=40, range=(np.mean(d_15_10)*0.9,np.mean(d_15_10)*1.1))
plt.title(r"Histogramme dark($t_{pose}=10s$) a $15^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")

plt.tight_layout()
plt.show()'''

