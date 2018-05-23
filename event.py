#whichsource.py
#code that analise which source are to be usen, given a certain direction
import subprocess
import re
import os
import numpy as np 

#funcion para calcular el timestep, cuantos datos de muestreo debe correrse el siguiente archivo para hacer la suma
def timestep (X,vel,deltar):
	time=X[:,0]
	step=np.zeros(np.size(time))
	suma=0
	c=0
	for i in range(1,np.size(time)):
		step[c]=time[i]-time[i-1]
		suma=suma+step[c]
		c=c+1
	deltat=suma/c #intervalo de tiempo en el archivo
	timestep=deltar/vel
	return (int(timestep/deltat),deltat)
"""
#función para contar el número de fuentes a sumar 
def howmanysources (ws,lenght,deltar,rmax):
	sources=0
	for i in range(np.size(ws)):
		if(ws[i]!=0):
			sources=sources+1		
	if (length >= rmax):
		return (sources,sources)
	else:
		return (sources,length//deltar)
"""
#funcion para sumar los archivos
def suma(X,Y,consecutivo,xy):
	newxy=xy*consecutivo	
	nf=np.size(X[:,0])+newxy
	nc=np.size(X[0,:])
	suma=np.zeros((nf,nc))	
	#print (np.size(X[:,0]))
	#print(nf)
	print ("-------------------",consecutivo,newxy,"-------------------")
	for k in range (1,129): #k controla las columnas
		for i in range(nf): #i controla las filas
			if(i < newxy):
				suma[i,k]=X[i,k]								
			elif (i<np.size(X[:,0])and i<np.size(Y[:,0])):
				suma[i,k]=X[i,k]+Y[i-newxy-1,k]
			elif (i>np.size(Y[:,0])):
				suma[i,k]=0
			elif(i>np.size(X[:,0])):
				suma[i,k]=Y[i-newxy-1,k]
	#print (suma)
	return(suma)

#función que determina las fuentes a usar
def whichsource(n,dirphi,dirteta):
	ws=np.zeros(n)
	for f in range(n):
		if(data[f,1]==dirteta):
			if(data[f,2]==dirphi):
				ws[c]=f+1
				c=c+1
	return(ws[1],ws[2],ws[3],ws[4],ws[5],ws[6],ws[7],ws[8],ws[9],)	

#Begin source

#intervalo del radio en la grilla
deltar=10

excel=pyxl.load_workbook("Tabla de eventos 20S.xlsx")
tabla=excel.get_sheet_by_name("Python_file")
file= open("GRILLA.txt","r")
lines=list(file)
n=np.size(lines)
file2="GRILLA.TXT"
data=np.loadtxt(file2)
origen=input(int("Ingrese fuente origen"))
f1="S"+str(origen)+".txt"
A=np.loadtxt(f1)

for i in range(3,n+3,1):
	fnum2,fnum3,fnum4,fnum5,fnum6,fnum7,fnum8,fnum9,fnum10=whichsource(n,tabla.cell(row=i+2,column=5).value,tabla.cell(row=i+2,column=6).value)
	f2="S"+str(fnum2)+".txt"
	f3="S"+str(fnum3)+".txt"
	f4="S"+str(fnum4)+".txt"
	f5="S"+str(fnum5)+".txt"
	f6="S"+str(fnum6)+".txt"
	f7="S"+str(fnum7)+".txt"
	f8="S"+str(fnum8)+".txt"
	f9="S"+str(fnum9)+".txt"
	f10="S"+str(fnum10)+".txt"
	tabla.cell(row=i+3,column=8).value=fnum10
	B=np.loadtxt(f2)
	C=np.loadtxt(f3)
	D=np.loadtxt(f4)
	E=np.loadtxt(f5)
	F=np.loadtxt(f6)
	G=np.loadtxt(f7)
	H=np.loadtxt(f8)
	I=np.loadtxt(f9)
	J=np.loadtxt(f10)
	vel=tabla.cell(row=i+2,column=4).value
	num,deltat=timestep(A,vel,deltar) #el primer archivo será el de referencia
	xy=num*9
	S=suma(A,B,1,xy)
	S=suma(S,C,2,xy)
	S=suma(S,D,3,xy)
	S=suma(A,E,4,xy)
	S=suma(S,F,5,xy)
	S=suma(S,G,6,xy)
	S=suma(A,H,7,xy)
	S=suma(S,I,8,xy)
	S=suma(S,J,9,xy)
	name=tabla.cell(row=i+3,colummn=2)
	#rellena la columna del tiempo 
	num,op=np.shape(S)
	time=np.zeros(num)
	for i in range (num):
		if (i<np.size(A[:,0])):
			time[i]=A[i,0]
		else:
			time[i]=time[i-1]+deltat

	for i in range (num):
		S[i,0]=time[i]

	np.savetxt(name,S, delimiter="   ")
	print("--------Finish ",name,"--------")

excel.save("Tabla de eventos lista para graf_seis.xlsx")