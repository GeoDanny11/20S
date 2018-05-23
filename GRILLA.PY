
import numpy as np 
import math 

def arraylenght(rmax,stepteta,stepphi,stepr):
	size=0
	cont=0
	for R in range (0,rmax+1,stepr):
		for teta in range(-90,90+1,stepteta):
			for phi in range(-180,180+1,stepphi):
				if (teta==-90 or teta==90):
					if(phi!=-180 or phi!=180):
						if(cont>0):
							break							
						else:
							cont=1	
				size=size+1
	return (size)

#radio terrestre
r=6371
#latitud del origen de la grilla
lat1=int(input("Ingrese la latitud origen de la Grilla: "))
#longitud del origen de la grilla
lon1=int(input("Ingrese la longitud origen de la Grilla: "))
#Profundidad del origen en km
D1=int(input("Ingrese la profundidad del origen en km: "))
#radio maximo de la grilla en km
rmax=int(input("Ingrese el radio máximo de la Grilla: "))
#intervalo phi
stepphi=int(input("Ingrese el delta_phi: "))
#intervalo teta
stepteta=int(input("Ingrese el delta_teta: "))
#intervalo radio
stepr=int(input("Ingrese el delta_r: "))
#file=open("GRILLA","w")
#graf=open("GRILLA_GRAF","w")
source=0
i=0
cont=0

n=arraylenght(rmax,stepteta,stepphi,stepr)
qlat=np.zeros(n)
qlon=np.zeros(n)
qd2=np.zeros(n)
qr=np.zeros(n)
qteta=np.zeros(n)
qphi=np.zeros(n)
for R in range (0,rmax,stepr):
	for teta in range(-90,90,stepteta):
		for phi in range(-180,180,stepphi):
			if (teta==-90 or teta==90):
				if(phi!=-180 or phi!=180):
					if(cont>0):
						break							
					else:
						cont=1	
			lat2=(R*math.sin(teta)*math.sin(phi))/r + lat1
			lon2=2*math.asin((math.sin((R*math.sin(teta)*math.cos(phi))/(2*r)))/math.cos(lat1))+lon1
			D2=R*math.sin(teta)*math.tan(teta/2)+D1
			qlat[i]=lat2
			qlon[i]=lon2
			qd2[i]=D2
			qr[i]=R
			qteta[i]=teta
			qphi[i]=phi	
			i=i+1				
file=np.column_stack((qd2,qlat,qlon))
file2=np.column_stack((qr,qteta,qphi))
np.savetxt("SOURCE.txt",file,fmt="%6.3f",delimiter="    ")
np.savetxt("GRILLA.txt",file2,fmt="%6.3f",delimiter="    ")

"""
#Stations
file = open("STATIONS_TESIS","w")
stat = 0
for lat in range(-90,90,5):
	for lon in range(0,360,5):
		if(lat == 90 or lat == -90 and lon != 0):
			break		
		qlon = round(lon,4) 
		qlat = round(lat,4)
		qstat = round(stat,1)  				
		stat = stat + 1
		file.write("%05d      II      %8.4f    %8.4f      %4.1f    %4.1f\n" % (qstat, qlon, qlat, 1910, 100))
		
"""

