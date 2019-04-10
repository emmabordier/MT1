#### FONCTIONS POUR EQUIVALENCES ANGLE <> LONGUEUR D'ONDE ####

from math import *
import numpy as np

def angle(degre,minute):
	conv_minute=minute/60
	deg_rad=((degre+conv_minute)-269.48)*(np.pi)/180
	return(deg_rad)

def equivalence_angle_lambda(deg_rad):        
	return ((sin(deg_rad)-6.750E-6)/(6.015E-5))

def equivalence_lambda_angle(lbda):
	eq=asin(6.015E-5*lbda+6.750E-6)
	angle=eq*180/np.pi+269.48
	decim_min=(angle-int(angle))*60
	return(int(angle),decim_min)


deg=np.arange((2,30))
for i in range(30):
