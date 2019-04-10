import astropy
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import curve_fit

direc='/Users/bordieremma/Documents/Magistere_3/MT1'

#Lecture des dark et calcul médiane, moyenne et std
offset=[]
dark001=[]
dark01=[]
dark1=[]
dark10=[]
dark60=[]
dark300=[]


N= 10

for x in range (N):
    dark=fits.getdata(direc+"/15_10/dark_300_00"+str(x)+".fit")
    dark300.append(dark)
for x in range (N):
    dark=fits.getdata(direc+"/15_10/dark_0.01_00"+str(x)+".fit")
    dark001.append(dark)
for x in range (N):
    dark=fits.getdata(direc+"/15_10/dark_0.1_00"+str(x)+".fit")
    dark01.append(dark)
for x in range (N):
    dark=fits.getdata(direc+"/15_10/dark_1_00"+str(x)+".fit")
    dark1.append(dark)
for x in range (N):
    dark=fits.getdata(direc+"/15_10/dark_10_00"+str(x)+".fit")
    dark10.append(dark)
for x in range (N):
    dark=fits.getdata(direc+"/15_10/dark_60_00"+str(x)+".fit")
    dark60.append(dark)
for x in range (N):
    off=fits.getdata(direc+"/15_10/dark_0.001_00"+str(x)+".fit")
    offset.append(off)

cube_offset=np.array(offset)
offset=np.mean(cube_offset)

cube_001=np.array(dark001)-offset
cube_01=np.array(dark01)-offset
cube_1=np.array(dark1)-offset
cube_10=np.array(dark10)-offset
cube_60=np.array(dark60)-offset
cube_300=np.array(dark300)-offset

dark_m001=np.mean(cube_001, axis=0)
dark_med001=np.median(cube_001, axis=0)
dark_std001=np.std(cube_001,axis=0)

dark_m01=np.mean(cube_01, axis=0)
dark_med01=np.median(cube_01, axis=0)
dark_std01=np.std(cube_01,axis=0)

dark_m1=np.mean(cube_1, axis=0)
dark_med1=np.median(cube_1, axis=0)
dark_std1=np.std(cube_1,axis=0)

dark_m10=np.mean(cube_10, axis=0)
dark_med10=np.median(cube_10, axis=0)
dark_std10=np.std(cube_10,axis=0)

dark_m60=np.mean(cube_60, axis=0)
dark_med60=np.median(cube_60, axis=0)
dark_std60=np.std(cube_60,axis=0)

dark_m300=np.mean(cube_300, axis=0)
dark_med300=np.median(cube_300, axis=0)
dark_std300=np.std(cube_300,axis=0)

#On utilisera la moyenne du dark_med pour le bruit
#print(np.mean(dark_med))

#plt.hist(dark_med.flatten(), normed=True, bins=100, range=(200,400) )


def Gauss(x, a, x0, sigma):
    return a * np.exp(-(x - x0)**2 / (2 * sigma**2))


#Ajustement d'une gaussienne sur le dark median et affichage d'un dark et du dark median

a= dark_med300.clip(0,100)
b= dark_med001.clip(0,100)
c= dark_med01.clip(0,100)
d= dark_med1.clip(0,100)
e= dark_med10.clip(0,100)
f= dark_med60.clip(0,100)
print(a)

(mean001, sigma001) = norm.fit(b.flatten())
(mean01, sigma01) = norm.fit(c.flatten())
(mean1, sigma1) = norm.fit(d.flatten())
(mean10, sigma10) = norm.fit(e.flatten())
(mean60, sigma60) = norm.fit(f.flatten())
(mean300, sigma300) = norm.fit(a.flatten())


n001 , bins001, patches = plt.hist(dark_med001.flatten(), bins=100,range=(0,100) , histtype='bar' )
x001 = np.linspace(bins001[0], bins001[-1], 100)

n01 , bins01, patches = plt.hist(dark_med01.flatten(), bins=100,range=(0,100) , histtype='bar' )
x01 = np.linspace(bins01[0], bins01[-1], 100)

n1 , bins1, patches = plt.hist(dark_med1.flatten(), bins=100,range=(0,100) , histtype='bar' )
x1 = np.linspace(bins1[0], bins1[-1], 100)

n10 , bins10, patches = plt.hist(dark_med10.flatten(), bins=100,range=(0,100) , histtype='bar' )
x10 = np.linspace(bins10[0], bins10[-1], 100)

n60 , bins60, patches = plt.hist(dark_med60.flatten(), bins=100,range=(0,100) , histtype='bar' )
x60 = np.linspace(bins60[0], bins60[-1], 100)

n300 , bins300, patches = plt.hist(dark_med300.flatten(), bins=100,range=(0,100) , histtype='bar' )
x300 = np.linspace(bins300[0], bins300[-1], 100)

popt001, pcov001 = curve_fit(Gauss, x001, n001, p0=(max(n001), np.mean(dark_med001),np.std(dark_med001)))
popt01, pcov01 = curve_fit(Gauss, x01, n01, p0=(max(n01), np.mean(dark_med01),np.std(dark_med01)))
popt1, pcov1 = curve_fit(Gauss, x1, n1, p0=(max(n1), np.mean(dark_med1),np.std(dark_med1)))
popt10, pcov10 = curve_fit(Gauss, x10, n10, p0=(max(n10), np.mean(dark_med10),np.std(dark_med10)))
popt60, pcov60 = curve_fit(Gauss, x60, n60, p0=(max(n60), np.mean(dark_med60),np.std(dark_med60)))
popt300, pcov300 = curve_fit(Gauss, x300, n300, p0=(max(n300), np.mean(dark_med300),np.std(dark_med300)))

mean=[popt001[1],popt01[1],popt1[1],popt10[1],popt60[1],popt300[1]]
err=[popt001[2],popt01[2],popt1[2],popt10[2],popt60[2],popt300[2]]
temps=[0.01,0.1,1,10,60,300]

print('err=', err,'mean=', mean)

plt.figure()
plt.subplot(2,1,1)
plt.plot(x300, Gauss(x300, *popt300), 'r-', label='fit: max=%5.3f, moyenne=%5.3f, sigma=%5.3f' % tuple(popt300))
plt.legend()
plt.hist(dark_med300.flatten(), bins=100, range=(0,100) , histtype='bar' )
plt.title(r"Histogramme dark($t_{pose}=300s$) a $5^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")

plt.subplot(2,1,2)
plt.scatter(np.log(temps),mean)
plt.errorbar(np.log(temps),mean,err, ls='none', ecolor = 'red')
plt.title(r"Caractérisation dark à différents temps de pose à $T=5^\circ$C")
plt.xlabel("log(Temps de pose)")
plt.ylabel("ADU")

plt.figure()
plt.subplot(2,1,1)
plt.hist(dark_med1.flatten(), bins=100,range=(-20,80) , histtype='bar' )
plt.title(r"Histogramme dark($t_{pose}=1s$) a $5^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")
plt.subplot(2,1,2)
plt.hist(dark_med300.flatten(), bins=100,range=(-20,80) , histtype='bar' )
plt.title(r"Histogramme dark($t_{pose}=300s$) a $5^\circ$C")
plt.xlabel("ADU")
plt.ylabel("Nombre de pixels")




plt.tight_layout()
plt.show()
plt.clf()
